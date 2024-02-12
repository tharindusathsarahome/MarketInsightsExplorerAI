# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainQibrSW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1039, 569)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QFrame(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.Header.setMinimumSize(QSize(0, 60))
        self.Header.setMaximumSize(QSize(16777215, 90))
        self.Header.setStyleSheet(u"background-color: rgb(52, 14, 84);")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Menu = QFrame(self.Header)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setMinimumSize(QSize(100, 0))
        self.Menu.setMaximumSize(QSize(100, 16777215))
        self.Menu.setFrameShape(QFrame.StyledPanel)
        self.Menu.setFrameShadow(QFrame.Raised)
        self.btnMenu = QPushButton(self.Menu)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setGeometry(QRect(10, 10, 41, 31))
        self.btnMenu.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(170, 0, 255, 100);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.Menu)

        self.Title = QFrame(self.Header)
        self.Title.setObjectName(u"Title")
        self.Title.setStyleSheet(u"")
        self.Title.setFrameShape(QFrame.StyledPanel)
        self.Title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(242, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.frame_5 = QFrame(self.Title)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(210, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 0, 141, 31))
        font = QFont()
        font.setFamily(u"Segoe Script")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(85, 255, 0);\n"
"font: 20pt \"Segoe Script\";")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(-40, 30, 281, 31))
        font1 = QFont()
        font1.setFamily(u"Letter Gothic Std")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(0, 255, 255);\n"
"font: 12pt \"Letter Gothic Std\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.frame_5)

        self.horizontalSpacer_2 = QSpacerItem(400, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.frame_3 = QFrame(self.Title)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(80, 0))
        self.frame_3.setMaximumSize(QSize(80, 16777215))
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"	border-radius: 2px;\n"
"}\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(170, 85, 255, 150);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnMini = QPushButton(self.frame_3)
        self.btnMini.setObjectName(u"btnMini")
        self.btnMini.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMini.setIcon(icon1)
        self.btnMini.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnMini)

        self.btnMax = QPushButton(self.frame_3)
        self.btnMax.setObjectName(u"btnMax")
        self.btnMax.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMax.setIcon(icon2)
        self.btnMax.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnMax)

        self.btnCls = QPushButton(self.frame_3)
        self.btnCls.setObjectName(u"btnCls")
        self.btnCls.setMaximumSize(QSize(20, 20))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCls.setIcon(icon3)
        self.btnCls.setIconSize(QSize(12, 12))

        self.horizontalLayout_5.addWidget(self.btnCls)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.Title)


        self.verticalLayout.addWidget(self.Header)

        self.Main = QFrame(self.centralwidget)
        self.Main.setObjectName(u"Main")
        self.Main.setFrameShape(QFrame.NoFrame)
        self.Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Main)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftBar = QFrame(self.Main)
        self.leftBar.setObjectName(u"leftBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBar.sizePolicy().hasHeightForWidth())
        self.leftBar.setSizePolicy(sizePolicy)
        self.leftBar.setMinimumSize(QSize(0, 0))
        self.leftBar.setMaximumSize(QSize(100, 16777215))
        self.leftBar.setStyleSheet(u"background-color: rgb(52, 14, 84);")
        self.leftBar.setFrameShape(QFrame.StyledPanel)
        self.leftBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftBar)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.MainTabs = QFrame(self.leftBar)
        self.MainTabs.setObjectName(u"MainTabs")
        self.MainTabs.setMinimumSize(QSize(0, 150))
        self.MainTabs.setMaximumSize(QSize(16777215, 170))
        self.MainTabs.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
