# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainframe.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QStackedWidget, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainFrame(object):
    def setupUi(self, MainFrame):
        if not MainFrame.objectName():
            MainFrame.setObjectName(u"MainFrame")
        MainFrame.resize(650, 700)
        MainFrame.setMinimumSize(QSize(650, 700))
        MainFrame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(MainFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.input_label = QLabel(self.page)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMinimumSize(QSize(0, 0))

        self.verticalLayout_8.addWidget(self.input_label)

        self.frames_table = QTableView(self.page)
        self.frames_table.setObjectName(u"frames_table")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frames_table.sizePolicy().hasHeightForWidth())
        self.frames_table.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.frames_table)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.drag_drop_label = QLabel(self.page)
        self.drag_drop_label.setObjectName(u"drag_drop_label")

        self.horizontalLayout_11.addWidget(self.drag_drop_label)

        self.horizontalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.input_browse_button = QPushButton(self.page)
        self.input_browse_button.setObjectName(u"input_browse_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_browse_button.sizePolicy().hasHeightForWidth())
        self.input_browse_button.setSizePolicy(sizePolicy2)
        self.input_browse_button.setAutoDefault(True)

        self.horizontalLayout_11.addWidget(self.input_browse_button)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.loop_frames_button = QPushButton(self.page_2)
        self.loop_frames_button.setObjectName(u"loop_frames_button")
        self.loop_frames_button.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.loop_frames_button)

        self.previous_frame_button = QPushButton(self.page_2)
        self.previous_frame_button.setObjectName(u"previous_frame_button")
        self.previous_frame_button.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout_12.addWidget(self.previous_frame_button)

        self.next_frame_button = QPushButton(self.page_2)
        self.next_frame_button.setObjectName(u"next_frame_button")
        self.next_frame_button.setMaximumSize(QSize(24, 16777215))

        self.horizontalLayout_12.addWidget(self.next_frame_button)

        self.frames_slider = QSlider(self.page_2)
        self.frames_slider.setObjectName(u"frames_slider")
        self.frames_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_12.addWidget(self.frames_slider)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.formats_stack = QStackedWidget(MainFrame)
        self.formats_stack.setObjectName(u"formats_stack")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.formats_stack.sizePolicy().hasHeightForWidth())
        self.formats_stack.setSizePolicy(sizePolicy4)
        self.formats_page = QWidget()
        self.formats_page.setObjectName(u"formats_page")
        self.verticalLayout_4 = QVBoxLayout(self.formats_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formats_group = QGroupBox(self.formats_page)
        self.formats_group.setObjectName(u"formats_group")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.formats_group.sizePolicy().hasHeightForWidth())
        self.formats_group.setSizePolicy(sizePolicy5)
        self.gridLayout = QGridLayout(self.formats_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gif_options_button = QPushButton(self.formats_group)
        self.gif_options_button.setObjectName(u"gif_options_button")
        sizePolicy2.setHeightForWidth(self.gif_options_button.sizePolicy().hasHeightForWidth())
        self.gif_options_button.setSizePolicy(sizePolicy2)
        self.gif_options_button.setMaximumSize(QSize(24, 24))
        self.gif_options_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.gif_options_button, 3, 1, 1, 1)

        self.apng_options_button = QPushButton(self.formats_group)
        self.apng_options_button.setObjectName(u"apng_options_button")
        self.apng_options_button.setMaximumSize(QSize(24, 24))
        self.apng_options_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.apng_options_button, 0, 1, 1, 1)

        self.apng_check = QCheckBox(self.formats_group)
        self.apng_check.setObjectName(u"apng_check")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.apng_check.sizePolicy().hasHeightForWidth())
        self.apng_check.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.apng_check, 0, 0, 1, 1)

        self.webp_check = QCheckBox(self.formats_group)
        self.webp_check.setObjectName(u"webp_check")
        sizePolicy6.setHeightForWidth(self.webp_check.sizePolicy().hasHeightForWidth())
        self.webp_check.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.webp_check, 2, 0, 1, 1)

        self.avif_check = QCheckBox(self.formats_group)
        self.avif_check.setObjectName(u"avif_check")
        sizePolicy6.setHeightForWidth(self.avif_check.sizePolicy().hasHeightForWidth())
        self.avif_check.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.avif_check, 1, 0, 1, 1)

        self.video_stack = QStackedWidget(self.formats_group)
        self.video_stack.setObjectName(u"video_stack")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.video_stack.sizePolicy().hasHeightForWidth())
        self.video_stack.setSizePolicy(sizePolicy7)
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
        sizePolicy2.setHeightForWidth(self.mp4_options_button.sizePolicy().hasHeightForWidth())
        self.mp4_options_button.setSizePolicy(sizePolicy2)
        self.mp4_options_button.setMaximumSize(QSize(24, 24))
        self.mp4_options_button.setAutoDefault(True)

        self.gridLayout_2.addWidget(self.mp4_options_button, 0, 1, 1, 1)

        self.webm_check = QCheckBox(self.page_3)
        self.webm_check.setObjectName(u"webm_check")

        self.gridLayout_2.addWidget(self.webm_check, 1, 0, 1, 1)

        self.webm_options_button = QPushButton(self.page_3)
        self.webm_options_button.setObjectName(u"webm_options_button")
        sizePolicy2.setHeightForWidth(self.webm_options_button.sizePolicy().hasHeightForWidth())
        self.webm_options_button.setSizePolicy(sizePolicy2)
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
        sizePolicy4.setHeightForWidth(self.requires_ffmpeg_label.sizePolicy().hasHeightForWidth())
        self.requires_ffmpeg_label.setSizePolicy(sizePolicy4)
        self.requires_ffmpeg_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.requires_ffmpeg_label)

        self.video_stack.addWidget(self.page_4)

        self.gridLayout.addWidget(self.video_stack, 4, 0, 1, 2)

        self.webp_options_button = QPushButton(self.formats_group)
        self.webp_options_button.setObjectName(u"webp_options_button")
        self.webp_options_button.setMaximumSize(QSize(24, 24))
        self.webp_options_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.webp_options_button, 2, 1, 1, 1)

        self.gif_check = QCheckBox(self.formats_group)
        self.gif_check.setObjectName(u"gif_check")
        sizePolicy6.setHeightForWidth(self.gif_check.sizePolicy().hasHeightForWidth())
        self.gif_check.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.gif_check, 3, 0, 1, 1)

        self.avif_options_button = QPushButton(self.formats_group)
        self.avif_options_button.setObjectName(u"avif_options_button")
        self.avif_options_button.setMaximumSize(QSize(24, 24))
        self.avif_options_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.avif_options_button, 1, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 5, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.formats_group)

        self.formats_stack.addWidget(self.formats_page)
        self.apng_page = QWidget()
        self.apng_page.setObjectName(u"apng_page")
        self.verticalLayout_11 = QVBoxLayout(self.apng_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.apng_page)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy8)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.apng_optimize_check = QCheckBox(self.groupBox)
        self.apng_optimize_check.setObjectName(u"apng_optimize_check")
        sizePolicy2.setHeightForWidth(self.apng_optimize_check.sizePolicy().hasHeightForWidth())
        self.apng_optimize_check.setSizePolicy(sizePolicy2)
        self.apng_optimize_check.setMinimumSize(QSize(25, 0))

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.apng_optimize_check)

        self.apng_compress_spinner = QSpinBox(self.groupBox)
        self.apng_compress_spinner.setObjectName(u"apng_compress_spinner")
        sizePolicy7.setHeightForWidth(self.apng_compress_spinner.sizePolicy().hasHeightForWidth())
        self.apng_compress_spinner.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy8)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.avif_quality_label = QLabel(self.groupBox_2)
        self.avif_quality_label.setObjectName(u"avif_quality_label")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.avif_quality_label)

        self.avif_quality_spinner = QSpinBox(self.groupBox_2)
        self.avif_quality_spinner.setObjectName(u"avif_quality_spinner")
        sizePolicy7.setHeightForWidth(self.avif_quality_spinner.sizePolicy().hasHeightForWidth())
        self.avif_quality_spinner.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy8)
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.webp_quality_label = QLabel(self.groupBox_3)
        self.webp_quality_label.setObjectName(u"webp_quality_label")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.LabelRole, self.webp_quality_label)

        self.webp_quality_spinner = QSpinBox(self.groupBox_3)
        self.webp_quality_spinner.setObjectName(u"webp_quality_spinner")
        sizePolicy7.setHeightForWidth(self.webp_quality_spinner.sizePolicy().hasHeightForWidth())
        self.webp_quality_spinner.setSizePolicy(sizePolicy7)
        self.webp_quality_spinner.setMaximum(100)
        self.webp_quality_spinner.setSingleStep(5)
        self.webp_quality_spinner.setValue(95)

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.FieldRole, self.webp_quality_spinner)

        self.webp_lossless_label = QLabel(self.groupBox_3)
        self.webp_lossless_label.setObjectName(u"webp_lossless_label")

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.LabelRole, self.webp_lossless_label)

        self.webp_lossless_check = QCheckBox(self.groupBox_3)
        self.webp_lossless_check.setObjectName(u"webp_lossless_check")
        sizePolicy2.setHeightForWidth(self.webp_lossless_check.sizePolicy().hasHeightForWidth())
        self.webp_lossless_check.setSizePolicy(sizePolicy2)
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
        sizePolicy8.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy8)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.gif_optimize_check = QCheckBox(self.groupBox_4)
        self.gif_optimize_check.setObjectName(u"gif_optimize_check")
        sizePolicy2.setHeightForWidth(self.gif_optimize_check.sizePolicy().hasHeightForWidth())
        self.gif_optimize_check.setSizePolicy(sizePolicy2)
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
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.mp4_page.sizePolicy().hasHeightForWidth())
        self.mp4_page.setSizePolicy(sizePolicy9)
        self.verticalLayout_9 = QVBoxLayout(self.mp4_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.mp4_page)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy5.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy5)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.mp4_codec_label = QLabel(self.groupBox_5)
        self.mp4_codec_label.setObjectName(u"mp4_codec_label")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.mp4_codec_label)

        self.mp4_codec_combo = QComboBox(self.groupBox_5)
        self.mp4_codec_combo.setObjectName(u"mp4_codec_combo")
        sizePolicy7.setHeightForWidth(self.mp4_codec_combo.sizePolicy().hasHeightForWidth())
        self.mp4_codec_combo.setSizePolicy(sizePolicy7)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.mp4_codec_combo)

        self.mp4_quality_label = QLabel(self.groupBox_5)
        self.mp4_quality_label.setObjectName(u"mp4_quality_label")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.mp4_quality_label)

        self.mp4_quality_spinner = QSpinBox(self.groupBox_5)
        self.mp4_quality_spinner.setObjectName(u"mp4_quality_spinner")
        sizePolicy7.setHeightForWidth(self.mp4_quality_spinner.sizePolicy().hasHeightForWidth())
        self.mp4_quality_spinner.setSizePolicy(sizePolicy7)
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
        sizePolicy8.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy8)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.webm_codec_combo = QComboBox(self.groupBox_6)
        self.webm_codec_combo.setObjectName(u"webm_codec_combo")
        sizePolicy7.setHeightForWidth(self.webm_codec_combo.sizePolicy().hasHeightForWidth())
        self.webm_codec_combo.setSizePolicy(sizePolicy7)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.webm_codec_combo)

        self.webm_codec_label = QLabel(self.groupBox_6)
        self.webm_codec_label.setObjectName(u"webm_codec_label")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.webm_codec_label)

        self.webm_quality_label = QLabel(self.groupBox_6)
        self.webm_quality_label.setObjectName(u"webm_quality_label")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.webm_quality_label)

        self.webm_quality_spinner = QSpinBox(self.groupBox_6)
        self.webm_quality_spinner.setObjectName(u"webm_quality_spinner")
        sizePolicy7.setHeightForWidth(self.webm_quality_spinner.sizePolicy().hasHeightForWidth())
        self.webm_quality_spinner.setSizePolicy(sizePolicy7)
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

        self.horizontalLayout_13.addWidget(self.formats_stack)

        self.frame = QFrame(MainFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(50, 0))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.parameters_group = QGroupBox(self.frame)
        self.parameters_group.setObjectName(u"parameters_group")
        sizePolicy5.setHeightForWidth(self.parameters_group.sizePolicy().hasHeightForWidth())
        self.parameters_group.setSizePolicy(sizePolicy5)
        self.formLayout_2 = QFormLayout(self.parameters_group)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.mode_label = QLabel(self.parameters_group)
        self.mode_label.setObjectName(u"mode_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.mode_label)

        self.mode_combo = QComboBox(self.parameters_group)
        self.mode_combo.setObjectName(u"mode_combo")
        sizePolicy7.setHeightForWidth(self.mode_combo.sizePolicy().hasHeightForWidth())
        self.mode_combo.setSizePolicy(sizePolicy7)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.mode_combo)

        self.duration_label = QLabel(self.parameters_group)
        self.duration_label.setObjectName(u"duration_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.duration_label)

        self.duration_spinbox = QSpinBox(self.parameters_group)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        sizePolicy7.setHeightForWidth(self.duration_spinbox.sizePolicy().hasHeightForWidth())
        self.duration_spinbox.setSizePolicy(sizePolicy7)
        self.duration_spinbox.setMinimum(1)
        self.duration_spinbox.setMaximum(10000)
        self.duration_spinbox.setValue(10)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.duration_spinbox)

        self.width_label = QLabel(self.parameters_group)
        self.width_label.setObjectName(u"width_label")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.width_label)

        self.width_spinner = QSpinBox(self.parameters_group)
        self.width_spinner.setObjectName(u"width_spinner")
        sizePolicy7.setHeightForWidth(self.width_spinner.sizePolicy().hasHeightForWidth())
        self.width_spinner.setSizePolicy(sizePolicy7)
        self.width_spinner.setMinimum(1)
        self.width_spinner.setMaximum(16383)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.width_spinner)

        self.height_label = QLabel(self.parameters_group)
        self.height_label.setObjectName(u"height_label")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.height_label)

        self.height_spinner = QSpinBox(self.parameters_group)
        self.height_spinner.setObjectName(u"height_spinner")
        sizePolicy7.setHeightForWidth(self.height_spinner.sizePolicy().hasHeightForWidth())
        self.height_spinner.setSizePolicy(sizePolicy7)
        self.height_spinner.setMinimum(1)
        self.height_spinner.setMaximum(16383)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.height_spinner)

        self.loop_label = QLabel(self.parameters_group)
        self.loop_label.setObjectName(u"loop_label")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.loop_label)

        self.loop_spinner = QSpinBox(self.parameters_group)
        self.loop_spinner.setObjectName(u"loop_spinner")
        sizePolicy7.setHeightForWidth(self.loop_spinner.sizePolicy().hasHeightForWidth())
        self.loop_spinner.setSizePolicy(sizePolicy7)
        self.loop_spinner.setMinimum(1)
        self.loop_spinner.setMaximum(100)

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.loop_spinner)


        self.verticalLayout_5.addWidget(self.parameters_group)


        self.horizontalLayout_13.addWidget(self.frame)

        self.frame_2 = QFrame(MainFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(50, 0))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.frame_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.method_groupbox = QGroupBox(self.frame_2)
        self.method_groupbox.setObjectName(u"method_groupbox")
        sizePolicy5.setHeightForWidth(self.method_groupbox.sizePolicy().hasHeightForWidth())
        self.method_groupbox.setSizePolicy(sizePolicy5)
        self.formLayout_10 = QFormLayout(self.method_groupbox)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.average_label = QLabel(self.method_groupbox)
        self.average_label.setObjectName(u"average_label")

        self.formLayout_10.setWidget(2, QFormLayout.ItemRole.LabelRole, self.average_label)

        self.average_spinner = QSpinBox(self.method_groupbox)
        self.average_spinner.setObjectName(u"average_spinner")
        sizePolicy7.setHeightForWidth(self.average_spinner.sizePolicy().hasHeightForWidth())
        self.average_spinner.setSizePolicy(sizePolicy7)
        self.average_spinner.setMinimum(1)

        self.formLayout_10.setWidget(2, QFormLayout.ItemRole.FieldRole, self.average_spinner)

        self.line_3 = QFrame(self.method_groupbox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout_10.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.line_3)

        self.subtract_label = QLabel(self.method_groupbox)
        self.subtract_label.setObjectName(u"subtract_label")

        self.formLayout_10.setWidget(4, QFormLayout.ItemRole.LabelRole, self.subtract_label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.subtract_check = QCheckBox(self.method_groupbox)
        self.subtract_check.setObjectName(u"subtract_check")
        sizePolicy2.setHeightForWidth(self.subtract_check.sizePolicy().hasHeightForWidth())
        self.subtract_check.setSizePolicy(sizePolicy2)
        self.subtract_check.setMinimumSize(QSize(25, 0))

        self.horizontalLayout_10.addWidget(self.subtract_check)

        self.horizontalSpacer_7 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.formLayout_10.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_10)

        self.spread_label = QLabel(self.method_groupbox)
        self.spread_label.setObjectName(u"spread_label")

        self.formLayout_10.setWidget(5, QFormLayout.ItemRole.LabelRole, self.spread_label)

        self.spread_spinner = QSpinBox(self.method_groupbox)
        self.spread_spinner.setObjectName(u"spread_spinner")
        sizePolicy7.setHeightForWidth(self.spread_spinner.sizePolicy().hasHeightForWidth())
        self.spread_spinner.setSizePolicy(sizePolicy7)
        self.spread_spinner.setMinimum(1)

        self.formLayout_10.setWidget(5, QFormLayout.ItemRole.FieldRole, self.spread_spinner)

        self.line = QFrame(self.method_groupbox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout_10.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.line)

        self.rotate_label = QLabel(self.method_groupbox)
        self.rotate_label.setObjectName(u"rotate_label")

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.LabelRole, self.rotate_label)

        self.rotate_spinner = QSpinBox(self.method_groupbox)
        self.rotate_spinner.setObjectName(u"rotate_spinner")
        sizePolicy7.setHeightForWidth(self.rotate_spinner.sizePolicy().hasHeightForWidth())
        self.rotate_spinner.setSizePolicy(sizePolicy7)
        self.rotate_spinner.setMinimum(-359)
        self.rotate_spinner.setMaximum(359)

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.FieldRole, self.rotate_spinner)


        self.verticalLayout_19.addWidget(self.method_groupbox)


        self.horizontalLayout_13.addWidget(self.frame_2)

        self.frame_3 = QFrame(MainFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(50, 0))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_20 = QVBoxLayout(self.frame_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.derotation_group = QGroupBox(self.frame_3)
        self.derotation_group.setObjectName(u"derotation_group")
        self.derotation_group.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.derotation_group.sizePolicy().hasHeightForWidth())
        self.derotation_group.setSizePolicy(sizePolicy5)
        self.derotation_group.setCheckable(True)
        self.derotation_group.setChecked(False)
        self.formLayout = QFormLayout(self.derotation_group)
        self.formLayout.setObjectName(u"formLayout")
        self.target_label = QLabel(self.derotation_group)
        self.target_label.setObjectName(u"target_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.target_label)

        self.target_combo = QComboBox(self.derotation_group)
        self.target_combo.setObjectName(u"target_combo")
        sizePolicy7.setHeightForWidth(self.target_combo.sizePolicy().hasHeightForWidth())
        self.target_combo.setSizePolicy(sizePolicy7)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.target_combo)

        self.latitude_label = QLabel(self.derotation_group)
        self.latitude_label.setObjectName(u"latitude_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.latitude_label)

        self.latitude_spin = QDoubleSpinBox(self.derotation_group)
        self.latitude_spin.setObjectName(u"latitude_spin")
        sizePolicy7.setHeightForWidth(self.latitude_spin.sizePolicy().hasHeightForWidth())
        self.latitude_spin.setSizePolicy(sizePolicy7)
        self.latitude_spin.setMinimum(-90.000000000000000)
        self.latitude_spin.setMaximum(90.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.latitude_spin)

        self.longitude_label = QLabel(self.derotation_group)
        self.longitude_label.setObjectName(u"longitude_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.longitude_label)

        self.longitude_spin = QDoubleSpinBox(self.derotation_group)
        self.longitude_spin.setObjectName(u"longitude_spin")
        sizePolicy7.setHeightForWidth(self.longitude_spin.sizePolicy().hasHeightForWidth())
        self.longitude_spin.setSizePolicy(sizePolicy7)
        self.longitude_spin.setMinimum(-180.000000000000000)
        self.longitude_spin.setMaximum(180.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.longitude_spin)

        self.az_tilt_spin = QDoubleSpinBox(self.derotation_group)
        self.az_tilt_spin.setObjectName(u"az_tilt_spin")
        sizePolicy7.setHeightForWidth(self.az_tilt_spin.sizePolicy().hasHeightForWidth())
        self.az_tilt_spin.setSizePolicy(sizePolicy7)
        self.az_tilt_spin.setMinimum(-90.000000000000000)
        self.az_tilt_spin.setMaximum(90.000000000000000)
        self.az_tilt_spin.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.az_tilt_spin)

        self.alt_tilt_label = QLabel(self.derotation_group)
        self.alt_tilt_label.setObjectName(u"alt_tilt_label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.alt_tilt_label)

        self.az_tilt_label = QLabel(self.derotation_group)
        self.az_tilt_label.setObjectName(u"az_tilt_label")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.az_tilt_label)

        self.alt_tilt_spin = QDoubleSpinBox(self.derotation_group)
        self.alt_tilt_spin.setObjectName(u"alt_tilt_spin")
        sizePolicy7.setHeightForWidth(self.alt_tilt_spin.sizePolicy().hasHeightForWidth())
        self.alt_tilt_spin.setSizePolicy(sizePolicy7)
        self.alt_tilt_spin.setMinimum(-90.000000000000000)
        self.alt_tilt_spin.setMaximum(90.000000000000000)
        self.alt_tilt_spin.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.alt_tilt_spin)


        self.verticalLayout_20.addWidget(self.derotation_group)


        self.horizontalLayout_13.addWidget(self.frame_3)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.output_label = QLabel(MainFrame)
        self.output_label.setObjectName(u"output_label")

        self.horizontalLayout_4.addWidget(self.output_label)

        self.output_path_edit = QLineEdit(MainFrame)
        self.output_path_edit.setObjectName(u"output_path_edit")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(2)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.output_path_edit.sizePolicy().hasHeightForWidth())
        self.output_path_edit.setSizePolicy(sizePolicy10)

        self.horizontalLayout_4.addWidget(self.output_path_edit)

        self.output_browse_button = QPushButton(MainFrame)
        self.output_browse_button.setObjectName(u"output_browse_button")
        self.output_browse_button.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.output_browse_button)

        self.output_name_label = QLabel(MainFrame)
        self.output_name_label.setObjectName(u"output_name_label")

        self.horizontalLayout_4.addWidget(self.output_name_label)

        self.output_name_edit = QLineEdit(MainFrame)
        self.output_name_edit.setObjectName(u"output_name_edit")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(1)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.output_name_edit.sizePolicy().hasHeightForWidth())
        self.output_name_edit.setSizePolicy(sizePolicy11)

        self.horizontalLayout_4.addWidget(self.output_name_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.settings_button = QPushButton(MainFrame)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy2.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy2)
        self.settings_button.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.settings_button)

        self.show_folder_check = QCheckBox(MainFrame)
        self.show_folder_check.setObjectName(u"show_folder_check")

        self.horizontalLayout_2.addWidget(self.show_folder_check, 0, Qt.AlignmentFlag.AlignRight)

        self.convert_button = QPushButton(MainFrame)
        self.convert_button.setObjectName(u"convert_button")
        sizePolicy2.setHeightForWidth(self.convert_button.sizePolicy().hasHeightForWidth())
        self.convert_button.setSizePolicy(sizePolicy2)
        self.convert_button.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.convert_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

