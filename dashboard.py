

import os
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QThread, QTime, QUrl, Qt, QEvent, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import QIcon, QPixmap
from datetime import datetime

import pyrebase
from dashboardui import Ui_Dashboard
import qtawesome as qta

from party import AddParty
from receive_rent import ReceiveRent
from rent_records import RentRecord
# from purchase import Purchase
# from pay import Pay
# from credit import Credit
# from company import Company
# from addparty import AddParty
# from addsite import AddSite
# from addmaterial import AddMaterial
# from purchase import Purchase
# from cashbankledger import CashBankLedger
# from siteledger import SiteLedger
# from ledger import Ledger
# from daybook import Daybook
# from newuser import NewUser
# from purchaseregister import PurchaseRegister

firebaseConfig = {
    'apiKey': "AIzaSyDsWveinI2Vkm3yxR8f2ax3XIOEQo_1yMA",
    'authDomain': "finacko-8e82b.firebaseapp.com",
    'databaseURL': "https://finacko-8e82b-default-rtdb.firebaseio.com",
    'projectId': "finacko-8e82b",
    'storageBucket': "finacko-8e82b.appspot.com",
    'messagingSenderId': "861428154184",
    'appId': "1:861428154184:web:1275031f280bfbecc2bd7d",
    'measurementId': "G-2XC3WBFK15",
  }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

class CloneThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def run(self):
        # message = QMessageBox.about(self,'note','update in progress')
        # self.sync()
        # buttonReply = QMessageBox.question(self, 'Note!', "Update Checking Will Close The Software. Do You Want To Continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # if buttonReply == QMessageBox.Yes:
            # time.sleep(5)
        os.system("taskkill /f /im  thekedaarsaathi.exe")

