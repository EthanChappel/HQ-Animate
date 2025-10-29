'''
MIT License

Copyright (c) 2025 Ethan Chappel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


import os
import logging
from pathlib import Path
import platform
import subprocess
import traceback
from PIL import Image
from PySide6.QtCore import Signal, QAbstractTableModel, Qt, QThread, QObject
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QFrame, QFileDialog, QHeaderView, QApplication, QMessageBox
from hq_animate.ui_mainframe import Ui_MainFrame
from hq_animate import convert


SYSTEM = platform.system()
SCRIPT_PATH = Path(__file__).resolve().parent


logger = logging.getLogger("app")


class MainFrame(QFrame, Ui_MainFrame):
    settings_clicked = Signal()
    setting_changed = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.worker_thread = None
        self.worker = None
        
        self.paths = []

        self.settings = parent.settings

        self.frames_table.setModel(TableModel(self.paths))
        self.frames_table.verticalHeader().setVisible(False)
        self.frames_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.frames_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.frames_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.frames_table.horizontalHeader().setVisible(False)

        self.target_combo.addItems(convert.TARGETS.keys())
        self.target_combo.setCurrentIndex(-1)

        self.apng_check.setChecked(self.settings.do_apng)
        self.avif_check.setChecked(self.settings.do_avif)
        self.webp_check.setChecked(self.settings.do_webp)
        self.gif_check.setChecked(self.settings.do_gif)
        self.mp4_check.setChecked(self.settings.do_mp4)
        self.webm_check.setChecked(self.settings.do_webm)

        self.apng_check.stateChanged.connect(self.set_convert_button_state)
        self.avif_check.stateChanged.connect(self.set_convert_button_state)
        self.webp_check.stateChanged.connect(self.set_convert_button_state)
        self.gif_check.stateChanged.connect(self.set_convert_button_state)
        self.mp4_check.stateChanged.connect(self.set_convert_button_state)
        self.webm_check.stateChanged.connect(self.set_convert_button_state)

        self.apng_options_button.clicked.connect(lambda: self.formats_stack.setCurrentWidget(self.apng_page))
        self.avif_options_button.clicked.connect(lambda: self.formats_stack.setCurrentWidget(self.avif_page))
        self.webp_options_button.clicked.connect(lambda: self.formats_stack.setCurrentWidget(self.webp_page))
        self.gif_options_button.clicked.connect(lambda: self.formats_stack.setCurrentWidget(self.gif_page))
        self.mp4_options_button.clicked.connect(lambda: self.formats_stack.setCurrentWidget(self.mp4_page))
        self.webm_options_button.clicked.connect(lambda: self.formats_stack.setCurrentWidget(self.webm_page))

        self.apng_back_button.clicked.connect(self.view_format_page)
        self.avif_back_button.clicked.connect(self.view_format_page)
        self.webp_back_button.clicked.connect(self.view_format_page)
        self.gif_back_button.clicked.connect(self.view_format_page)
        self.mp4_back_button.clicked.connect(self.view_format_page)
        self.webm_back_button.clicked.connect(self.view_format_page)

        self.apng_compress_spinner.setValue(self.settings.apng_options.compression_level)
        self.apng_optimize_check.setChecked(self.settings.apng_options.optimize)

        self.avif_quality_spinner.setValue(self.settings.avif_options.quality)

        self.webp_quality_spinner.setValue(self.settings.webp_options.quality)
        self.webp_lossless_check.setChecked(self.settings.webp_options.lossless)

        self.gif_optimize_check.setChecked(self.settings.gif_options.optimize)

        for m in convert.AnimationMode:
            self.mode_combo.addItem(m.name)
        
        self.mode_combo.setCurrentIndex(int(self.settings.animation_options.animation_mode))

        self.duration_spinbox.setValue(self.settings.frame_length)
        self.derotation_group.setChecked(self.settings.field_derotation)
        self.latitude_spin.setValue(self.settings.derotation_options.latitude)
        self.longitude_spin.setValue(self.settings.derotation_options.longitude)
        self.alt_tilt_spin.setValue(self.settings.derotation_options.altitude_tilt)
        self.az_tilt_spin.setValue(self.settings.derotation_options.azimuth_tilt)
        self.show_folder_check.setChecked(self.settings.show_folder)

        self.output_path_edit.textChanged.connect(self.set_convert_button_state)
        self.output_name_edit.textChanged.connect(self.set_convert_button_state)
        self.derotation_group.toggled.connect(self.set_convert_button_state)
        self.target_combo.currentIndexChanged.connect(self.set_convert_button_state)

        self.input_browse_button.clicked.connect(self.set_input_frames)
        self.output_browse_button.clicked.connect(self.set_output_path)
        self.derotation_group.toggled.connect(self.set_field_derotation_state)
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

        if self.settings.mp4_options:
            self.mp4_codec_combo.setCurrentText(self.settings.mp4_options.codec.name)
            self.mp4_quality_spinner.setValue(self.settings.mp4_options.quality)
        if self.settings.webm_options:
            self.webm_codec_combo.setCurrentText(self.settings.webm_options.codec.name)
            self.webm_quality_spinner.setValue(self.settings.webm_options.quality)
        
        self.loop_spinner.setValue(self.settings.video_options.loop)

    
    def set_input_frames(self, event):
        paths, _ = QFileDialog.getOpenFileNames(self, "Select animation frames...", self.output_path_edit.text(), f"Images ({self.wildcards})")

        if paths:
            self.paths.clear()
            self.frames_table.horizontalHeader().setVisible(True)
            enable_field_rotation_option = True
            target = None
            self.frames_table.model().beginResetModel()
            self.frames_table.hideColumn(1)
            max_width = 0
            max_height = 0
            duration = 0
            for p in paths:
                f = convert.Frame(p)
                max_width = max(max_width, f.width)
                max_height = max(max_height, f.height)
                self.paths.append(f)
                if not target:
                    target = f.target
                    enable_field_rotation_option = enable_field_rotation_option and f.date_time is not None and f.target is not None
                if f.date_time:
                    self.frames_table.showColumn(1)
                if duration == 0:
                    duration = f.duration
            if self.all_dates():
                self.paths.sort(key=lambda f: f.date_time)
            self.frames_table.model().endResetModel()
            self.derotation_group.setEnabled(enable_field_rotation_option)
            self.set_field_derotation_state()
            if target:
                self.target_combo.setCurrentText(target)
            self.output_path_edit.setText(str(self.paths[0].path.parent))
            self.width_spinner.setValue(max_width)
            self.height_spinner.setValue(max_height)
            if duration > 0:
                self.duration_spinbox.setValue(duration)
        
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
    
    def all_dates(self):
        for f in self.paths:
            if not f.date_time:
                return False
        return len(self.paths) > 0
    
    def set_field_derotation_state(self, index=None):
        is_enabled = self.all_dates()
        is_checked = self.derotation_group.isChecked() and (is_enabled or len(self.paths) == 0)
        
        self.derotation_group.setEnabled(is_enabled)
        self.derotation_group.setChecked(is_checked)
    
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
        do_derotate = self.derotation_group.isChecked()
        derotate_and_target = (not do_derotate) or (do_derotate and not self.target_combo.currentText() not in convert.TARGETS.keys())

        self.convert_button.setEnabled((do_apng or do_avif or do_webp or do_gif or do_mp4 or do_webm) and has_input and has_output_dir and has_output_name and derotate_and_target)
    
    def update_ffmpeg_widgets(self):
        is_valid_ffmpeg = convert.validate_ffmpeg(self.settings.ffmpeg_path)

        self.can_avc = is_valid_ffmpeg["avc"]
        self.can_av1 = is_valid_ffmpeg["av1"]
        self.can_vp9 = is_valid_ffmpeg["vp9"]

        can_mp4 = self.can_av1 or self.can_vp9 or self.can_avc
        can_webm = self.can_av1 and self.can_vp9
        can_video = can_mp4 and can_webm

        self.loop_label.setVisible(can_video)
        self.loop_spinner.setVisible(can_video)
        
        if not can_video:
            self.video_stack.setCurrentIndex(1)
            return

        self.video_stack.setCurrentIndex(0)

        self.mp4_check.setEnabled(can_mp4)
        self.webm_check.setEnabled(can_webm)

        if not can_mp4:
            self.mp4_check.setChecked(False)
        if not can_webm:
            self.webm_check.setChecked(False)

        self.mp4_codec_combo.setEnabled(can_mp4)
        self.webm_codec_combo.setEnabled(can_webm)

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

        frame_path = self.paths[row].path.absolute()

        logger.info(f"View frame Path={frame_path}")

        if column == 0:
            if SYSTEM == 'Windows':
                os.startfile(frame_path)
            elif SYSTEM == 'Darwin':
                subprocess.Popen(('open', frame_path))
            else:
                subprocess.Popen(('xdg-open', frame_path))
    
    def view_format_page(self):
        self.formats_stack.setCurrentWidget(self.formats_page)
    
    def on_convert_start(self):
        logger.info("Disable GUI while processing frames.")
        self.setting_changed.emit()
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        self.setEnabled(False)

        apng_options = None
        if self.apng_check.isChecked():
            apng_options = convert.APNGOptions(self.apng_compress_spinner.value(), self.apng_optimize_check.isChecked())
        
        avif_options = None
        if self.avif_check.isChecked():
            avif_options = convert.AVIFOptions(self.avif_quality_spinner.value())
        
        webp_options = None
        if self.webp_check.isChecked():
            webp_options = convert.WebPOptions(self.webp_quality_spinner.value(), self.webp_lossless_check.isChecked())
        
        gif_options = None
        if self.gif_check.isChecked():
            gif_options = convert.GIFOptions(self.gif_optimize_check.isChecked())
        
        mp4_options = None
        if self.mp4_check.isChecked():
            mp4_options = convert.MP4Options(self.mp4_quality_spinner.value(), convert.MP4Codec[self.mp4_codec_combo.currentText()])
        
        webm_options = None
        if self.webm_check.isChecked():
            webm_options = convert.WebMOptions(self.webm_quality_spinner.value(), convert.WebMCodec[self.webm_codec_combo.currentText()])

        derotation_options = None
        if self.derotation_group.isChecked():
            derotation_options = convert.DerotationOptions(self.latitude_spin.value(), self.longitude_spin.value(), self.alt_tilt_spin.value(), self.az_tilt_spin.value(), self.target_combo.currentText())
        
        video_options = convert.VideoOptions(self.loop_spinner.value())

        process_options = convert.ProcessOptions(self.width_spinner.value(), self.height_spinner.value(), self.rotate_spinner.value(), self.average_spinner.value(), self.subtract_check.isChecked(), self.spread_spinner.value())
        animation_options = convert.AnimationOptions(convert.AnimationMode[self.mode_combo.currentText()])

        self.worker_thread = QThread()
        self.worker = ConvertWorker(
            tuple(self.paths),
            Path(self.output_path_edit.text(), self.output_name_edit.text()),
            self.duration_spinbox.value(),
            apng_options,
            avif_options,
            gif_options,
            webp_options,
            mp4_options,
            webm_options,
            derotation_options,
            video_options,
            process_options,
            animation_options,
            Path(self.settings.ffmpeg_path),
        )
        self.worker.moveToThread(self.worker_thread)
        self.worker.finished.connect(self.on_convert_end)
        self.worker.error.connect(self.on_convert_error)
        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.error.connect(self.worker_thread.quit)
        self.worker.error.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker.deleteLater)
        self.worker_thread.start()
    
    def on_convert_end(self):
        logger.info("Enable GUI after processing frames.")
        
        QApplication.restoreOverrideCursor()
        self.setEnabled(True)

        if not self.show_folder_check.isChecked():
            return

        open_path = self.output_path_edit.text()
        
        logger.info(f"Show folder: {open_path}")

        if SYSTEM == 'Windows':
            os.startfile(open_path)
        elif SYSTEM == 'Darwin':
            subprocess.Popen(('open', open_path))
        else:
            subprocess.Popen(('xdg-open', open_path))
    
    def on_convert_error(self, error: str):
        QApplication.restoreOverrideCursor()
        logger.error(f"Error while converting:\n{error}")
        messagebox = QMessageBox(QMessageBox.Icon.Critical, "HQ Animate - Error while converting", "Unable to create some or all animations due to an error.", parent=self)
        messagebox.setDetailedText(error)
        messagebox.exec()

        self.on_convert_end()


class ConvertWorker(QObject):
    finished = Signal()
    error = Signal(str)

    process_result: convert.ProcessResult = convert.ProcessResult()

    def __init__(self, paths: tuple[convert.Frame], output: Path, duration: int, apng_options: convert.APNGOptions=None, avif_options: convert.AVIFOptions=None, gif_options: convert.GIFOptions=None, webp_options: convert.WebPOptions=None, mp4_options: convert.MP4Options=None, webm_options: convert.WebMOptions=None, derotation_options: convert.DerotationOptions=None, video_options: convert.VideoOptions=None, process_options: convert.ProcessOptions=None, animation_options: convert.AnimationOptions=None, ffmpeg_path: Path=None):
        super().__init__()
        self.paths = paths
        self.output = output
        self.duration = duration
        self.apng_options = apng_options
        self.avif_options = avif_options
        self.webp_options = webp_options
        self.mp4_options = mp4_options
        self.webm_options = webm_options
        self.gif_options = gif_options
        self.derotation_options = derotation_options
        self.video_options = video_options
        self.process_options = process_options
        self.animation_options = animation_options
        self.ffmpeg_path = ffmpeg_path


    def run(self):
        try:
            image_paths = tuple(map(lambda x: x.path, self.paths))
            newest_modified = max(map(lambda x: Path(x.path).stat().st_mtime, self.paths))

            if image_paths == ConvertWorker.process_result.image_paths and newest_modified == ConvertWorker.process_result.newest_modified and self.derotation_options == ConvertWorker.process_result.derotation_options and self.process_options == ConvertWorker.process_result.process_options:
                frames = ConvertWorker.process_result.frames
                icc_profile = ConvertWorker.process_result.icc_profile
                is_color = ConvertWorker.process_result.is_color
            else:
                frames, icc_profile, is_color = convert.process_frames(self.paths, self.derotation_options, self.process_options)
                ConvertWorker.process_result = convert.ProcessResult(image_paths, newest_modified, self.derotation_options, self.process_options, frames, icc_profile, is_color)

            convert.save_animations(
                frames,
                icc_profile,
                is_color,
                self.output,
                self.duration,
                self.apng_options,
                self.avif_options,
                self.gif_options,
                self.webp_options,
                self.mp4_options,
                self.video_options,
                self.webm_options,
                self.animation_options,
                self.ffmpeg_path,
            )
            self.finished.emit()
        except Exception as e:
            self.error.emit(traceback.format_exc())
            


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

