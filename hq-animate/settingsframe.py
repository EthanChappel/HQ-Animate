import platform
from pathlib import Path
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QFileDialog
from .settings import Settings
from .ui_settingsframe import Ui_SettingsFrame


SYSTEM = platform.system()
SCRIPT_PATH = Path(__file__).resolve().parent


class SettingsFrame(QFrame, Ui_SettingsFrame):
    back_clicked = Signal()
    setting_changed = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.settings = Settings.from_file_or_default(Path(SCRIPT_PATH, "settings.json"))
        
        with open(Path(SCRIPT_PATH, "dep-terms.txt"), "r", encoding='utf-16-le') as f:
            self.dependencies_textbox.setPlainText(f.read())
        
        self.ffmpeg_path_edit.setText(str(self.settings.ffmpeg_path))

        self.back_button.clicked.connect(self.switch_to_main_page)

        self.ffmpeg_path_edit.editingFinished.connect(self.ffmpeg_path_edited)
        self.ffmpeg_browse_button.clicked.connect(self.set_ffmpeg_path)
    
    def set_ffmpeg_path(self, event):
        wildcards = "Executable files (*.exe)" if SYSTEM == 'Windows' else "Executable files (*)"
        path, _ = QFileDialog.getOpenFileName(self, "Select FFmpeg executable...", self.ffmpeg_path_edit.text(), wildcards)

        if path:
            self.ffmpeg_path_edit.setText(path)
            self.setting_changed.emit()
    
    def ffmpeg_path_edited(self):
        self.setting_changed.emit()
    
    def switch_to_main_page(self):
        self.back_clicked.emit()
