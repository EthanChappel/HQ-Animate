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
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTableView, QVBoxLayout,
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
        self.input_label = QLabel(MainFrame)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.input_label)

        self.frames_table = QTableView(MainFrame)
        self.frames_table.setObjectName(u"frames_table")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frames_table.sizePolicy().hasHeightForWidth())
        self.frames_table.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.frames_table)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.drag_drop_label = QLabel(MainFrame)
        self.drag_drop_label.setObjectName(u"drag_drop_label")

        self.horizontalLayout_11.addWidget(self.drag_drop_label)

        self.horizontalSpacer_8 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.input_browse_button = QPushButton(MainFrame)
        self.input_browse_button.setObjectName(u"input_browse_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_browse_button.sizePolicy().hasHeightForWidth())
        self.input_browse_button.setSizePolicy(sizePolicy1)
        self.input_browse_button.setAutoDefault(True)

        self.horizontalLayout_11.addWidget(self.input_browse_button)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.parameters_group.sizePolicy().hasHeightForWidth())
        self.parameters_group.setSizePolicy(sizePolicy2)
        self.formLayout_2 = QFormLayout(self.parameters_group)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.width_label = QLabel(self.parameters_group)
        self.width_label.setObjectName(u"width_label")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.width_label)

        self.width_spinner = QSpinBox(self.parameters_group)
        self.width_spinner.setObjectName(u"width_spinner")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.width_spinner.sizePolicy().hasHeightForWidth())
        self.width_spinner.setSizePolicy(sizePolicy3)
        self.width_spinner.setMinimum(1)
        self.width_spinner.setMaximum(16383)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.width_spinner)

        self.height_label = QLabel(self.parameters_group)
        self.height_label.setObjectName(u"height_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.height_label)

        self.height_spinner = QSpinBox(self.parameters_group)
        self.height_spinner.setObjectName(u"height_spinner")
        sizePolicy3.setHeightForWidth(self.height_spinner.sizePolicy().hasHeightForWidth())
        self.height_spinner.setSizePolicy(sizePolicy3)
        self.height_spinner.setMinimum(1)
        self.height_spinner.setMaximum(16383)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.height_spinner)


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
        sizePolicy2.setHeightForWidth(self.method_groupbox.sizePolicy().hasHeightForWidth())
        self.method_groupbox.setSizePolicy(sizePolicy2)
        self.formLayout_10 = QFormLayout(self.method_groupbox)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.average_label = QLabel(self.method_groupbox)
        self.average_label.setObjectName(u"average_label")

        self.formLayout_10.setWidget(2, QFormLayout.ItemRole.LabelRole, self.average_label)

        self.average_spinner = QSpinBox(self.method_groupbox)
        self.average_spinner.setObjectName(u"average_spinner")
        sizePolicy3.setHeightForWidth(self.average_spinner.sizePolicy().hasHeightForWidth())
        self.average_spinner.setSizePolicy(sizePolicy3)
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
        sizePolicy1.setHeightForWidth(self.subtract_check.sizePolicy().hasHeightForWidth())
        self.subtract_check.setSizePolicy(sizePolicy1)
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
        sizePolicy3.setHeightForWidth(self.spread_spinner.sizePolicy().hasHeightForWidth())
        self.spread_spinner.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.rotate_spinner.sizePolicy().hasHeightForWidth())
        self.rotate_spinner.setSizePolicy(sizePolicy3)
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
        sizePolicy2.setHeightForWidth(self.derotation_group.sizePolicy().hasHeightForWidth())
        self.derotation_group.setSizePolicy(sizePolicy2)
        self.derotation_group.setCheckable(True)
        self.derotation_group.setChecked(False)
        self.formLayout = QFormLayout(self.derotation_group)
        self.formLayout.setObjectName(u"formLayout")
        self.target_label = QLabel(self.derotation_group)
        self.target_label.setObjectName(u"target_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.target_label)

        self.target_combo = QComboBox(self.derotation_group)
        self.target_combo.setObjectName(u"target_combo")
        sizePolicy3.setHeightForWidth(self.target_combo.sizePolicy().hasHeightForWidth())
        self.target_combo.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.target_combo)

        self.latitude_label = QLabel(self.derotation_group)
        self.latitude_label.setObjectName(u"latitude_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.latitude_label)

        self.latitude_spin = QDoubleSpinBox(self.derotation_group)
        self.latitude_spin.setObjectName(u"latitude_spin")
        sizePolicy3.setHeightForWidth(self.latitude_spin.sizePolicy().hasHeightForWidth())
        self.latitude_spin.setSizePolicy(sizePolicy3)
        self.latitude_spin.setMinimum(-90.000000000000000)
        self.latitude_spin.setMaximum(90.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.latitude_spin)

        self.longitude_label = QLabel(self.derotation_group)
        self.longitude_label.setObjectName(u"longitude_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.longitude_label)

        self.longitude_spin = QDoubleSpinBox(self.derotation_group)
        self.longitude_spin.setObjectName(u"longitude_spin")
        sizePolicy3.setHeightForWidth(self.longitude_spin.sizePolicy().hasHeightForWidth())
        self.longitude_spin.setSizePolicy(sizePolicy3)
        self.longitude_spin.setMinimum(-180.000000000000000)
        self.longitude_spin.setMaximum(180.000000000000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.longitude_spin)

        self.az_tilt_spin = QDoubleSpinBox(self.derotation_group)
        self.az_tilt_spin.setObjectName(u"az_tilt_spin")
        sizePolicy3.setHeightForWidth(self.az_tilt_spin.sizePolicy().hasHeightForWidth())
        self.az_tilt_spin.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.alt_tilt_spin.sizePolicy().hasHeightForWidth())
        self.alt_tilt_spin.setSizePolicy(sizePolicy3)
        self.alt_tilt_spin.setMinimum(-90.000000000000000)
        self.alt_tilt_spin.setMaximum(90.000000000000000)
        self.alt_tilt_spin.setSingleStep(0.100000000000000)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.alt_tilt_spin)


        self.verticalLayout_20.addWidget(self.derotation_group)


        self.horizontalLayout_13.addWidget(self.frame_3)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.settings_button = QPushButton(MainFrame)
        self.settings_button.setObjectName(u"settings_button")
        sizePolicy1.setHeightForWidth(self.settings_button.sizePolicy().hasHeightForWidth())
        self.settings_button.setSizePolicy(sizePolicy1)
        self.settings_button.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.settings_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.next_button = QPushButton(MainFrame)
        self.next_button.setObjectName(u"next_button")
        sizePolicy1.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy1)
        self.next_button.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.next_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