"	color: rgb(102, 252, 255);\n"
"	font: 13pt \"Mongolian Baiti\";\n"
"	text-align: left;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(170, 0, 255, 100);\n"
"}")
        self.MainTabs.setFrameShape(QFrame.StyledPanel)
        self.MainTabs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.MainTabs)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(4, 2, 0, 0)
        self.btnHome = QPushButton(self.MainTabs)
        self.btnHome.setObjectName(u"btnHome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy1)
        self.btnHome.setMinimumSize(QSize(85, 35))
        self.btnHome.setMaximumSize(QSize(50, 35))
        self.btnHome.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamily(u"Mongolian Baiti")
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.btnHome.setFont(font2)
        self.btnHome.setToolTipDuration(-1)
        self.btnHome.setLayoutDirection(Qt.LeftToRight)
        self.btnHome.setAutoFillBackground(False)
        self.btnHome.setStyleSheet(u"background-image: url(:/icons/icons/cil-home.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left;")
        self.btnHome.setText(u"Home")
        self.btnHome.setIconSize(QSize(22, 22))
        self.btnHome.setAutoDefault(False)

        self.verticalLayout_4.addWidget(self.btnHome)

        self.btnStore = QPushButton(self.MainTabs)
        self.btnStore.setObjectName(u"btnStore")
        self.btnStore.setMinimumSize(QSize(85, 35))
        self.btnStore.setMaximumSize(QSize(50, 35))
        font3 = QFont()
        font3.setFamily(u"Mongolian Baiti")
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.btnStore.setFont(font3)
        self.btnStore.setStyleSheet(u"background-image: url(:/icons/icons/cil-truck.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left;")
        self.btnStore.setIconSize(QSize(22, 22))

        self.verticalLayout_4.addWidget(self.btnStore)

        self.btnAnylise = QPushButton(self.MainTabs)
        self.btnAnylise.setObjectName(u"btnAnylise")
        sizePolicy1.setHeightForWidth(self.btnAnylise.sizePolicy().hasHeightForWidth())
        self.btnAnylise.setSizePolicy(sizePolicy1)
        self.btnAnylise.setMinimumSize(QSize(85, 35))
        self.btnAnylise.setMaximumSize(QSize(50, 35))
        self.btnAnylise.setFont(font3)
        self.btnAnylise.setStyleSheet(u"background-image: url(:/icons/icons/cil-chart-line.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left;")
        self.btnAnylise.setIconSize(QSize(22, 22))

        self.verticalLayout_4.addWidget(self.btnAnylise)

        self.btnSetting = QPushButton(self.MainTabs)
        self.btnSetting.setObjectName(u"btnSetting")
        self.btnSetting.setMinimumSize(QSize(90, 35))
        self.btnSetting.setMaximumSize(QSize(50, 35))
        self.btnSetting.setFont(font3)
        self.btnSetting.setStyleSheet(u"background-image: url(:/icons/icons/cil-settings.png);\n"
"background-repeat:none;\n"
"padding-left:30px;\n"
"background-position:center left;")
        self.btnSetting.setIconSize(QSize(22, 22))

        self.verticalLayout_4.addWidget(self.btnSetting)


        self.verticalLayout_3.addWidget(self.MainTabs)

        self.MiddleTab = QFrame(self.leftBar)
        self.MiddleTab.setObjectName(u"MiddleTab")
        self.MiddleTab.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(170, 0, 255, 100);\n"
"}")
        self.MiddleTab.setFrameShape(QFrame.StyledPanel)
        self.MiddleTab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.MiddleTab)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(4, 2, 0, 0)

        self.verticalLayout_3.addWidget(self.MiddleTab)


        self.horizontalLayout.addWidget(self.leftBar)

        self.frame_4 = QFrame(self.Main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.MainItem = QFrame(self.frame_4)
        self.MainItem.setObjectName(u"MainItem")
        self.MainItem.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.MainItem.setFrameShape(QFrame.NoFrame)
        self.MainItem.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.MainItem)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.MainItem)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setMinimumSize(QSize(0, 0))
        self.Home.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.Home)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setPointSize(10)
        self.frame_2.setFont(font4)
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(167, 23, 136);\n"
"}\n"
"\n"
"Line{\n"
"	background-color: rgba(190, 144, 255, 150);\n"
"}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(20, 0))
        self.label.setMaximumSize(QSize(106, 106))
        font5 = QFont()
        font5.setPointSize(11)
        self.label.setFont(font5)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-1)

        self.horizontalLayout_4.addWidget(self.label)

        self.line_5 = QFrame(self.frame_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(120, 0))
        self.label_6.setMaximumSize(QSize(16777215, 16777215))
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.line_4 = QFrame(self.frame_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_4)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(120, 0))
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.line_3 = QFrame(self.frame_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setFont(font5)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(37, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setSizeIncrement(QSize(0, 0))
        self.scrollArea.setBaseSize(QSize(0, 0))
        self.scrollArea.setStyleSheet(u"background-color: rgb(187, 187, 241);")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 941, 384))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)


        self.verticalLayout_7.addWidget(self.frame)

        self.stackedWidget.addWidget(self.Home)
        self.Anylise = QWidget()
        self.Anylise.setObjectName(u"Anylise")
        self.stackedWidget.addWidget(self.Anylise)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.verticalLayout_10 = QVBoxLayout(self.Settings)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_17 = QFrame(self.Settings)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.frame_17)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 919, 382))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 150))
        font6 = QFont()
        font6.setFamily(u"Mongolian Baiti")
        font6.setPointSize(13)
        self.groupBox_2.setFont(font6)
        self.groupBox_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 3px;\n"
