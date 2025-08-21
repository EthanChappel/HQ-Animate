import os
import platform
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QFrame, QFileDialog
from settings import Settings
from ui_settingsframe import Ui_SettingsFrame
from pathlib import Path


SYSTEM = platform.system()


class SettingsFrame(QFrame, Ui_SettingsFrame):
    back_clicked = Signal()
    setting_changed = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

        self.settings = Settings.from_file_or_default(Path("./settings.json"))

        if not self.settings.ffmpeg_path:
            exe_name = "ffmpeg.exe" if SYSTEM == "Windows" else "ffmpeg"

            for p in [Path(exe_name)] + [Path(p, exe_name) for p in os.environ["PATH"].split(os.pathsep)]:
                if p.is_file():
                    self.settings.ffmpeg_path = p.resolve()
                    break
        
        with open(Path("./dep-terms.txt"), "r", encoding='utf-16-le') as f:
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
