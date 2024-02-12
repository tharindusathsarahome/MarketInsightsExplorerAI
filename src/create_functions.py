
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from ui.ui_AddNewDealer import *
from ui.ui_AddDiscount import *
from ui.ui_AddNewItem import *
from datetime import datetime
import sqlite3


conn = sqlite3.connect('data/data.sqlite')
cursor = conn.cursor()


def CreateAddItemBox(self, row):
    itemNoAttribute = row
    self.ui.Item[itemNoAttribute] = QFrame(self.ui.scrollAreaWidgetContents)
    self.ui.Item[itemNoAttribute].setObjectName(u"Item")
    self.ui.Item[itemNoAttribute].setMinimumSize(QSize(0, 0))
    self.ui.Item[itemNoAttribute].setStyleSheet(u"QFrame {\n"
                                "   border-radius: 5px;\n"
                                "   background-color: rgb(159, 159, 239);\n"
                                "}\n"
                                "QLineEdit {\n"
                                "   max-height:25px;\n"
                                "   min-height:25px;\n"
                                "   border-radius: 3px;\n"
                                "   background-color: rgb(233, 205, 255);\n"
                                "   font: 75 14pt \"Comic Sans MS\";\n"
                                "}\n"
                                "QLineEdit::hover {\n"
                                "   background-color: rgb(217, 191, 238);\n"
                                "}")
    self.ui.Item[itemNoAttribute].setFrameShape(QFrame.Box)
    self.ui.Item[itemNoAttribute].setFrameShadow(QFrame.Raised)
    self.ui.horizontalLayout_3[itemNoAttribute] = QHBoxLayout(self.ui.Item[itemNoAttribute])
    self.ui.horizontalLayout_3[itemNoAttribute].setSpacing(2)
    self.ui.horizontalLayout_3[itemNoAttribute].setObjectName(u"horizontalLayout_3")
    self.ui.horizontalLayout_3[itemNoAttribute].setSizeConstraint(QLayout.SetDefaultConstraint)
    self.ui.horizontalLayout_3[itemNoAttribute].setContentsMargins(5, 5, 5, 5)

    self.ui.countItem[itemNoAttribute] = QLabel(self.ui.Item[itemNoAttribute])
    self.ui.countItem[itemNoAttribute].setObjectName(u"countItem")

    self.ui.horizontalLayout_3[itemNoAttribute].addWidget(self.ui.countItem[itemNoAttribute])

    self.ui.textID[itemNoAttribute] = QLineEdit(self.ui.Item[itemNoAttribute])
    self.ui.textID[itemNoAttribute].setObjectName(u"textID")
    self.ui.textID[itemNoAttribute].setMinimumSize(QSize(80, 25))
    self.ui.textID[itemNoAttribute].setMaximumSize(QSize(80, 25))
    self.ui.textID[itemNoAttribute].setAlignment(Qt.AlignCenter)

    self.ui.horizontalLayout_3[itemNoAttribute].addWidget(self.ui.textID[itemNoAttribute])

    self.ui.TextName[itemNoAttribute] = QLineEdit(self.ui.Item[itemNoAttribute])
    self.ui.TextName[itemNoAttribute].setObjectName(u"TextName")
    self.ui.TextName[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextName[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextName[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_3[itemNoAttribute].addWidget(self.ui.TextName[itemNoAttribute])

    self.ui.TextPrize[itemNoAttribute] = QLineEdit(self.ui.Item[itemNoAttribute])
    self.ui.TextPrize[itemNoAttribute].setObjectName(u"TextPrize")
    self.ui.TextPrize[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextPrize[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextPrize[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_3[itemNoAttribute].addWidget(self.ui.TextPrize[itemNoAttribute])

    self.ui.TextDisc[itemNoAttribute] = QLineEdit(self.ui.Item[itemNoAttribute])
    self.ui.TextDisc[itemNoAttribute].setObjectName(u"TextDisc")
    self.ui.TextDisc[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextDisc[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextDisc[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_3[itemNoAttribute].addWidget(self.ui.TextDisc[itemNoAttribute])

    self.ui.TextQty[itemNoAttribute] = QLineEdit(self.ui.Item[itemNoAttribute])
    self.ui.TextQty[itemNoAttribute].setObjectName(u"TextQty")
    self.ui.TextQty[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextQty[itemNoAttribute].setAlignment(Qt.AlignCenter)

    self.ui.horizontalLayout_3[itemNoAttribute].addWidget(self.ui.TextQty[itemNoAttribute])

    self.ui.TextTotal[itemNoAttribute] = QLineEdit(self.ui.Item[itemNoAttribute])
    self.ui.TextTotal[itemNoAttribute].setObjectName(u"TextTotal")
    sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    sizePolicy1.setHorizontalStretch(0)
    sizePolicy1.setVerticalStretch(0)
    sizePolicy1.setHeightForWidth(self.ui.TextTotal[itemNoAttribute].sizePolicy().hasHeightForWidth())
    self.ui.TextTotal[itemNoAttribute].setSizePolicy(sizePolicy1)
    self.ui.TextTotal[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextTotal[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextTotal[itemNoAttribute].setMaxLength(32767)
    self.ui.TextTotal[itemNoAttribute].setFrame(True)
    self.ui.TextTotal[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_3[itemNoAttribute].addWidget(self.ui.TextTotal[itemNoAttribute])

    self.ui.btnCloseItem[itemNoAttribute] = QPushButton(self.ui.Item[itemNoAttribute])
    self.ui.btnCloseItem[itemNoAttribute].setObjectName(u"btnCloseItem")
    self.ui.btnCloseItem[itemNoAttribute].setMinimumSize(QSize(0, 20))
    self.ui.btnCloseItem[itemNoAttribute].setStyleSheet(u"QPushButton {\n"
                                                        "   border-radius: 5px;\n"
                                                        "   text-align: center;\n"
                                                        "   background-color: rgb(255, 176, 177);\n"
                                                        "}\n"
                                                        "QPushButton::hover {\n"
                                                        "   background-color: rgb(255, 140, 165);\n"
                                                        "}")
    icon5 = QIcon()
    icon5.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
    self.ui.btnCloseItem[itemNoAttribute].setIcon(icon5)

    self.ui.btnCloseItem[itemNoAttribute].clicked.connect(lambda: deleteSellItem(self, itemNoAttribute))

    self.ui.horizontalLayout_3[itemNoAttribute].addWidget(self.ui.btnCloseItem[itemNoAttribute])

    self.ui.gridLayout.addWidget(self.ui.Item[itemNoAttribute], itemNoAttribute + 1, 0, 1, 1)

    self.ui.textID[itemNoAttribute].installEventFilter(self)
    self.ui.TextName[itemNoAttribute].installEventFilter(self)
    self.ui.TextQty[itemNoAttribute].installEventFilter(self)
    self.ui.TextPrize[itemNoAttribute].installEventFilter(self)
    self.ui.TextDisc[itemNoAttribute].installEventFilter(self)
    self.ui.TextTotal[itemNoAttribute].installEventFilter(self)

    self.ui.countItem[itemNoAttribute].setText(QCoreApplication.translate("MainWindow", u"" + str(itemNoAttribute + 1) + ".", None))
    self.ui.textID[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
    self.ui.TextName[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Item Name", None))
    self.ui.TextQty[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantity", None))
    self.ui.TextPrize[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
    self.ui.TextDisc[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Discount", None))
    self.ui.TextTotal[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Total", None))
    self.ui.btnCloseItem[itemNoAttribute].setText("")

    self.ui.textID[itemNoAttribute].editingFinished.connect(lambda: SellItemOnIDSetted(self, itemNoAttribute))
    self.ui.TextQty[itemNoAttribute].textChanged.connect(lambda: SellItemOnQtyChanging(self, itemNoAttribute))
    self.ui.TextQty[itemNoAttribute].returnPressed.connect(lambda: SellItemSetted(self, itemNoAttribute))

    self.ui.textID[itemNoAttribute].setCompleter(self.completerItems)




def CreatePurchaseItemBox(self, row):
    itemNoAttribute = row
    self.ui.ItemP[itemNoAttribute] = QFrame(self.ui.scrollAreaWidgetContents)
    self.ui.ItemP[itemNoAttribute].setObjectName(u"ItemP")
    self.ui.ItemP[itemNoAttribute].setMinimumSize(QSize(0, 0))
    self.ui.ItemP[itemNoAttribute].setStyleSheet(u"QFrame[frameShape=\"5\"]{\n"
                                                "   background-color: rgb(255, 0, 0);\n"
                                                "}\n"
                                                "QFrame[frameShape=\"5\"]::hover{\n"
                                                "   background-color: rgb(255, 0, 0);\n"
                                                "}\n"
                                                "QFrame {\n"
                                                "   border-radius: 5px;\n"
                                                "   background-color: rgb(0, 255, 255);\n"
                                                "}\n"
                                                "QLineEdit {\n"
                                                "   max-height:25px;\n"
                                                "   min-height:25px;\n"
                                                "   border-radius: 5px;\n"
                                                "   background-color: rgb(170, 85, 255);\n"
                                                "   font: 75 14pt \"Comic Sans MS\";\n"
                                                "}\n"
                                                "QLineEdit::hover {\n"
                                                "   background-color: rgb(201, 136, 248);\n"
                                                "}")
    self.ui.ItemP[itemNoAttribute].setFrameShape(QFrame.Box)
    self.ui.ItemP[itemNoAttribute].setFrameShadow(QFrame.Raised)
    self.ui.horizontalLayout_98[itemNoAttribute] = QHBoxLayout(self.ui.ItemP[itemNoAttribute])
    self.ui.horizontalLayout_98[itemNoAttribute].setSpacing(2)
    self.ui.horizontalLayout_98[itemNoAttribute].setObjectName(u"horizontalLayout_98")
    self.ui.horizontalLayout_98[itemNoAttribute].setSizeConstraint(QLayout.SetDefaultConstraint)
    self.ui.horizontalLayout_98[itemNoAttribute].setContentsMargins(5, 5, 5, 5)

    self.ui.countItemP[itemNoAttribute] = QLabel(self.ui.ItemP[itemNoAttribute])
    self.ui.countItemP[itemNoAttribute].setObjectName(u"countItemP")

    self.ui.horizontalLayout_98[itemNoAttribute].addWidget(self.ui.countItemP[itemNoAttribute])

    self.ui.textIDP[itemNoAttribute] = QLineEdit(self.ui.ItemP[itemNoAttribute])
    self.ui.textIDP[itemNoAttribute].setObjectName(u"textIDP")
    self.ui.textIDP[itemNoAttribute].setMinimumSize(QSize(80, 25))
    self.ui.textIDP[itemNoAttribute].setMaximumSize(QSize(80, 25))
    self.ui.textIDP[itemNoAttribute].setAlignment(Qt.AlignCenter)

    self.ui.horizontalLayout_98[itemNoAttribute].addWidget(self.ui.textIDP[itemNoAttribute])

    self.ui.TextNameP[itemNoAttribute] = QLineEdit(self.ui.ItemP[itemNoAttribute])
    self.ui.TextNameP[itemNoAttribute].setObjectName(u"TextNameP")
    self.ui.TextNameP[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextNameP[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextNameP[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_98[itemNoAttribute].addWidget(self.ui.TextNameP[itemNoAttribute])

    self.ui.TextPrizeP[itemNoAttribute] = QLineEdit(self.ui.ItemP[itemNoAttribute])
    self.ui.TextPrizeP[itemNoAttribute].setObjectName(u"TextPrizeP")
    self.ui.TextPrizeP[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextPrizeP[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextPrizeP[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_98[itemNoAttribute].addWidget(self.ui.TextPrizeP[itemNoAttribute])

    self.ui.TextQtyP[itemNoAttribute] = QLineEdit(self.ui.ItemP[itemNoAttribute])
    self.ui.TextQtyP[itemNoAttribute].setObjectName(u"TextQtyP")
    self.ui.TextQtyP[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextQtyP[itemNoAttribute].setAlignment(Qt.AlignCenter)

    self.ui.horizontalLayout_98[itemNoAttribute].addWidget(self.ui.TextQtyP[itemNoAttribute])

    self.ui.TextTotalP[itemNoAttribute] = QLineEdit(self.ui.ItemP[itemNoAttribute])
    self.ui.TextTotalP[itemNoAttribute].setObjectName(u"TextTotalP")
    sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    sizePolicy1.setHorizontalStretch(0)
    sizePolicy1.setVerticalStretch(0)
    sizePolicy1.setHeightForWidth(self.ui.TextTotalP[itemNoAttribute].sizePolicy().hasHeightForWidth())
    self.ui.TextTotalP[itemNoAttribute].setSizePolicy(sizePolicy1)
    self.ui.TextTotalP[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextTotalP[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextTotalP[itemNoAttribute].setMaxLength(32767)
    self.ui.TextTotalP[itemNoAttribute].setFrame(True)
    self.ui.TextTotalP[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_98[itemNoAttribute].addWidget(self.ui.TextTotalP[itemNoAttribute])

    self.ui.btnCloseItemP[itemNoAttribute] = QPushButton(self.ui.ItemP[itemNoAttribute])
    self.ui.btnCloseItemP[itemNoAttribute].setObjectName(u"btnCloseItemP")
    self.ui.btnCloseItemP[itemNoAttribute].setMinimumSize(QSize(0, 20))
    self.ui.btnCloseItemP[itemNoAttribute].setStyleSheet(u"QPushButton {\n"
                                                        "   border-radius: 5px;\n"
                                                        "   text-align: center;\n"
                                                        "   background-color: rgb(255, 176, 177);\n"
                                                        "}\n"
                                                        "QPushButton::hover {\n"
                                                        "   background-color: rgb(255, 140, 165);\n"
                                                        "}")
    iconP = QIcon()
    iconP.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
    self.ui.btnCloseItemP[itemNoAttribute].setIcon(iconP)

    self.ui.btnCloseItemP[itemNoAttribute].clicked.connect(lambda: deletePurchaseItem(self, itemNoAttribute))

    self.ui.horizontalLayout_98[itemNoAttribute].addWidget(self.ui.btnCloseItemP[itemNoAttribute])

    self.ui.gridLayout_3.addWidget(self.ui.ItemP[itemNoAttribute], itemNoAttribute + 1, 0, 1, 1)

    self.ui.textIDP[itemNoAttribute].installEventFilter(self)
    self.ui.TextNameP[itemNoAttribute].installEventFilter(self)
    self.ui.TextQtyP[itemNoAttribute].installEventFilter(self)
    self.ui.TextPrizeP[itemNoAttribute].installEventFilter(self)
    self.ui.TextTotalP[itemNoAttribute].installEventFilter(self)

    self.ui.countItemP[itemNoAttribute].setText(QCoreApplication.translate("MainWindow", u"" + str(itemNoAttribute + 1) + ".", None))
    self.ui.textIDP[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
    self.ui.TextNameP[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Item Name", None))
    self.ui.TextQtyP[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantity", None))
    self.ui.TextPrizeP[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
    self.ui.TextTotalP[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Total", None))
    self.ui.btnCloseItemP[itemNoAttribute].setText("")

    self.ui.textIDP[itemNoAttribute].editingFinished.connect(lambda: PurchaseItemOnIDSetted(self, itemNoAttribute))
    self.ui.TextQtyP[itemNoAttribute].textChanged.connect(lambda: PurchaseItemOnQtyChanging(self, itemNoAttribute))
    self.ui.TextQtyP[itemNoAttribute].returnPressed.connect(lambda: PurchaseItemSetted(self, itemNoAttribute))

    self.ui.textIDP[itemNoAttribute].setCompleter(self.completerItems)




def CreateStoreItem(self, row , red , green):
    itemNoAttribute = row
    self.ui.ItemS[itemNoAttribute] = QFrame(self.ui.scrollAreaWidgetContents_2)
    self.ui.ItemS[itemNoAttribute].setObjectName(u"ItemS")
    self.ui.ItemS[itemNoAttribute].setMinimumSize(QSize(0, 0))
    self.ui.ItemS[itemNoAttribute].setStyleSheet(u"QFrame {\n"
                            "   border-radius: 5px;\n"
                            "   background-color: rgb("+ str(red) +", "+ str(green) +", 125);\n"
                            "}\n"
                            "QLineEdit {\n"
                            "   max-height:25px;\n"
                            "   min-height:25px;\n"
                            "   border-radius: 5px;\n"
                            "   background-color: rgba(255, 255, 255, 180);\n"
                            "   font: 75 14pt \"Comic Sans MS\";\n"
                            "}\n"
                            "QLineEdit::hover {\n"
                            "   background-color: rgba(255, 255, 255, 230);\n"
                            "}")
    self.ui.ItemS[itemNoAttribute].setFrameShape(QFrame.Box)
    self.ui.ItemS[itemNoAttribute].setFrameShadow(QFrame.Raised)
    self.ui.horizontalLayout_99[itemNoAttribute] = QHBoxLayout(self.ui.ItemS[itemNoAttribute])
    self.ui.horizontalLayout_99[itemNoAttribute].setSpacing(2)
    self.ui.horizontalLayout_99[itemNoAttribute].setObjectName(u"horizontalLayout_99")
    self.ui.horizontalLayout_99[itemNoAttribute].setSizeConstraint(QLayout.SetDefaultConstraint)
    self.ui.horizontalLayout_99[itemNoAttribute].setContentsMargins(5, 5, 5, 5)

    self.ui.countItemS[itemNoAttribute] = QLabel(self.ui.ItemS[itemNoAttribute])
    self.ui.countItemS[itemNoAttribute].setObjectName(u"countItemS")

    self.ui.horizontalLayout_99[itemNoAttribute].addWidget(self.ui.countItemS[itemNoAttribute])

    self.ui.textIDS[itemNoAttribute] = QLineEdit(self.ui.ItemS[itemNoAttribute])
    self.ui.textIDS[itemNoAttribute].setObjectName(u"textIDS")
    self.ui.textIDS[itemNoAttribute].setMinimumSize(QSize(80, 25))
    self.ui.textIDS[itemNoAttribute].setMaximumSize(QSize(80, 25))
    self.ui.textIDS[itemNoAttribute].setAlignment(Qt.AlignLeft)
    self.ui.textIDS[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_99[itemNoAttribute].addWidget(self.ui.textIDS[itemNoAttribute])

    self.ui.TextNameS[itemNoAttribute] = QLineEdit(self.ui.ItemS[itemNoAttribute])
    self.ui.TextNameS[itemNoAttribute].setObjectName(u"TextNameS")
    self.ui.TextNameS[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextNameS[itemNoAttribute].setAlignment(Qt.AlignLeft)
    self.ui.TextNameS[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_99[itemNoAttribute].addWidget(self.ui.TextNameS[itemNoAttribute])

    self.ui.TextPrizeS[itemNoAttribute] = QLineEdit(self.ui.ItemS[itemNoAttribute])
    self.ui.TextPrizeS[itemNoAttribute].setObjectName(u"TextPrizeS")
    self.ui.TextPrizeS[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextPrizeS[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextPrizeS[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_99[itemNoAttribute].addWidget(self.ui.TextPrizeS[itemNoAttribute])

    self.ui.TextUpdateS[itemNoAttribute] = QLineEdit(self.ui.ItemS[itemNoAttribute])
    self.ui.TextUpdateS[itemNoAttribute].setObjectName(u"TextUpdateS")
    self.ui.TextUpdateS[itemNoAttribute].setMinimumSize(QSize(120, 25))
    self.ui.TextUpdateS[itemNoAttribute].setAlignment(Qt.AlignLeft)
    self.ui.TextUpdateS[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_99[itemNoAttribute].addWidget(self.ui.TextUpdateS[itemNoAttribute])

    self.ui.TextStock[itemNoAttribute] = QLineEdit(self.ui.ItemS[itemNoAttribute])
    self.ui.TextStock[itemNoAttribute].setObjectName(u"TextStock")
    self.ui.TextStock[itemNoAttribute].setMinimumSize(QSize(90, 25))
    self.ui.TextStock[itemNoAttribute].setMaximumSize(QSize(210, 25))
    self.ui.TextStock[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextStock[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_99[itemNoAttribute].addWidget(self.ui.TextStock[itemNoAttribute])

    self.ui.TextDiscS[itemNoAttribute] = QLineEdit(self.ui.ItemS[itemNoAttribute])
    self.ui.TextDiscS[itemNoAttribute].setObjectName(u"TextDiscS")
    self.ui.TextDiscS[itemNoAttribute].setMinimumSize(QSize(90, 25))
    self.ui.TextDiscS[itemNoAttribute].setMaximumSize(QSize(210, 25))
    self.ui.TextDiscS[itemNoAttribute].setAlignment(Qt.AlignCenter)
    self.ui.TextDiscS[itemNoAttribute].setReadOnly(True)

    self.ui.horizontalLayout_99[itemNoAttribute].addWidget(self.ui.TextDiscS[itemNoAttribute])

    self.ui.btnAddDiscount[itemNoAttribute] = QPushButton(self.ui.ItemS[itemNoAttribute])
    self.ui.btnAddDiscount[itemNoAttribute].setObjectName(u"btnAddDiscount")
    self.ui.btnAddDiscount[itemNoAttribute].setMinimumSize(QSize(40, 25))
    self.ui.btnAddDiscount[itemNoAttribute].setStyleSheet(u"QPushButton {\n"
                                                        "   border-radius: 5px;\n"
                                                        "   text-align: center;\n"
                                                        "   background-color: rgb(0, 221, 255);\n"
                                                        "}\n"
                                                        "QPushButton::hover {\n"
                                                        "   background-color: rgb(0, 255, 255);\n"
                                                        "}")

    self.ui.btnAddDiscount[itemNoAttribute].clicked.connect(lambda: AddDiscount(self,itemNoAttribute))

    self.ui.horizontalLayout_99[itemNoAttribute].addWidget(self.ui.btnAddDiscount[itemNoAttribute])


    self.ui.gridLayout_2.addWidget(self.ui.ItemS[itemNoAttribute], itemNoAttribute + 1, 0, 1, 1)

    self.ui.textIDS[itemNoAttribute].installEventFilter(self)
    self.ui.TextNameS[itemNoAttribute].installEventFilter(self)
    self.ui.TextPrizeS[itemNoAttribute].installEventFilter(self)
    self.ui.TextUpdateS[itemNoAttribute].installEventFilter(self)
    self.ui.TextStock[itemNoAttribute].installEventFilter(self)
    self.ui.TextDiscS[itemNoAttribute].installEventFilter(self)

    self.ui.countItemS[itemNoAttribute].setText(QCoreApplication.translate("MainWindow", u"" + str(itemNoAttribute + 1) + ".", None))
    self.ui.textIDS[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
    self.ui.TextNameS[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Item Name", None))
    self.ui.TextPrizeS[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Price", None))
    self.ui.TextUpdateS[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Update", None))
    self.ui.TextStock[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Stock", None))
    self.ui.TextDiscS[itemNoAttribute].setPlaceholderText(QCoreApplication.translate("MainWindow", u"Discount", None))
    self.ui.btnAddDiscount[itemNoAttribute].setText("ADD")




def AddDiscount(self, x):
    self.windowAddDiscount = QDialog()
    self.uiAddDiscount = Ui_AddDiscount()
    self.uiAddDiscount.setupUi(self.windowAddDiscount)
    self.windowAddDiscount.setFixedSize(self.windowAddDiscount.size())
    self.windowAddDiscount.show()
    self.uiAddDiscount.btnCancelAddToStore.clicked.connect(lambda: self.windowAddDiscount.close())

    self.uiAddDiscount.itemID.setText(self.ui.textIDS[x].text())

    cursor.execute("SELECT Name,Prize FROM Item_tb WHERE ItemID = '" + self.ui.textIDS[x].text() + "';")
    for item in cursor.fetchall():
        self.uiAddDiscount.itemName.setText(item[0])
        self.uiAddDiscount.Price.setText(str(item[1]))

    self.uiAddDiscount.OK.setEnabled(False)
    self.uiAddDiscount.Discount.textChanged.connect(lambda: discountChanged(self))
    def discountChanged(self):
        if (len(self.uiAddDiscount.Discount.text()) > 0):
            self.uiAddDiscount.OK.setEnabled(True)
        price = float(self.uiAddDiscount.Price.text())
        discount = float(self.uiAddDiscount.Discount.text())
        if(discount == ""):
            self.uiAddDiscount.lastPrice.setText("0")
        else:
            self.uiAddDiscount.lastPrice.setText(str(price - (price*discount/100)))

    self.uiAddDiscount.OK.clicked.connect(lambda: AddDiscountNow(self))
    def AddDiscountNow(self):
        cursor.execute("SELECT 1 FROM Discount_tb WHERE ItemID = '" +  self.ui.textIDS[x].text() + "';")
        if(cursor.fetchall()):
            sql = "UPDATE Discount_tb SET Discount = '" + self.uiAddDiscount.Discount.text() + "' WHERE ItemID = '" +  self.ui.textIDS[x].text() + "';"
            cursor.execute(sql)
        else:
            sql = "INSERT INTO Discount_tb (ItemID, Discount) VALUES('" + self.ui.textIDS[x].text() + "', '" + self.uiAddDiscount.Discount.text() + "');"
            cursor.execute(sql)        

        conn.commit()
        self.windowAddDiscount.close()
        StoreSetting(self)




def AddNewItem(self):
    self.windowAddNewItem = QDialog()
    self.uiAddNewItem = Ui_AddNewItem()
    self.uiAddNewItem.setupUi(self.windowAddNewItem)
    self.windowAddNewItem.setFixedSize(self.windowAddNewItem.size())
    self.windowAddNewItem.show()
    self.uiAddNewItem.btnCancelAddToStore.clicked.connect(lambda: self.windowAddNewItem.close())

    now = datetime.now()
    today = now.strftime("%d/%m/%Y")

    self.uiAddNewItem.catergory.setCompleter(self.completerCategory)

    self.uiAddNewItem.OK.setEnabled(False)
    self.uiAddNewItem.itemID.textChanged.connect(lambda: disableButton(self))
    self.uiAddNewItem.itemName.textChanged.connect(lambda: disableButton(self))
    self.uiAddNewItem.Price.textChanged.connect(lambda: disableButton(self))
    self.uiAddNewItem.catergory.textChanged.connect(lambda: disableButton(self))
    self.uiAddNewItem.barCode.textChanged.connect(lambda: disableButton(self))
    def disableButton(self):
        if (len(self.uiAddNewItem.itemID.text()) > 0) and (len(self.uiAddNewItem.itemName.text()) > 0) and (len(self.uiAddNewItem.Price.text()) > 0) and (len(self.uiAddNewItem.catergory.text()) > 0) and (len(self.uiAddNewItem.barCode.text()) > 0):
            self.uiAddNewItem.OK.setEnabled(True)

    self.uiAddNewItem.OK.clicked.connect(lambda: AddItemNow(self))

    def AddItemNow(self):
        ID = self.uiAddNewItem.itemID.text()

        try:
            cursor.execute("SELECT Name FROM Item_tb WHERE ItemID = '" + ID + "';")
            item1 = cursor.fetchall()
            print(item1[0][0] + " ID Exist")

        except:
            ItemName = self.uiAddNewItem.itemName.text()
            Price = self.uiAddNewItem.Price.text()
            Category = self.uiAddNewItem.catergory.text()
            BarCode = self.uiAddNewItem.barCode.text()
            Qty = self.uiAddNewItem.Qty.text()

            cursor.execute("SELECT CategoryID FROM Category_tb WHERE Category = '" + Category + "';")
            item1 = cursor.fetchall()
            Category = item1[0][0]

            sql = "INSERT INTO Item_tb (BarCode, ItemID, Name, Prize, Category) VALUES ('" + BarCode + "','" +  ID + "','" +  ItemName + "','" + Price + "','" +  Category + "')"
            cursor.execute(sql)
            print(sql)

            sql = "INSERT INTO Store_tb (Stock, ItemID, LastUpdate) VALUES ('" + Qty + "','" +  ID + "','" +  today + "')"
            cursor.execute(sql)
            print(sql)

            conn.commit()
            self.windowAddNewItem.close()




def AddNewDealer(self):
    self.windowAddNewDealer = QDialog()
    self.uiAddNewDealer = Ui_AddNewDealer()
    self.uiAddNewDealer.setupUi(self.windowAddNewDealer)
    self.windowAddNewDealer.setFixedSize(self.windowAddNewDealer.size())
    self.windowAddNewDealer.show()
    self.uiAddNewDealer.btnCancelAddToStore.clicked.connect(lambda: self.windowAddNewDealer.close())

    Select = "SELECT DealerID FROM Dealers_tb ORDER BY DealerID DESC LIMIT 1"
    cursor.execute(Select)
    myresult = cursor.fetchall()
    LastDealer=int(myresult[0][0])
    LastDealer+=1
    self.uiAddNewDealer.dealerID.setText(str(LastDealer))

    self.uiAddNewDealer.OK.setEnabled(False)
    self.uiAddNewDealer.dealerID.textChanged.connect(lambda: disableButton(self))
    self.uiAddNewDealer.name.textChanged.connect(lambda: disableButton(self))
    self.uiAddNewDealer.nic.textChanged.connect(lambda: disableButton(self))
    self.uiAddNewDealer.tele.textChanged.connect(lambda: disableButton(self))
    self.uiAddNewDealer.address.textChanged.connect(lambda: disableButton(self))
    def disableButton(self):
        if (len(self.uiAddNewDealer.dealerID.text()) > 0) and (len(self.uiAddNewDealer.name.text()) > 0) and (len(self.uiAddNewDealer.nic.text()) > 0) and (len(self.uiAddNewDealer.tele.text()) > 0) and (len(self.uiAddNewDealer.address.text()) > 0):
            self.uiAddNewDealer.OK.setEnabled(True)

    self.uiAddNewDealer.OK.clicked.connect(lambda: AddDealerNow(self))

    def AddDealerNow(self):

        Name = self.uiAddNewDealer.name.text()
        NIC = self.uiAddNewDealer.nic.text()
        Tele = self.uiAddNewDealer.tele.text()
        Address = self.uiAddNewDealer.address.text()

        sql = "INSERT INTO Dealers_tb (DealerID, Name, NIC, Telephone, Address) VALUES ('" + str(LastDealer) + "','" +  Name + "','" +  NIC + "','" + Tele + "','" +  Address + "')"
        cursor.execute(sql)
        print(sql)

        conn.commit()
        self.windowAddNewDealer.close()




def StoreSetting(self):

    self.ui.stackedWidget.setCurrentWidget(self.ui.Store)
    self.ui.stackedWidget_2.setCurrentWidget(self.ui.Normal)

    search = self.ui.SearchStore.text()

    self.ui.btnBuyItems.show()
    self.ui.btnStock.hide()
    self.ui.searchItems.show()
    self.ui.BillDetails.hide()
    self.ui.Balance.hide()

    cursor.execute("SELECT ItemID,Name,Prize FROM Item_tb WHERE ItemID LIKE '%" + search + "%' OR Name LIKE '%" + search + "%';")
    result = cursor.fetchall()

    #myArray = result
    myArray = []

    if self.ui.orderByStock.isChecked() == True:
        cursor.execute("SELECT ItemID FROM Store_tb ORDER BY Stock")
        sortOrder = cursor.fetchall()
        for sortItem in sortOrder:
            for item in result:
                if(sortItem[0] == item[0]):
                    myArray.append(item)

    if self.ui.orderByDate.isChecked() == True:
        cursor.execute("SELECT ItemID FROM Store_tb ORDER BY LastUpdate DESC")
        sortOrder = cursor.fetchall()
        for sortItem in sortOrder:
            for item in result:
                if(sortItem[0] == item[0]):
                    myArray.append(item)

    if self.ui.orderByPrice.isChecked() == True:
        cursor.execute("SELECT ItemID FROM Item_tb ORDER BY Prize DESC")
        sortOrder = cursor.fetchall()
        for sortItem in sortOrder:
            for item in result:
                if(sortItem[0] == item[0]):
                    myArray.append(item)

    if self.ui.orderByDiscount.isChecked() == True:
        cursor.execute("SELECT ItemID FROM Discount_tb ORDER BY Discount DESC")
        sortOrder = cursor.fetchall()
        for sortItem in sortOrder:
            for item in result:
                if(sortItem[0] == item[0]):
                    myArray.append(item)

    for x in range(0,len(self.ui.ItemS)):
        try:
            self.ui.ItemS[x].deleteLater()
        except:
            pass
        
    for row, item in enumerate(myArray):
        cursor.execute("SELECT Stock FROM Store_tb WHERE ItemID = '" + item[0] + "';")
        item1 = cursor.fetchall()
        stock = int(item1[0][0])

        if(stock == 0):
            green = 0
            red = 255
        elif(stock == 100):
            green = 255
            red = 255
        elif(stock >= 200):
            green = 255
            red = 0
        elif(100 < stock < 200):
            green = 255
            red = 255 - ((stock-100)/100*255)
        elif(0 < stock < 100):
            green = ((stock)/100*255)
            red = 255

        if(red >= 255):
            red = 255
        if(red < 0):
            red = 0
        if(green >= 255):
            green = 255
        if(green < 0):
            green = 0

        CreateStoreItem(self, row, red, green)

        self.ui.textIDS[row].setText(item[0])
        self.ui.TextNameS[row].setText(item[1])
        self.ui.TextPrizeS[row].setText(str(item[2]))
        id = item[0]

        #WHERE Username LIKE '%$inputText%' OR CUS_ID LIKE '%$inputText%'

        cursor.execute("SELECT Stock,LastUpdate FROM Store_tb WHERE ItemID = '" + id + "';")
        item1 = cursor.fetchall()
        self.ui.TextStock[row].setText(str(item1[0][0]))
        self.ui.TextUpdateS[row].setText(item1[0][1])

        cursor.execute("SELECT Discount FROM Discount_tb WHERE ItemID = '" + id + "';")
        item1 = cursor.fetchall()
        try:
            self.ui.TextDiscS[row].setText(str(item1[0][0]) + " %")
        except:
            self.ui.TextDiscS[row].setText("0 %")

    # mylist2 = [item for item in mylist]
    # print(mylist)

   # self.ui.TextName[0].setText(mylist[])

    width = self.ui.DownFooter.height()
    self.animation = QPropertyAnimation(self.ui.DownFooter, b"maximumHeight")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(10)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()




def SellItemsNow(self):

    InvNo = self.ui.lblInv.text()

    for x in range(0,len(self.ui.Item)):
        try:
            itemID = self.ui.textID[x].text()
            Qty = self.ui.TextQty[x].text()
            Discount = self.ui.TextDisc[x].text()
            Price = self.ui.TextPrize[x].text()

            now = datetime.now()
            date = now.strftime("%d/%m/%Y")
            time = now.strftime("%H:%M")

            if (itemID != ""):
                sql = "INSERT INTO Sales_tb (ItemID, Quantity, ItemPrize, Discount, dateAdded, timeAdded, SaleInvoiceNo) VALUES ('" + itemID + "','" + Qty + "','" + Price + "','" + Discount + "','" + date + "','" + time + "','" + InvNo + "')"
                cursor.execute(sql)

                cursor.execute("SELECT Stock FROM Store_tb WHERE ItemID = '" + itemID + "';")
                myresult = cursor.fetchall()
                Stock=int(myresult[0][0])
                Stock -= int(Qty)

                cursor.execute("UPDATE Store_tb SET Stock = '" + str(Stock) + "' WHERE ItemID = '" +  itemID + "';")

            else:
                pass

        except:
            pass

    conn.commit()

    for x in range(0,len(self.ui.Item)):
        try:
            self.ui.Item[x].deleteLater()
        except:
            pass

    self.rows = 0
    CreateAddItemBox(self,self.rows)

    Select = "SELECT SaleInvoiceNo FROM Sales_tb ORDER BY SaleInvoiceNo DESC LIMIT 1"
    cursor.execute(Select)
    myresult = cursor.fetchall()
    InvNo=int(myresult[0][0])
    InvNo+=1
    InvNo = str(InvNo)
    InvNo = InvNo.zfill(7)
    self.ui.lblInv.setText(InvNo)

    self.totalPrice = 0
    self.ui.lblPrice.setText("Rs " + str("%.2f" % round(self.totalPrice, 2)))
    self.totalDiscount = 0
    self.ui.lblDisc.setText("Rs " + str("%.2f" % round(self.totalDiscount, 2)))
    self.netTotal = 0
    self.ui.lblTot.setText("Rs " + str("%.2f" % round(self.netTotal, 2)))

    print("Inserted ...")





def AddItemsToStockNow(self):
    InvNo = self.ui.AddStoreInvNo.text()

    cursor.execute("SELECT DealerID FROM Dealers_tb WHERE Name = '" + self.ui.AddStoreDealerID.text() + "';")
    item1 = cursor.fetchall()
    DealerID = item1[0][0]

    for x in range(0,len(self.ui.ItemP)):
        try:
            itemID = self.ui.textIDP[x].text()
            Qty = self.ui.TextQtyP[x].text()
            Price = self.ui.TextPrizeP[x].text()

            now = datetime.now()
            today = now.strftime("%d/%m/%Y")

            if (itemID != ""):
                sql = "INSERT INTO Purchases_tb (ItemID, Amount, ItemPrize, PurchaseInvoiceNo) VALUES ('" + itemID + "','" + Qty + "','" + Price + "','" + InvNo + "')"
                cursor.execute(sql)

                cursor.execute("SELECT Stock FROM Store_tb WHERE ItemID = '" + itemID + "';")
                myresult = cursor.fetchall()
                Stock=int(myresult[0][0])
                Stock += int(Qty)

                cursor.execute("UPDATE Store_tb SET Stock = '" + str(Stock) + "', LastUpdate= '" + today + "' WHERE ItemID = '" +  itemID + "';")

            else:
                pass

        except:
            pass

    sql = "INSERT INTO PurchasesDealer_tb (DealerID, PurchaseInvoiceNo, AddedDate) VALUES ('" + DealerID + "','" +  InvNo + "','" +  today + "')"
    cursor.execute(sql)

    conn.commit()

    for x in range(0,len(self.ui.ItemP)):
        try:
            self.ui.ItemP[x].deleteLater()
        except:
            pass

    self.PurchaseRows = 0
    CreatePurchaseItemBox(self,self.PurchaseRows)
    StoreSetting(self)




def windowType(self):

    self.ui.Item = {}
    self.ui.countItem = {}
    self.ui.TextName = {}
    self.ui.countItem = {}
    self.ui.textID = {}
    self.ui.TextName = {}
    self.ui.TextDisc = {}
    self.ui.TextQty = {}
    self.ui.TextPrize = {}
    self.ui.TextTotal = {}
    self.ui.btnCloseItem = {}
    self.ui.horizontalLayout_3 = {}
    self.ui.horizontalLayout_12 = {}



    self.ui.ItemP = {}
    self.ui.countItemP = {}
    self.ui.textIDP = {}
    self.ui.TextNameP = {}
    self.ui.TextQtyP = {}
    self.ui.TextPrizeP = {}
    self.ui.TextTotalP = {}
    self.ui.btnCloseItemP = {}
    self.ui.horizontalLayout_98 = {}



    self.ui.ItemS = {}
    self.ui.textIDS = {}
    self.ui.countItemS = {}
    self.ui.TextNameS = {}
    self.ui.TextDiscS = {}
    self.ui.TextPrizeS = {}
    self.ui.TextUpdateS = {}
    self.ui.TextStock = {}
    self.ui.btnAddDiscount = {}
    self.ui.horizontalLayout_99 = {}

    # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(20)
    self.shadow.setXOffset(0)
    self.shadow.setYOffset(0)
    self.shadow.setColor(QColor(0, 92, 157, 150))
    self.ui.centralwidget.setGraphicsEffect(self.shadow)

    self.ui.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    self.ui.gridLayout.addItem(self.ui.verticalSpacer, 999, 0, 1, 1)

    self.ui.verticalSpacerS = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    self.ui.gridLayout_2.addItem(self.ui.verticalSpacerS, 999, 0, 1, 1)

    self.ui.verticalSpacerP = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    self.ui.gridLayout_3.addItem(self.ui.verticalSpacerP, 999, 0, 1, 1)

    self.ui.btnMini.clicked.connect(lambda: self.showMinimized())
    self.ui.btnCls.clicked.connect(lambda: self.close())
    self.ui.btnMax.clicked.connect(lambda: restore_or_maximize_window(self))

    self.ui.btnMenu.clicked.connect(lambda: slideLeftMenu(self))

    self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
    self.ui.stackedWidget_2.setCurrentWidget(self.ui.Normal)

    self.ui.btnHome.clicked.connect(lambda:  HomeClicked(self))
    def HomeClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.BillDetails.show()
        self.ui.Balance.show()
        self.ui.frmBlnce.show()
        width = self.ui.DownFooter.height()
        self.animation = QPropertyAnimation(self.ui.DownFooter, b"maximumHeight")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(10000)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    self.ui.btnStore.clicked.connect(lambda: StoreSetting(self))
    self.ui.btnAnylise.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Anylise))
    self.ui.btnSetting.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Settings))

    self.ui.btnBuyItems.clicked.connect(lambda: BuyItemsClicked(self))

    def BuyItemsClicked(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.AddStock)
        self.ui.Balance.show()
        self.ui.frmBlnce.hide()
        Select = "SELECT PurchaseInvoiceNo FROM Purchases_tb ORDER BY PurchaseInvoiceNo DESC LIMIT 1"
        cursor.execute(Select)
        myresult = cursor.fetchall()
        InvNo = int(myresult[0][0])
        InvNo += 1
        InvNo = str(InvNo)
        InvNo = InvNo.zfill(6)
        self.ui.AddStoreInvNo.setText(InvNo)
        self.ui.btnBuyItems.hide()
        self.ui.btnStock.show()
        self.ui.searchItems.hide()
        width = self.ui.DownFooter.height()
        self.animation = QPropertyAnimation(self.ui.DownFooter, b"maximumHeight")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(10000)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    self.ui.orderByDate.setChecked(True)
    self.ui.orderByDate.toggled.connect(lambda: StoreSetting(self))
    self.ui.orderByStock.toggled.connect(lambda: StoreSetting(self))
    self.ui.orderByDiscount.toggled.connect(lambda: StoreSetting(self))
    self.ui.orderByPrice.toggled.connect(lambda: StoreSetting(self))

    self.ui.btnStock.hide()
    self.ui.btnStock.clicked.connect(lambda: btnStockClicked(self))
    def btnStockClicked(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.Normal)
        self.ui.btnBuyItems.show()
        self.ui.btnStock.hide()
        self.ui.searchItems.show()
        self.ui.BillDetails.hide()
        self.ui.Balance.hide()
        width = self.ui.DownFooter.height()
        self.animation = QPropertyAnimation(self.ui.DownFooter, b"maximumHeight")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(10)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    self.ui.AddStoreDealerID.setCompleter(self.completerDealers)

    self.ui.CashierName.setCompleter(self.completerCashiers)

    self.ui.btnAddStoreOK.clicked.connect(lambda: AddItemsToStockNow(self))

    self.ui.btnAddStoreOK.setEnabled(False)
    self.ui.AddStoreDealerID.textChanged.connect(lambda: disableButton(self))
    def disableButton(self):
        if (len(self.ui.AddStoreDealerID.text()) > 0):
            self.ui.btnAddStoreOK.setEnabled(True)



    def moveWindow(e):
        if self.isMaximized() == False:  # Not maximized
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

    self.ui.Header.mouseMoveEvent = moveWindow


    def restore_or_maximize_window(self):
        win_status = self.WINDOW_SIZE

        if win_status == 0:
            self.WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
            self.showMaximized()

            self.ui.btnMax.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))  # Show minized icon
        else:
            # Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.WINDOW_SIZE = 0
            self.showNormal()

            self.ui.btnMax.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))  # Show maximize icon

    def slideLeftMenu(self):
        width = self.ui.leftBar.width()

        if width == 37:
            newWidth = 100
        else:
            newWidth = 37

        self.animation = QPropertyAnimation(self.ui.leftBar, b"maximumWidth")  # Animate minimumWidht
        self.animation.setDuration(250)
        # Start value is the current menu width
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()



 
def deleteSellItem(self, x):
    self.totalPrice -= (float(self.ui.TextPrize[x].text()) * int(self.ui.TextQty[x].text()))
    self.ui.lblPrice.setText("Rs " + str(self.totalPrice))
    self.totalDiscount -= float(self.ui.TextDisc[x].text())
    self.ui.lblDisc.setText("Rs " + str(self.totalDiscount))
    self.netTotal -= float(self.ui.TextTotal[x].text())
    self.ui.lblTot.setText("Rs " + str("%.2f" % round(self.netTotal, 2)))

    self.ui.Item[x].deleteLater()


def SellItemSetted(self, x):
    self.rows += 1
    CreateAddItemBox(self,self.rows)
    self.ui.textID[x + 1].setFocusPolicy(Qt.StrongFocus)
    self.ui.textID[x + 1].setFocus()

    self.totalPrice += (float(self.ui.TextPrize[x].text()) * float(self.ui.TextQty[x].text()))
    self.ui.lblPrice.setText("Rs " + str("%.2f" % round(self.totalPrice, 2)))
    self.totalDiscount += float(self.ui.TextDisc[x].text())
    self.ui.lblDisc.setText("Rs " + str("%.2f" % round(self.totalDiscount, 2)))
    self.netTotal += float(self.ui.TextTotal[x].text())
    self.ui.lblTot.setText("Rs " + str("%.2f" % round(self.netTotal, 2)))
    self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())

def SellItemOnQtyChanging(self, x):
    prize = self.ui.TextPrize[x].text()
    disc = self.ui.TextDisc[x].text()
    qty = self.ui.TextQty[x].text()

    if (qty == ""):
        self.ui.TextDisc[x].setText(str(self.discountItem))
        self.ui.TextTotal[x].setText("0.00")
    else:
        Discount = float(disc) * int(qty)
        self.ui.TextDisc[x].setText(str("%.2f" % round(Discount, 2)))

        total = ((float(prize) - float(disc)) * int(qty))
        self.ui.TextTotal[x].setText(str("%.2f" % round(total, 2)))


def SellItemOnIDSetted(self, x):
    id = self.ui.textID[x].text()

    cursor.execute("SELECT Name,Prize FROM Item_tb WHERE ItemID = '" + id + "';")
    for item in cursor.fetchall():
        self.ui.TextName[x].setText(item[0])
        self.ui.TextPrize[x].setText(str(item[1]))

        cursor.execute("SELECT Discount FROM Discount_tb WHERE ItemID = '" + id + "';")
        item1 = cursor.fetchall()
        if(len(item1) > 0):
            Discount = float(item1[0][0]) * float(item[1]) / 100
            self.ui.TextDisc[x].setText(str("%.2f" % round(Discount, 2)))
            self.discountItem = float("%.2f" % round(Discount, 2))
        else:
            self.ui.TextDisc[x].setText("0.00")

    self.ui.TextQty[x].setText("1")
    self.ui.TextQty[x].selectAll() 
    self.ui.TextQty[x].setFocusPolicy(Qt.StrongFocus)
    self.ui.TextQty[x].setFocus()



def deletePurchaseItem(self, x):
    self.netTotal -= float(self.ui.TextTotalP[x].text())
    self.ui.lblTot.setText("Rs " + str("%.2f" % round(self.netTotal, 2)))

    self.ui.ItemP[x].deleteLater()


def PurchaseItemSetted(self, x):
    self.PurchaseRows += 1
    CreatePurchaseItemBox(self,self.PurchaseRows)
    self.ui.textIDP[x + 1].setFocusPolicy(Qt.StrongFocus)
    self.ui.textIDP[x + 1].setFocus()

    self.netTotal += float(self.ui.TextTotalP[x].text())
    self.ui.lblTot.setText("Rs " + str(self.netTotal))
    self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())

def PurchaseItemOnQtyChanging(self, x):
    prize = self.ui.TextPrizeP[x].text()
    qty = self.ui.TextQtyP[x].text()

    if (qty == ""):
        self.ui.TextTotalP[x].setText("0.00")
    else:
        total = (float(prize) * int(qty))
        self.ui.TextTotalP[x].setText(str("%.2f" % round(total, 2)))


def PurchaseItemOnIDSetted(self, x):
    id = self.ui.textIDP[x].text()

    cursor.execute("SELECT Name,Prize FROM Item_tb WHERE ItemID = '" + id + "';")
    for item in cursor.fetchall():
        self.ui.TextNameP[x].setText(item[0])
        self.ui.TextPrizeP[x].setText(str(item[1]))

    self.ui.TextQtyP[x].setText("1")
    self.ui.TextQtyP[x].selectAll() 
    self.ui.TextQtyP[x].setFocusPolicy(Qt.StrongFocus)
    self.ui.TextQtyP[x].setFocus()


