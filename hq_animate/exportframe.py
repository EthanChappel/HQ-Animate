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
from PIL import ImageQt
from PySide6.QtCore import Signal, QAbstractTableModel, Qt, QThread, QObject, QTimer
from PySide6.QtGui import QCursor, QPixmap
from PySide6.QtWidgets import QFrame, QFileDialog, QHeaderView, QApplication, QMessageBox
from hq_animate.ui_exportframe import Ui_ExportFrame
from hq_animate.convert import AnimationMode, ProcessResult, AnimationOptions, APNGOptions, AVIFOptions, WebPOptions, GIFOptions, MP4Options, WebMOptions, VideoOptions, MP4Codec, WebMCodec, save_animations, validate_ffmpeg


SYSTEM = platform.system()
SCRIPT_PATH = Path(__file__).resolve().parent


logger = logging.getLogger("app")


class ExportFrame(QFrame, Ui_ExportFrame):
    back_clicked = Signal()
    setting_changed = Signal()
    export_complete = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.setAcceptDrops(True)

        self.preview_frames = tuple()
        self.preview_timer = QTimer(self)
        self.preview_counter = 0
        self.preview_direction = 1

        self.preview_timer.timeout.connect(self.on_preview_timeout)

        self.settings = parent.settings
        parent.main_frame.duration_set.connect(self.on_duration_set)
        parent.main_frame.convert_complete.connect(self.on_convert_complete)

        for m in AnimationMode:
            self.mode_combo.addItem(m.name)
        
        self.mode_combo.setCurrentIndex(int(self.settings.animation_options.animation_mode))

        self.duration_spinbox.setValue(self.settings.frame_length)
        self.duration_spinbox.editingFinished.connect(self.on_fps_change)
        self.mode_combo.currentIndexChanged.connect(self.on_fps_change)

        self.process_result = None

        self.apng_check.setChecked(self.settings.do_apng)
        self.avif_check.setChecked(self.settings.do_avif)
        self.webp_check.setChecked(self.settings.do_webp)
        self.gif_check.setChecked(self.settings.do_gif)
        self.mp4_check.setChecked(self.settings.do_mp4)
        self.webm_check.setChecked(self.settings.do_webm)

        self.apng_check.stateChanged.connect(self.set_export_button_state)
        self.avif_check.stateChanged.connect(self.set_export_button_state)
        self.webp_check.stateChanged.connect(self.set_export_button_state)
        self.gif_check.stateChanged.connect(self.set_export_button_state)
        self.mp4_check.stateChanged.connect(self.set_export_button_state)
        self.webm_check.stateChanged.connect(self.set_export_button_state)

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

        self.back_button.clicked.connect(self.switch_to_main_page)

        self.output_name_edit.textChanged.connect(self.set_export_button_state)

        self.apng_compress_spinner.setValue(self.settings.apng_options.compression_level)
        self.apng_optimize_check.setChecked(self.settings.apng_options.optimize)

        self.avif_quality_spinner.setValue(self.settings.avif_options.quality)

        self.webp_quality_spinner.setValue(self.settings.webp_options.quality)
        self.webp_lossless_check.setChecked(self.settings.webp_options.lossless)

        self.gif_optimize_check.setChecked(self.settings.gif_options.optimize)

        self.can_avc = False
        self.can_av1 = False
        self.can_vp9 = False

        self.can_mp4 = False
        self.can_webm = False

        parent.settings_updated.connect(self.update_settings)

        if self.settings.mp4_options:
            self.mp4_codec_combo.setCurrentText(self.settings.mp4_options.codec.name)
            self.mp4_quality_spinner.setValue(self.settings.mp4_options.quality)
        if self.settings.webm_options:
            self.webm_codec_combo.setCurrentText(self.settings.webm_options.codec.name)
            self.webm_quality_spinner.setValue(self.settings.webm_options.quality)

        self.export_button.clicked.connect(self.on_export_start)

        self.loop_spinner.setValue(self.settings.video_options.loop)

        self.update_ffmpeg_widgets()
        self.set_export_button_state()
    
    def set_export_button_state(self):
        do_apng = self.apng_check.isChecked()
        do_avif = self.avif_check.isChecked()
        do_webp = self.webp_check.isChecked()
        do_gif = self.gif_check.isChecked()
        do_mp4 = self.mp4_check.isChecked()
        do_webm = self.webm_check.isChecked()
        has_output_name = len(self.output_name_edit.text()) > 0

        self.export_button.setEnabled((do_apng or do_avif or do_webp or do_gif or do_mp4 or do_webm) and has_output_name)
    
    def update_ffmpeg_widgets(self):
        is_valid_ffmpeg = validate_ffmpeg(self.settings.ffmpeg_path)

        self.can_avc = is_valid_ffmpeg["avc"]
        self.can_av1 = is_valid_ffmpeg["av1"]
        self.can_vp9 = is_valid_ffmpeg["vp9"]

        self.can_mp4 = self.can_av1 or self.can_vp9 or self.can_avc
        self.can_webm = self.can_av1 or self.can_vp9
        can_video = self.can_mp4 or self.can_webm
        
        if not can_video:
            self.video_stack.setCurrentIndex(1)
            return

        self.video_stack.setCurrentIndex(0)

        self.mp4_check.setVisible(self.can_mp4)
        self.mp4_options_button.setVisible(self.can_mp4)

        self.webm_check.setVisible(self.can_webm)
        self.webm_options_button.setVisible(self.can_webm)

        if not self.can_mp4:
            self.mp4_check.setChecked(False)
        if not self.can_webm:
            self.webm_check.setChecked(False)

        self.mp4_codec_combo.setEnabled(self.can_mp4)
        self.webm_codec_combo.setEnabled(self.can_webm)

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

        self.loop_label.setVisible(can_video)
        self.loop_spinner.setVisible(can_video)
    
    def view_format_page(self):
        self.formats_stack.setCurrentWidget(self.formats_page)
    
    def switch_to_main_page(self):
        self.back_clicked.emit()
        self.preview_timer.stop()
    
    def on_duration_set(self, duration):
        self.duration_spinbox.setValue(duration)
    
    def on_convert_complete(self, process_result: ProcessResult):
        self.process_result = process_result
        self.preview_frames = [QPixmap.fromImageInPlace(ImageQt.ImageQt(f)) for f in self.process_result.frames]
        self.preview_timer.start(1000 // self.duration_spinbox.value())
        self.preview_counter = 0
        self.on_preview_timeout()
    
    def on_preview_timeout(self):
        current = AnimationMode(str(self.mode_combo.currentIndex()))
        if self.preview_counter == len(self.preview_frames) and current == AnimationMode.Loop:
            self.preview_counter = 0
            self.preview_direction = 1
        elif self.preview_counter == len(self.preview_frames) and current == AnimationMode.Rock:
            self.preview_counter -= 2
            self.preview_direction = -1
        elif self.preview_counter == 0 and current == AnimationMode.Rock:
            self.preview_direction = 1
        
        self.preview_label.setPixmap(self.preview_frames[self.preview_counter])
        self.preview_counter += 1 * self.preview_direction
    
    def on_fps_change(self):
        self.preview_timer.start(1000 // self.duration_spinbox.value())
        self.preview_direction = 1 if AnimationMode(str(self.mode_combo.currentIndex())) == AnimationMode.Loop else -1
        self.preview_counter = 0
    
    def update_settings(self):
        self.update_ffmpeg_widgets()

    def on_export_start(self):
        self.setting_changed.emit()
        apng_options = None
        if self.apng_check.isChecked():
            apng_options = APNGOptions(self.apng_compress_spinner.value(), self.apng_optimize_check.isChecked())
        
        avif_options = None
        if self.avif_check.isChecked():
            avif_options = AVIFOptions(self.avif_quality_spinner.value())
        
        webp_options = None
        if self.webp_check.isChecked():
            webp_options = WebPOptions(self.webp_quality_spinner.value(), self.webp_lossless_check.isChecked())
        
        gif_options = None
        if self.gif_check.isChecked():
            gif_options = GIFOptions(self.gif_optimize_check.isChecked())
        
        mp4_options = None
        if self.mp4_check.isChecked() and self.can_mp4:
            mp4_options = MP4Options(self.mp4_quality_spinner.value(), MP4Codec[self.mp4_codec_combo.currentText()])
        
        webm_options = None
        if self.webm_check.isChecked() and self.can_webm:
            webm_options = WebMOptions(self.webm_quality_spinner.value(), WebMCodec[self.webm_codec_combo.currentText()])
        
        video_options = VideoOptions(self.loop_spinner.value())

        animation_options = AnimationOptions(self.duration_spinbox.value(), AnimationMode[self.mode_combo.currentText()])

        path = QFileDialog.getExistingDirectory(self, "Select output folder...", "")

        if not path:
            return
        
        self.worker_thread = QThread()
        self.worker = ExportWorker(
            self.process_result,
            Path(path, self.output_name_edit.text()),
            apng_options,
            avif_options,
            gif_options,
            webp_options,
            mp4_options,
            webm_options,
            video_options,
            animation_options,
            Path(self.settings.ffmpeg_path),
        )

        self.worker.moveToThread(self.worker_thread)
        self.worker.finished.connect(self.on_export_end)
        self.worker.error.connect(self.on_export_error)
        self.worker_thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.worker_thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.error.connect(self.worker_thread.quit)
        self.worker.error.connect(self.worker.deleteLater)
        self.worker_thread.finished.connect(self.worker.deleteLater)

        logger.info("Disable GUI while exporting frames.")
        self.setting_changed.emit()
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        self.setEnabled(False)

        self.worker_thread.start()

    def on_export_end(self):
        logger.info("Enable GUI after processing frames.")
        
        self.export_complete.emit()

        QApplication.restoreOverrideCursor()
        self.setEnabled(True)
    
    def on_export_error(self, error: str):
        QApplication.restoreOverrideCursor()
        logger.error(f"Error while converting:\n{error}")
        messagebox = QMessageBox(QMessageBox.Icon.Critical, "HQ Animate - Error while converting", "Unable to create some or all animations due to an error.", parent=self)
        messagebox.setDetailedText(error)
        messagebox.exec()

        QApplication.restoreOverrideCursor()
        self.setEnabled(True)


class ExportWorker(QObject):
    finished = Signal()
    error = Signal(str)

    def __init__(self, process_result: ProcessResult, out_path: Path, apng_options: APNGOptions|None, avif_options: AVIFOptions|None, gif_options: GIFOptions|None, webp_options: WebPOptions|None, mp4_options: MP4Options|None, webm_options: WebMOptions|None, video_options: VideoOptions|None, animation_options: AnimationOptions|None, ffmpeg_path: Path|None):
        super().__init__()
        self.process_result = process_result
        self.out_path = out_path
        self.apng_options = apng_options
        self.avif_options = avif_options
        self.gif_options = gif_options
        self.webp_options = webp_options
        self.mp4_options = mp4_options
        self.webm_options = webm_options
        self.video_options = video_options
        self.animation_options = animation_options
        self.ffmpeg_path = ffmpeg_path


    def run(self):
        try:
            save_animations(
                self.process_result,
                self.out_path,
                self.apng_options,
                self.avif_options,
                self.gif_options,
                self.webp_options,
                self.mp4_options,
                self.webm_options,
                self.video_options,
                self.animation_options,
                self.ffmpeg_path,
            )

            self.finished.emit()
        except Exception as e:
            self.error.emit(traceback.format_exc())
