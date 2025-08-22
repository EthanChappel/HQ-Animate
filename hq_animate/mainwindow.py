import os
import platform
from pathlib import Path
import platformdirs
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QStackedWidget
from hq_animate import convert
from hq_animate.mainframe import MainFrame
from hq_animate.settings import Settings
from hq_animate.settingsframe import SettingsFrame


SYSTEM = platform.system()
SCRIPT_PATH = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    settings_updated = Signal()

    def __init__(self):
        super().__init__()

        self.settings = Settings.from_file_or_default(Path(platformdirs.user_config_dir("hq-animate", "", ensure_exists=True), "settings.json"))

        if not self.settings.ffmpeg_path:
            exe_name = "ffmpeg.exe" if SYSTEM == "Windows" else "ffmpeg"

            for p in [Path(SCRIPT_PATH, exe_name)] + [Path(p, exe_name) for p in os.environ["PATH"].split(os.pathsep)]:
                if p.is_file():
                    self.settings.ffmpeg_path = p.resolve()
                    break

        self.setWindowTitle("HQ Animate")

        self.stack_frame = QStackedWidget()

        self.main_frame = MainFrame(self)
        self.main_frame.setting_changed.connect(self.save_settings)
        self.main_frame.settings_clicked.connect(self.show_settings)
        self.stack_frame.addWidget(self.main_frame)
        
        self.settings_frame = SettingsFrame(self)
        self.settings_frame.setting_changed.connect(self.save_settings)
        self.settings_frame.back_clicked.connect(self.show_main)
        self.stack_frame.addWidget(self.settings_frame)

        # Set the central widget of the Window.
        self.setCentralWidget(self.stack_frame)
    
    def show_settings(self):
        self.stack_frame.setCurrentWidget(self.settings_frame)
    
    def save_settings(self):
        mp4_codec = self.main_frame.mp4_codec_combo.currentText()
        webm_codec = self.main_frame.webm_codec_combo.currentText()

        self.settings.field_derotation = self.main_frame.enable_check.isChecked()
        self.settings.latitude = self.main_frame.latitude_spin.value()
        self.settings.longitude = self.main_frame.longitude_spin.value()
        self.settings.do_apng = self.main_frame.apng_check.isChecked()
        self.settings.do_avif = self.main_frame.avif_check.isChecked()
        self.settings.do_webp = self.main_frame.webp_check.isChecked()
        self.settings.do_gif = self.main_frame.gif_check.isChecked()
        self.settings.do_mp4 = self.main_frame.mp4_check.isChecked()
        self.settings.do_webm = self.main_frame.webm_check.isChecked()
        self.settings.frame_length = self.main_frame.duration_spinbox.value()
        self.settings.quality = self.main_frame.quality_spinbox.value()
        self.settings.lossless = self.main_frame.lossless_check.isChecked()
        self.settings.mp4_codec = convert.MP4Codec[mp4_codec] if mp4_codec else None
        self.settings.webm_codec = convert.WebMCodec[webm_codec] if webm_codec else None
        self.settings.show_folder = self.main_frame.show_folder_check.isChecked()
        self.settings.ffmpeg_path = self.settings_frame.ffmpeg_path_edit.text()

        self.settings.save()
        self.settings_updated.emit()
    
    def show_main(self):
        self.stack_frame.setCurrentWidget(self.main_frame)
    
    def closeEvent(self, event):
        self.save_settings()
        return super().closeEvent(event)