"	background-color: rgb(170, 85, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(0, 255, 255);\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.AddNewDealer = QPushButton(self.groupBox_2)
        self.AddNewDealer.setObjectName(u"AddNewDealer")
        self.AddNewDealer.setMinimumSize(QSize(0, 45))
        font7 = QFont()
        font7.setFamily(u"Palatino Linotype")
        font7.setPointSize(14)
        self.AddNewDealer.setFont(font7)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddNewDealer.setIcon(icon4)
        self.AddNewDealer.setIconSize(QSize(25, 25))

        self.verticalLayout_14.addWidget(self.AddNewDealer)

        self.AddNewItem = QPushButton(self.groupBox_2)
        self.AddNewItem.setObjectName(u"AddNewItem")
        self.AddNewItem.setMinimumSize(QSize(0, 45))
        self.AddNewItem.setFont(font7)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/cil-library-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddNewItem.setIcon(icon5)
        self.AddNewItem.setIconSize(QSize(25, 25))

        self.verticalLayout_14.addWidget(self.AddNewItem)


        self.verticalLayout_17.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font6)
        self.verticalLayout_18 = QVBoxLayout(self.groupBox)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.AddNewDealer_2 = QPushButton(self.groupBox)
        self.AddNewDealer_2.setObjectName(u"AddNewDealer_2")
        self.AddNewDealer_2.setMinimumSize(QSize(0, 45))
        self.AddNewDealer_2.setFont(font7)
        self.AddNewDealer_2.setIcon(icon4)
        self.AddNewDealer_2.setIconSize(QSize(25, 25))

        self.verticalLayout_18.addWidget(self.AddNewDealer_2)


        self.verticalLayout_17.addWidget(self.groupBox)

        self.verticalSpacer_2 = QSpacerItem(20, 132, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_13.addWidget(self.scrollArea_4)


        self.verticalLayout_10.addWidget(self.frame_17)

        self.stackedWidget.addWidget(self.Settings)
        self.Store = QWidget()
        self.Store.setObjectName(u"Store")
        self.horizontalLayout_9 = QHBoxLayout(self.Store)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.Store)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(180, 0))
        self.frame_11.setMaximumSize(QSize(180, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(4, 4, 142, 111))
        self.frame_13.setMaximumSize(QSize(16777215, 111))
        self.frame_13.setStyleSheet(u"QPushButton {\n"
"	border-radius: 7px;\n"
"	\n"
"	background-color: rgb(170, 85, 255);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(170, 0, 255, 100);\n"
"}")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_13)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_21)

        self.btnBuyItems = QPushButton(self.frame_13)
        self.btnBuyItems.setObjectName(u"btnBuyItems")
        self.btnBuyItems.setMinimumSize(QSize(0, 25))
        self.btnBuyItems.setFont(font5)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/cil-exit-to-app.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnBuyItems.setIcon(icon6)

        self.verticalLayout_5.addWidget(self.btnBuyItems)

        self.btnStock = QPushButton(self.frame_13)
        self.btnStock.setObjectName(u"btnStock")
        self.btnStock.setMinimumSize(QSize(0, 25))
        self.btnStock.setFont(font5)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/cil-arrow-circle-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStock.setIcon(icon7)

        self.verticalLayout_5.addWidget(self.btnStock)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.searchItems = QFrame(self.frame_11)
        self.searchItems.setObjectName(u"searchItems")
        self.searchItems.setGeometry(QRect(4, 118, 172, 282))
        self.searchItems.setStyleSheet(u"QRadioButton {\n"
"	color: rgb(0, 0, 255);\n"
"	font: 75 11pt \"Comic Sans MS\";\n"
"}\n"
"QRadioButton:hover {\n"
"	color: rgb(170, 0, 255);\n"
"}\n"
"QRadioButton:checked {\n"
"	background-color: rgba(85, 255, 0, 150);\n"
"    border-radius:          5px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  20px;\n"
"    height:                 17px;\n"
"    border-radius:          2px;\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"	image: url(:/icons/icons/cil-arrow-right.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	background-color: rgb(62, 186, 0);\n"
"	image: url(:/icons/icons/cil-check.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.searchItems.setFrameShape(QFrame.NoFrame)
        self.searchItems.setFrameShadow(QFrame.Raised)
        self.SearchStore = QLineEdit(self.searchItems)
        self.SearchStore.setObjectName(u"SearchStore")
        self.SearchStore.setGeometry(QRect(20, 40, 141, 31))
        font8 = QFont()
        font8.setPointSize(12)
        self.SearchStore.setFont(font8)
        self.SearchStore.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 3px;\n"
"	background-color: rgb(170, 85, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(170, 0, 255);\n"
"}")
        self.label_20 = QLabel(self.searchItems)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 10, 111, 21))
        self.label_20.setFont(font6)
        self.orderByStock = QRadioButton(self.searchItems)
        self.orderByStock.setObjectName(u"orderByStock")
        self.orderByStock.setGeometry(QRect(10, 120, 151, 20))
        font9 = QFont()
        font9.setFamily(u"Comic Sans MS")
        font9.setPointSize(11)
        font9.setBold(False)
        font9.setItalic(False)
        font9.setWeight(9)
        self.orderByStock.setFont(font9)
        self.orderByStock.setCheckable(True)
        self.orderByDate = QRadioButton(self.searchItems)
        self.orderByDate.setObjectName(u"orderByDate")
        self.orderByDate.setGeometry(QRect(10, 150, 151, 20))
        self.orderByDate.setCheckable(True)
        self.orderByDiscount = QRadioButton(self.searchItems)
        self.orderByDiscount.setObjectName(u"orderByDiscount")
        self.orderByDiscount.setGeometry(QRect(10, 180, 151, 20))
        self.orderByDiscount.setCheckable(True)
        self.orderByPrice = QRadioButton(self.searchItems)
        self.orderByPrice.setObjectName(u"orderByPrice")
        self.orderByPrice.setGeometry(QRect(10, 210, 141, 20))
        self.orderByPrice.setCheckable(True)
        self.label_32 = QLabel(self.searchItems)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 90, 111, 21))
        self.label_32.setFont(font6)

        self.horizontalLayout_9.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.Store)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.stackedWidget_2 = QStackedWidget(self.frame_12)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setFrameShape(QFrame.StyledPanel)
        self.Normal = QWidget()
        self.Normal.setObjectName(u"Normal")
        self.verticalLayout_11 = QVBoxLayout(self.Normal)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_15 = QFrame(self.Normal)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 20))
        font10 = QFont()
        font10.setFamily(u"MS Shell Dlg 2")
        font10.setPointSize(11)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setWeight(50)
        self.frame_15.setFont(font10)
        self.frame_15.setStyleSheet(u"QFrame{\n"
"background-color: rgb(34, 27, 129);\n"
"color: rgb(255, 255, 127);\n"
"font: 10.5pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"Line{\n"
"	background-color: rgba(255, 255, 127, 150);\n"
"}")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMinimumSize(QSize(20, 0))
        self.label_15.setMaximumSize(QSize(106, 106))
        self.label_15.setFont(font10)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setIndent(-1)

        self.horizontalLayout_12.addWidget(self.label_15)

        self.line_6 = QFrame(self.frame_15)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_6)

        self.label_16 = QLabel(self.frame_15)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(120, 0))
        self.label_16.setMaximumSize(QSize(16777215, 16777215))
        self.label_16.setFont(font10)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_16)

        self.line_7 = QFrame(self.frame_15)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_7)

        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(120, 0))
        self.label_18.setFont(font10)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_18)

        self.line_9 = QFrame(self.frame_15)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_9)

        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(120, 0))
        self.label_17.setFont(font10)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_17)

        self.line_8 = QFrame(self.frame_15)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_8)

        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(50, 0))
        self.label_19.setFont(font10)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.line_10 = QFrame(self.frame_15)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_10)

        self.label_22 = QLabel(self.frame_15)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(50, 0))
        self.label_22.setFont(font10)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_22)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(25, 0))
        self.frame_16.setMaximumSize(QSize(25, 16777215))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_16)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.scrollArea_2 = QScrollArea(self.Normal)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 721, 341))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_11.addWidget(self.scrollArea_2)

        self.stackedWidget_2.addWidget(self.Normal)
        self.AddStock = QWidget()
        self.AddStock.setObjectName(u"AddStock")
        self.verticalLayout_15 = QVBoxLayout(self.AddStock)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_22 = QFrame(self.AddStock)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 20))
        self.frame_22.setFont(font10)
        self.frame_22.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(9, 85, 18);\n"
