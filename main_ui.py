# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 575)
        MainWindow.setStyleSheet(u"QStackedWidget{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(253, 253, 253);\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(90, 16777215))
        self.frame_6.setStyleSheet(u"QFrame:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.HOME = QPushButton(self.frame_6)
        self.HOME.setObjectName(u"HOME")
        self.HOME.setMinimumSize(QSize(0, 30))
        self.HOME.setMaximumSize(QSize(16777215, 40))
        self.HOME.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/img/homeAsset 46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.HOME.setIcon(icon)
        self.HOME.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.HOME)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(50, 16777215))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"		\n"
"	background-color: rgb(22, 22, 22);\n"
"}\n"
"\n"
"QFrame:hover{\n"
"		\n"
"	background-color: rgb(66, 148, 208);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Bn_Min = QPushButton(self.frame_7)
        self.Bn_Min.setObjectName(u"Bn_Min")
        self.Bn_Min.setMinimumSize(QSize(0, 40))
        self.Bn_Min.setMaximumSize(QSize(16777215, 40))
        self.Bn_Min.setCursor(QCursor(Qt.PointingHandCursor))
        self.Bn_Min.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/img/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bn_Min.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.Bn_Min)


        self.horizontalLayout.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(50, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"		\n"
"	background-color: rgb(22, 22, 22);\n"
"}\n"
"\n"
"QFrame:hover{\n"
"		\n"
"	\n"
"	background-color: rgb(235, 0, 0);\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Bn_Close = QPushButton(self.frame_4)
        self.Bn_Close.setObjectName(u"Bn_Close")
        self.Bn_Close.setMinimumSize(QSize(0, 0))
        self.Bn_Close.setMaximumSize(QSize(16777215, 40))
        self.Bn_Close.setCursor(QCursor(Qt.ClosedHandCursor))
        self.Bn_Close.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/img/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Bn_Close.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.Bn_Close)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.Info_1 = QWidget()
        self.Info_1.setObjectName(u"Info_1")
        self.verticalLayout_5 = QVBoxLayout(self.Info_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_11 = QFrame(self.Info_1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	\n"
"	background-color: rgb(239, 239, 239);\n"
"	/*border:1px solid gray;*/\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
" 	\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    "
                        "border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.comboBox = QComboBox(self.frame_11)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 39))
        self.comboBox.setMaximumSize(QSize(16777215, 39))

        self.gridLayout_7.addWidget(self.comboBox, 7, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_11)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 39))
        self.comboBox_2.setMaximumSize(QSize(16777215, 39))

        self.gridLayout_7.addWidget(self.comboBox_2, 7, 2, 1, 1)

        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_7.addWidget(self.label_3, 6, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.verticalSpacer_6, 11, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 11, 4, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_11)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 39))
        self.comboBox_3.setMaximumSize(QSize(16777215, 39))

        self.gridLayout_7.addWidget(self.comboBox_3, 7, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.Addr = QLineEdit(self.frame_11)
        self.Addr.setObjectName(u"Addr")
        self.Addr.setMinimumSize(QSize(0, 70))
        self.Addr.setMaximumSize(QSize(16777215, 60))
        self.Addr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.Addr, 10, 0, 1, 7)

        self.img = QPushButton(self.frame_11)
        self.img.setObjectName(u"img")
        self.img.setMinimumSize(QSize(160, 160))
        self.img.setMaximumSize(QSize(16777215, 160))
        self.img.setCursor(QCursor(Qt.PointingHandCursor))
        self.img.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:15px;\n"
"}")
        self.img.setIconSize(QSize(150, 150))

        self.gridLayout_7.addWidget(self.img, 1, 0, 5, 3)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)

        self.gridLayout_7.addWidget(self.label_7, 1, 3, 1, 2)

        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 10))
        self.label.setMaximumSize(QSize(16777215, 10))

        self.gridLayout_7.addWidget(self.label, 4, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 0, 4, 1, 1)

        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_5, 8, 0, 1, 1)

        self.Email = QLineEdit(self.frame_11)
        self.Email.setObjectName(u"Email")
        self.Email.setMinimumSize(QSize(0, 40))
        self.Email.setMaximumSize(QSize(16777215, 40))
        self.Email.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.Email, 5, 5, 1, 1)

        self.phone = QLineEdit(self.frame_11)
        self.phone.setObjectName(u"phone")
        self.phone.setMinimumSize(QSize(0, 40))
        self.phone.setMaximumSize(QSize(16777215, 40))
        self.phone.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.phone, 3, 5, 1, 1)

        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 4, 5, 1, 1)

        self.L_name = QLineEdit(self.frame_11)
        self.L_name.setObjectName(u"L_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.L_name.sizePolicy().hasHeightForWidth())
        self.L_name.setSizePolicy(sizePolicy1)
        self.L_name.setMinimumSize(QSize(0, 40))
        self.L_name.setMaximumSize(QSize(500, 40))
        self.L_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.L_name, 3, 3, 1, 2)

        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_7.addWidget(self.label_6, 2, 5, 1, 1)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 10))
        self.label_2.setMaximumSize(QSize(16777215, 10))

        self.gridLayout_7.addWidget(self.label_2, 2, 3, 1, 1)

        self.F_name = QLineEdit(self.frame_11)
        self.F_name.setObjectName(u"F_name")
        sizePolicy1.setHeightForWidth(self.F_name.sizePolicy().hasHeightForWidth())
        self.F_name.setSizePolicy(sizePolicy1)
        self.F_name.setMinimumSize(QSize(160, 40))
        self.F_name.setMaximumSize(QSize(400, 40))
        self.F_name.setStyleSheet(u"")
        self.F_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.F_name, 5, 3, 1, 2)

        self.lineEdit_5 = QLineEdit(self.frame_11)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 40))
        self.lineEdit_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.lineEdit_5, 7, 3, 1, 3)

        self.label_21 = QLabel(self.frame_11)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 6, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.Info_1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 80))
        self.frame_12.setMaximumSize(QSize(16777215, 80))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_12)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 1, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_19, 0, 4, 1, 1)

        self.B_pre = QPushButton(self.frame_12)
        self.B_pre.setObjectName(u"B_pre")
        self.B_pre.setMinimumSize(QSize(100, 30))
        self.B_pre.setMaximumSize(QSize(100, 30))
        self.B_pre.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_pre.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.B_pre, 0, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_18, 0, 0, 1, 1)

        self.B_suiv = QPushButton(self.frame_12)
        self.B_suiv.setObjectName(u"B_suiv")
        self.B_suiv.setMinimumSize(QSize(100, 30))
        self.B_suiv.setMaximumSize(QSize(100, 30))
        self.B_suiv.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_suiv.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.B_suiv, 0, 3, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_9, 1, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.Info_1)
        self.Formation = QWidget()
        self.Formation.setObjectName(u"Formation")
        self.verticalLayout_6 = QVBoxLayout(self.Formation)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.Formation)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.Terminer = QPushButton(self.frame_5)
        self.Terminer.setObjectName(u"Terminer")
        self.Terminer.setMinimumSize(QSize(100, 27))
        self.Terminer.setMaximumSize(QSize(16777215, 30))
        self.Terminer.setCursor(QCursor(Qt.PointingHandCursor))
        self.Terminer.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_10.addWidget(self.Terminer, 2, 0, 1, 1, Qt.AlignHCenter)

        self.toolBox = QToolBox(self.frame_5)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QToolBox::tab {\n"
"	background-color: rgb(66, 148, 208);\n"
"    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    color: white;\n"
"	font:bold;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 426, 298))
        self.gridLayout_12 = QGridLayout(self.page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_14 = QFrame(self.page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	\n"
"	background-color: rgb(239, 239, 239);\n"
"	/*border:1px solid gray;*/\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
""
                        "    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_14)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_13.addWidget(self.label_10, 3, 4, 1, 1)

        self.label_9 = QLabel(self.frame_14)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_13.addWidget(self.label_9, 3, 0, 1, 2)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_11, 8, 3, 1, 1)

        self.label_12 = QLabel(self.frame_14)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_13.addWidget(self.label_12, 5, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_14)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 50))
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.lineEdit_4, 4, 4, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_6, 6, 0, 2, 1)

        self.Date_D = QComboBox(self.frame_14)
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.addItem("")
        self.Date_D.setObjectName(u"Date_D")
        sizePolicy.setHeightForWidth(self.Date_D.sizePolicy().hasHeightForWidth())
        self.Date_D.setSizePolicy(sizePolicy)
        self.Date_D.setMinimumSize(QSize(150, 40))

        self.gridLayout_13.addWidget(self.Date_D, 6, 1, 2, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 43, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_7, 5, 5, 2, 1)

        self.horizontalSpacer_5 = QSpacerItem(133, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_5, 5, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_4, 7, 4, 1, 2)

        self.Date_F = QComboBox(self.frame_14)
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.addItem("")
        self.Date_F.setObjectName(u"Date_F")
        sizePolicy.setHeightForWidth(self.Date_F.sizePolicy().hasHeightForWidth())
        self.Date_F.setSizePolicy(sizePolicy)
        self.Date_F.setMinimumSize(QSize(150, 40))

        self.gridLayout_13.addWidget(self.Date_F, 6, 3, 2, 1)

        self.horizontalSpacer_3 = QSpacerItem(406, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_3, 0, 2, 1, 4)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_13.addWidget(self.label_11, 5, 3, 1, 1)

        self.Etabl = QLineEdit(self.frame_14)
        self.Etabl.setObjectName(u"Etabl")
        self.Etabl.setMinimumSize(QSize(0, 50))
        self.Etabl.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.Etabl, 4, 0, 1, 4)

        self.verticalSpacer_12 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.verticalSpacer_12, 2, 0, 1, 1)

        self.Form = QLineEdit(self.frame_14)
        self.Form.setObjectName(u"Form")
        self.Form.setMinimumSize(QSize(0, 50))
        self.Form.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.Form, 1, 0, 1, 6)

        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_13.addWidget(self.label_8, 0, 0, 1, 2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_10, 8, 1, 1, 1)


        self.gridLayout_12.addWidget(self.frame_14, 0, 0, 1, 1)

        self.toolBox.addItem(self.page, u"Formation")

        self.gridLayout_10.addWidget(self.toolBox, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_13 = QFrame(self.Formation)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 80))
        self.frame_13.setMaximumSize(QSize(16777215, 80))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_13)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.B_pre_2 = QPushButton(self.frame_13)
        self.B_pre_2.setObjectName(u"B_pre_2")
        self.B_pre_2.setMinimumSize(QSize(100, 30))
        self.B_pre_2.setMaximumSize(QSize(100, 30))
        self.B_pre_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_pre_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_11.addWidget(self.B_pre_2, 0, 1, 1, 1)

        self.B_suiv_2 = QPushButton(self.frame_13)
        self.B_suiv_2.setObjectName(u"B_suiv_2")
        self.B_suiv_2.setMinimumSize(QSize(100, 30))
        self.B_suiv_2.setMaximumSize(QSize(100, 30))
        self.B_suiv_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_suiv_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_11.addWidget(self.B_suiv_2, 0, 4, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_13)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(108, 27))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	color: red;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	color:red;\n"
