

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
from due_paid_rent import DuePaidRent
from lease_expiry import LeaseExpiry

from party import AddParty
from receive_rent import ReceiveRent
from rent_records import RentRecord
from newuser import NewUser


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



        # self.frame_12.setMinimumSize(QtCore.QSize(self.adjusted_size, 680))
        # self.frame_5.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        # # self.frame_6.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        # self.frame_7.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        # self.frame_8.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))


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
        # self.pushButton_11.setIcon(qta.icon('ei.adult',color='grey'))
        self.pushButton_15.setIcon(qta.icon('fa.code-fork',color='grey'))
        # self.pushButton_18.setIcon(qta.icon('fa.paypal',color='grey'))
        # self.pushButton_19.setIcon(qta.icon('mdi.credit-card-plus-outline',color='grey'))
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
        # self.pushButton_23.setIcon(qta.icon('mdi.plus-box-multiple',color='white'))
        self.pushButton_12.setIcon(qta.icon('mdi.plus-box-multiple',color='white'))
        # self.pushButton_20.setIcon(qta.icon('mdi.plus-box-multiple',color='white'))
        # self.pushButton_3.setIcon(qta.icon('fa.calendar-plus-o',color='grey'))
        # self.pushButton_2.setIcon(qta.icon('mdi.refresh-circle',color='grey'))
        self.pushButton_24.setIcon(qta.icon('mdi.notebook-edit',color='grey'))



        
        self.git_thread = CloneThread()




        #click button actions

        self.pushButton_7.clicked.connect(self.addparty)
        self.pushButton_13.clicked.connect(self.dueLease)

        self.pushButton_12.clicked.connect(self.addparty)
        self.pushButton_16.clicked.connect(self.dueRent)
        self.pushButton_17.clicked.connect(self.dueLease)

        self.pushButton_15.clicked.connect(self.receiveRent)
        # self.pushButton_53.clicked.connect(self.company)
        self.pushButton_54.clicked.connect(self.newuser)
        self.pushButton_32.clicked.connect(self.logout)
        # self.pushButton_59.clicked.connect(self.updatesync)
        self.pushButton_24.clicked.connect(self.rentRegister)

        # self.label_5.hide()
        # self.label_3.hide()
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
        from login import Login
        self.main = Login()
        self.main.show()
    
    def receiveRent(self):
        self.ui = ReceiveRent()
        self.ui.show()
    
    def rentRegister(self):
        self.ui = RentRecord()
        self.ui.show()

    # def company(self):
    #     # self.ui = Company()
    #     self.ui.show()
        
    def newuser(self):
        self.ui = NewUser()
        self.ui.show()
    # def loginhistory(self):
    #     self.window = QtWidgets.QDialog()
    #     self.ui = Ui_loginhistory()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    def dueRent(self):
        self.ui = DuePaidRent()
        self.ui.show()

    def addparty(self):
        self.ui = AddParty()
        self.ui.show()

    def dueLease(self):
        self.ui = LeaseExpiry()
        self.ui.show()

    def autoload(self):
        conn = sqlite3.connect("details.db")
        cursor = conn.cursor()
        cursor.execute("select count(partyname) from newparty")
        res = cursor.fetchone()
        print(res)
        # if res[0]!=2:
        #     conn.execute("insert into newparty(partyname,paddress,gstin,pmobile,pinitial) values ('CASH','','','','')")
        #     conn.execute("insert into newparty(partyname,paddress,gstin,pmobile,pinitial) values ('BANK','','','','')")
        #     conn.commit()

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
        
       
        conn.close()
    
    # def updatesync(self):
    #     added = datetime.now().strftime("%y/%m/%d")
    #     print(added)
    #     abc = 0
        
    #     try:
    #         users = db.child('dfile').get()
    #     except Exception:
    #         QMessageBox.warning(self,'Note','Internet Connection not found')
    #         abc = 1
    #         return
    #     if abc ==0:
    #         conn = sqlite3.connect('details.db')
    #         cursor = conn.cursor()
    #         cursor.execute('select updatedate from registration')
    #         resultu = cursor.fetchall()
    #         try:
    #             resultu = resultu[0][0]
    #         except Exception:
    #             resultu = ''
    #         for user in users.each():
    #             self.filename = user.val()['dfilenamecontra']
    #             self.updatedate = user.val()['date']

    #         if self.filename =='' or self.updatedate==resultu:
    #             QMessageBox.about(self,'Note!',"Software is already Up to date!")
    #         else:
    #             buttonReply = QMessageBox.question(self, 'Update Found!', "Update Window Will Close The Software. Do You Want To Continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #             if buttonReply == QMessageBox.Yes:
    #                 self.git_thread.start()
    #                 self.close()

    #                 # try:
    #                 print('os running')

    #                 os.system('"sync.exe"')
    #                 # sys.exit(app.exec_())

    #                 # except Exception as e:
    #                 #     print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = Dashboard()
    sys.exit(app.exec_())
