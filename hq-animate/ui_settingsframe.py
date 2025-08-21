# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsframe.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_SettingsFrame(object):
    def setupUi(self, SettingsFrame):
        if not SettingsFrame.objectName():
            SettingsFrame.setObjectName(u"SettingsFrame")
        SettingsFrame.resize(550, 500)
        SettingsFrame.setMinimumSize(QSize(550, 500))
        SettingsFrame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(SettingsFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ffmpeg_path_label = QLabel(SettingsFrame)
        self.ffmpeg_path_label.setObjectName(u"ffmpeg_path_label")

        self.horizontalLayout.addWidget(self.ffmpeg_path_label)

        self.ffmpeg_path_edit = QLineEdit(SettingsFrame)
        self.ffmpeg_path_edit.setObjectName(u"ffmpeg_path_edit")

        self.horizontalLayout.addWidget(self.ffmpeg_path_edit)

        self.ffmpeg_browse_button = QPushButton(SettingsFrame)
        self.ffmpeg_browse_button.setObjectName(u"ffmpeg_browse_button")

        self.horizontalLayout.addWidget(self.ffmpeg_browse_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(SettingsFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.dependencies_textbox = QPlainTextEdit(SettingsFrame)
        self.dependencies_textbox.setObjectName(u"dependencies_textbox")
        self.dependencies_textbox.setUndoRedoEnabled(False)
        self.dependencies_textbox.setReadOnly(True)

        self.verticalLayout.addWidget(self.dependencies_textbox)

        self.back_button = QPushButton(SettingsFrame)
        self.back_button.setObjectName(u"back_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.back_button)

#if QT_CONFIG(shortcut)
        self.ffmpeg_path_label.setBuddy(self.ffmpeg_browse_button)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(SettingsFrame)

        QMetaObject.connectSlotsByName(SettingsFrame)
    # setupUi

    def retranslateUi(self, SettingsFrame):
        SettingsFrame.setWindowTitle(QCoreApplication.translate("SettingsFrame", u"Frame", None))
        self.ffmpeg_path_label.setText(QCoreApplication.translate("SettingsFrame", u"&FFmpeg path", None))
        self.ffmpeg_browse_button.setText(QCoreApplication.translate("SettingsFrame", u"Browse...", None))
        self.back_button.setText(QCoreApplication.translate("SettingsFrame", u"&Back", None))
    # retranslateUi

