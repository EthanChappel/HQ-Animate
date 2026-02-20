# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exportframe.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_ExportFrame(object):
    def setupUi(self, ExportFrame):
        if not ExportFrame.objectName():
            ExportFrame.setObjectName(u"ExportFrame")
        ExportFrame.resize(650, 700)
        ExportFrame.setMinimumSize(QSize(650, 700))
        self.verticalLayout = QVBoxLayout(ExportFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.scrollArea = QScrollArea(ExportFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 650, 393))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.preview_label = QLabel(self.scrollAreaWidgetContents)
        self.preview_label.setObjectName(u"preview_label")
        sizePolicy1.setHeightForWidth(self.preview_label.sizePolicy().hasHeightForWidth())
        self.preview_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.preview_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.options_frame = QFrame(ExportFrame)
        self.options_frame.setObjectName(u"options_frame")
        self.options_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.options_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.options_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, -1)
        self.formats_stack = QStackedWidget(self.options_frame)
        self.formats_stack.setObjectName(u"formats_stack")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.formats_stack.sizePolicy().hasHeightForWidth())
        self.formats_stack.setSizePolicy(sizePolicy2)
        self.formats_page = QWidget()
        self.formats_page.setObjectName(u"formats_page")
        self.verticalLayout_4 = QVBoxLayout(self.formats_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formats_group = QGroupBox(self.formats_page)
        self.formats_group.setObjectName(u"formats_group")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.formats_group.sizePolicy().hasHeightForWidth())
        self.formats_group.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.formats_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gif_options_button = QPushButton(self.formats_group)
        self.gif_options_button.setObjectName(u"gif_options_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.gif_options_button.sizePolicy().hasHeightForWidth())
        self.gif_options_button.setSizePolicy(sizePolicy4)
        self.gif_options_button.setMaximumSize(QSize(24, 24))
        self.gif_options_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.gif_options_button, 3, 1, 1, 1)

        self.video_stack = QStackedWidget(self.formats_group)
        self.video_stack.setObjectName(u"video_stack")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.video_stack.sizePolicy().hasHeightForWidth())
        self.video_stack.setSizePolicy(sizePolicy5)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_2 = QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mp4_check = QCheckBox(self.page_3)
        self.mp4_check.setObjectName(u"mp4_check")

        self.gridLayout_2.addWidget(self.mp4_check, 0, 0, 1, 1)

        self.mp4_options_button = QPushButton(self.page_3)
        self.mp4_options_button.setObjectName(u"mp4_options_button")
        sizePolicy4.setHeightForWidth(self.mp4_options_button.sizePolicy().hasHeightForWidth())
        self.mp4_options_button.setSizePolicy(sizePolicy4)
        self.mp4_options_button.setMaximumSize(QSize(24, 24))
        self.mp4_options_button.setAutoDefault(True)

        self.gridLayout_2.addWidget(self.mp4_options_button, 0, 1, 1, 1)

        self.webm_check = QCheckBox(self.page_3)
        self.webm_check.setObjectName(u"webm_check")

        self.gridLayout_2.addWidget(self.webm_check, 1, 0, 1, 1)

        self.webm_options_button = QPushButton(self.page_3)
        self.webm_options_button.setObjectName(u"webm_options_button")
        sizePolicy4.setHeightForWidth(self.webm_options_button.sizePolicy().hasHeightForWidth())
        self.webm_options_button.setSizePolicy(sizePolicy4)
        self.webm_options_button.setMaximumSize(QSize(24, 24))
        self.webm_options_button.setAutoDefault(True)

        self.gridLayout_2.addWidget(self.webm_options_button, 1, 1, 1, 1)

        self.video_stack.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.requires_ffmpeg_label = QLabel(self.page_4)
        self.requires_ffmpeg_label.setObjectName(u"requires_ffmpeg_label")
        sizePolicy2.setHeightForWidth(self.requires_ffmpeg_label.sizePolicy().hasHeightForWidth())
        self.requires_ffmpeg_label.setSizePolicy(sizePolicy2)
        self.requires_ffmpeg_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.requires_ffmpeg_label)

        self.video_stack.addWidget(self.page_4)

        self.gridLayout.addWidget(self.video_stack, 4, 0, 1, 2)

        self.avif_check = QCheckBox(self.formats_group)
        self.avif_check.setObjectName(u"avif_check")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.avif_check.sizePolicy().hasHeightForWidth())
        self.avif_check.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.avif_check, 1, 0, 1, 1)

        self.gif_check = QCheckBox(self.formats_group)
        self.gif_check.setObjectName(u"gif_check")
        sizePolicy6.setHeightForWidth(self.gif_check.sizePolicy().hasHeightForWidth())
        self.gif_check.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.gif_check, 3, 0, 1, 1)

        self.apng_check = QCheckBox(self.formats_group)
        self.apng_check.setObjectName(u"apng_check")
        sizePolicy6.setHeightForWidth(self.apng_check.sizePolicy().hasHeightForWidth())
        self.apng_check.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.apng_check, 0, 0, 1, 1)

        self.avif_options_button = QPushButton(self.formats_group)
        self.avif_options_button.setObjectName(u"avif_options_button")
        self.avif_options_button.setMaximumSize(QSize(24, 24))
        self.avif_options_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.avif_options_button, 1, 1, 1, 1)

        self.webp_check = QCheckBox(self.formats_group)
        self.webp_check.setObjectName(u"webp_check")
        sizePolicy6.setHeightForWidth(self.webp_check.sizePolicy().hasHeightForWidth())
        self.webp_check.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.webp_check, 2, 0, 1, 1)

        self.apng_options_button = QPushButton(self.formats_group)
        self.apng_options_button.setObjectName(u"apng_options_button")
        self.apng_options_button.setMaximumSize(QSize(24, 24))
        self.apng_options_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.apng_options_button, 0, 1, 1, 1)

        self.webp_options_button = QPushButton(self.formats_group)
        self.webp_options_button.setObjectName(u"webp_options_button")
        self.webp_options_button.setMaximumSize(QSize(24, 24))
        self.webp_options_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.webp_options_button, 2, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.formats_group)

        self.formats_stack.addWidget(self.formats_page)
        self.apng_page = QWidget()
        self.apng_page.setObjectName(u"apng_page")
        self.verticalLayout_11 = QVBoxLayout(self.apng_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.apng_page)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.apng_optimize_check = QCheckBox(self.groupBox)
        self.apng_optimize_check.setObjectName(u"apng_optimize_check")
        sizePolicy4.setHeightForWidth(self.apng_optimize_check.sizePolicy().hasHeightForWidth())
        self.apng_optimize_check.setSizePolicy(sizePolicy4)
        self.apng_optimize_check.setMinimumSize(QSize(25, 0))

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.apng_optimize_check)

        self.apng_compress_spinner = QSpinBox(self.groupBox)
        self.apng_compress_spinner.setObjectName(u"apng_compress_spinner")
        sizePolicy5.setHeightForWidth(self.apng_compress_spinner.sizePolicy().hasHeightForWidth())
        self.apng_compress_spinner.setSizePolicy(sizePolicy5)
        self.apng_compress_spinner.setMaximum(9)
        self.apng_compress_spinner.setValue(9)

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.apng_compress_spinner)

        self.apng_compress_label = QLabel(self.groupBox)
        self.apng_compress_label.setObjectName(u"apng_compress_label")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.apng_compress_label)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_6.setItem(2, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer_6)


        self.verticalLayout_12.addLayout(self.formLayout_6)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.apng_back_button = QPushButton(self.groupBox)
        self.apng_back_button.setObjectName(u"apng_back_button")
        self.apng_back_button.setAutoDefault(True)

        self.horizontalLayout_6.addWidget(self.apng_back_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_6)


        self.verticalLayout_11.addWidget(self.groupBox)

        self.formats_stack.addWidget(self.apng_page)
        self.avif_page = QWidget()
        self.avif_page.setObjectName(u"avif_page")
        self.verticalLayout_7 = QVBoxLayout(self.avif_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.avif_page)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy7)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.avif_quality_label = QLabel(self.groupBox_2)
        self.avif_quality_label.setObjectName(u"avif_quality_label")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.avif_quality_label)

        self.avif_quality_spinner = QSpinBox(self.groupBox_2)
        self.avif_quality_spinner.setObjectName(u"avif_quality_spinner")
        sizePolicy5.setHeightForWidth(self.avif_quality_spinner.sizePolicy().hasHeightForWidth())
        self.avif_quality_spinner.setSizePolicy(sizePolicy5)
        self.avif_quality_spinner.setMaximum(100)
        self.avif_quality_spinner.setSingleStep(5)
        self.avif_quality_spinner.setValue(95)

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.avif_quality_spinner)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_7.setItem(1, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer_5)


        self.verticalLayout_13.addLayout(self.formLayout_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.avif_back_button = QPushButton(self.groupBox_2)
        self.avif_back_button.setObjectName(u"avif_back_button")
        self.avif_back_button.setAutoDefault(True)

        self.horizontalLayout_7.addWidget(self.avif_back_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)


        self.verticalLayout_13.addLayout(self.horizontalLayout_7)


        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.formats_stack.addWidget(self.avif_page)
        self.webp_page = QWidget()
        self.webp_page.setObjectName(u"webp_page")
        self.verticalLayout_14 = QVBoxLayout(self.webp_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.webp_page)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy7.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy7)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.webp_quality_label = QLabel(self.groupBox_3)
        self.webp_quality_label.setObjectName(u"webp_quality_label")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.LabelRole, self.webp_quality_label)

        self.webp_quality_spinner = QSpinBox(self.groupBox_3)
        self.webp_quality_spinner.setObjectName(u"webp_quality_spinner")
        sizePolicy5.setHeightForWidth(self.webp_quality_spinner.sizePolicy().hasHeightForWidth())
        self.webp_quality_spinner.setSizePolicy(sizePolicy5)
        self.webp_quality_spinner.setMaximum(100)
        self.webp_quality_spinner.setSingleStep(5)
        self.webp_quality_spinner.setValue(95)

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.FieldRole, self.webp_quality_spinner)

        self.webp_lossless_label = QLabel(self.groupBox_3)
        self.webp_lossless_label.setObjectName(u"webp_lossless_label")

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.LabelRole, self.webp_lossless_label)

        self.webp_lossless_check = QCheckBox(self.groupBox_3)
        self.webp_lossless_check.setObjectName(u"webp_lossless_check")
        sizePolicy4.setHeightForWidth(self.webp_lossless_check.sizePolicy().hasHeightForWidth())
        self.webp_lossless_check.setSizePolicy(sizePolicy4)
        self.webp_lossless_check.setMaximumSize(QSize(25, 16777215))

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.FieldRole, self.webp_lossless_check)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_9.setItem(2, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer_4)


        self.verticalLayout_15.addLayout(self.formLayout_9)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.webp_back_button = QPushButton(self.groupBox_3)
        self.webp_back_button.setObjectName(u"webp_back_button")
        self.webp_back_button.setAutoDefault(True)

        self.horizontalLayout_9.addWidget(self.webp_back_button)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.verticalLayout_15.addLayout(self.horizontalLayout_9)


        self.verticalLayout_14.addWidget(self.groupBox_3)

        self.formats_stack.addWidget(self.webp_page)
        self.gif_page = QWidget()
        self.gif_page.setObjectName(u"gif_page")
        self.verticalLayout_10 = QVBoxLayout(self.gif_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.gif_page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy7.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy7)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.gif_optimize_check = QCheckBox(self.groupBox_4)
        self.gif_optimize_check.setObjectName(u"gif_optimize_check")
        sizePolicy4.setHeightForWidth(self.gif_optimize_check.sizePolicy().hasHeightForWidth())
        self.gif_optimize_check.setSizePolicy(sizePolicy4)
        self.gif_optimize_check.setMaximumSize(QSize(25, 16777215))

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.gif_optimize_check)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_8.setItem(1, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer_3)


        self.verticalLayout_16.addLayout(self.formLayout_8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gif_back_button = QPushButton(self.groupBox_4)
        self.gif_back_button.setObjectName(u"gif_back_button")
        self.gif_back_button.setAutoDefault(True)

        self.horizontalLayout_8.addWidget(self.gif_back_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)


        self.verticalLayout_10.addWidget(self.groupBox_4)

        self.formats_stack.addWidget(self.gif_page)
        self.mp4_page = QWidget()
        self.mp4_page.setObjectName(u"mp4_page")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.mp4_page.sizePolicy().hasHeightForWidth())
        self.mp4_page.setSizePolicy(sizePolicy8)
        self.verticalLayout_9 = QVBoxLayout(self.mp4_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.mp4_page)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.mp4_codec_label = QLabel(self.groupBox_5)
        self.mp4_codec_label.setObjectName(u"mp4_codec_label")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.mp4_codec_label)

        self.mp4_codec_combo = QComboBox(self.groupBox_5)
        self.mp4_codec_combo.setObjectName(u"mp4_codec_combo")
        sizePolicy5.setHeightForWidth(self.mp4_codec_combo.sizePolicy().hasHeightForWidth())
        self.mp4_codec_combo.setSizePolicy(sizePolicy5)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.mp4_codec_combo)

        self.mp4_quality_label = QLabel(self.groupBox_5)
        self.mp4_quality_label.setObjectName(u"mp4_quality_label")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.mp4_quality_label)

        self.mp4_quality_spinner = QSpinBox(self.groupBox_5)
        self.mp4_quality_spinner.setObjectName(u"mp4_quality_spinner")
        sizePolicy5.setHeightForWidth(self.mp4_quality_spinner.sizePolicy().hasHeightForWidth())
        self.mp4_quality_spinner.setSizePolicy(sizePolicy5)
        self.mp4_quality_spinner.setMinimum(1)
        self.mp4_quality_spinner.setMaximum(100)
        self.mp4_quality_spinner.setValue(95)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.mp4_quality_spinner)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_3.setItem(2, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer_2)


        self.verticalLayout_17.addLayout(self.formLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mp4_back_button = QPushButton(self.groupBox_5)
        self.mp4_back_button.setObjectName(u"mp4_back_button")
        self.mp4_back_button.setAutoDefault(True)

        self.horizontalLayout_5.addWidget(self.mp4_back_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addWidget(self.groupBox_5)

        self.formats_stack.addWidget(self.mp4_page)
        self.webm_page = QWidget()
        self.webm_page.setObjectName(u"webm_page")
        self.verticalLayout_6 = QVBoxLayout(self.webm_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.webm_page)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy7.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy7)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.webm_codec_combo = QComboBox(self.groupBox_6)
        self.webm_codec_combo.setObjectName(u"webm_codec_combo")
        sizePolicy5.setHeightForWidth(self.webm_codec_combo.sizePolicy().hasHeightForWidth())
        self.webm_codec_combo.setSizePolicy(sizePolicy5)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.webm_codec_combo)

        self.webm_codec_label = QLabel(self.groupBox_6)
        self.webm_codec_label.setObjectName(u"webm_codec_label")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.webm_codec_label)

        self.webm_quality_label = QLabel(self.groupBox_6)
        self.webm_quality_label.setObjectName(u"webm_quality_label")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.webm_quality_label)

        self.webm_quality_spinner = QSpinBox(self.groupBox_6)
        self.webm_quality_spinner.setObjectName(u"webm_quality_spinner")
        sizePolicy5.setHeightForWidth(self.webm_quality_spinner.sizePolicy().hasHeightForWidth())
        self.webm_quality_spinner.setSizePolicy(sizePolicy5)
        self.webm_quality_spinner.setMinimum(1)
        self.webm_quality_spinner.setMaximum(100)
        self.webm_quality_spinner.setValue(95)

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.webm_quality_spinner)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_4.setItem(2, QFormLayout.ItemRole.SpanningRole, self.verticalSpacer)


        self.verticalLayout_18.addLayout(self.formLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.webm_back_button = QPushButton(self.groupBox_6)
        self.webm_back_button.setObjectName(u"webm_back_button")
        self.webm_back_button.setAutoDefault(True)

        self.horizontalLayout_3.addWidget(self.webm_back_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_18.addLayout(self.horizontalLayout_3)


        self.verticalLayout_6.addWidget(self.groupBox_6)

        self.formats_stack.addWidget(self.webm_page)

        self.horizontalLayout.addWidget(self.formats_stack)

        self.parameters_group = QGroupBox(self.options_frame)
        self.parameters_group.setObjectName(u"parameters_group")
        sizePolicy3.setHeightForWidth(self.parameters_group.sizePolicy().hasHeightForWidth())
        self.parameters_group.setSizePolicy(sizePolicy3)
        self.formLayout_2 = QFormLayout(self.parameters_group)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.mode_label = QLabel(self.parameters_group)
        self.mode_label.setObjectName(u"mode_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.mode_label)

        self.mode_combo = QComboBox(self.parameters_group)
        self.mode_combo.setObjectName(u"mode_combo")
        sizePolicy5.setHeightForWidth(self.mode_combo.sizePolicy().hasHeightForWidth())
        self.mode_combo.setSizePolicy(sizePolicy5)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.mode_combo)

        self.duration_label = QLabel(self.parameters_group)
        self.duration_label.setObjectName(u"duration_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.duration_label)

        self.duration_spinbox = QSpinBox(self.parameters_group)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        sizePolicy5.setHeightForWidth(self.duration_spinbox.sizePolicy().hasHeightForWidth())
        self.duration_spinbox.setSizePolicy(sizePolicy5)
        self.duration_spinbox.setMinimum(1)
        self.duration_spinbox.setMaximum(10000)
        self.duration_spinbox.setValue(10)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.duration_spinbox)

        self.loop_label = QLabel(self.parameters_group)
        self.loop_label.setObjectName(u"loop_label")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.loop_label)

        self.loop_spinner = QSpinBox(self.parameters_group)
        self.loop_spinner.setObjectName(u"loop_spinner")
        sizePolicy5.setHeightForWidth(self.loop_spinner.sizePolicy().hasHeightForWidth())
        self.loop_spinner.setSizePolicy(sizePolicy5)
        self.loop_spinner.setMinimum(1)
        self.loop_spinner.setMaximum(100)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.loop_spinner)


        self.horizontalLayout.addWidget(self.parameters_group)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, 9, -1)
        self.output_name_label = QLabel(self.options_frame)
        self.output_name_label.setObjectName(u"output_name_label")

        self.horizontalLayout_4.addWidget(self.output_name_label)

        self.output_name_edit = QLineEdit(self.options_frame)
        self.output_name_edit.setObjectName(u"output_name_edit")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.output_name_edit.sizePolicy().hasHeightForWidth())
        self.output_name_edit.setSizePolicy(sizePolicy9)

        self.horizontalLayout_4.addWidget(self.output_name_edit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.back_button = QPushButton(self.options_frame)
        self.back_button.setObjectName(u"back_button")
        sizePolicy4.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.back_button)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.show_folder_check = QCheckBox(self.options_frame)
        self.show_folder_check.setObjectName(u"show_folder_check")

        self.horizontalLayout_2.addWidget(self.show_folder_check)

        self.export_button = QPushButton(self.options_frame)
        self.export_button.setObjectName(u"export_button")
        sizePolicy4.setHeightForWidth(self.export_button.sizePolicy().hasHeightForWidth())
        self.export_button.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.export_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.options_frame)