#if QT_CONFIG(shortcut)
        self.input_label.setBuddy(self.input_browse_button)
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
        self.width_label.setBuddy(self.width_spinner)
        self.height_label.setBuddy(self.height_spinner)
        self.loop_label.setBuddy(self.loop_spinner)
        self.average_label.setBuddy(self.average_spinner)
        self.subtract_label.setBuddy(self.subtract_check)
        self.spread_label.setBuddy(self.spread_spinner)
        self.rotate_label.setBuddy(self.rotate_spinner)
        self.target_label.setBuddy(self.target_combo)
        self.latitude_label.setBuddy(self.latitude_spin)
        self.longitude_label.setBuddy(self.longitude_spin)
        self.alt_tilt_label.setBuddy(self.alt_tilt_spin)
        self.az_tilt_label.setBuddy(self.az_tilt_spin)
        self.output_label.setBuddy(self.output_browse_button)
        self.output_name_label.setBuddy(self.output_name_edit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.frames_table, self.input_browse_button)
        QWidget.setTabOrder(self.input_browse_button, self.mp4_check)
        QWidget.setTabOrder(self.mp4_check, self.webm_check)
        QWidget.setTabOrder(self.webm_check, self.mode_combo)
        QWidget.setTabOrder(self.mode_combo, self.duration_spinbox)
        QWidget.setTabOrder(self.duration_spinbox, self.loop_spinner)
        QWidget.setTabOrder(self.loop_spinner, self.rotate_spinner)
        QWidget.setTabOrder(self.rotate_spinner, self.average_spinner)
        QWidget.setTabOrder(self.average_spinner, self.subtract_check)
        QWidget.setTabOrder(self.subtract_check, self.spread_spinner)
        QWidget.setTabOrder(self.spread_spinner, self.derotation_group)
        QWidget.setTabOrder(self.derotation_group, self.target_combo)
        QWidget.setTabOrder(self.target_combo, self.latitude_spin)
        QWidget.setTabOrder(self.latitude_spin, self.longitude_spin)
        QWidget.setTabOrder(self.longitude_spin, self.alt_tilt_spin)
        QWidget.setTabOrder(self.alt_tilt_spin, self.az_tilt_spin)
        QWidget.setTabOrder(self.az_tilt_spin, self.output_path_edit)
        QWidget.setTabOrder(self.output_path_edit, self.output_browse_button)
        QWidget.setTabOrder(self.output_browse_button, self.output_name_edit)
        QWidget.setTabOrder(self.output_name_edit, self.settings_button)
        QWidget.setTabOrder(self.settings_button, self.show_folder_check)
        QWidget.setTabOrder(self.show_folder_check, self.convert_button)
        QWidget.setTabOrder(self.convert_button, self.gif_optimize_check)
        QWidget.setTabOrder(self.gif_optimize_check, self.gif_back_button)
        QWidget.setTabOrder(self.gif_back_button, self.mp4_codec_combo)
        QWidget.setTabOrder(self.mp4_codec_combo, self.mp4_back_button)
        QWidget.setTabOrder(self.mp4_back_button, self.webm_codec_combo)
        QWidget.setTabOrder(self.webm_codec_combo, self.webm_back_button)
        QWidget.setTabOrder(self.webm_back_button, self.loop_frames_button)
        QWidget.setTabOrder(self.loop_frames_button, self.avif_back_button)
        QWidget.setTabOrder(self.avif_back_button, self.next_frame_button)
        QWidget.setTabOrder(self.next_frame_button, self.frames_slider)
        QWidget.setTabOrder(self.frames_slider, self.webp_quality_spinner)
        QWidget.setTabOrder(self.webp_quality_spinner, self.webp_lossless_check)
        QWidget.setTabOrder(self.webp_lossless_check, self.apng_back_button)
        QWidget.setTabOrder(self.apng_back_button, self.webp_back_button)
        QWidget.setTabOrder(self.webp_back_button, self.previous_frame_button)
        QWidget.setTabOrder(self.previous_frame_button, self.apng_compress_spinner)
        QWidget.setTabOrder(self.apng_compress_spinner, self.apng_optimize_check)
        QWidget.setTabOrder(self.apng_optimize_check, self.avif_quality_spinner)

        self.retranslateUi(MainFrame)
        self.subtract_check.toggled.connect(self.spread_label.setVisible)
        self.subtract_check.toggled.connect(self.spread_spinner.setVisible)

        self.stackedWidget.setCurrentIndex(0)
        self.formats_stack.setCurrentIndex(0)
        self.video_stack.setCurrentIndex(0)
        self.convert_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainFrame)
    # setupUi

    def retranslateUi(self, MainFrame):
        MainFrame.setWindowTitle(QCoreApplication.translate("MainFrame", u"Frame", None))
        self.input_label.setText(QCoreApplication.translate("MainFrame", u"&Input frames", None))
        self.drag_drop_label.setText("")
