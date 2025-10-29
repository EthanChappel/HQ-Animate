#!/usr/bin/env python3
'''
MIT License

Copyright (c) 2020-2025 Ethan Chappel

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


import sys
from datetime import datetime, timezone
import logging
from importlib.metadata import version
from pathlib import Path
from PySide6.QtWidgets import QApplication
import platformdirs
from hq_animate.mainwindow import MainWindow


__version__ = version("hq_animate")


log_path = Path(platformdirs.user_log_dir("hq-animate", "", ensure_exists=True))
Path.mkdir(log_path, exist_ok=True)

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(Path(log_path, f"log_{datetime.now(timezone.utc).strftime("%Y-%m-%d-%H-%M-%S.%f")}.txt"))
logger.addHandler(file_handler)

logger.info(f"HQ-Animate {__version__}")


def log_unhandled_exception(exc_type, exc_value, exc_traceback):
    logger.error("Unhandled exception:", exc_info=(exc_type, exc_value, exc_traceback))

def main():
    sys.excepthook = log_unhandled_exception

    logger.info(f"Starting application")

    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()

    logger.info(f"Closing application")

if __name__ == '__main__':
    main()
