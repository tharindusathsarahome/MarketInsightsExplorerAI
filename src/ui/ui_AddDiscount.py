# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddDiscountVsOfjb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_AddDiscount(object):
    def setupUi(self, AddDiscount):
        if not AddDiscount.objectName():
            AddDiscount.setObjectName(u"AddDiscount")
        AddDiscount.resize(305, 394)
        self.verticalLayout_3 = QVBoxLayout(AddDiscount)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(AddDiscount)
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
        self.label = QLabel(self.Top)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 161, 31))
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 16pt \"MV Boli\";")
        self.label.setAlignment(Qt.AlignCenter)

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
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 111, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.itemID = QLineEdit(self.frame_2)
        self.itemID.setObjectName(u"itemID")
        self.itemID.setGeometry(QRect(120, 10, 161, 21))
        font2 = QFont()
        font2.setPointSize(13)
        self.itemID.setFont(font2)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(285, 50))
        self.frame_3.setMaximumSize(QSize(285, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.itemName = QLineEdit(self.frame_3)
        self.itemName.setObjectName(u"itemName")
        self.itemName.setGeometry(QRect(120, 10, 161, 21))
        self.itemName.setFont(font2)
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
        self.Price = QLineEdit(self.frame_4)
        self.Price.setObjectName(u"Price")
        self.Price.setGeometry(QRect(120, 10, 161, 21))
        self.Price.setFont(font2)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 91, 21))
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Main)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(285, 50))
        self.frame_5.setMaximumSize(QSize(285, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.Discount = QLineEdit(self.frame_5)
        self.Discount.setObjectName(u"Discount")
        self.Discount.setGeometry(QRect(120, 10, 161, 21))
        self.Discount.setFont(font2)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 10, 81, 21))
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.Main)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(285, 50))
        self.frame_6.setMaximumSize(QSize(285, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.lastPrice = QLineEdit(self.frame_6)
        self.lastPrice.setObjectName(u"lastPrice")
        self.lastPrice.setGeometry(QRect(120, 10, 161, 21))
        self.lastPrice.setFont(font2)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 10, 111, 21))
        self.label_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.frame_6)


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


        self.retranslateUi(AddDiscount)

        QMetaObject.connectSlotsByName(AddDiscount)
    # setupUi

    def retranslateUi(self, AddDiscount):
        AddDiscount.setWindowTitle(QCoreApplication.translate("AddDiscount", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddDiscount", u"Add Discount", None))
        self.label_2.setText(QCoreApplication.translate("AddDiscount", u"Item ID", None))
        self.itemID.setText("")
        self.label_6.setText(QCoreApplication.translate("AddDiscount", u"Name", None))
        self.label_4.setText(QCoreApplication.translate("AddDiscount", u"Price", None))
        self.label_5.setText(QCoreApplication.translate("AddDiscount", u"Discount", None))
        self.label_7.setText(QCoreApplication.translate("AddDiscount", u"Last Price", None))
        self.btnCancelAddToStore.setText(QCoreApplication.translate("AddDiscount", u"Cancel", None))
        self.OK.setText(QCoreApplication.translate("AddDiscount", u"OK", None))
    # retranslateUi