"	color: rgb(142, 253, 255);\n"
"font: 10.5pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"Line{\n"
"	background-color:rgba(142, 253, 255, 150);\n"
"}\n"
"")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_22)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        self.label_24.setMinimumSize(QSize(20, 0))
        self.label_24.setMaximumSize(QSize(106, 106))
        self.label_24.setFont(font10)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setIndent(-1)

        self.horizontalLayout_13.addWidget(self.label_24)

        self.line_11 = QFrame(self.frame_22)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_11)

        self.label_25 = QLabel(self.frame_22)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(120, 0))
        self.label_25.setMaximumSize(QSize(16777215, 16777215))
        self.label_25.setFont(font10)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_25)

        self.line_12 = QFrame(self.frame_22)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_12)

        self.label_26 = QLabel(self.frame_22)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(120, 0))
        self.label_26.setFont(font10)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_26)

        self.line_13 = QFrame(self.frame_22)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_13)

        self.label_27 = QLabel(self.frame_22)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(120, 0))
        self.label_27.setFont(font10)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_27)

        self.line_14 = QFrame(self.frame_22)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line_14)

        self.label_28 = QLabel(self.frame_22)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(50, 0))
        self.label_28.setFont(font10)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_28)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(25, 0))
        self.frame_23.setMaximumSize(QSize(25, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_13.addWidget(self.frame_23)


        self.verticalLayout_15.addWidget(self.frame_22)

        self.scrollArea_3 = QScrollArea(self.AddStock)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 719, 303))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_15.addWidget(self.scrollArea_3)

        self.frame_24 = QFrame(self.AddStock)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(0, 30))
        self.frame_24.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 3px;\n"