#if QT_CONFIG(shortcut)
        self.label_7.setBuddy(self.apng_optimize_check)
        self.avif_quality_label.setBuddy(self.avif_quality_spinner)
        self.webp_quality_label.setBuddy(self.webp_quality_spinner)
        self.webp_lossless_label.setBuddy(self.webp_lossless_check)
        self.label_8.setBuddy(self.gif_optimize_check)
        self.mp4_codec_label.setBuddy(self.mp4_codec_combo)
        self.mp4_quality_label.setBuddy(self.mp4_quality_spinner)
        self.webm_codec_label.setBuddy(self.webm_codec_combo)
        self.webm_quality_label.setBuddy(self.webm_quality_spinner)
        self.mode_label.setBuddy(self.mode_combo)
        self.duration_label.setBuddy(self.duration_spinbox)
        self.loop_label.setBuddy(self.loop_spinner)
        self.output_name_label.setBuddy(self.output_name_edit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ExportFrame)

        self.formats_stack.setCurrentIndex(0)
        self.video_stack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ExportFrame)
    # setupUi

    def retranslateUi(self, ExportFrame):
        ExportFrame.setWindowTitle(QCoreApplication.translate("ExportFrame", u"Frame", None))
        self.preview_label.setText("")
        self.formats_group.setTitle(QCoreApplication.translate("ExportFrame", u"Formats", None))
        self.gif_options_button.setText(QCoreApplication.translate("ExportFrame", u"...", None))
        self.mp4_check.setText(QCoreApplication.translate("ExportFrame", u"MP&4", None))
        self.mp4_options_button.setText(QCoreApplication.translate("ExportFrame", u"...", None))
        self.webm_check.setText(QCoreApplication.translate("ExportFrame", u"Web&M", None))
        self.webm_options_button.setText(QCoreApplication.translate("ExportFrame", u"...", None))
        self.requires_ffmpeg_label.setText(QCoreApplication.translate("ExportFrame", u"MP4 and WebM requires FFmpeg.", None))
        self.avif_check.setText(QCoreApplication.translate("ExportFrame", u"A&VIF", None))
        self.gif_check.setText(QCoreApplication.translate("ExportFrame", u"&GIF", None))
        self.apng_check.setText(QCoreApplication.translate("ExportFrame", u"A&PNG", None))
        self.avif_options_button.setText(QCoreApplication.translate("ExportFrame", u"...", None))
        self.webp_check.setText(QCoreApplication.translate("ExportFrame", u"&WebP", None))
        self.apng_options_button.setText(QCoreApplication.translate("ExportFrame", u"...", None))
        self.webp_options_button.setText(QCoreApplication.translate("ExportFrame", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("ExportFrame", u"APNG options", None))
        self.label_7.setText(QCoreApplication.translate("ExportFrame", u"Optimize size", None))
        self.apng_optimize_check.setText("")
        self.apng_compress_label.setText(QCoreApplication.translate("ExportFrame", u"Compress level", None))
        self.apng_back_button.setText(QCoreApplication.translate("ExportFrame", u"Back", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ExportFrame", u"AVIF options", None))
        self.avif_quality_label.setText(QCoreApplication.translate("ExportFrame", u"Quality", None))
        self.avif_back_button.setText(QCoreApplication.translate("ExportFrame", u"Back", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ExportFrame", u"WebP options", None))
        self.webp_quality_label.setText(QCoreApplication.translate("ExportFrame", u"Quality", None))
        self.webp_lossless_label.setText(QCoreApplication.translate("ExportFrame", u"Lossless", None))
        self.webp_lossless_check.setText("")
        self.webp_back_button.setText(QCoreApplication.translate("ExportFrame", u"Back", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ExportFrame", u"GIF options", None))
        self.gif_optimize_check.setText("")
        self.label_8.setText(QCoreApplication.translate("ExportFrame", u"Optimize palette", None))
        self.gif_back_button.setText(QCoreApplication.translate("ExportFrame", u"Back", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ExportFrame", u"MP4 options", None))
        self.mp4_codec_label.setText(QCoreApplication.translate("ExportFrame", u"Codec", None))
        self.mp4_quality_label.setText(QCoreApplication.translate("ExportFrame", u"Quality", None))
        self.mp4_back_button.setText(QCoreApplication.translate("ExportFrame", u"Back", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ExportFrame", u"WebM options", None))
        self.webm_codec_label.setText(QCoreApplication.translate("ExportFrame", u"Codec", None))
        self.webm_quality_label.setText(QCoreApplication.translate("ExportFrame", u"Quality", None))
        self.webm_back_button.setText(QCoreApplication.translate("ExportFrame", u"Back", None))
        self.parameters_group.setTitle(QCoreApplication.translate("ExportFrame", u"Animation", None))
        self.mode_label.setText(QCoreApplication.translate("ExportFrame", u"Mo&de", None))
#if QT_CONFIG(tooltip)
        self.mode_combo.setToolTip(QCoreApplication.translate("ExportFrame", u"Type of animation to create.\n"
"\n"
"Loop will begin on the first frame and end on the last.\n"
"\n"
"Rock will play the frames in normal order, followed by a repeat in reverse order.", None))
#endif // QT_CONFIG(tooltip)
        self.duration_label.setText(QCoreApplication.translate("ExportFrame", u"&FPS", None))
#if QT_CONFIG(tooltip)
        self.duration_spinbox.setToolTip(QCoreApplication.translate("ExportFrame", u"Number of frames to progress per one second.", None))
#endif // QT_CONFIG(tooltip)
        self.loop_label.setText(QCoreApplication.translate("ExportFrame", u"&Loop", None))
#if QT_CONFIG(tooltip)
        self.loop_spinner.setToolTip(QCoreApplication.translate("ExportFrame", u"Number of times to repeat animation for MP4 and WebM formats.", None))
#endif // QT_CONFIG(tooltip)
        self.output_name_label.setText(QCoreApplication.translate("ExportFrame", u"&Name", None))
#if QT_CONFIG(tooltip)
        self.output_name_edit.setToolTip(QCoreApplication.translate("ExportFrame", u"Base name for the output animations. File extensions will be added automatically.", None))
#endif // QT_CONFIG(tooltip)
        self.back_button.setText(QCoreApplication.translate("ExportFrame", u"&Back", None))
        self.show_folder_check.setText(QCoreApplication.translate("ExportFrame", u"&Open when finished", None))
        self.export_button.setText(QCoreApplication.translate("ExportFrame", u"&Export to folder", None))
    # retranslateUi

