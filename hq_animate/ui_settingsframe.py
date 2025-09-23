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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_SettingsFrame(object):
    def setupUi(self, SettingsFrame):
        if not SettingsFrame.objectName():
            SettingsFrame.setObjectName(u"SettingsFrame")
        SettingsFrame.resize(650, 700)
        SettingsFrame.setMinimumSize(QSize(650, 700))
        SettingsFrame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(SettingsFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ffmpeg_path_label = QLabel(SettingsFrame)
        self.ffmpeg_path_label.setObjectName(u"ffmpeg_path_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ffmpeg_path_label.sizePolicy().hasHeightForWidth())
        self.ffmpeg_path_label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.ffmpeg_path_label)

        self.ffmpeg_path_combo = QComboBox(SettingsFrame)
        self.ffmpeg_path_combo.setObjectName(u"ffmpeg_path_combo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ffmpeg_path_combo.sizePolicy().hasHeightForWidth())
        self.ffmpeg_path_combo.setSizePolicy(sizePolicy1)
        self.ffmpeg_path_combo.setEditable(True)

        self.horizontalLayout.addWidget(self.ffmpeg_path_combo)

        self.ffmpeg_browse_button = QPushButton(SettingsFrame)
        self.ffmpeg_browse_button.setObjectName(u"ffmpeg_browse_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ffmpeg_browse_button.sizePolicy().hasHeightForWidth())
        self.ffmpeg_browse_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.ffmpeg_browse_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(SettingsFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.dependencies_textbox = QTextBrowser(SettingsFrame)
        self.dependencies_textbox.setObjectName(u"dependencies_textbox")
        self.dependencies_textbox.setOpenLinks(False)

        self.verticalLayout.addWidget(self.dependencies_textbox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.back_button = QPushButton(SettingsFrame)
        self.back_button.setObjectName(u"back_button")
        sizePolicy2.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.open_logs_button = QPushButton(SettingsFrame)
        self.open_logs_button.setObjectName(u"open_logs_button")

        self.horizontalLayout_2.addWidget(self.open_logs_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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
        self.open_logs_button.setText(QCoreApplication.translate("SettingsFrame", u"Open logs folder...", None))
    # retranslateUi