"	background-color: rgb(170, 85, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(0, 170, 255);\n"
"	border-radius: 3px;\n"
"}\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(0, 255, 255);\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.btnAddStoreOK = QPushButton(self.frame_24)
        self.btnAddStoreOK.setObjectName(u"btnAddStoreOK")
        self.btnAddStoreOK.setGeometry(QRect(656, 8, 55, 21))
        self.AddStoreInvNo = QLineEdit(self.frame_24)
        self.AddStoreInvNo.setObjectName(u"AddStoreInvNo")
        self.AddStoreInvNo.setGeometry(QRect(79, 8, 106, 20))
        self.AddStoreInvNo.setFont(font4)
        self.AddStoreDealerID = QLineEdit(self.frame_24)
        self.AddStoreDealerID.setObjectName(u"AddStoreDealerID")
        self.AddStoreDealerID.setGeometry(QRect(400, 8, 106, 20))
        self.AddStoreDealerID.setFont(font4)
        self.label_30 = QLabel(self.frame_24)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 10, 71, 21))
        font11 = QFont()
        font11.setFamily(u"Mongolian Baiti")
        font11.setPointSize(10)
        self.label_30.setFont(font11)
        self.label_31 = QLabel(self.frame_24)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(313, 10, 81, 20))
        self.label_31.setFont(font11)

        self.verticalLayout_15.addWidget(self.frame_24)

        self.stackedWidget_2.addWidget(self.AddStock)

        self.horizontalLayout_10.addWidget(self.stackedWidget_2)


        self.horizontalLayout_9.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.Store)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.MainItem)

        self.Footer = QFrame(self.frame_4)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 0))
        self.Footer.setMaximumSize(QSize(16777215, 120))
        self.Footer.setStyleSheet(u"background-color: rgb(52, 14, 84);")
        self.Footer.setFrameShape(QFrame.NoFrame)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.Footer)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.Footer)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 20))
        self.frame_19.setMaximumSize(QSize(16777215, 20))
        self.frame_19.setStyleSheet(u"background-color: rgb(191, 140, 217);")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_19)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(140, 0))
        self.frame_7.setMaximumSize(QSize(140, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 2, 47, 13))
        self.label_14.setFont(font5)
        self.date = QLabel(self.frame_7)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(50, 2, 91, 16))
        self.date.setFont(font5)

        self.horizontalLayout_6.addWidget(self.frame_7)

        self.frame_10 = QFrame(self.frame_19)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(170, 0))
        self.frame_10.setMaximumSize(QSize(170, 16777215))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 2, 47, 13))
        self.label_23.setFont(font5)
        self.time = QLabel(self.frame_10)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(80, 2, 81, 16))
        self.time.setFont(font5)

        self.horizontalLayout_6.addWidget(self.frame_10)

        self.horizontalSpacer_4 = QSpacerItem(498, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.CashierName = QLineEdit(self.frame_19)
        self.CashierName.setObjectName(u"CashierName")
        self.CashierName.setMinimumSize(QSize(130, 0))
        self.CashierName.setMaximumSize(QSize(130, 16777215))
        font12 = QFont()
        font12.setFamily(u"Mongolian Baiti")
        font12.setPointSize(11)
        self.CashierName.setFont(font12)
        self.CashierName.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 3px;\n"
"	background-color: rgb(132, 128, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"	background-color: rgb(88, 197, 255);\n"
"}\n"
"")
        self.CashierName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.CashierName)


        self.verticalLayout_12.addWidget(self.frame_19)

        self.DownFooter = QFrame(self.Footer)
        self.DownFooter.setObjectName(u"DownFooter")
        self.DownFooter.setStyleSheet(u"")
        self.DownFooter.setFrameShape(QFrame.NoFrame)
        self.DownFooter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.DownFooter)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.BillDetails = QFrame(self.DownFooter)
        self.BillDetails.setObjectName(u"BillDetails")
        self.BillDetails.setMinimumSize(QSize(630, 85))
        self.BillDetails.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 127);\n"