#if QT_CONFIG(shortcut)
        self.input_label.setBuddy(self.input_browse_button)
        self.width_label.setBuddy(self.width_spinner)
        self.height_label.setBuddy(self.height_spinner)
        self.average_label.setBuddy(self.average_spinner)
        self.subtract_label.setBuddy(self.subtract_check)
        self.spread_label.setBuddy(self.spread_spinner)
        self.rotate_label.setBuddy(self.rotate_spinner)
        self.target_label.setBuddy(self.target_combo)
        self.latitude_label.setBuddy(self.latitude_spin)
        self.longitude_label.setBuddy(self.longitude_spin)
        self.alt_tilt_label.setBuddy(self.alt_tilt_spin)
        self.az_tilt_label.setBuddy(self.az_tilt_spin)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.input_browse_button, self.width_spinner)
        QWidget.setTabOrder(self.width_spinner, self.height_spinner)
        QWidget.setTabOrder(self.height_spinner, self.rotate_spinner)
        QWidget.setTabOrder(self.rotate_spinner, self.average_spinner)
        QWidget.setTabOrder(self.average_spinner, self.subtract_check)
        QWidget.setTabOrder(self.subtract_check, self.spread_spinner)
        QWidget.setTabOrder(self.spread_spinner, self.derotation_group)
        QWidget.setTabOrder(self.derotation_group, self.target_combo)
        QWidget.setTabOrder(self.target_combo, self.latitude_spin)
        QWidget.setTabOrder(self.latitude_spin, self.longitude_spin)
        QWidget.setTabOrder(self.longitude_spin, self.alt_tilt_spin)
        QWidget.setTabOrder(self.alt_tilt_spin, self.az_tilt_spin)
        QWidget.setTabOrder(self.az_tilt_spin, self.settings_button)
        QWidget.setTabOrder(self.settings_button, self.next_button)

        self.retranslateUi(MainFrame)
        self.subtract_check.toggled.connect(self.spread_label.setVisible)
        self.subtract_check.toggled.connect(self.spread_spinner.setVisible)

        self.next_button.setDefault(True)


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
        self.input_browse_button.setText(QCoreApplication.translate("MainFrame", u"Select frames", None))
        self.parameters_group.setTitle(QCoreApplication.translate("MainFrame", u"Dimemsions", None))
        self.width_label.setText(QCoreApplication.translate("MainFrame", u"&Width", None))
