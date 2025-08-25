# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainframe.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QTableView, QVBoxLayout, QWidget)

class Ui_MainFrame(object):
    def setupUi(self, MainFrame):
        if not MainFrame.objectName():
            MainFrame.setObjectName(u"MainFrame")
        MainFrame.resize(600, 600)
        MainFrame.setMinimumSize(QSize(600, 600))
        MainFrame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(MainFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_label = QLabel(MainFrame)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMinimumSize(QSize(0, 24))

        self.verticalLayout_2.addWidget(self.input_label)

        self.frames_table = QTableView(MainFrame)
        self.frames_table.setObjectName(u"frames_table")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frames_table.sizePolicy().hasHeightForWidth())
        self.frames_table.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.frames_table)

        self.input_browse_button = QPushButton(MainFrame)
        self.input_browse_button.setObjectName(u"input_browse_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_browse_button.sizePolicy().hasHeightForWidth())
        self.input_browse_button.setSizePolicy(sizePolicy1)
        self.input_browse_button.setAutoDefault(True)

        self.verticalLayout_2.addWidget(self.input_browse_button, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formats_group = QGroupBox(MainFrame)
        self.formats_group.setObjectName(u"formats_group")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.formats_group.sizePolicy().hasHeightForWidth())
        self.formats_group.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.formats_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.webp_check = QCheckBox(self.formats_group)
        self.webp_check.setObjectName(u"webp_check")

        self.gridLayout.addWidget(self.webp_check, 1, 0, 1, 1)

        self.avif_check = QCheckBox(self.formats_group)
        self.avif_check.setObjectName(u"avif_check")

        self.gridLayout.addWidget(self.avif_check, 0, 1, 1, 1)

        self.apng_check = QCheckBox(self.formats_group)
        self.apng_check.setObjectName(u"apng_check")

        self.gridLayout.addWidget(self.apng_check, 0, 0, 1, 1)

        self.line = QFrame(self.formats_group)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 2, 2)

        self.gif_check = QCheckBox(self.formats_group)
        self.gif_check.setObjectName(u"gif_check")

        self.gridLayout.addWidget(self.gif_check, 1, 1, 1, 1)

        self.video_stack = QStackedWidget(self.formats_group)
        self.video_stack.setObjectName(u"video_stack")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.video_stack.sizePolicy().hasHeightForWidth())
        self.video_stack.setSizePolicy(sizePolicy3)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mp4_check = QCheckBox(self.page_3)
        self.mp4_check.setObjectName(u"mp4_check")

        self.gridLayout_3.addWidget(self.mp4_check, 0, 0, 1, 1)

        self.webm_codec_combo = QComboBox(self.page_3)
        self.webm_codec_combo.setObjectName(u"webm_codec_combo")
        sizePolicy3.setHeightForWidth(self.webm_codec_combo.sizePolicy().hasHeightForWidth())
        self.webm_codec_combo.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.webm_codec_combo, 1, 1, 1, 1)

        self.mp4_codec_combo = QComboBox(self.page_3)
        self.mp4_codec_combo.setObjectName(u"mp4_codec_combo")
        sizePolicy3.setHeightForWidth(self.mp4_codec_combo.sizePolicy().hasHeightForWidth())
        self.mp4_codec_combo.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.mp4_codec_combo, 0, 1, 1, 1)

        self.webm_check = QCheckBox(self.page_3)
        self.webm_check.setObjectName(u"webm_check")

        self.gridLayout_3.addWidget(self.webm_check, 1, 0, 1, 1)

        self.video_stack.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.requires_ffmpeg_label = QLabel(self.page_4)
        self.requires_ffmpeg_label.setObjectName(u"requires_ffmpeg_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.requires_ffmpeg_label.sizePolicy().hasHeightForWidth())
        self.requires_ffmpeg_label.setSizePolicy(sizePolicy4)
        self.requires_ffmpeg_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.requires_ffmpeg_label)

        self.video_stack.addWidget(self.page_4)

        self.gridLayout.addWidget(self.video_stack, 4, 0, 1, 2)


        self.horizontalLayout.addWidget(self.formats_group)

        self.parameters_group = QGroupBox(MainFrame)
        self.parameters_group.setObjectName(u"parameters_group")
        sizePolicy2.setHeightForWidth(self.parameters_group.sizePolicy().hasHeightForWidth())
        self.parameters_group.setSizePolicy(sizePolicy2)
        self.formLayout_2 = QFormLayout(self.parameters_group)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.duration_label = QLabel(self.parameters_group)
        self.duration_label.setObjectName(u"duration_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.duration_label)

        self.duration_spinbox = QSpinBox(self.parameters_group)
        self.duration_spinbox.setObjectName(u"duration_spinbox")
        sizePolicy3.setHeightForWidth(self.duration_spinbox.sizePolicy().hasHeightForWidth())
        self.duration_spinbox.setSizePolicy(sizePolicy3)
        self.duration_spinbox.setMinimum(1)
        self.duration_spinbox.setMaximum(10000)
        self.duration_spinbox.setValue(10)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.duration_spinbox)

        self.quality_label = QLabel(self.parameters_group)
        self.quality_label.setObjectName(u"quality_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.quality_label)

        self.quality_spinbox = QSpinBox(self.parameters_group)
        self.quality_spinbox.setObjectName(u"quality_spinbox")
        sizePolicy3.setHeightForWidth(self.quality_spinbox.sizePolicy().hasHeightForWidth())
        self.quality_spinbox.setSizePolicy(sizePolicy3)
        self.quality_spinbox.setMinimum(1)
        self.quality_spinbox.setMaximum(100)
        self.quality_spinbox.setValue(100)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.quality_spinbox)

        self.lossless_label = QLabel(self.parameters_group)
        self.lossless_label.setObjectName(u"lossless_label")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lossless_label)

        self.lossless_check = QCheckBox(self.parameters_group)
        self.lossless_check.setObjectName(u"lossless_check")
        sizePolicy1.setHeightForWidth(self.lossless_check.sizePolicy().hasHeightForWidth())
        self.lossless_check.setSizePolicy(sizePolicy1)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.lossless_check)


        self.horizontalLayout.addWidget(self.parameters_group)

        self.derotation_group = QGroupBox(MainFrame)
        self.derotation_group.setObjectName(u"derotation_group")
        sizePolicy2.setHeightForWidth(self.derotation_group.sizePolicy().hasHeightForWidth())
        self.derotation_group.setSizePolicy(sizePolicy2)
        self.derotation_group.setCheckable(False)
        self.derotation_group.setChecked(False)
        self.formLayout = QFormLayout(self.derotation_group)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.enable_label = QLabel(self.derotation_group)
        self.enable_label.setObjectName(u"enable_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.enable_label)

        self.target_label = QLabel(self.derotation_group)
        self.target_label.setObjectName(u"target_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.target_label)

        self.target_combo = QComboBox(self.derotation_group)
        self.target_combo.setObjectName(u"target_combo")
        sizePolicy3.setHeightForWidth(self.target_combo.sizePolicy().hasHeightForWidth())
        self.target_combo.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.target_combo)

        self.latitude_label = QLabel(self.derotation_group)
        self.latitude_label.setObjectName(u"latitude_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.latitude_label)

        self.latitude_spin = QDoubleSpinBox(self.derotation_group)
        self.latitude_spin.setObjectName(u"latitude_spin")
        sizePolicy3.setHeightForWidth(self.latitude_spin.sizePolicy().hasHeightForWidth())
        self.latitude_spin.setSizePolicy(sizePolicy3)
        self.latitude_spin.setMinimum(-90.000000000000000)
        self.latitude_spin.setMaximum(90.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.latitude_spin)

        self.longitude_label = QLabel(self.derotation_group)
        self.longitude_label.setObjectName(u"longitude_label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.longitude_label)

        self.longitude_spin = QDoubleSpinBox(self.derotation_group)
        self.longitude_spin.setObjectName(u"longitude_spin")
        sizePolicy3.setHeightForWidth(self.longitude_spin.sizePolicy().hasHeightForWidth())
        self.longitude_spin.setSizePolicy(sizePolicy3)
        self.longitude_spin.setMinimum(-180.000000000000000)
        self.longitude_spin.setMaximum(180.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.longitude_spin)

        self.enable_check = QCheckBox(self.derotation_group)
        self.enable_check.setObjectName(u"enable_check")
        sizePolicy1.setHeightForWidth(self.enable_check.sizePolicy().hasHeightForWidth())
        self.enable_check.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.enable_check)


        self.horizontalLayout.addWidget(self.derotation_group)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.output_label = QLabel(MainFrame)
        self.output_label.setObjectName(u"output_label")

        self.horizontalLayout_4.addWidget(self.output_label)

        self.output_path_edit = QLineEdit(MainFrame)
        self.output_path_edit.setObjectName(u"output_path_edit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.output_path_edit.sizePolicy().hasHeightForWidth())
        self.output_path_edit.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.output_path_edit)

        self.output_line = QFrame(MainFrame)
        self.output_line.setObjectName(u"output_line")
        self.output_line.setFrameShape(QFrame.Shape.VLine)
        self.output_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.output_line)

        self.output_name_label = QLabel(MainFrame)
        self.output_name_label.setObjectName(u"output_name_label")

        self.horizontalLayout_4.addWidget(self.output_name_label)

        self.output_name_edit = QLineEdit(MainFrame)
        self.output_name_edit.setObjectName(u"output_name_edit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.output_name_edit.sizePolicy().hasHeightForWidth())
        self.output_name_edit.setSizePolicy(sizePolicy6)

        self.horizontalLayout_4.addWidget(self.output_name_edit)

        self.output_browse_button = QPushButton(MainFrame)
        self.output_browse_button.setObjectName(u"output_browse_button")
        self.output_browse_button.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.output_browse_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.settings_button = QPushButton(MainFrame)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy1.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy1)
        self.settings_button.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.settings_button)

        self.show_folder_check = QCheckBox(MainFrame)
        self.show_folder_check.setObjectName(u"show_folder_check")

        self.horizontalLayout_2.addWidget(self.show_folder_check, 0, Qt.AlignmentFlag.AlignRight)

        self.convert_button = QPushButton(MainFrame)
        self.convert_button.setObjectName(u"convert_button")
        sizePolicy1.setHeightForWidth(self.convert_button.sizePolicy().hasHeightForWidth())
        self.convert_button.setSizePolicy(sizePolicy1)
        self.convert_button.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.convert_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