"	font: 14pt \"Mongolian Baiti\";\n"
"}")
        self.BillDetails.setFrameShape(QFrame.NoFrame)
        self.BillDetails.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.BillDetails)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 101, 21))
        font13 = QFont()
        font13.setFamily(u"Mongolian Baiti")
        font13.setPointSize(14)
        font13.setBold(False)
        font13.setItalic(False)
        font13.setWeight(50)
        self.label_9.setFont(font13)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblpay = QLabel(self.BillDetails)
        self.lblpay.setObjectName(u"lblpay")
        self.lblpay.setGeometry(QRect(120, 40, 91, 31))
        self.lblPrice = QLabel(self.BillDetails)
        self.lblPrice.setObjectName(u"lblPrice")
        self.lblPrice.setGeometry(QRect(120, 10, 91, 21))
        self.label_10 = QLabel(self.BillDetails)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 45, 101, 21))
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblCashMethod = QLabel(self.BillDetails)
        self.lblCashMethod.setObjectName(u"lblCashMethod")
        self.lblCashMethod.setGeometry(QRect(220, 40, 111, 31))
        self.lblCashMethod.setStyleSheet(u"color: rgb(85, 255, 255);\n"
"font: 10pt \"MV Boli\";")
        self.lblDisc = QLabel(self.BillDetails)
        self.lblDisc.setObjectName(u"lblDisc")
        self.lblDisc.setGeometry(QRect(490, 10, 91, 21))
        self.label_11 = QLabel(self.BillDetails)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(350, 10, 131, 21))
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_29 = QLabel(self.BillDetails)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(540, 50, 71, 21))
        font14 = QFont()
        font14.setFamily(u"Mongolian Baiti")
        font14.setPointSize(11)
        font14.setBold(False)
        font14.setItalic(False)
        font14.setWeight(50)
        self.label_29.setFont(font14)
        self.label_29.setStyleSheet(u"QLabel {\n"
"	color: rgb(106, 255, 106);\n"
"	font: 11pt \"Mongolian Baiti\";\n"
"}")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblInv = QLabel(self.BillDetails)
        self.lblInv.setObjectName(u"lblInv")
        self.lblInv.setGeometry(QRect(420, 50, 111, 21))
        self.lblInv.setFont(font14)
        self.lblInv.setStyleSheet(u"QLabel {\n"
"	color: rgb(106, 255, 106);\n"
"	font: 11pt \"Mongolian Baiti\";\n"
"}")
        self.lblInv.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.BillDetails)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.Balance = QFrame(self.DownFooter)
        self.Balance.setObjectName(u"Balance")
        self.Balance.setMinimumSize(QSize(300, 85))
        self.Balance.setMaximumSize(QSize(300, 16777215))
        self.Balance.setFrameShape(QFrame.NoFrame)
        self.Balance.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.Balance)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(14, 8, 270, 70))
        self.frame_8.setMinimumSize(QSize(270, 70))
        self.frame_8.setMaximumSize(QSize(270, 16777215))
        font15 = QFont()
        font15.setBold(False)
        font15.setWeight(50)
        self.frame_8.setFont(font15)
        self.frame_8.setStyleSheet(u"QLabel{\n"
"	color: rgb(193, 255, 151);\n"
"	font: 16pt \"Mongolian Baiti\";\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: rgb(141, 13, 130);\n"
"border-radius: 10px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 8, 111, 21))
        self.label_12.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblTot = QLabel(self.frame_9)
        self.lblTot.setObjectName(u"lblTot")
        self.lblTot.setGeometry(QRect(120, 8, 131, 21))
        self.lblTot.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_9.addWidget(self.frame_9)

        self.frmBlnce = QFrame(self.frame_8)
        self.frmBlnce.setObjectName(u"frmBlnce")
        self.frmBlnce.setFrameShape(QFrame.StyledPanel)
        self.frmBlnce.setFrameShadow(QFrame.Raised)
        self.lblBlnceT = QLabel(self.frmBlnce)
        self.lblBlnceT.setObjectName(u"lblBlnceT")
        self.lblBlnceT.setGeometry(QRect(20, 0, 91, 31))
        self.lblBlnceT.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.lblBlnceT.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblBlnce = QLabel(self.frmBlnce)
        self.lblBlnce.setObjectName(u"lblBlnce")
        self.lblBlnce.setGeometry(QRect(120, 0, 141, 31))
        self.lblBlnce.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")

        self.verticalLayout_9.addWidget(self.frmBlnce)


        self.horizontalLayout_7.addWidget(self.Balance)


        self.verticalLayout_12.addWidget(self.DownFooter)


        self.verticalLayout_2.addWidget(self.Footer)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.Main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnMenu.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"My Store", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Main Street, Alawwa.", None))
        self.btnMini.setText("")
        self.btnMax.setText("")
        self.btnCls.setText("")
#if QT_CONFIG(accessibility)
        self.btnHome.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btnStore.setText(QCoreApplication.translate("MainWindow", u"Store", None))
        self.btnAnylise.setText(QCoreApplication.translate("MainWindow", u"Anylise", None))
        self.btnSetting.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Item ID", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"New Additions :", None))
        self.AddNewDealer.setText(QCoreApplication.translate("MainWindow", u"    Add New Dealers", None))
        self.AddNewItem.setText(QCoreApplication.translate("MainWindow", u"    Add New Items", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.AddNewDealer_2.setText(QCoreApplication.translate("MainWindow", u"    Add New Dealers", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Available Store :", None))
        self.btnBuyItems.setText(QCoreApplication.translate("MainWindow", u"  Buy Items", None))
        self.btnStock.setText(QCoreApplication.translate("MainWindow", u" Back To Stock", None))
        self.SearchStore.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Item Name/ID", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Search Items :", None))
        self.orderByStock.setText(QCoreApplication.translate("MainWindow", u"Stock Order", None))
        self.orderByDate.setText(QCoreApplication.translate("MainWindow", u"Last Added Date", None))
        self.orderByDiscount.setText(QCoreApplication.translate("MainWindow", u"Item Discount", None))
        self.orderByPrice.setText(QCoreApplication.translate("MainWindow", u"Item Price", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Sort By ;", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Item ID", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Last Update", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Discount", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Item ID", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Item Name", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Puschase Price", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.btnAddStoreOK.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Invoice No.", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Dealer Name :", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"24.03.2021", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"9.59", None))
        self.CashierName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cashier", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Total Price :", None))
        self.lblpay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblPrice.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Payment :", None))
        self.lblCashMethod.setText(QCoreApplication.translate("MainWindow", u"by Cash/Card", None))
        self.lblDisc.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Total Discount :", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Invoice", None))
        self.lblInv.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Net Total :", None))
        self.lblTot.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblBlnceT.setText(QCoreApplication.translate("MainWindow", u"Balance :", None))
        self.lblBlnce.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

