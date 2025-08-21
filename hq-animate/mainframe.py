import os
from pathlib import Path
import platform
import subprocess
from PIL import Image
from PySide6.QtCore import Signal, QAbstractTableModel, Qt, QThread, QObject
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QFrame, QFileDialog, QHeaderView, QApplication
from .settings import Settings
from .ui_mainframe import Ui_MainFrame
from . import convert


SYSTEM = platform.system()
SCRIPT_PATH = Path(__file__).resolve().parent


class MainFrame(QFrame, Ui_MainFrame):
    settings_clicked = Signal()
    setting_changed = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.worker_thread = None
        self.worker = None
        
        self.paths = []

        self.settings = Settings.from_file_or_default(Path(SCRIPT_PATH, "settings.json"))

        self.frames_table.setModel(TableModel(self.paths))
        self.frames_table.verticalHeader().setVisible(False)
        self.frames_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.frames_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.frames_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.enable_label.setEnabled(False)
        self.enable_check.setEnabled(False)
        self.target_combo.addItems(convert.TARGETS.keys())
        self.target_combo.setCurrentIndex(-1)

        self.apng_check.setChecked(self.settings.do_apng)
        self.avif_check.setChecked(self.settings.do_avif)
        self.webp_check.setChecked(self.settings.do_webp)
        self.gif_check.setChecked(self.settings.do_gif)
        self.mp4_check.setChecked(self.settings.do_mp4)
        self.webm_check.setChecked(self.settings.do_webm)

        self.duration_spinbox.setValue(self.settings.frame_length)
        self.quality_spinbox.setValue(self.settings.quality)
        self.latitude_spin.setValue(self.settings.latitude)
        self.longitude_spin.setValue(self.settings.longitude)
        self.lossless_check.setChecked(self.settings.lossless)
        self.show_folder_check.setChecked(self.settings.show_folder)

        self.apng_check.stateChanged.connect(self.set_convert_button_state)
        self.avif_check.stateChanged.connect(self.set_convert_button_state)
        self.webp_check.stateChanged.connect(self.set_convert_button_state)
        self.gif_check.stateChanged.connect(self.set_convert_button_state)
        self.mp4_check.stateChanged.connect(self.set_convert_button_state)
        self.webm_check.stateChanged.connect(self.set_convert_button_state)

        self.output_path_edit.textChanged.connect(self.set_convert_button_state)
        self.output_name_edit.textChanged.connect(self.set_convert_button_state)

        self.input_browse_button.clicked.connect(self.set_input_frames)
        self.output_browse_button.clicked.connect(self.set_output_path)
        self.enable_check.toggled.connect(self.set_field_derotation_state)
        self.settings_button.clicked.connect(self.switch_to_settings_page)
        self.convert_button.clicked.connect(self.on_convert_start)
        self.wildcards = " ".join(sorted({f"*{ex}" for ex, f in Image.registered_extensions().items() if f in Image.OPEN}))

        self.can_avc = False
        self.can_av1 = False
        self.can_vp9 = False

        self.frames_table.doubleClicked.connect(self.view_frame)

        parent.settings_updated.connect(self.update_settings)

        self.set_field_derotation_state()
        self.update_ffmpeg_widgets()
        self.set_convert_button_state()

        if self.settings.mp4_codec:
            self.mp4_codec_combo.setCurrentText(self.settings.mp4_codec.name)
        if self.settings.webm_codec:
            self.webm_codec_combo.setCurrentText(self.settings.webm_codec.name)

    
    def set_input_frames(self, event):
        paths, _ = QFileDialog.getOpenFileNames(self, "Select animation frames...", self.output_path_edit.text(), f"Images ({self.wildcards})")

        if paths:
            self.paths.clear()
            enable_field_rotation_option = True
            target = None
            self.frames_table.model().beginResetModel()
            for p in paths:
                f = convert.Frame(p)
                self.paths.append(f)
                if not target:
                    target = f.target
                    enable_field_rotation_option = enable_field_rotation_option and f.date_time is not None and f.target is not None
            self.frames_table.model().endResetModel()
            self.enable_label.setEnabled(enable_field_rotation_option)
            self.enable_check.setEnabled(enable_field_rotation_option)
            if not enable_field_rotation_option:
                self.enable_check.setChecked(False)
            self.set_field_derotation_state()
            if target:
                self.target_combo.setCurrentText(target)
            self.output_path_edit.setText(str(self.paths[0].path.parent))
        
        self.set_convert_button_state()
    
    def set_output_path(self, event):
        path = QFileDialog.getExistingDirectory(self, "Select output folder...", "")

        if path:
            self.output_path_edit.setText(path)
        
        self.set_convert_button_state()
    
    def switch_to_settings_page(self):
        self.settings_clicked.emit()
    
    def update_settings(self):
        self.update_ffmpeg_widgets()
    
    def set_field_derotation_state(self, index=None):
        is_checked = self.enable_check.isChecked()

        for f in self.paths:
            if f.date_time:
                break
        else:
            is_checked = False

        self.latitude_label.setEnabled(is_checked)
        self.latitude_spin.setEnabled(is_checked)
        
        self.longitude_label.setEnabled(is_checked)
        self.longitude_spin.setEnabled(is_checked)

        self.target_label.setEnabled(is_checked)
        self.target_combo.setEnabled(is_checked)
    
    def set_convert_button_state(self):
        out_dir = Path(self.output_path_edit.text())

        do_apng = self.apng_check.isChecked()
        do_avif = self.avif_check.isChecked()
        do_webp = self.webp_check.isChecked()
        do_gif = self.gif_check.isChecked()
        do_mp4 = self.mp4_check.isChecked()
        do_webm = self.webm_check.isChecked()
        has_input = self.frames_table.model().rowCount(0) > 0
        has_output_dir = out_dir.exists() and out_dir.is_absolute()
        has_output_name = len(self.output_name_edit.text()) > 0
        do_derotate = self.enable_check.isChecked()
        derotate_and_target = (not do_derotate) or (do_derotate and not self.target_combo.currentText() not in convert.TARGETS.keys())

        self.convert_button.setEnabled((do_apng or do_avif or do_webp or do_gif or do_mp4 or do_webm) and has_input and has_output_dir and has_output_name and derotate_and_target)
    
    def update_ffmpeg_widgets(self):
        is_valid_ffmpeg = convert.validate_ffmpeg(self.settings.ffmpeg_path)
        
        if not is_valid_ffmpeg["avc"] and not is_valid_ffmpeg["av1"] and not is_valid_ffmpeg["vp9"]:
            self.video_stack.setCurrentIndex(1)
            return

        self.video_stack.setCurrentIndex(0)

        self.can_avc = is_valid_ffmpeg["avc"]
        self.can_av1 = is_valid_ffmpeg["av1"]
        self.can_vp9 = is_valid_ffmpeg["vp9"]

        self.mp4_check.setEnabled(self.can_av1 and self.can_vp9 and self.can_avc)
        self.webm_check.setEnabled(self.can_av1 and self.can_vp9)

        self.mp4_codec_combo.setEnabled(self.can_av1 or self.can_vp9 or self.can_avc)
        self.webm_codec_combo.setEnabled(self.can_av1 or self.can_vp9)
        mp4_selection = self.mp4_codec_combo.currentText()
        webm_selection = self.webm_codec_combo.currentText()
        self.mp4_codec_combo.clear()
        self.webm_codec_combo.clear()
        if self.can_avc:
            self.mp4_codec_combo.addItem("AVC")
        if self.can_av1:
            self.mp4_codec_combo.addItem("AV1")
            self.webm_codec_combo.addItem("AV1")
        if self.can_vp9:
            self.mp4_codec_combo.addItem("VP9")
            self.webm_codec_combo.addItem("VP9")
        self.mp4_codec_combo.setCurrentText(mp4_selection)
        self.webm_codec_combo.setCurrentText(webm_selection)
    
    def view_frame(self, index):
        row = index.row()
        column = index.column()
        if column == 0:
            if SYSTEM == 'Windows':
                os.startfile(self.paths[row].path)
            elif SYSTEM == 'Darwin':
                subprocess.call(('open', self.paths[row].path.absolute()))
            else:
                subprocess.call(('xdg-open', self.paths[row].path.absolute()))
    
    def on_convert_start(self):
        self.setting_changed.emit()
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        self.setEnabled(False)
        self.worker_thread = QThread()
        print(f'{self.mp4_codec_combo.currentText()} {convert.MP4Codec[self.mp4_codec_combo.currentText()]}')
        print(f'{self.webm_codec_combo.currentText()} {convert.WebMCodec[self.webm_codec_combo.currentText()]}')
        self.worker = ConvertWorker(
            self.paths,
            Path(self.output_path_edit.text(), self.output_name_edit.text()),
            self.duration_spinbox.value(),
            self.gif_check.isChecked(),
            self.webp_check.isChecked(),
            self.apng_check.isChecked(),
            self.avif_check.isChecked(),
            self.mp4_check.isChecked(),
            self.webm_check.isChecked(),
            convert.MP4Codec[self.mp4_codec_combo.currentText()],
            convert.WebMCodec[self.webm_codec_combo.currentText()],
            self.quality_spinbox.value(),
            self.lossless_check.isChecked(),
            self.enable_check.isChecked(),
            self.latitude_spin.value(),
            self.longitude_spin.value(),
            self.target_combo.currentText(),
        )
        self.worker.moveToThread(self.worker_thread)
        self.worker.finished.connect(self.on_convert_end)
        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.worker_thread.start()
    
    def on_convert_end(self):
        QApplication.restoreOverrideCursor()
        self.setEnabled(True)

        if not self.show_folder_check.isChecked():
            return

        if SYSTEM == 'Windows':
            os.startfile(self.output_path_edit.text())
        elif SYSTEM == 'Darwin':
            subprocess.call(('open', self.output_path_edit.text()))
        else:
            subprocess.call(('xdg-open', self.output_path_edit.text()))