#if QT_CONFIG(shortcut)
        self.input_label.setBuddy(self.input_browse_button)
        self.duration_label.setBuddy(self.duration_spinbox)
        self.quality_label.setBuddy(self.quality_spinbox)
        self.lossless_label.setBuddy(self.lossless_check)
        self.enable_label.setBuddy(self.enable_check)
        self.target_label.setBuddy(self.target_combo)
        self.latitude_label.setBuddy(self.latitude_spin)
        self.longitude_label.setBuddy(self.longitude_spin)
        self.output_label.setBuddy(self.output_browse_button)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.frames_table, self.input_browse_button)
        QWidget.setTabOrder(self.input_browse_button, self.apng_check)
        QWidget.setTabOrder(self.apng_check, self.avif_check)
        QWidget.setTabOrder(self.avif_check, self.webp_check)
        QWidget.setTabOrder(self.webp_check, self.gif_check)
        QWidget.setTabOrder(self.gif_check, self.duration_spinbox)
        QWidget.setTabOrder(self.duration_spinbox, self.quality_spinbox)
        QWidget.setTabOrder(self.quality_spinbox, self.lossless_check)
        QWidget.setTabOrder(self.lossless_check, self.target_combo)
        QWidget.setTabOrder(self.target_combo, self.latitude_spin)
        QWidget.setTabOrder(self.latitude_spin, self.longitude_spin)
        QWidget.setTabOrder(self.longitude_spin, self.output_path_edit)
        QWidget.setTabOrder(self.output_path_edit, self.output_name_edit)
        QWidget.setTabOrder(self.output_name_edit, self.output_browse_button)
        QWidget.setTabOrder(self.output_browse_button, self.settings_button)
        QWidget.setTabOrder(self.settings_button, self.show_folder_check)
        QWidget.setTabOrder(self.show_folder_check, self.convert_button)

        self.retranslateUi(MainFrame)

        self.video_stack.setCurrentIndex(0)
        self.convert_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainFrame)
    # setupUi

    def retranslateUi(self, MainFrame):
        MainFrame.setWindowTitle(QCoreApplication.translate("MainFrame", u"Frame", None))
        self.input_label.setText(QCoreApplication.translate("MainFrame", u"&Input frames", None))
        self.input_browse_button.setText(QCoreApplication.translate("MainFrame", u"Browse...", None))
        self.formats_group.setTitle(QCoreApplication.translate("MainFrame", u"Formats", None))
        self.webp_check.setText(QCoreApplication.translate("MainFrame", u"&WebP", None))
        self.avif_check.setText(QCoreApplication.translate("MainFrame", u"A&VIF", None))
        self.apng_check.setText(QCoreApplication.translate("MainFrame", u"A&PNG", None))
        self.gif_check.setText(QCoreApplication.translate("MainFrame", u"&GIF", None))
        self.mp4_check.setText(QCoreApplication.translate("MainFrame", u"MP&4", None))
        self.webm_check.setText(QCoreApplication.translate("MainFrame", u"Web&M", None))
        self.requires_ffmpeg_label.setText(QCoreApplication.translate("MainFrame", u"MP4 and WebM requires FFmpeg.", None))
        self.parameters_group.setTitle(QCoreApplication.translate("MainFrame", u"Conversion parameters", None))
        self.duration_label.setText(QCoreApplication.translate("MainFrame", u"&FPS", None))
        self.quality_label.setText(QCoreApplication.translate("MainFrame", u"&Quality", None))
        self.lossless_label.setText(QCoreApplication.translate("MainFrame", u"&Lossless", None))
        self.lossless_check.setText("")
        self.derotation_group.setTitle(QCoreApplication.translate("MainFrame", u"Alt-az field derotation", None))
        self.enable_label.setText(QCoreApplication.translate("MainFrame", u"&Enable", None))
        self.target_label.setText(QCoreApplication.translate("MainFrame", u"&Target", None))
        self.latitude_label.setText(QCoreApplication.translate("MainFrame", u"L&atitude", None))
        self.latitude_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.longitude_label.setText(QCoreApplication.translate("MainFrame", u"Lo&ngitude", None))
        self.longitude_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.enable_check.setText("")
        self.output_label.setText(QCoreApplication.translate("MainFrame", u"&Output folder", None))
        self.output_name_label.setText(QCoreApplication.translate("MainFrame", u"Name", None))
        self.output_browse_button.setText(QCoreApplication.translate("MainFrame", u"Browse...", None))
        self.settings_button.setText(QCoreApplication.translate("MainFrame", u"&Settings", None))
        self.show_folder_check.setText(QCoreApplication.translate("MainFrame", u"Show folder when &done", None))
        self.convert_button.setText(QCoreApplication.translate("MainFrame", u"&Convert", None))
    # retranslateUi