#if QT_CONFIG(tooltip)
        self.input_browse_button.setToolTip(QCoreApplication.translate("MainFrame", u"Browse for input frames.\n"
"\n"
"Supported images or folders with multiple images can also be dropped anywhere on this window to add them as input frames.", None))
#endif // QT_CONFIG(tooltip)
        self.input_browse_button.setText(QCoreApplication.translate("MainFrame", u"Browse...", None))
        self.label_10.setText("")
        self.loop_frames_button.setText(QCoreApplication.translate("MainFrame", u"Loop", None))
        self.previous_frame_button.setText(QCoreApplication.translate("MainFrame", u"<", None))
        self.next_frame_button.setText(QCoreApplication.translate("MainFrame", u">", None))
        self.formats_group.setTitle(QCoreApplication.translate("MainFrame", u"Formats", None))
        self.gif_options_button.setText(QCoreApplication.translate("MainFrame", u"...", None))
        self.apng_options_button.setText(QCoreApplication.translate("MainFrame", u"...", None))
        self.apng_check.setText(QCoreApplication.translate("MainFrame", u"A&PNG", None))
        self.webp_check.setText(QCoreApplication.translate("MainFrame", u"&WebP", None))
        self.avif_check.setText(QCoreApplication.translate("MainFrame", u"A&VIF", None))
        self.mp4_check.setText(QCoreApplication.translate("MainFrame", u"MP&4", None))
        self.mp4_options_button.setText(QCoreApplication.translate("MainFrame", u"...", None))
        self.webm_check.setText(QCoreApplication.translate("MainFrame", u"Web&M", None))
        self.webm_options_button.setText(QCoreApplication.translate("MainFrame", u"...", None))
        self.requires_ffmpeg_label.setText(QCoreApplication.translate("MainFrame", u"MP4 and WebM requires FFmpeg.", None))
        self.webp_options_button.setText(QCoreApplication.translate("MainFrame", u"...", None))
        self.gif_check.setText(QCoreApplication.translate("MainFrame", u"&GIF", None))
        self.avif_options_button.setText(QCoreApplication.translate("MainFrame", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainFrame", u"APNG options", None))
        self.label_7.setText(QCoreApplication.translate("MainFrame", u"Optimize size", None))
        self.apng_optimize_check.setText("")
        self.apng_compress_label.setText(QCoreApplication.translate("MainFrame", u"Compress level", None))
        self.apng_back_button.setText(QCoreApplication.translate("MainFrame", u"Back", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainFrame", u"AVIF options", None))
        self.avif_quality_label.setText(QCoreApplication.translate("MainFrame", u"Quality", None))
        self.avif_back_button.setText(QCoreApplication.translate("MainFrame", u"Back", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainFrame", u"WebP options", None))
        self.webp_quality_label.setText(QCoreApplication.translate("MainFrame", u"Quality", None))
        self.webp_lossless_label.setText(QCoreApplication.translate("MainFrame", u"Lossless", None))
        self.webp_lossless_check.setText("")
        self.webp_back_button.setText(QCoreApplication.translate("MainFrame", u"Back", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainFrame", u"GIF options", None))
        self.gif_optimize_check.setText("")
        self.label_8.setText(QCoreApplication.translate("MainFrame", u"Optimize palette", None))
        self.gif_back_button.setText(QCoreApplication.translate("MainFrame", u"Back", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainFrame", u"MP4 options", None))
        self.mp4_codec_label.setText(QCoreApplication.translate("MainFrame", u"Codec", None))
        self.mp4_quality_label.setText(QCoreApplication.translate("MainFrame", u"Quality", None))
        self.mp4_back_button.setText(QCoreApplication.translate("MainFrame", u"Back", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainFrame", u"WebM options", None))
        self.webm_codec_label.setText(QCoreApplication.translate("MainFrame", u"Codec", None))
        self.webm_quality_label.setText(QCoreApplication.translate("MainFrame", u"Quality", None))
        self.webm_back_button.setText(QCoreApplication.translate("MainFrame", u"Back", None))
        self.parameters_group.setTitle(QCoreApplication.translate("MainFrame", u"Parameters", None))
        self.mode_label.setText(QCoreApplication.translate("MainFrame", u"Mode", None))
#if QT_CONFIG(tooltip)
        self.mode_combo.setToolTip(QCoreApplication.translate("MainFrame", u"Type of animation to create.\n"
"\n"
"Loop will begin on the first frame and end on the last.\n"
"\n"
"Rock will play the frames in normal order, followed by a repeat in reverse order.", None))
#endif // QT_CONFIG(tooltip)
        self.duration_label.setText(QCoreApplication.translate("MainFrame", u"&FPS", None))
#if QT_CONFIG(tooltip)
        self.duration_spinbox.setToolTip(QCoreApplication.translate("MainFrame", u"Number of frames to progress per one second.", None))
#endif // QT_CONFIG(tooltip)
        self.width_label.setText(QCoreApplication.translate("MainFrame", u"Width", None))
#if QT_CONFIG(tooltip)
        self.width_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Horizontal width in pixels of the animation.", None))
#endif // QT_CONFIG(tooltip)
        self.width_spinner.setSuffix(QCoreApplication.translate("MainFrame", u"px", None))
        self.height_label.setText(QCoreApplication.translate("MainFrame", u"Height", None))
#if QT_CONFIG(tooltip)
        self.height_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Vertical height in pixels of the animation.", None))
#endif // QT_CONFIG(tooltip)
        self.height_spinner.setSuffix(QCoreApplication.translate("MainFrame", u"px", None))
        self.loop_label.setText(QCoreApplication.translate("MainFrame", u"Loop", None))
#if QT_CONFIG(tooltip)
        self.loop_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Number of times to repeat animation for MP4 and WebM formats.", None))
#endif // QT_CONFIG(tooltip)
        self.method_groupbox.setTitle(QCoreApplication.translate("MainFrame", u"Process", None))
        self.average_label.setText(QCoreApplication.translate("MainFrame", u"Average", None))
#if QT_CONFIG(tooltip)
        self.average_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Each frame of the output animation is a result of a moving average of input frames.\n"
"\n"
"No effect if set to 1.", None))
#endif // QT_CONFIG(tooltip)
        self.average_spinner.setPrefix("")
        self.subtract_label.setText(QCoreApplication.translate("MainFrame", u"Subtract", None))
#if QT_CONFIG(tooltip)
        self.subtract_check.setToolTip(QCoreApplication.translate("MainFrame", u"Each frame of the output animation becomes the subtraction of one frame from another. Color frames will be converted to monochrome.", None))
#endif // QT_CONFIG(tooltip)
        self.subtract_check.setText("")
        self.spread_label.setText(QCoreApplication.translate("MainFrame", u"Spread", None))
#if QT_CONFIG(tooltip)
        self.spread_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"How many frames apart the frame to subtract with is from the input frame.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_label.setText(QCoreApplication.translate("MainFrame", u"Rotate", None))
#if QT_CONFIG(tooltip)
        self.rotate_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Rotate each frame by an arbitrary amount in degrees. Positive values rotate clockwise and negative rotate counterclockwise.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_spinner.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.rotate_spinner.setPrefix("")
        self.derotation_group.setTitle(QCoreApplication.translate("MainFrame", u"Alt-az field d&erotation", None))
        self.target_label.setText(QCoreApplication.translate("MainFrame", u"&Target", None))
        self.latitude_label.setText(QCoreApplication.translate("MainFrame", u"L&atitude", None))
#if QT_CONFIG(tooltip)
        self.latitude_spin.setToolTip(QCoreApplication.translate("MainFrame", u"Decimal degrees of latitude. Positive is north and negative is south.", None))
#endif // QT_CONFIG(tooltip)
        self.latitude_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.longitude_label.setText(QCoreApplication.translate("MainFrame", u"Lo&ngitude", None))
#if QT_CONFIG(tooltip)
        self.longitude_spin.setToolTip(QCoreApplication.translate("MainFrame", u"Decimal degrees of longitude. Positive is east and negative is west.", None))
#endif // QT_CONFIG(tooltip)
        self.longitude_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
#if QT_CONFIG(tooltip)
        self.az_tilt_spin.setToolTip(QCoreApplication.translate("MainFrame", u"When an alt-az telescope is not leveled, field derotation will not work perfectly and a slight drift in rotation will occur over a timelapse. Positive when telescope is tilted towards east and negative towards west.", None))
#endif // QT_CONFIG(tooltip)
        self.az_tilt_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.alt_tilt_label.setText(QCoreApplication.translate("MainFrame", u"North tilt", None))
        self.az_tilt_label.setText(QCoreApplication.translate("MainFrame", u"East tilt", None))
#if QT_CONFIG(tooltip)
        self.alt_tilt_spin.setToolTip(QCoreApplication.translate("MainFrame", u"When an alt-az telescope is not leveled, field derotation will not work perfectly and a slight drift in rotation will occur over a timelapse. Positive when telescope is tilted towards north and negative towards south.", None))
#endif // QT_CONFIG(tooltip)
        self.alt_tilt_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.output_label.setText(QCoreApplication.translate("MainFrame", u"&Output folder", None))
#if QT_CONFIG(tooltip)
        self.output_path_edit.setToolTip(QCoreApplication.translate("MainFrame", u"Folder to output animation files to.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.output_browse_button.setToolTip(QCoreApplication.translate("MainFrame", u"Browse for output folder.", None))
#endif // QT_CONFIG(tooltip)
        self.output_browse_button.setText(QCoreApplication.translate("MainFrame", u"Browse...", None))
        self.output_name_label.setText(QCoreApplication.translate("MainFrame", u"Name", None))
#if QT_CONFIG(tooltip)
        self.output_name_edit.setToolTip(QCoreApplication.translate("MainFrame", u"Base name for the output animations. File extensions will be added automatically.", None))
#endif // QT_CONFIG(tooltip)
        self.settings_button.setText(QCoreApplication.translate("MainFrame", u"&Settings", None))
#if QT_CONFIG(tooltip)
        self.show_folder_check.setToolTip(QCoreApplication.translate("MainFrame", u"Open the output folder after all animations are created", None))
#endif // QT_CONFIG(tooltip)
        self.show_folder_check.setText(QCoreApplication.translate("MainFrame", u"Show folder when &done", None))
        self.convert_button.setText(QCoreApplication.translate("MainFrame", u"&Convert", None))
    # retranslateUi

