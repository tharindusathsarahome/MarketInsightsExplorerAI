import sys,os,platform,sqlite3
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import *
from ui.ui_Main import *
from create_functions import *

# os.system('pyrcc5 Icons.qrc -o Icons_rc.py')

conn = sqlite3.connect('data/data.sqlite')
cursor = conn.cursor()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.WINDOW_SIZE = 0
        self.ui = Ui_MainWindow()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.rows = 0
        self.PurchaseRows = 0
        self.ui.setupUi(self)

        cursor.execute('SELECT ItemID FROM Item_tb')
        IDlist = [item[0] for item in cursor.fetchall()]
        self.completerItems = QCompleter()
        modelItems = QStringListModel()
        modelItems.setStringList(IDlist)
        self.completerItems.setModel(modelItems)

        cursor.execute('SELECT Category FROM Category_tb')
        Categorylist = [item[0] for item in cursor.fetchall()]
        self.completerCategory = QCompleter()
        modelCategory = QStringListModel()
        modelCategory.setStringList(Categorylist)
        self.completerCategory.setModel(modelCategory)

        cursor.execute('SELECT Name FROM Dealers_tb')
        Dealerlist = [item[0] for item in cursor.fetchall()]
        self.completerDealers = QCompleter()
        modelDealers = QStringListModel()
        modelDealers.setStringList(Dealerlist)
        self.completerDealers.setModel(modelDealers)

        cursor.execute('SELECT CashierName FROM Cashiers_tb')
        Cashierlist = [item[0] for item in cursor.fetchall()]
        self.completerCashiers = QCompleter()
        modelCashiers = QStringListModel()
        modelCashiers.setStringList(Cashierlist)
        self.completerCashiers.setModel(modelCashiers)

        windowType(self)

        self.ui.AddNewItem.clicked.connect(lambda: AddNewItem(self))
        self.ui.AddNewDealer.clicked.connect(lambda: AddNewDealer(self))
        self.ui.SearchStore.textChanged.connect(lambda: StoreSetting(self))

        CreateAddItemBox(self,self.rows)
        CreatePurchaseItemBox(self,self.PurchaseRows)
        self.totalPrice = 0
        self.totalDiscount = 0
        self.netTotal = 0

        now = datetime.now()
        self.ui.date.setText(now.strftime("%Y-%m-%d"))
        self.ui.time.setText(now.strftime("%H:%M:%S"))

        Select = "SELECT SaleInvoiceNo FROM Sales_tb ORDER BY SaleInvoiceNo DESC LIMIT 1"
        cursor.execute(Select)
        myresult = cursor.fetchall()
        InvNo=int(myresult[0][0])
        InvNo+=1
        InvNo = str(InvNo)
        InvNo = InvNo.zfill(7)
        self.ui.lblInv.setText(InvNo)

        self.show()





    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Q:
            print("Killing")
        elif event.key() == QtCore.Qt.Key_Insert:
            SellItemsNow(self)
        event.accept()

    def eventFilter(self, source, event):
        if (event.type() == QEvent.KeyPress):
            print('key press:', (event.key(), event.text())) 
        # for x in range(len(self.ui.textID)):
        # if (event.type() == QEvent.KeyPress and source is self.ui.SearchStore):
        #     print(self.ui.SearchStore.text())
        #     self.StoreSetting()
        return super(MainWindow, self).eventFilter(source, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
else:
    print(__name__, "hh")