"	\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/img/remv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(20, 25))

        self.gridLayout_11.addWidget(self.pushButton_3, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.frame_13)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(108, 27))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	color: #408fc9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/img/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(20, 25))

        self.gridLayout_11.addWidget(self.pushButton, 0, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_22, 0, 5, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_24, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.Formation)
        self.Exper = QWidget()
        self.Exper.setObjectName(u"Exper")
        self.verticalLayout_7 = QVBoxLayout(self.Exper)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_15 = QFrame(self.Exper)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_15)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.Terminer_1 = QPushButton(self.frame_15)
        self.Terminer_1.setObjectName(u"Terminer_1")
        self.Terminer_1.setMinimumSize(QSize(100, 27))
        self.Terminer_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.Terminer_1.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_14.addWidget(self.Terminer_1, 1, 0, 1, 1, Qt.AlignHCenter)

        self.toolBox_2 = QToolBox(self.frame_15)
        self.toolBox_2.setObjectName(u"toolBox_2")
        self.toolBox_2.setStyleSheet(u"QToolBox::tab {\n"
"	background-color: rgb(66, 148, 208);\n"
"    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    color: white;\n"
"	font:bold;\n"
"}")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 305, 331))
        self.gridLayout_15 = QGridLayout(self.page_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_17 = QFrame(self.page_5)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(239, 239, 239);\n"
"	/*border:1px solid gray;*/\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-l"
                        "eft-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-radius:4px;\n"
"}\n"
"QTextEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_17)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.comboBox_7 = QComboBox(self.frame_17)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMinimumSize(QSize(0, 30))

        self.gridLayout_17.addWidget(self.comboBox_7, 5, 3, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame_17)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.gridLayout_17.addWidget(self.textEdit_2, 7, 0, 1, 4)

        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_17.addWidget(self.label_14, 2, 0, 1, 1)

        self.comboBox_5 = QComboBox(self.frame_17)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(0, 30))

        self.gridLayout_17.addWidget(self.comboBox_5, 5, 1, 1, 1)

        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_17.addWidget(self.label_16, 4, 0, 1, 1)

        self.comboBox_6 = QComboBox(self.frame_17)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(0, 30))

        self.gridLayout_17.addWidget(self.comboBox_6, 5, 2, 1, 1)

        self.label_13 = QLabel(self.frame_17)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_17.addWidget(self.label_13, 0, 0, 1, 1)

        self.Poste = QLineEdit(self.frame_17)
        self.Poste.setObjectName(u"Poste")
        self.Poste.setMinimumSize(QSize(0, 50))
        self.Poste.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.Poste, 3, 0, 1, 2)

        self.Ville_1 = QLineEdit(self.frame_17)
        self.Ville_1.setObjectName(u"Ville_1")
        self.Ville_1.setMinimumSize(QSize(0, 50))
        self.Ville_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.Ville_1, 3, 2, 1, 2)

        self.label_18 = QLabel(self.frame_17)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_17.addWidget(self.label_18, 6, 0, 1, 1)

        self.label_15 = QLabel(self.frame_17)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_17.addWidget(self.label_15, 2, 2, 1, 1)

        self.comboBox_4 = QComboBox(self.frame_17)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 30))

        self.gridLayout_17.addWidget(self.comboBox_4, 5, 0, 1, 1)

        self.Entrep = QLineEdit(self.frame_17)
        self.Entrep.setObjectName(u"Entrep")
        self.Entrep.setMinimumSize(QSize(0, 50))
        self.Entrep.setAlignment(Qt.AlignCenter)

        self.gridLayout_17.addWidget(self.Entrep, 1, 0, 1, 4)

        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_17.addWidget(self.label_17, 4, 2, 1, 1)


        self.gridLayout_15.addWidget(self.frame_17, 0, 0, 1, 1)

        self.toolBox_2.addItem(self.page_5, u"Experience")

        self.gridLayout_14.addWidget(self.toolBox_2, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.Exper)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 80))
        self.frame_16.setMaximumSize(QSize(16777215, 80))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_16)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.pushButton_2 = QPushButton(self.frame_16)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(108, 27))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	color: #408fc9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QSize(20, 25))

        self.gridLayout_16.addWidget(self.pushButton_2, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.frame_16)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(108, 27))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	color: red;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(20, 25))

        self.gridLayout_16.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.B_suiv_3 = QPushButton(self.frame_16)
        self.B_suiv_3.setObjectName(u"B_suiv_3")
        self.B_suiv_3.setMinimumSize(QSize(100, 30))
        self.B_suiv_3.setMaximumSize(QSize(100, 30))
        self.B_suiv_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_suiv_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_16.addWidget(self.B_suiv_3, 0, 4, 1, 1)

        self.B_pre_3 = QPushButton(self.frame_16)
        self.B_pre_3.setObjectName(u"B_pre_3")
        self.B_pre_3.setMinimumSize(QSize(100, 30))
        self.B_pre_3.setMaximumSize(QSize(100, 30))
        self.B_pre_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_pre_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_16.addWidget(self.B_pre_3, 0, 1, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_25, 0, 0, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_27, 0, 5, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.Exper)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_18 = QGridLayout(self.page_6)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.frame_18 = QFrame(self.page_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 0))
        self.frame_18.setMaximumSize(QSize(16777215, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_18)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_14, 5, 1, 1, 1)

        self.toolBox_3 = QToolBox(self.frame_18)
        self.toolBox_3.setObjectName(u"toolBox_3")
        self.toolBox_3.setEnabled(True)
        self.toolBox_3.setStyleSheet(u"QToolBox::tab {\n"
"	background-color: rgb(66, 148, 208);\n"
"    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    color: white;\n"
"	font:bold;\n"
"}")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 98, 124))
        self.gridLayout_22 = QGridLayout(self.page_4)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_21 = QFrame(self.page_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(239, 239, 239);\n"
"	/*border:1px solid gray;*/\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-l"
                        "eft-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-radius:4px;\n"
"}\n"
"QTextEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_21)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.lineEdit_2 = QLineEdit(self.frame_21)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 60))
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_24.addWidget(self.lineEdit_2, 1, 0, 1, 1)

        self.label_19 = QLabel(self.frame_21)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 20))
        self.label_19.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_24.addWidget(self.label_19, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frame_21, 0, 0, 1, 1)

        self.toolBox_3.addItem(self.page_4, u"Comp\u00e9tence")

        self.gridLayout_20.addWidget(self.toolBox_3, 0, 0, 1, 3)

        self.pushButton_5 = QPushButton(self.frame_18)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 25))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	color: #408fc9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_5.setIcon(icon4)

        self.gridLayout_20.addWidget(self.pushButton_5, 2, 0, 1, 3)

        self.pushButton_6 = QPushButton(self.frame_18)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 25))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	color: red;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_6.setIcon(icon3)

        self.gridLayout_20.addWidget(self.pushButton_6, 3, 0, 1, 3)

        self.pushButton_7 = QPushButton(self.frame_18)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 25))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_20.addWidget(self.pushButton_7, 4, 0, 1, 3)


        self.gridLayout_18.addWidget(self.frame_18, 0, 0, 1, 1)

        self.frame_19 = QFrame(self.page_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_19)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.toolBox_4 = QToolBox(self.frame_19)
        self.toolBox_4.setObjectName(u"toolBox_4")
        self.toolBox_4.setStyleSheet(u"QToolBox::tab {\n"
"	background-color: rgb(66, 148, 208);\n"
"    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    color: white;\n"
"	font:bold;\n"
"}")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setGeometry(QRect(0, 0, 148, 118))
        self.gridLayout_23 = QGridLayout(self.page_8)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.frame_22 = QFrame(self.page_8)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 100))
        self.frame_22.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(239, 239, 239);\n"