class Dashboard(QMainWindow,Ui_Dashboard):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = Ui_Dashboard()
        self.setupUi(self)
        screen_width = QtWidgets.QDesktopWidget().screenGeometry().width()
        screen_height = QtWidgets.QDesktopWidget().screenGeometry().height()

        self.adjusted_size = int(screen_width / 4.4)
        self.blockwidth = int(screen_width / 5.5)
        self.blockheight = int(screen_height / 4.5)



        self.frame_12.setMinimumSize(QtCore.QSize(self.adjusted_size, 680))
        self.frame_5.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        self.frame_6.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        self.frame_7.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        self.frame_8.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))


        # print(desktop_size)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_6.clicked.connect(lambda:self.close())
        effect = QtWidgets.QGraphicsDropShadowEffect()
        effect.setOffset(5, 5)
        effect.setBlurRadius(40)
        effect.setColor(QColor('grey'))
        self.frame.setGraphicsEffect(effect)
        
        # self.pushButton_5.setIcon(qta.icon('fa.sitemap',color='grey'))
        self.pushButton_7.setIcon(qta.icon('fa5s.people-carry',color='grey'))
        # self.pushButton_33.setIcon(qta.icon('ei.inbox-alt',color='grey'))
        self.pushButton_11.setIcon(qta.icon('ei.adult',color='grey'))
        self.pushButton_15.setIcon(qta.icon('fa.code-fork',color='grey'))
        self.pushButton_18.setIcon(qta.icon('fa.paypal',color='grey'))
        self.pushButton_19.setIcon(qta.icon('mdi.credit-card-plus-outline',color='grey'))
        self.pushButton_16.setIcon(qta.icon('fa5s.book-open',color='grey'))
        self.pushButton_17.setIcon(qta.icon('mdi.notebook-edit',color='grey'))
        # self.pushButton_21.setIcon(qta.icon('mdi.bank-transfer',color='grey'))
        # self.pushButton_22.setIcon(qta.icon('mdi.office-building-marker-outline',color='grey'))
        self.pushButton_53.setIcon(qta.icon('mdi.office-building-marker',color='grey'))
        self.pushButton_54.setIcon(qta.icon('fa.user-plus',color='grey'))
        self.pushButton_55.setIcon(qta.icon('mdi.help-rhombus',color='grey'))
        self.pushButton_58.setIcon(qta.icon('mdi.checkbox-multiple-marked-circle',color='grey'))
        self.pushButton_59.setIcon(qta.icon('mdi.update',color='grey'))
        self.pushButton_57.setIcon(qta.icon('ei.asl',color='grey'))
        self.pushButton_32.setIcon(qta.icon('mdi.logout-variant',color='grey'))
        self.pushButton_13.setIcon(qta.icon('mdi.plus-box-multiple',color='white'))
        self.pushButton_23.setIcon(qta.icon('mdi.plus-box-multiple',color='white'))
        self.pushButton_12.setIcon(qta.icon('mdi.plus-box-multiple',color='white'))
        self.pushButton_20.setIcon(qta.icon('mdi.plus-box-multiple',color='white'))
        # self.pushButton_3.setIcon(qta.icon('fa.calendar-plus-o',color='grey'))
        # self.pushButton_2.setIcon(qta.icon('mdi.refresh-circle',color='grey'))
        self.pushButton_24.setIcon(qta.icon('mdi.notebook-edit',color='grey'))



        
        self.git_thread = CloneThread()




        #click button actions
        # self.pushButton_5.clicked.connect(self.addsite)
        self.pushButton_23.clicked.connect(self.addsite)

        self.pushButton_7.clicked.connect(self.addparty)
        self.pushButton_13.clicked.connect(self.addparty)

        
        # self.pushButton_33.clicked.connect(self.addmaterial)
        self.pushButton_12.clicked.connect(self.addmaterial)

        self.pushButton_15.clicked.connect(self.receiveRent)
        self.pushButton_18.clicked.connect(self.receiveRent)
        self.pushButton_19.clicked.connect(self.credit)
        self.pushButton_16.clicked.connect(self.daybook)
        self.pushButton_17.clicked.connect(self.partyledger)
        # self.pushButton_21.clicked.connect(self.cashledger)
        # self.pushButton_22.clicked.connect(self.siteledger)
        self.pushButton_53.clicked.connect(self.company)
        self.pushButton_54.clicked.connect(self.newuser)
        self.pushButton_32.clicked.connect(self.logout)
        self.pushButton_59.clicked.connect(self.updatesync)
        self.pushButton_24.clicked.connect(self.rentRegister)

        self.label_5.hide()
        self.label_3.hide()
        self.showMaximized()
        # self.autoload()

    def siteledger(self):
        # self.ui = SiteLedger()
        
        self.ui.show()
    # def aboutus(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_aboutWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

    def logout(self):
        self.close()
        # from login import Login
        # self.main = Login()
        self.main.show()
    
    def receiveRent(self):
        self.ui = ReceiveRent()
        self.ui.show()
    
    def rentRegister(self):
        self.ui = RentRecord()
        self.ui.show()

    def company(self):
        # self.ui = Company()
        self.ui.show()
    def newuser(self):
        # self.ui = NewUser()
        self.ui.show()
    # def loginhistory(self):
    #     self.window = QtWidgets.QDialog()
    #     self.ui = Ui_loginhistory()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    def addsite(self):
        self.ui = AddSite()
        self.ui.show()
    def addparty(self):
        self.ui = AddParty()
        self.ui.show()
    def addmaterial(self):
        self.ui = AddMaterial()
        self.ui.show()
    def daybook(self):
        self.ui = Daybook()
        self.ui.show()
    # def daybookp(self):
    #     self.ui = Ui_daysearchWindow()
    #     self.ui.show()
    def credit(self):
        self.ui = Credit()
        self.ui.show()
    def partyledger(self):
        self.ui = Ledger()
        self.ui.show()
    def purchase(self):
        self.ui = Purchase()
        self.ui.show()
    def cashledger(self):
        self.ui = CashBankLedger()
        self.ui.show()

    def autoload(self):
        conn = sqlite3.connect("details.db")
        cursor = conn.cursor()
        cursor.execute("select count(partyname) from newparty where partyname='CASH' OR partyname='BANK'")
        res = cursor.fetchone()
        print(res)
        if res[0]!=2:
            conn.execute("insert into newparty(partyname,paddress,gstin,pmobile,pinitial) values ('CASH','','','','')")
            conn.execute("insert into newparty(partyname,paddress,gstin,pmobile,pinitial) values ('BANK','','','','')")
            conn.commit()

        # optional updating the changes in credit, purchase and pay
        try:
            cursor.execute("SELECT distinct pid from purchase where pid not like 'P%'")
            res = cursor.fetchall()
            if len(res)>0:
                for i in res:
                    pid = str(i[0])
                    pid = 'P'+pid
                    conn.execute("update purchase set pid = ? where pid = ?",(pid,i[0]))
                    conn.execute("update ledger set transid = ? where transid = ?",(pid,i[0]))
                    conn.commit()
            cursor.execute("SELECT distinct pid from credit where pid not like 'C%'")
            res = cursor.fetchall()
            if len(res)>0:
                for i in res:
                    pid = str(i[0])
                    pid = 'C'+pid
                    conn.execute("update credit set pid = ? where pid = ?",(pid,i[0]))
                    conn.execute("update ledger set transid = ? where transid = ?",(pid,i[0]))
                    conn.commit()
            cursor.execute("SELECT distinct pid from pay where pid not like 'D%'")
            res = cursor.fetchall()
            if len(res)>0:
                for i in res:
                    pid = str(i[0])
                    pid = 'D'+pid
                    conn.execute("update pay set pid = ? where pid = ?",(pid,i[0]))
                    conn.execute("update ledger set transid = ? where transid = ?",(pid,i[0]))
                    conn.commit()
        except Exception:
            pass
        cursor.execute("select firm from firminfo")
        resu = cursor.fetchall()
        try:
            resu = str(resu[0][0])
        except Exception:
            resu = " FIRM NAME NOT SET"
        self.pushButton.setText(resu)
        
        curedate = QDateTime.currentDateTime()
        curedate = curedate.toString('yyyy/MM/dd hh:mm:ss')
        self.label_5.setText('Current Login: '+curedate)
        cursor.execute("SELECT date FROM loginhistory ORDER BY date DESC LIMIT 2")
        resu = cursor.fetchall()
        try:
            resu = str(resu[1][0])
        except Exception:
            resu = ""
        self.label_3.setText('Last Login: '+resu)
        cursor.execute("SELECT count(matid) from newmaterial where activated=True")
        resu = cursor.fetchone()
        self.label_13.setText(str(resu[0]))
        cursor.execute("SELECT count(partyid) from newparty where activated=True")
        resu = cursor.fetchone()
        self.label_20.setText(str(resu[0]))
        cursor.execute("SELECT count(siteid) from newsite where activated=True")
        resu = cursor.fetchone()
        self.label_26.setText(str(resu[0]))
        cursor.execute("SELECT count(eid) from employee")
        resu = cursor.fetchone()
        self.label_23.setText(str(resu[0]))
        print(resu)
        conn.close()
    
    def updatesync(self):
        added = datetime.now().strftime("%y/%m/%d")
        print(added)
        abc = 0
        
        try:
            users = db.child('dfile').get()
        except Exception:
            QMessageBox.warning(self,'Note','Internet Connection not found')
            abc = 1
            return
        if abc ==0:
            conn = sqlite3.connect('details.db')
            cursor = conn.cursor()
            cursor.execute('select updatedate from registration')
            resultu = cursor.fetchall()
            try:
                resultu = resultu[0][0]
            except Exception:
                resultu = ''
            for user in users.each():
                self.filename = user.val()['dfilenamecontra']
                self.updatedate = user.val()['date']

            if self.filename =='' or self.updatedate==resultu:
                QMessageBox.about(self,'Note!',"Software is already Up to date!")
            else:
                buttonReply = QMessageBox.question(self, 'Update Found!', "Update Window Will Close The Software. Do You Want To Continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if buttonReply == QMessageBox.Yes:
                    self.git_thread.start()
                    self.close()

                    # try:
                    print('os running')

                    os.system('"sync.exe"')
                    # sys.exit(app.exec_())

                    # except Exception as e:
                    #     print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Dashboard()
    sys.exit(app.exec_())
