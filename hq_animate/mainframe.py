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
    duration_set = Signal(int)
    convert_complete = Signal(convert.ProcessResult)

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)

        self.worker_thread = None
        self.worker = None
        
        self.paths = []

        self.initial_dir = str(Path.home())

        self.settings = parent.settings

        self.frames_table.setModel(TableModel(self.paths))
        self.frames_table.verticalHeader().setVisible(False)
        self.frames_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.frames_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.frames_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.frames_table.horizontalHeader().setVisible(False)

        self.target_combo.addItems(convert.TARGETS.keys())
        self.target_combo.setCurrentIndex(-1)

        self.derotation_group.setChecked(self.settings.field_derotation)
        self.latitude_spin.setValue(self.settings.derotation_options.latitude)
        self.longitude_spin.setValue(self.settings.derotation_options.longitude)
        self.alt_tilt_spin.setValue(self.settings.derotation_options.altitude_tilt)
        self.az_tilt_spin.setValue(self.settings.derotation_options.azimuth_tilt)

        self.derotation_group.toggled.connect(self.set_convert_button_state)
        self.target_combo.currentIndexChanged.connect(self.set_convert_button_state)

        self.input_browse_button.clicked.connect(self.select_input_frames_dialog)
        self.derotation_group.toggled.connect(self.set_field_derotation_state)
        self.settings_button.clicked.connect(self.switch_to_settings_page)
        self.convert_button.clicked.connect(self.on_convert_start)
        self.supports_open = {ex for ex, f in Image.registered_extensions().items() if f in Image.OPEN}
        self.wildcards = " ".join(sorted({f"*{ex}" for ex in self.supports_open}))

        self.frames_table.doubleClicked.connect(self.view_frame)

        show_spread = self.subtract_check.isChecked()
        self.spread_label.setVisible(show_spread)
        self.spread_spinner.setVisible(show_spread)

        show_spread = self.subtract_check.isChecked()
        self.spread_label.setVisible(show_spread)
        self.spread_spinner.setVisible(show_spread)

        self.set_field_derotation_state()
        self.set_convert_button_state()

        
    def select_input_frames_dialog(self, event):

        paths, _ = QFileDialog.getOpenFileNames(self, "Select animation frames...", self.initial_dir, f"Images ({self.wildcards})")

        if paths:
            self.set_input_frames(paths)
            self.initial_dir = str(Path(paths[0]).parent)

    def set_input_frames(self, paths: list[str]):
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
        self.width_spinner.setValue(max_width)
        self.height_spinner.setValue(max_height)
        if duration > 0:
            self.duration_set.emit(1000 / duration)
        
        self.set_convert_button_state()
    
    def switch_to_settings_page(self):
        self.settings_clicked.emit()
    
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
        has_input = self.frames_table.model().rowCount(0) > 0
        do_derotate = self.derotation_group.isChecked()
        derotate_and_target = (not do_derotate) or (do_derotate and not self.target_combo.currentText() not in convert.TARGETS.keys())

        self.convert_button.setEnabled(has_input and derotate_and_target)
    
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
    
    def on_convert_start(self):
        logger.info("Disable GUI while processing frames.")
        self.setting_changed.emit()
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        self.setEnabled(False)

        derotation_options = None
        if self.derotation_group.isChecked():
            derotation_options = convert.DerotationOptions(self.latitude_spin.value(), self.longitude_spin.value(), self.alt_tilt_spin.value(), self.az_tilt_spin.value(), self.target_combo.currentText())

        process_options = convert.ProcessOptions(self.width_spinner.value(), self.height_spinner.value(), self.rotate_spinner.value(), self.average_spinner.value(), self.subtract_check.isChecked(), self.spread_spinner.value())

        self.worker_thread = QThread()
        self.worker = ConvertWorker(
            tuple(self.paths),
            derotation_options,
            process_options,
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
    
    def on_convert_end(self, process_result: convert.ProcessResult):
        logger.info("Enable GUI after processing frames.")
        
        self.convert_complete.emit(process_result)

        QApplication.restoreOverrideCursor()
        self.setEnabled(True)
    
    def on_convert_error(self, error: str):
        QApplication.restoreOverrideCursor()
        logger.error(f"Error while converting:\n{error}")
        messagebox = QMessageBox(QMessageBox.Icon.Critical, "HQ Animate - Error while converting", "Unable to create some or all animations due to an error.", parent=self)
        messagebox.setDetailedText(error)
        messagebox.exec()

        QApplication.restoreOverrideCursor()
        self.setEnabled(True)
    
    def ignore_drag_drop(self, event, message: str):
        self.drag_drop_label.setText(message)
        self.drag_drop_label.setVisible(True)
        event.ignore()
    
    def dragEnterEvent(self, event):
        if not event.mimeData().hasUrls():
            event.ignore()
            return
        
        not_supported_exts = set()

        paths = [Path(u.toLocalFile()) for u in event.mimeData().urls() if u.isLocalFile()]
        
        if len(paths) == 1 and paths[0].is_dir():
            paths = [p for p in paths[0].iterdir() if p.is_file()]
        
        dir_count = 0
        for path in paths:
            if path.is_dir():
                dir_count += 1

            suffix = path.suffix
            if not suffix in self.supports_open and path.is_file():
                not_supported_exts.add(suffix)
        
        paths_len = len(paths)
        not_supported_exts_len = len(not_supported_exts)
        joined_not_supported_exts = " ".join(not_supported_exts)
        
        if paths_len == 0:
            self.ignore_drag_drop(event, "Folder has no files")
            return
        elif dir_count > 1 and dir_count == paths_len:
            self.ignore_drag_drop(event, "Multiple folders are not supported")
            return
        elif dir_count > 0 and paths_len > 1:
            self.ignore_drag_drop(event, "Selecting files and folders is not supported")
            return
        elif not_supported_exts_len > 1:
            self.ignore_drag_drop(event, f"File types{joined_not_supported_exts} are not supported")
            return
        elif not_supported_exts_len > 0:
            self.ignore_drag_drop(event, f"File type {joined_not_supported_exts} is not supported")
            return
        
        event.acceptProposedAction()
    
    def dragLeaveEvent(self, event):
        if self.drag_drop_label.isVisible():
            self.drag_drop_label.setVisible(False)
        event.accept()
    
    def dropEvent(self, event):
        if not event.mimeData().hasUrls():
            event.ignore()
            return
        
        paths = [Path(u.toLocalFile()) for u in event.mimeData().urls() if u.isLocalFile()]

        if len(paths) == 1 and paths[0].is_dir():
            paths = [p for p in paths[0].iterdir() if p.is_file()]

        if len(paths) == 0:
            event.ignore()
            return

        self.set_input_frames([str(p) for p in paths])
        event.acceptProposedAction()


class ConvertWorker(QObject):
    finished = Signal(convert.ProcessResult)
    error = Signal(str)

    process_result: convert.ProcessResult = convert.ProcessResult()

    def __init__(self, paths: tuple[convert.Frame], derotation_options: convert.DerotationOptions=None, process_options: convert.ProcessOptions=None, ffmpeg_path: Path=None):
        super().__init__()
        self.paths = paths
        self.derotation_options = derotation_options
        self.process_options = process_options
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

            self.finished.emit(ConvertWorker.process_result)
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