"	/*border:1px solid gray;*/\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-l"
                        "eft-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-radius:4px;\n"
"}\n"
"QTextEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_22)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_20 = QLabel(self.frame_22)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 20))
        self.label_20.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_8.addWidget(self.label_20)

        self.lineEdit_3 = QLineEdit(self.frame_22)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 60))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lineEdit_3)


        self.gridLayout_23.addWidget(self.frame_22, 0, 0, 1, 1)

        self.toolBox_4.addItem(self.page_8, u"Comp\u00e9tence Personnel")

        self.gridLayout_21.addWidget(self.toolBox_4, 0, 0, 1, 3)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_16, 4, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.frame_19)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 25))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	color: #408fc9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_8.setIcon(icon4)

        self.gridLayout_21.addWidget(self.pushButton_8, 1, 0, 1, 3)

        self.pushButton_9 = QPushButton(self.frame_19)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 25))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	color: red;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_9.setIcon(icon3)

        self.gridLayout_21.addWidget(self.pushButton_9, 2, 0, 1, 3)

        self.pushButton_10 = QPushButton(self.frame_19)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 25))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_21.addWidget(self.pushButton_10, 3, 0, 1, 3)


        self.gridLayout_18.addWidget(self.frame_19, 0, 1, 1, 1)

        self.frame_20 = QFrame(self.page_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 80))
        self.frame_20.setMaximumSize(QSize(16777215, 80))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_20)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalSpacer_29 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_29, 0, 0, 1, 1)

        self.B_pre_4 = QPushButton(self.frame_20)
        self.B_pre_4.setObjectName(u"B_pre_4")
        self.B_pre_4.setMinimumSize(QSize(100, 30))
        self.B_pre_4.setMaximumSize(QSize(100, 30))
        self.B_pre_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_pre_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_19.addWidget(self.B_pre_4, 0, 1, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_30, 0, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(97, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_9, 0, 3, 1, 1)

        self.B_suiv_4 = QPushButton(self.frame_20)
        self.B_suiv_4.setObjectName(u"B_suiv_4")
        self.B_suiv_4.setMinimumSize(QSize(100, 30))
        self.B_suiv_4.setMaximumSize(QSize(100, 30))
        self.B_suiv_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_suiv_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_19.addWidget(self.B_suiv_4, 0, 4, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_28, 0, 5, 1, 1)


        self.gridLayout_18.addWidget(self.frame_20, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_6)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.gridLayout_32 = QGridLayout(self.page_9)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.frame_26 = QFrame(self.page_9)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_26)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.pushButton_13 = QPushButton(self.frame_26)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 25))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	color: red;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_13.setIcon(icon3)

        self.gridLayout_30.addWidget(self.pushButton_13, 2, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.frame_26)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 25))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_30.addWidget(self.pushButton_14, 3, 0, 1, 1)

        self.toolBox_5 = QToolBox(self.frame_26)
        self.toolBox_5.setObjectName(u"toolBox_5")
        self.toolBox_5.setStyleSheet(u"QToolBox::tab {\n"
"	background-color: rgb(66, 148, 208);\n"
"    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    color: white;\n"
"	font:bold;\n"
"}")
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.page_16.setGeometry(QRect(0, 0, 230, 68))
        self.gridLayout_34 = QGridLayout(self.page_16)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.frame_28 = QFrame(self.page_16)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	\n"
