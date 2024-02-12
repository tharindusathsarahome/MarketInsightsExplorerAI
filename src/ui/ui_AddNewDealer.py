# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddNewDealerANVFKo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_AddNewDealer(object):
    def setupUi(self, AddNewDealer):
        if not AddNewDealer.objectName():
            AddNewDealer.setObjectName(u"AddNewDealer")
        AddNewDealer.resize(305, 394)
        self.verticalLayout_3 = QVBoxLayout(AddNewDealer)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(AddNewDealer)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top = QFrame(self.frame)
        self.Top.setObjectName(u"Top")
        self.Top.setMinimumSize(QSize(0, 50))
        self.Top.setMaximumSize(QSize(16777215, 50))
        self.Top.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.Top.setFrameShape(QFrame.StyledPanel)
        self.Top.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.Top)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 191, 31))
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 16pt \"MV Boli\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Top)

        self.Main = QFrame(self.frame)
        self.Main.setObjectName(u"Main")
        self.Main.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 5px;\n"
"	background-color: rgba(85, 85, 255,180);\n"
"}\n"
"QLineEdit:hover {\n"
"	border-radius: 5px;\n"
"	background-color: rgba(85, 85, 255, 250);\n"
"}")
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.Main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(285, 50))
        self.frame_2.setMaximumSize(QSize(285, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 111, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.dealerID = QLineEdit(self.frame_2)
        self.dealerID.setObjectName(u"dealerID")
        self.dealerID.setGeometry(QRect(120, 10, 161, 21))
        font2 = QFont()
        font2.setPointSize(13)
        self.dealerID.setFont(font2)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(285, 50))
        self.frame_3.setMaximumSize(QSize(285, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.name = QLineEdit(self.frame_3)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(120, 10, 161, 21))
        self.name.setFont(font2)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 10, 91, 21))
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.Main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(285, 50))
        self.frame_4.setMaximumSize(QSize(285, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.nic = QLineEdit(self.frame_4)
        self.nic.setObjectName(u"nic")
        self.nic.setGeometry(QRect(120, 10, 161, 21))
        self.nic.setFont(font2)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 101, 21))
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.Main)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(285, 50))
        self.frame_7.setMaximumSize(QSize(285, 50))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.tele = QLineEdit(self.frame_7)
        self.tele.setObjectName(u"tele")
        self.tele.setGeometry(QRect(120, 10, 161, 21))
        self.tele.setFont(font2)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 101, 21))
        self.label_9.setFont(font1)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.Main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(285, 50))
        self.frame_5.setMaximumSize(QSize(285, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.address = QLineEdit(self.frame_5)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(120, 10, 161, 21))
        self.address.setFont(font2)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 10, 81, 21))
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.Main)

        self.Bottom = QFrame(self.frame)
        self.Bottom.setObjectName(u"Bottom")
        self.Bottom.setMinimumSize(QSize(0, 50))
        self.Bottom.setMaximumSize(QSize(16777215, 50))
        self.Bottom.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 85, 200);\n"
"}\n"
"QPushButton {\n"
"	border-radius: 7px;\n"
"	\n"
"	background-color: rgb(140, 0, 255);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgba(140, 0, 255, 200);\n"
"}")
        self.Bottom.setFrameShape(QFrame.StyledPanel)
        self.Bottom.setFrameShadow(QFrame.Raised)
        self.btnCancelAddToStore = QPushButton(self.Bottom)
        self.btnCancelAddToStore.setObjectName(u"btnCancelAddToStore")
        self.btnCancelAddToStore.setGeometry(QRect(30, 16, 81, 25))
        self.btnCancelAddToStore.setFont(font2)
        self.OK = QPushButton(self.Bottom)
        self.OK.setObjectName(u"OK")
        self.OK.setGeometry(QRect(204, 16, 80, 25))
        self.OK.setFont(font2)

        self.verticalLayout.addWidget(self.Bottom)


        self.verticalLayout_3.addWidget(self.frame)


        self.retranslateUi(AddNewDealer)

        QMetaObject.connectSlotsByName(AddNewDealer)
    # setupUi

    def retranslateUi(self, AddNewDealer):
        AddNewDealer.setWindowTitle(QCoreApplication.translate("AddNewDealer", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AddNewDealer", u"Add New Dealer", None))
        self.label_3.setText(QCoreApplication.translate("AddNewDealer", u"Dealer ID", None))
        self.dealerID.setText("")
        self.label_6.setText(QCoreApplication.translate("AddNewDealer", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("AddNewDealer", u"NIC", None))
        self.label_9.setText(QCoreApplication.translate("AddNewDealer", u"TelePhone", None))
        self.label_5.setText(QCoreApplication.translate("AddNewDealer", u"Address", None))
        self.btnCancelAddToStore.setText(QCoreApplication.translate("AddNewDealer", u"Cancel", None))
        self.OK.setText(QCoreApplication.translate("AddNewDealer", u"OK", None))
    # retranslateUi

