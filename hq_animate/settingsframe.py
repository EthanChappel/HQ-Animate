import logging
import platform
from importlib.metadata import version
from pathlib import Path
import subprocess
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QFileDialog
from hq_animate.ui_settingsframe import Ui_SettingsFrame


SYSTEM = platform.system()
SCRIPT_PATH = Path(__file__).resolve().parent


logger = logging.getLogger("app")


class SettingsFrame(QFrame, Ui_SettingsFrame):
    back_clicked = Signal()
    setting_changed = Signal()

    def __init__(self, parent, ffmpeg_paths: list[Path]):
        super().__init__(parent)
        self.setupUi(self)

        self.settings = parent.settings

        self.version_label.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">HQ Animate</span><br/>"
            f"<span style=\" font-weight:700;\"></span><span>{version("hq_animate")}</span><br/>"
            "</span>©2025 Ethan Chappel</p></body></html>"
        )
        
        with open(Path(SCRIPT_PATH, "dep-terms.txt"), "r", encoding='utf-16-le') as f:
            self.dependencies_textbox.setPlainText(f.read())
        
        ffmpeg = Path(self.settings.ffmpeg_path).absolute()

        self.ffmpeg_path_combo.addItems([str(p.absolute()) for p in ffmpeg_paths])
        if ffmpeg.exists():
            s = str(ffmpeg)
            if self.ffmpeg_path_combo.findText(s) == -1:
                self.ffmpeg_path_combo.addItem(s)
            self.ffmpeg_path_combo.setCurrentText(s)

        self.back_button.clicked.connect(self.switch_to_main_page)
        self.open_logs_button.clicked.connect(self.open_logs_path)

        self.ffmpeg_path_combo.lineEdit().editingFinished.connect(self.ffmpeg_path_edited)
        self.ffmpeg_browse_button.clicked.connect(self.set_ffmpeg_path)
    
    def set_ffmpeg_path(self, event):
        wildcards = "Executable files (*.exe)" if SYSTEM == 'Windows' else "Executable files (*)"
        path, _ = QFileDialog.getOpenFileName(self, "Select FFmpeg executable...", self.ffmpeg_path_combo.currentText(), wildcards)

        if not path:
            return
        
        path = str(Path(path).absolute())
        
        if self.ffmpeg_path_combo.findText(path) == -1:
            self.ffmpeg_path_combo.addItem(path)
        
        self.ffmpeg_path_combo.setCurrentText(path)
        self.setting_changed.emit()
    
    def open_logs_path(self):
        log_file_path = None
        for handler in logger.handlers:
            if isinstance(handler, (logging.FileHandler)):
                log_file_path = handler.baseFilename
                break
        
        logging.info(log_file_path)
        
        if SYSTEM == "Windows":
            subprocess.Popen(f"explorer /select,\"{log_file_path}\"", creationflags=subprocess.CREATE_NO_WINDOW)

    def ffmpeg_path_edited(self):
        self.setting_changed.emit()
    
    def switch_to_main_page(self):
        self.back_clicked.emit()