"	background-color: rgb(239, 239, 239);\n"
"	/*border:1px solid gray;*/\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-"
                        "right-radius: 3px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_28)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.comboBox_8 = QComboBox(self.frame_28)
        icon5 = QIcon()
        icon5.addFile(u":/flag/flag/ar.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/flag/flag/eng.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/flag/flag/fr.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/flag/flag/russ.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/flag/flag/chin.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/flag/flag/germ.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon10, "")
        icon11 = QIcon()
        icon11.addFile(u":/flag/flag/jap.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon11, "")
        icon12 = QIcon()
        icon12.addFile(u":/flag/flag/esp.PNG", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_8.addItem(icon12, "")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMinimumSize(QSize(0, 30))
        self.comboBox_8.setCursor(QCursor(Qt.OpenHandCursor))
        self.comboBox_8.setIconSize(QSize(19, 19))

        self.gridLayout_33.addWidget(self.comboBox_8, 0, 0, 1, 1)

        self.comboBox_9 = QComboBox(self.frame_28)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMinimumSize(QSize(0, 30))
        self.comboBox_9.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout_33.addWidget(self.comboBox_9, 0, 1, 1, 1)


        self.gridLayout_34.addWidget(self.frame_28, 0, 0, 1, 1)

        self.toolBox_5.addItem(self.page_16, u"LANGUES")

        self.gridLayout_30.addWidget(self.toolBox_5, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.frame_26)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 25))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	color: #408fc9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_12.setIcon(icon4)

        self.gridLayout_30.addWidget(self.pushButton_12, 1, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_30.addItem(self.verticalSpacer_13, 4, 0, 1, 1)


        self.gridLayout_32.addWidget(self.frame_26, 0, 0, 1, 1)

        self.frame_27 = QFrame(self.page_9)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_27)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.toolBox_6 = QToolBox(self.frame_27)
        self.toolBox_6.setObjectName(u"toolBox_6")
        self.toolBox_6.setStyleSheet(u"QToolBox::tab {\n"
"	background-color: rgb(66, 148, 208);\n"
"    \n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolBox::tab:selected { /* italicize selected tabs */\n"
"    color: white;\n"
"	font:bold;\n"
"}")
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.page_18.setGeometry(QRect(0, 0, 83, 68))
        self.gridLayout_36 = QGridLayout(self.page_18)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.frame_29 = QFrame(self.page_18)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	\n"
"	background-color: rgb(239, 239, 239);\n"
"	/*border:1px solid gray;*/\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-"
                        "right-radius: 3px;\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_29)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.comboBox_10 = QComboBox(self.frame_29)
        icon13 = QIcon()
        icon13.addFile(u":/loiser/loiser/icons8-sports-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon13, "")
        icon14 = QIcon()
        icon14.addFile(u":/loiser/loiser/gaming.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon14, "")
        icon15 = QIcon()
        icon15.addFile(u":/loiser/loiser/icons8-drawing-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon15, "")
        icon16 = QIcon()
        icon16.addFile(u":/loiser/loiser/icons8-lire-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon16, "")
        icon17 = QIcon()
        icon17.addFile(u":/loiser/loiser/icons8-musique-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon17, "")
        icon18 = QIcon()
        icon18.addFile(u":/loiser/loiser/icons8-natation-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon18, "")
        icon19 = QIcon()
        icon19.addFile(u":/loiser/loiser/icons8-cyclisme-de-montagne-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon19, "")
        icon20 = QIcon()
        icon20.addFile(u":/loiser/loiser/icons8-boxing-glove-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon20, "")
        icon21 = QIcon()
        icon21.addFile(u":/loiser/loiser/icons8-person-surfing-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon21, "")
        icon22 = QIcon()
        icon22.addFile(u":/loiser/loiser/icons8-football-2-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon22, "")
        icon23 = QIcon()
        icon23.addFile(u":/loiser/loiser/icons8-chess-pawn-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon23, "")
        icon24 = QIcon()
        icon24.addFile(u":/loiser/loiser/icons8-\u00e9quitation-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon24, "")
        icon25 = QIcon()
        icon25.addFile(u":/loiser/loiser/icons8-trekking-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon25, "")
        icon26 = QIcon()
        icon26.addFile(u":/loiser/loiser/icons8-skateboard-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_10.addItem(icon26, "")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMinimumSize(QSize(20, 30))
        self.comboBox_10.setCursor(QCursor(Qt.OpenHandCursor))

        self.gridLayout_35.addWidget(self.comboBox_10, 0, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(110, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_14, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(110, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_35.addItem(self.horizontalSpacer_15, 0, 2, 1, 1)


        self.gridLayout_36.addWidget(self.frame_29, 0, 0, 1, 1)

        self.toolBox_6.addItem(self.page_18, u"LOISER")

        self.gridLayout_31.addWidget(self.toolBox_6, 0, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.frame_27)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 25))
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	color: #408fc9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_15.setIcon(icon4)

        self.gridLayout_31.addWidget(self.pushButton_15, 1, 0, 1, 1)

        self.pushButton_16 = QPushButton(self.frame_27)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 25))
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	color: red;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	\n"
"}")
        self.pushButton_16.setIcon(icon3)

        self.gridLayout_31.addWidget(self.pushButton_16, 2, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.frame_27)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(0, 25))
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_31.addWidget(self.pushButton_17, 3, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_31.addItem(self.verticalSpacer_15, 4, 0, 1, 1)


        self.gridLayout_32.addWidget(self.frame_27, 0, 1, 1, 1)

        self.frame_25 = QFrame(self.page_9)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 80))
        self.frame_25.setMaximumSize(QSize(16777215, 80))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_25)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.horizontalSpacer_34 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_34, 0, 0, 1, 1)

        self.B_pre_6 = QPushButton(self.frame_25)
        self.B_pre_6.setObjectName(u"B_pre_6")
        self.B_pre_6.setMinimumSize(QSize(100, 30))
        self.B_pre_6.setMaximumSize(QSize(100, 30))
        self.B_pre_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_pre_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_29.addWidget(self.B_pre_6, 0, 1, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_35, 0, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(97, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_13, 0, 3, 1, 1)

        self.B_suiv_6 = QPushButton(self.frame_25)
        self.B_suiv_6.setObjectName(u"B_suiv_6")
        self.B_suiv_6.setMinimumSize(QSize(100, 30))
        self.B_suiv_6.setMaximumSize(QSize(100, 30))
        self.B_suiv_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.B_suiv_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_29.addWidget(self.B_suiv_6, 0, 4, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_36, 0, 5, 1, 1)


        self.gridLayout_32.addWidget(self.frame_25, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_9)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_27 = QGridLayout(self.page_7)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.frame_24 = QFrame(self.page_7)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(239, 239, 239);\n"
"	border:1px solid gray;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
" \n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    border-left-color: darkgray;\n"
"    border-left-"
                        "style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QTextEdit{\n"
"\n"
"	background-color: rgb(239, 239, 239);\n"
"	border-radius:4px;\n"
"}\n"
"QTextEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_24)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.label_34 = QLabel(self.frame_24)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_37.addWidget(self.label_34, 8, 3, 1, 1)

        self.label_33 = QLabel(self.frame_24)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_37.addWidget(self.label_33, 8, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_24)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 30))
        self.lineEdit_9.setAlignment(Qt.AlignCenter)
        self.lineEdit_9.setReadOnly(True)

        self.gridLayout_37.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.label_31 = QLabel(self.frame_24)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_37.addWidget(self.label_31, 6, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.frame_24)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton_19.setFont(font1)
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: white;\n"
"	border:1px solid red;\n"
"	border-radius:5px;\n"
"	\n"
"	color: red;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 41, 41);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color:white;\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u":/img/pdf_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon27)

        self.gridLayout_37.addWidget(self.pushButton_19, 11, 1, 1, 1)

        self.label_32 = QLabel(self.frame_24)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_37.addWidget(self.label_32, 6, 3, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_24)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 25))
        self.pushButton_20.setFont(font1)
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: none;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	\n"
"	color: #408fc9;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:#408fc9;\n"
"	border:1px solid #408fc9;\n"
"	border-radius:5px;\n"
"	color:white;\n"
"	\n"
"	\n"
"}")
        icon28 = QIcon()
        icon28.addFile(u":/img/word_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_20.setIcon(icon28)

        self.gridLayout_37.addWidget(self.pushButton_20, 11, 3, 1, 1)

        self.label_29 = QLabel(self.frame_24)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_37.addWidget(self.label_29, 4, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.frame_24)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(0, 30))
        self.lineEdit_14.setAlignment(Qt.AlignCenter)
        self.lineEdit_14.setReadOnly(True)

        self.gridLayout_37.addWidget(self.lineEdit_14, 2, 3, 1, 1)

        self.label_30 = QLabel(self.frame_24)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_37.addWidget(self.label_30, 4, 3, 1, 1)

        self.pushButton_18 = QPushButton(self.frame_24)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(130, 130))
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"	border:1px solid gray;\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:15px;\n"
"}")

        self.gridLayout_37.addWidget(self.pushButton_18, 0, 0, 3, 1)

        self.lineEdit_6 = QLineEdit(self.frame_24)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout_37.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_24)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 30))
        self.lineEdit_8.setAlignment(Qt.AlignCenter)
        self.lineEdit_8.setReadOnly(True)

        self.gridLayout_37.addWidget(self.lineEdit_8, 1, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.frame_24)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(0, 30))
        self.lineEdit_13.setAlignment(Qt.AlignCenter)
        self.lineEdit_13.setReadOnly(True)

        self.gridLayout_37.addWidget(self.lineEdit_13, 1, 3, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_24)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(0, 30))
        self.lineEdit_12.setAlignment(Qt.AlignCenter)
        self.lineEdit_12.setReadOnly(True)

        self.gridLayout_37.addWidget(self.lineEdit_12, 0, 3, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout_37.addItem(self.verticalSpacer_18, 3, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.frame_24)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_37.addWidget(self.textBrowser, 5, 1, 1, 1)

        self.textBrowser_2 = QTextBrowser(self.frame_24)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_37.addWidget(self.textBrowser_2, 5, 3, 1, 1)

        self.textBrowser_3 = QTextBrowser(self.frame_24)
        self.textBrowser_3.setObjectName(u"textBrowser_3")

        self.gridLayout_37.addWidget(self.textBrowser_3, 7, 1, 1, 1)

        self.textBrowser_4 = QTextBrowser(self.frame_24)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.gridLayout_37.addWidget(self.textBrowser_4, 7, 3, 1, 1)

        self.textBrowser_5 = QTextBrowser(self.frame_24)
        self.textBrowser_5.setObjectName(u"textBrowser_5")

        self.gridLayout_37.addWidget(self.textBrowser_5, 9, 1, 1, 1)

        self.textBrowser_6 = QTextBrowser(self.frame_24)
        self.textBrowser_6.setObjectName(u"textBrowser_6")

        self.gridLayout_37.addWidget(self.textBrowser_6, 9, 3, 1, 1)


        self.gridLayout_27.addWidget(self.frame_24, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_7)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout_4 = QVBoxLayout(self.Home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.Logo = QPushButton(self.Home)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon29 = QIcon()
        icon29.addFile(u":/img cv/logo cv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Logo.setIcon(icon29)
        self.Logo.setIconSize(QSize(300, 300))

        self.verticalLayout_4.addWidget(self.Logo)

        self.lineEdit = QLineEdit(self.Home)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(500, 50))
        self.lineEdit.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"	\n"
"	color: rgb(66, 148, 208);\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lineEdit, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Btn_cr = QPushButton(self.Home)
        self.Btn_cr.setObjectName(u"Btn_cr")
        self.Btn_cr.setMinimumSize(QSize(100, 40))
        self.Btn_cr.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.Btn_cr.setFont(font3)
        self.Btn_cr.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_cr.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: white;\n"
"	border:1px solid rgb(66, 148, 208);\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(66, 148, 208);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_cr, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.Home)
        self.Page_CV = QWidget()
        self.Page_CV.setObjectName(u"Page_CV")
        self.verticalLayout_3 = QVBoxLayout(self.Page_CV)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.Page_CV)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)

        self.precedent = QPushButton(self.frame_9)
        self.precedent.setObjectName(u"precedent")
        self.precedent.setCursor(QCursor(Qt.PointingHandCursor))
        self.precedent.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon30 = QIcon()
        icon30.addFile(u":/img/2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.precedent.setIcon(icon30)
        self.precedent.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.precedent)

        self.stackedWidget_2 = QStackedWidget(self.frame_9)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(380, 0))
        self.stackedWidget_2.setMaximumSize(QSize(380, 16777215))
        self.cv1 = QWidget()
        self.cv1.setObjectName(u"cv1")
        self.gridLayout_2 = QGridLayout(self.cv1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CV1 = QPushButton(self.cv1)
        self.CV1.setObjectName(u"CV1")
        self.CV1.setCursor(QCursor(Qt.PointingHandCursor))
        self.CV1.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon31 = QIcon()
        icon31.addFile(u":/img cv/PAGE1-min-21-724x1024.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.CV1.setIcon(icon31)
        self.CV1.setIconSize(QSize(500, 430))
        self.CV1.setCheckable(False)
        self.CV1.setAutoDefault(False)
        self.CV1.setFlat(False)

        self.gridLayout_2.addWidget(self.CV1, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.cv1)
        self.cv2 = QWidget()
        self.cv2.setObjectName(u"cv2")
        self.gridLayout_3 = QGridLayout(self.cv2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.CV2 = QPushButton(self.cv2)
        self.CV2.setObjectName(u"CV2")
        self.CV2.setCursor(QCursor(Qt.PointingHandCursor))
        self.CV2.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon32 = QIcon()
        icon32.addFile(u":/img cv/215-modele-cv-professionnel.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.CV2.setIcon(icon32)
        self.CV2.setIconSize(QSize(430, 430))

        self.gridLayout_3.addWidget(self.CV2, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.cv2)
        self.cv3 = QWidget()
        self.cv3.setObjectName(u"cv3")
        self.gridLayout_4 = QGridLayout(self.cv3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.CV3 = QPushButton(self.cv3)
        self.CV3.setObjectName(u"CV3")
        self.CV3.setCursor(QCursor(Qt.PointingHandCursor))
        self.CV3.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon33 = QIcon()
        icon33.addFile(u":/img cv/PAGE1-min-22-724x1024.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.CV3.setIcon(icon33)
        self.CV3.setIconSize(QSize(430, 430))

        self.gridLayout_4.addWidget(self.CV3, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.cv3)
        self.cv4 = QWidget()
        self.cv4.setObjectName(u"cv4")
        self.gridLayout_5 = QGridLayout(self.cv4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.CV4 = QPushButton(self.cv4)
        self.CV4.setObjectName(u"CV4")
        self.CV4.setCursor(QCursor(Qt.PointingHandCursor))
        self.CV4.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon34 = QIcon()
        icon34.addFile(u":/img cv/PAGE1-min-23-724x1024.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.CV4.setIcon(icon34)
        self.CV4.setIconSize(QSize(430, 430))

        self.gridLayout_5.addWidget(self.CV4, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.cv4)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_8 = QGridLayout(self.page_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.CV5 = QPushButton(self.page_2)
        self.CV5.setObjectName(u"CV5")
        self.CV5.setCursor(QCursor(Qt.PointingHandCursor))
        self.CV5.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon35 = QIcon()
        icon35.addFile(u":/img cv/CV5.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.CV5.setIcon(icon35)
        self.CV5.setIconSize(QSize(430, 430))

        self.gridLayout_8.addWidget(self.CV5, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_9 = QGridLayout(self.page_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.CV6 = QPushButton(self.page_3)
        self.CV6.setObjectName(u"CV6")
        self.CV6.setCursor(QCursor(Qt.PointingHandCursor))
        self.CV6.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon36 = QIcon()
        icon36.addFile(u":/img cv/CV6.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.CV6.setIcon(icon36)
        self.CV6.setIconSize(QSize(430, 430))

        self.gridLayout_9.addWidget(self.CV6, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_3)

        self.horizontalLayout_6.addWidget(self.stackedWidget_2)

        self.suivant = QPushButton(self.frame_9)
        self.suivant.setObjectName(u"suivant")
        self.suivant.setEnabled(True)
        self.suivant.setCursor(QCursor(Qt.PointingHandCursor))
        self.suivant.setStyleSheet(u"QPushButton{\n"
"	background-color: none;\n"
"	border:0px solid;\n"
"}")
        icon37 = QIcon()
        icon37.addFile(u":/img/3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.suivant.setIcon(icon37)
        self.suivant.setIconSize(QSize(50, 50))
        self.suivant.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.suivant)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_21)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.Page_CV)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setMinimumSize(QSize(0, 50))
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.Page_CV)
        self.info_2 = QWidget()
        self.info_2.setObjectName(u"info_2")
        self.gridLayout_25 = QGridLayout(self.info_2)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.frame_23 = QFrame(self.info_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	\n"
"	background-color: rgb(239, 239, 239);\n"
"	/*border:1px solid gray;*/\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:1px solid #00aaff;\n"
"	border-radius:4px;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #00ff7f;\n"
"	background-color: rgb(239, 239, 239);\n"
"    border-radius: 2px;\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
" 	\n"
"}\n"
"QComboBox:hover\n"
"{\n"
"	background-color: rgb(66, 148, 208);\n"
"    color:white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    background-color: rgb(66, 148, 208);\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    background-color: white;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"    selection-background-color:rgb(66, 148, 208);\n"
"    color: black;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 0px;\n"
"    "
                        "border-left-color: darkgray;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_23)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(9, -1, -1, -1)
        self.lineEdit_11 = QLineEdit(self.frame_23)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 30))
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.lineEdit_11, 12, 0, 1, 1)

        self.label_25 = QLabel(self.frame_23)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_26.addWidget(self.label_25, 7, 0, 1, 2)

        self.com_2 = QLineEdit(self.frame_23)
        self.com_2.setObjectName(u"com_2")
        self.com_2.setMinimumSize(QSize(0, 30))
        self.com_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.com_2, 8, 0, 1, 2)

        self.label_26 = QLabel(self.frame_23)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_26.addWidget(self.label_26, 9, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_23)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 30))
        self.lineEdit_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.lineEdit_10, 10, 0, 1, 2)

        self.label_27 = QLabel(self.frame_23)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_26.addWidget(self.label_27, 11, 0, 1, 2)

        self.label_23 = QLabel(self.frame_23)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_26.addWidget(self.label_23, 3, 0, 1, 1)

        self.label_24 = QLabel(self.frame_23)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_26.addWidget(self.label_24, 5, 0, 1, 1)

        self.com_1 = QLineEdit(self.frame_23)
        self.com_1.setObjectName(u"com_1")
        self.com_1.setMinimumSize(QSize(0, 30))
        self.com_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.com_1, 6, 0, 1, 2)

        self.Nb_Form = QLineEdit(self.frame_23)
        self.Nb_Form.setObjectName(u"Nb_Form")
        self.Nb_Form.setMinimumSize(QSize(0, 30))
        self.Nb_Form.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.Nb_Form, 1, 0, 1, 2)

        self.label_22 = QLabel(self.frame_23)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_26.addWidget(self.label_22, 0, 0, 1, 2)

        self.lineEdit_7 = QLineEdit(self.frame_23)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 30))
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_26.addWidget(self.lineEdit_7, 4, 0, 1, 2)

        self.verticalSpacer_17 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_26.addItem(self.verticalSpacer_17, 13, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.frame_23)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 30))
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(66, 148, 208);\n"
"	border:0px solid;\n"
"	border-radius:5px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.gridLayout_26.addWidget(self.pushButton_11, 14, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frame_23, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_10, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.info_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)
        self.toolBox.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        self.toolBox_3.setCurrentIndex(0)
        self.toolBox_4.setCurrentIndex(0)
        self.toolBox_5.setCurrentIndex(0)
        self.toolBox_6.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.CV1.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.HOME.setText("")
        self.Bn_Min.setText("")
        self.Bn_Close.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"01", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"02", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"03", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"04", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"05", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"06", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"07", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"08", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"09", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1990", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"1991", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"1992", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"1993", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"1994", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"1995", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"1996", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"1997", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"1998", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"1999", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"2000", None))
        self.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"2001", None))
        self.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"2002", None))
        self.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"2003", None))
        self.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"2004", None))
        self.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"2005", None))
        self.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"2006", None))
        self.comboBox_2.setItemText(17, QCoreApplication.translate("MainWindow", u"2007", None))
        self.comboBox_2.setItemText(18, QCoreApplication.translate("MainWindow", u"2009", None))
        self.comboBox_2.setItemText(19, QCoreApplication.translate("MainWindow", u"2010", None))
        self.comboBox_2.setItemText(20, QCoreApplication.translate("MainWindow", u"2011", None))
        self.comboBox_2.setItemText(21, QCoreApplication.translate("MainWindow", u"2012", None))
        self.comboBox_2.setItemText(22, QCoreApplication.translate("MainWindow", u"2013", None))
        self.comboBox_2.setItemText(23, QCoreApplication.translate("MainWindow", u"2014", None))
        self.comboBox_2.setItemText(24, QCoreApplication.translate("MainWindow", u"2015", None))
        self.comboBox_2.setItemText(25, QCoreApplication.translate("MainWindow", u"2016", None))
        self.comboBox_2.setItemText(26, QCoreApplication.translate("MainWindow", u"2017", None))
        self.comboBox_2.setItemText(27, QCoreApplication.translate("MainWindow", u"2018", None))
        self.comboBox_2.setItemText(28, QCoreApplication.translate("MainWindow", u"2019", None))
        self.comboBox_2.setItemText(29, QCoreApplication.translate("MainWindow", u"2020", None))
        self.comboBox_2.setItemText(30, QCoreApplication.translate("MainWindow", u"2021", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Date de Naissance", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"01", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"02", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"03", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"04", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"05", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"06", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"07", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"08", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"09", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.comboBox_3.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.comboBox_3.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.comboBox_3.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.comboBox_3.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.comboBox_3.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.comboBox_3.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_3.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_3.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.comboBox_3.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.comboBox_3.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.comboBox_3.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.comboBox_3.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.comboBox_3.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.comboBox_3.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.comboBox_3.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.comboBox_3.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.comboBox_3.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox_3.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))

        self.img.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u026a\u0274\u0493\u1d0f\u0280\u1d0d\u1d00\u1d1b\u026a\u1d0f\u0274s \u1d18\u1d07\u0280s\u1d0f\u0274\u0274\u1d07\u029f\u029f\u1d07s", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Num.T\u00e9l\u00e9phone", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Poste", None))
        self.B_pre.setText(QCoreApplication.translate("MainWindow", u"Precedent", None))
        self.B_suiv.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.Terminer.setText(QCoreApplication.translate("MainWindow", u"Terminer", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ville", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Etablissement", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Date de d\u00e9but", None))
        self.Date_D.setItemText(0, QCoreApplication.translate("MainWindow", u"2030", None))
        self.Date_D.setItemText(1, QCoreApplication.translate("MainWindow", u"2029", None))
        self.Date_D.setItemText(2, QCoreApplication.translate("MainWindow", u"2028", None))
        self.Date_D.setItemText(3, QCoreApplication.translate("MainWindow", u"2027", None))
        self.Date_D.setItemText(4, QCoreApplication.translate("MainWindow", u"2026", None))
        self.Date_D.setItemText(5, QCoreApplication.translate("MainWindow", u"2025", None))
        self.Date_D.setItemText(6, QCoreApplication.translate("MainWindow", u"2024", None))
        self.Date_D.setItemText(7, QCoreApplication.translate("MainWindow", u"2023", None))
        self.Date_D.setItemText(8, QCoreApplication.translate("MainWindow", u"2022", None))
        self.Date_D.setItemText(9, QCoreApplication.translate("MainWindow", u"2021", None))
        self.Date_D.setItemText(10, QCoreApplication.translate("MainWindow", u"2020", None))
        self.Date_D.setItemText(11, QCoreApplication.translate("MainWindow", u"2019", None))
        self.Date_D.setItemText(12, QCoreApplication.translate("MainWindow", u"2018", None))
        self.Date_D.setItemText(13, QCoreApplication.translate("MainWindow", u"2017", None))
        self.Date_D.setItemText(14, QCoreApplication.translate("MainWindow", u"2016", None))
        self.Date_D.setItemText(15, QCoreApplication.translate("MainWindow", u"2015", None))
        self.Date_D.setItemText(16, QCoreApplication.translate("MainWindow", u"2014", None))
        self.Date_D.setItemText(17, QCoreApplication.translate("MainWindow", u"2013", None))
        self.Date_D.setItemText(18, QCoreApplication.translate("MainWindow", u"2012", None))
        self.Date_D.setItemText(19, QCoreApplication.translate("MainWindow", u"2011", None))
        self.Date_D.setItemText(20, QCoreApplication.translate("MainWindow", u"2010", None))
        self.Date_D.setItemText(21, QCoreApplication.translate("MainWindow", u"2009", None))
        self.Date_D.setItemText(22, QCoreApplication.translate("MainWindow", u"2008", None))
        self.Date_D.setItemText(23, QCoreApplication.translate("MainWindow", u"2007", None))
        self.Date_D.setItemText(24, QCoreApplication.translate("MainWindow", u"2006", None))
        self.Date_D.setItemText(25, QCoreApplication.translate("MainWindow", u"2005", None))
        self.Date_D.setItemText(26, QCoreApplication.translate("MainWindow", u"2004", None))
        self.Date_D.setItemText(27, QCoreApplication.translate("MainWindow", u"2003", None))
        self.Date_D.setItemText(28, QCoreApplication.translate("MainWindow", u"2002", None))
        self.Date_D.setItemText(29, QCoreApplication.translate("MainWindow", u"2000", None))
        self.Date_D.setItemText(30, QCoreApplication.translate("MainWindow", u"1999", None))
        self.Date_D.setItemText(31, QCoreApplication.translate("MainWindow", u"1998", None))
        self.Date_D.setItemText(32, QCoreApplication.translate("MainWindow", u"1997", None))
        self.Date_D.setItemText(33, QCoreApplication.translate("MainWindow", u"1996", None))
        self.Date_D.setItemText(34, QCoreApplication.translate("MainWindow", u"1995", None))
        self.Date_D.setItemText(35, QCoreApplication.translate("MainWindow", u"1994", None))
        self.Date_D.setItemText(36, QCoreApplication.translate("MainWindow", u"1993", None))
        self.Date_D.setItemText(37, QCoreApplication.translate("MainWindow", u"1992", None))
        self.Date_D.setItemText(38, QCoreApplication.translate("MainWindow", u"1991", None))
        self.Date_D.setItemText(39, QCoreApplication.translate("MainWindow", u"1990", None))
        self.Date_D.setItemText(40, "")

        self.Date_F.setItemText(0, QCoreApplication.translate("MainWindow", u"2030", None))
        self.Date_F.setItemText(1, QCoreApplication.translate("MainWindow", u"2029", None))
        self.Date_F.setItemText(2, QCoreApplication.translate("MainWindow", u"2028", None))
        self.Date_F.setItemText(3, QCoreApplication.translate("MainWindow", u"2027", None))
        self.Date_F.setItemText(4, QCoreApplication.translate("MainWindow", u"2026", None))
        self.Date_F.setItemText(5, QCoreApplication.translate("MainWindow", u"2025", None))
        self.Date_F.setItemText(6, QCoreApplication.translate("MainWindow", u"2024", None))
        self.Date_F.setItemText(7, QCoreApplication.translate("MainWindow", u"2023", None))
        self.Date_F.setItemText(8, QCoreApplication.translate("MainWindow", u"2022", None))
        self.Date_F.setItemText(9, QCoreApplication.translate("MainWindow", u"2021", None))
        self.Date_F.setItemText(10, QCoreApplication.translate("MainWindow", u"2020", None))
        self.Date_F.setItemText(11, QCoreApplication.translate("MainWindow", u"2019", None))
        self.Date_F.setItemText(12, QCoreApplication.translate("MainWindow", u"2018", None))
        self.Date_F.setItemText(13, QCoreApplication.translate("MainWindow", u"2017", None))
        self.Date_F.setItemText(14, QCoreApplication.translate("MainWindow", u"2016", None))
        self.Date_F.setItemText(15, QCoreApplication.translate("MainWindow", u"2015", None))
        self.Date_F.setItemText(16, QCoreApplication.translate("MainWindow", u"2014", None))
        self.Date_F.setItemText(17, QCoreApplication.translate("MainWindow", u"2013", None))
        self.Date_F.setItemText(18, QCoreApplication.translate("MainWindow", u"2012", None))
        self.Date_F.setItemText(19, QCoreApplication.translate("MainWindow", u"2011", None))
        self.Date_F.setItemText(20, QCoreApplication.translate("MainWindow", u"2010", None))
        self.Date_F.setItemText(21, QCoreApplication.translate("MainWindow", u"2009", None))
        self.Date_F.setItemText(22, QCoreApplication.translate("MainWindow", u"2008", None))
        self.Date_F.setItemText(23, QCoreApplication.translate("MainWindow", u"2007", None))
        self.Date_F.setItemText(24, QCoreApplication.translate("MainWindow", u"2006", None))
        self.Date_F.setItemText(25, QCoreApplication.translate("MainWindow", u"2005", None))
        self.Date_F.setItemText(26, QCoreApplication.translate("MainWindow", u"2004", None))
        self.Date_F.setItemText(27, QCoreApplication.translate("MainWindow", u"2003", None))
        self.Date_F.setItemText(28, QCoreApplication.translate("MainWindow", u"2002", None))
        self.Date_F.setItemText(29, QCoreApplication.translate("MainWindow", u"2000", None))
        self.Date_F.setItemText(30, QCoreApplication.translate("MainWindow", u"1999", None))
        self.Date_F.setItemText(31, QCoreApplication.translate("MainWindow", u"1998", None))
        self.Date_F.setItemText(32, QCoreApplication.translate("MainWindow", u"1997", None))
        self.Date_F.setItemText(33, QCoreApplication.translate("MainWindow", u"1996", None))
        self.Date_F.setItemText(34, QCoreApplication.translate("MainWindow", u"1995", None))
        self.Date_F.setItemText(35, QCoreApplication.translate("MainWindow", u"1994", None))
        self.Date_F.setItemText(36, QCoreApplication.translate("MainWindow", u"1993", None))
        self.Date_F.setItemText(37, QCoreApplication.translate("MainWindow", u"1992", None))
        self.Date_F.setItemText(38, QCoreApplication.translate("MainWindow", u"1991", None))
        self.Date_F.setItemText(39, QCoreApplication.translate("MainWindow", u"1990", None))
        self.Date_F.setItemText(40, "")

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Date de fin", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Formation", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Formation", None))
        self.B_pre_2.setText(QCoreApplication.translate("MainWindow", u"Precedent", None))
        self.B_suiv_2.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.Terminer_1.setText(QCoreApplication.translate("MainWindow", u"Terminer", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"1990", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"1991", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"1992", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainWindow", u"1993", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("MainWindow", u"1994", None))
        self.comboBox_7.setItemText(5, QCoreApplication.translate("MainWindow", u"1995", None))
        self.comboBox_7.setItemText(6, QCoreApplication.translate("MainWindow", u"1996", None))
        self.comboBox_7.setItemText(7, QCoreApplication.translate("MainWindow", u"1997", None))
        self.comboBox_7.setItemText(8, QCoreApplication.translate("MainWindow", u"1998", None))
        self.comboBox_7.setItemText(9, QCoreApplication.translate("MainWindow", u"1999", None))
        self.comboBox_7.setItemText(10, QCoreApplication.translate("MainWindow", u"2000", None))
        self.comboBox_7.setItemText(11, QCoreApplication.translate("MainWindow", u"2001", None))
        self.comboBox_7.setItemText(12, QCoreApplication.translate("MainWindow", u"2002", None))
        self.comboBox_7.setItemText(13, QCoreApplication.translate("MainWindow", u"2003", None))
        self.comboBox_7.setItemText(14, QCoreApplication.translate("MainWindow", u"2004", None))
        self.comboBox_7.setItemText(15, QCoreApplication.translate("MainWindow", u"2005", None))
        self.comboBox_7.setItemText(16, QCoreApplication.translate("MainWindow", u"2006", None))
        self.comboBox_7.setItemText(17, QCoreApplication.translate("MainWindow", u"2007", None))
        self.comboBox_7.setItemText(18, QCoreApplication.translate("MainWindow", u"2008", None))
        self.comboBox_7.setItemText(19, QCoreApplication.translate("MainWindow", u"2009", None))
        self.comboBox_7.setItemText(20, QCoreApplication.translate("MainWindow", u"2010", None))
        self.comboBox_7.setItemText(21, QCoreApplication.translate("MainWindow", u"2011", None))
        self.comboBox_7.setItemText(22, QCoreApplication.translate("MainWindow", u"2012", None))
        self.comboBox_7.setItemText(23, QCoreApplication.translate("MainWindow", u"2013", None))
        self.comboBox_7.setItemText(24, QCoreApplication.translate("MainWindow", u"2014", None))
        self.comboBox_7.setItemText(25, QCoreApplication.translate("MainWindow", u"2015", None))
        self.comboBox_7.setItemText(26, QCoreApplication.translate("MainWindow", u"2016", None))
        self.comboBox_7.setItemText(27, QCoreApplication.translate("MainWindow", u"2017", None))
        self.comboBox_7.setItemText(28, QCoreApplication.translate("MainWindow", u"2018", None))
        self.comboBox_7.setItemText(29, QCoreApplication.translate("MainWindow", u"2019", None))
        self.comboBox_7.setItemText(30, QCoreApplication.translate("MainWindow", u"2020", None))
        self.comboBox_7.setItemText(31, QCoreApplication.translate("MainWindow", u"2021", None))
        self.comboBox_7.setItemText(32, QCoreApplication.translate("MainWindow", u"2022", None))
        self.comboBox_7.setItemText(33, QCoreApplication.translate("MainWindow", u"2023", None))
        self.comboBox_7.setItemText(34, QCoreApplication.translate("MainWindow", u"2024", None))
        self.comboBox_7.setItemText(35, QCoreApplication.translate("MainWindow", u"2025", None))
        self.comboBox_7.setItemText(36, QCoreApplication.translate("MainWindow", u"2026", None))
        self.comboBox_7.setItemText(37, QCoreApplication.translate("MainWindow", u"2027", None))
        self.comboBox_7.setItemText(38, QCoreApplication.translate("MainWindow", u"2028", None))
        self.comboBox_7.setItemText(39, QCoreApplication.translate("MainWindow", u"2029", None))
        self.comboBox_7.setItemText(40, QCoreApplication.translate("MainWindow", u"2030", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"POSTE", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"1990", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"1991", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"1992", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"1993", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"1994", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"1995", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"1996", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"1997", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("MainWindow", u"1998", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("MainWindow", u"1999", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("MainWindow", u"2000", None))
        self.comboBox_5.setItemText(11, QCoreApplication.translate("MainWindow", u"2001", None))
        self.comboBox_5.setItemText(12, QCoreApplication.translate("MainWindow", u"2002", None))
        self.comboBox_5.setItemText(13, QCoreApplication.translate("MainWindow", u"2003", None))
        self.comboBox_5.setItemText(14, QCoreApplication.translate("MainWindow", u"2004", None))
        self.comboBox_5.setItemText(15, QCoreApplication.translate("MainWindow", u"2005", None))
        self.comboBox_5.setItemText(16, QCoreApplication.translate("MainWindow", u"2006", None))
        self.comboBox_5.setItemText(17, QCoreApplication.translate("MainWindow", u"2007", None))
        self.comboBox_5.setItemText(18, QCoreApplication.translate("MainWindow", u"2008", None))
        self.comboBox_5.setItemText(19, QCoreApplication.translate("MainWindow", u"2009", None))
        self.comboBox_5.setItemText(20, QCoreApplication.translate("MainWindow", u"2010", None))
        self.comboBox_5.setItemText(21, QCoreApplication.translate("MainWindow", u"2011", None))
        self.comboBox_5.setItemText(22, QCoreApplication.translate("MainWindow", u"2012", None))
        self.comboBox_5.setItemText(23, QCoreApplication.translate("MainWindow", u"2013", None))
        self.comboBox_5.setItemText(24, QCoreApplication.translate("MainWindow", u"2014", None))
        self.comboBox_5.setItemText(25, QCoreApplication.translate("MainWindow", u"2015", None))
        self.comboBox_5.setItemText(26, QCoreApplication.translate("MainWindow", u"2016", None))
        self.comboBox_5.setItemText(27, QCoreApplication.translate("MainWindow", u"2017", None))
        self.comboBox_5.setItemText(28, QCoreApplication.translate("MainWindow", u"2018", None))
        self.comboBox_5.setItemText(29, QCoreApplication.translate("MainWindow", u"2019", None))
        self.comboBox_5.setItemText(30, QCoreApplication.translate("MainWindow", u"2020", None))
        self.comboBox_5.setItemText(31, QCoreApplication.translate("MainWindow", u"2021", None))
        self.comboBox_5.setItemText(32, QCoreApplication.translate("MainWindow", u"2022", None))
        self.comboBox_5.setItemText(33, QCoreApplication.translate("MainWindow", u"2023", None))
        self.comboBox_5.setItemText(34, QCoreApplication.translate("MainWindow", u"2024", None))
        self.comboBox_5.setItemText(35, QCoreApplication.translate("MainWindow", u"2025", None))
        self.comboBox_5.setItemText(36, QCoreApplication.translate("MainWindow", u"2026", None))
        self.comboBox_5.setItemText(37, QCoreApplication.translate("MainWindow", u"2027", None))
        self.comboBox_5.setItemText(38, QCoreApplication.translate("MainWindow", u"2028", None))
        self.comboBox_5.setItemText(39, QCoreApplication.translate("MainWindow", u"2029", None))
        self.comboBox_5.setItemText(40, QCoreApplication.translate("MainWindow", u"2030", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Date de d\u00e9but", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"Janv", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"F\u00e9vr", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"Mars", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"Avri", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"Mai", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"Juin", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("MainWindow", u"Juil", None))
        self.comboBox_6.setItemText(7, QCoreApplication.translate("MainWindow", u"Auot", None))
        self.comboBox_6.setItemText(8, QCoreApplication.translate("MainWindow", u"Sept", None))
        self.comboBox_6.setItemText(9, QCoreApplication.translate("MainWindow", u"Oct", None))
        self.comboBox_6.setItemText(10, QCoreApplication.translate("MainWindow", u"Nev", None))
        self.comboBox_6.setItemText(11, QCoreApplication.translate("MainWindow", u"D\u00e9c", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"NOM DE L\u2019ENTREPRISE  ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"T\u00e2ches r\u00e9alis\u00e9es ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"VILLE", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Janv", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"F\u00e9vr", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Mars", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Avri", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"Mai", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"Juin", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"Juil", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"Auot", None))
        self.comboBox_4.setItemText(8, QCoreApplication.translate("MainWindow", u"Sept", None))
        self.comboBox_4.setItemText(9, QCoreApplication.translate("MainWindow", u"Oct", None))
        self.comboBox_4.setItemText(10, QCoreApplication.translate("MainWindow", u"Nov", None))
        self.comboBox_4.setItemText(11, QCoreApplication.translate("MainWindow", u"D\u00e9c", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Date de fin", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Experience", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.B_suiv_3.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.B_pre_3.setText(QCoreApplication.translate("MainWindow", u"Precedent", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Comp\u00e9tence", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Comp\u00e9tence", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Terminer", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Comp\u00e9tence Personnel", None))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.page_8), QCoreApplication.translate("MainWindow", u"Comp\u00e9tence Personnel", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Terminer", None))
        self.B_pre_4.setText(QCoreApplication.translate("MainWindow", u"Precedent", None))
        self.B_suiv_4.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Terminer", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"Arabic", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"Francais", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("MainWindow", u"Russien", None))
        self.comboBox_8.setItemText(4, QCoreApplication.translate("MainWindow", u"Chine", None))
        self.comboBox_8.setItemText(5, QCoreApplication.translate("MainWindow", u"Germany", None))
        self.comboBox_8.setItemText(6, QCoreApplication.translate("MainWindow", u"Japan", None))
        self.comboBox_8.setItemText(7, QCoreApplication.translate("MainWindow", u"Espane", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Langue maternelle", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"Courant", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"Notions", None))
        self.comboBox_9.setItemText(3, QCoreApplication.translate("MainWindow", u"Scolaire", None))

        self.toolBox_5.setItemText(self.toolBox_5.indexOf(self.page_16), QCoreApplication.translate("MainWindow", u"LANGUES", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"Sport", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"Gaming", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"Dessin", None))
        self.comboBox_10.setItemText(3, QCoreApplication.translate("MainWindow", u"Lecture", None))
        self.comboBox_10.setItemText(4, QCoreApplication.translate("MainWindow", u"Musique", None))
        self.comboBox_10.setItemText(5, QCoreApplication.translate("MainWindow", u"Natation", None))
        self.comboBox_10.setItemText(6, QCoreApplication.translate("MainWindow", u"Cyclisme de montagne", None))
        self.comboBox_10.setItemText(7, QCoreApplication.translate("MainWindow", u"Boxe", None))
        self.comboBox_10.setItemText(8, QCoreApplication.translate("MainWindow", u"Surf", None))
        self.comboBox_10.setItemText(9, QCoreApplication.translate("MainWindow", u"Football", None))
        self.comboBox_10.setItemText(10, QCoreApplication.translate("MainWindow", u"Chess", None))
        self.comboBox_10.setItemText(11, QCoreApplication.translate("MainWindow", u"\u00e9quitation", None))
        self.comboBox_10.setItemText(12, QCoreApplication.translate("MainWindow", u"Trekking", None))
        self.comboBox_10.setItemText(13, QCoreApplication.translate("MainWindow", u"Skateboard", None))

        self.toolBox_6.setItemText(self.toolBox_6.indexOf(self.page_18), QCoreApplication.translate("MainWindow", u"LOISER", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Terminer", None))
        self.B_pre_6.setText(QCoreApplication.translate("MainWindow", u"Precedent", None))
        self.B_suiv_6.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Loiser", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Langue", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Comp\u00e9tence", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Comp\u00e9tence Personnel", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"WORD", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Formation", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Experience", None))
        self.pushButton_18.setText("")
        self.Logo.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Creation CV Professionnel", None))
        self.Btn_cr.setText(QCoreApplication.translate("MainWindow", u"Cr\u00e9e Un CV", None))
        self.precedent.setText("")
        self.CV1.setText("")
        self.CV2.setText("")
        self.CV3.setText("")
        self.CV4.setText("")
        self.CV5.setText("")
        self.CV6.setText("")
        self.suivant.setText("")
        self.lineEdit_11.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Combien De Comp\u00e9tence Personnel", None))
        self.com_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Combien De Langue", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Combien De Loiser", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Combien De Experience", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Combien De Comp\u00e9tence", None))
        self.com_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Nb_Form.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Combien De Formation", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Suivant", None))
    # retranslateUi