class ConvertWorker(QObject):
    finished = Signal()

    def __init__(self, paths: list[convert.Frame], output: str, duration: int, gif: bool, webp: bool, apng: bool, avif: bool, mp4: bool, webm: bool, mp4_codec: convert.MP4Codec, webm_codec: convert.WebMCodec, quality: int, lossless: bool=True, derotate: bool=False, latitude: float=0, longitude: float=0, target: str=None):
        super().__init__()
        self.paths = paths
        self.output = output
        self.duration = duration
        self.gif = gif
        self.webp = webp
        self.apng = apng
        self.avif = avif
        self.mp4 = mp4
        self.webm = webm
        self.mp4_codec = mp4_codec
        self.webm_codec = webm_codec
        self.quality = quality
        self.lossless = lossless
        self.derotate = derotate
        self.latitude = latitude
        self.longitude = longitude
        self.target = target


    def run(self):
        try:
            convert.save(
                self.paths,
                self.output,
                self.duration,
                self.gif,
                self.webp,
                self.apng,
                self.avif,
                self.mp4,
                self.webm,
                self.mp4_codec,
                self.webm_codec,
                self.quality,
                self.lossless,
                self.derotate,
                self.latitude,
                self.longitude,
                self.target,
            )
        finally:
            self.finished.emit()


class TableModel(QAbstractTableModel):
    def __init__(self, data: list[convert.Frame]):
        super().__init__()
        self.table_data = data
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            obj = self.table_data[index.row()]
            if index.column() == 0:
                return obj.path.name
            elif index.column() == 1:
                return str(obj.date_time.strftime("%Y-%m-%d %H:%M:%S UTC")) if obj.date_time else ""

    def rowCount(self, index):
        return len(self.table_data)

    def columnCount(self, index):
        return 2
    
    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        #for setting columns name
        if orientation == Qt.Horizontal and role == Qt.DisplayRole and section == 0:
            return "Name"
        elif orientation == Qt.Horizontal and role == Qt.DisplayRole and section == 1:
            return "Time"
        #for setting rows name
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return f"{section + 1}"