#if QT_CONFIG(tooltip)
        self.width_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Horizontal width in pixels of the animation.", None))
#endif // QT_CONFIG(tooltip)
        self.width_spinner.setSuffix(QCoreApplication.translate("MainFrame", u"px", None))
        self.height_label.setText(QCoreApplication.translate("MainFrame", u"&Height", None))
#if QT_CONFIG(tooltip)
        self.height_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Vertical height in pixels of the animation.", None))
#endif // QT_CONFIG(tooltip)
        self.height_spinner.setSuffix(QCoreApplication.translate("MainFrame", u"px", None))
        self.method_groupbox.setTitle(QCoreApplication.translate("MainFrame", u"Process", None))
        self.average_label.setText(QCoreApplication.translate("MainFrame", u"&Average", None))
#if QT_CONFIG(tooltip)
        self.average_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Each frame of the output animation is a result of a moving average of input frames.\n"
"\n"
"No effect if set to 1.", None))
#endif // QT_CONFIG(tooltip)
        self.average_spinner.setPrefix("")
        self.subtract_label.setText(QCoreApplication.translate("MainFrame", u"Su&btract", None))
#if QT_CONFIG(tooltip)
        self.subtract_check.setToolTip(QCoreApplication.translate("MainFrame", u"Each frame of the output animation becomes the subtraction of one frame from another. Color frames will be converted to monochrome.", None))
#endif // QT_CONFIG(tooltip)
        self.subtract_check.setText("")
        self.spread_label.setText(QCoreApplication.translate("MainFrame", u"S&pread", None))
#if QT_CONFIG(tooltip)
        self.spread_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"How many frames apart the frame to subtract with is from the input frame.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_label.setText(QCoreApplication.translate("MainFrame", u"&Rotate", None))
#if QT_CONFIG(tooltip)
        self.rotate_spinner.setToolTip(QCoreApplication.translate("MainFrame", u"Rotate each frame by an arbitrary amount in degrees. Positive values rotate clockwise and negative rotate counterclockwise.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_spinner.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.rotate_spinner.setPrefix("")
        self.derotation_group.setTitle(QCoreApplication.translate("MainFrame", u"Alt-az field &derotation", None))
        self.target_label.setText(QCoreApplication.translate("MainFrame", u"&Target", None))
        self.latitude_label.setText(QCoreApplication.translate("MainFrame", u"L&atitude", None))
#if QT_CONFIG(tooltip)
        self.latitude_spin.setToolTip(QCoreApplication.translate("MainFrame", u"Decimal degrees of latitude. Positive is north and negative is south.", None))
#endif // QT_CONFIG(tooltip)
        self.latitude_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.longitude_label.setText(QCoreApplication.translate("MainFrame", u"Lon&gitude", None))
#if QT_CONFIG(tooltip)
        self.longitude_spin.setToolTip(QCoreApplication.translate("MainFrame", u"Decimal degrees of longitude. Positive is east and negative is west.", None))
#endif // QT_CONFIG(tooltip)
        self.longitude_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
#if QT_CONFIG(tooltip)
        self.az_tilt_spin.setToolTip(QCoreApplication.translate("MainFrame", u"When an alt-az telescope is not leveled, field derotation will not work perfectly and a slight drift in rotation will occur over a timelapse. Positive when telescope is tilted towards east and negative towards west.", None))
#endif // QT_CONFIG(tooltip)
        self.az_tilt_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.alt_tilt_label.setText(QCoreApplication.translate("MainFrame", u"N&orth tilt", None))
        self.az_tilt_label.setText(QCoreApplication.translate("MainFrame", u"&East tilt", None))
#if QT_CONFIG(tooltip)
        self.alt_tilt_spin.setToolTip(QCoreApplication.translate("MainFrame", u"When an alt-az telescope is not leveled, field derotation will not work perfectly and a slight drift in rotation will occur over a timelapse. Positive when telescope is tilted towards north and negative towards south.", None))
#endif // QT_CONFIG(tooltip)
        self.alt_tilt_spin.setSuffix(QCoreApplication.translate("MainFrame", u"\u00b0", None))
        self.settings_button.setText(QCoreApplication.translate("MainFrame", u"&Settings", None))
        self.next_button.setText(QCoreApplication.translate("MainFrame", u"&Next", None))
    # retranslateUi

