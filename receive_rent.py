# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from datetime import datetime
from xmlrpc.client import DateTime
from database_operations import DatabaseOperations
from icondelegate import maxpid, maxpidint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from receive_rentui import Ui_ReceiveRent
from PyQt5.QtGui import QColor
import sqlite3
import sys

from shared_classes import SharedClasses
from shared_functions import maxIdInt

class ReceiveRent(QtWidgets.QDialog,Ui_ReceiveRent):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ReceiveRent()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_2.clicked.connect(lambda:self.close())
        effect = QtWidgets.QGraphicsDropShadowEffect(self.frame_3)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        effect.setColor(QColor('black'))
        self.lineEdit_13.setEnabled(False)
        self.frame_3.setGraphicsEffect(effect)
        self.onlyfloat = QtGui.QDoubleValidator()
        self.lineEdit_11.textEdited.connect(self.cplusch)
        self.lineEdit_11.textChanged.connect(self.cplusch)
        self.pushButton.clicked.connect(self.receive)
        # self.orderlist = list()
        self.showMaximized()
        self.partydict ={}
        self.sitedict = {}
        self.pid = None
        # self.pushButton_3.clicked.connect(self.savepurchase)
        self.autoload()
        self.pushButton_3.hide()
        self.pushButton_3.clicked.connect(self.deleterecord)
        # if self.pid!=None:
        self.comboBox_2.currentIndexChanged.connect(self.partyChanged)


    def partyChanged(self):
        partyName = self.comboBox_2.currentText()
        pid = DatabaseOperations.findPidFromName(partyName)
        rent = DatabaseOperations.selectRentFromParty(pid)['rent']
        self.lineEdit_11.setText(str(rent))
        print(f"{pid} printing pid")
    
    def clickload(self,pid):
        self.pid = pid
        self.pushButton_3.show()
        conn = sqlite3.connect("details.db")
        cur = conn.cursor()
        cur.execute("SELECT newparty.partyname,rentreceive,rentMonth,chqdate,chqnumber,rentreceivedate,remark from rentledger \
            LEFT JOIN newparty on rentledger.partyid=newparty.partyid \
                    where id = ?",(pid,))
        result = cur.fetchone()
        print(result)
        self.label_9.setText(str(pid))
        # index = self.comboBox.findText(result[0])
        # self.comboBox.setCurrentIndex(index)
        index = self.comboBox_2.findText(result[0])
        self.comboBox_2.setCurrentIndex(index)

        self.lineEdit_11.setText(str(result[1]))

        index = self.comboBox.findText(result[2])
        self.comboBox.setCurrentIndex(index)

        self.lineEdit_10.setText(str(result[4]))
        
        d = QtCore.QDate.fromString(result[3],'yyyy-MM-dd')
        self.dateEdit.setDate(d)

        d = QtCore.QDateTime.fromString(result[5],'yyyy-MM-dd hh:mm')
        self.dateTimeEdit.setDateTime(d)

        self.lineEdit_9.setText(str(result[6]))
        
        
        self.pushButton.setText('UPDATE')
        print(result)
        
    def autoload(self):

        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        asd =  SharedClasses().partyDict
        self.comboBox_2.clear()
        for key in asd:
            self.comboBox_2.addItem(key)

        result = maxIdInt('id','rentledger')
        self.label_9.setText(result)
        self.comboBox_2.setCurrentIndex(-1)
    
    def cplusch(self):
        try:
            cash = float(self.lineEdit_11.text())
        except Exception:
            cash = 0
        cheque = 0
        total = cash + cheque
        self.lineEdit_13.setText(str(total))

    
    def receive(self):
        
        pid = self.label_9.text()
        # site = self.comboBox.currentText()
        party = self.comboBox_2.currentText()
        partyId = SharedClasses().partyDict[party]
        try:
            cash = float(self.lineEdit_11.text())
        except Exception:
            cash = 0
        cheque = 0
        # try:
        #     chqamount = float(self.lineEdit_12.text())
        # except Exception:
        #     chqamount = 0
        credit = self.lineEdit_13.text()
        chqno = self.lineEdit_10.text()
        desc = self.lineEdit_9.text()
        chqdate = self.dateEdit.dateTime()
        chqdate = chqdate.toString("yyyy-MM-dd")
        rentMonth = self.comboBox.currentText()

        date = self.dateTimeEdit.dateTime()
        rentreceivedate = date.toString("yyyy-MM-dd hh:mm")
        conn = sqlite3.connect("details.db")
        c=conn.cursor()

        
        # if site=='':
        #     QMessageBox.warning(self,'Alert!',"Please select Site!")
        if party=='':
            QMessageBox.warning(self,'Alert!',"Please select Party!")
        elif credit=='' or credit== '0':
            QMessageBox.warning(self,'Alert!',"Please provide amount!")
        else:
            if self.pushButton.text().startswith('UPDATE'):
                try:
                    conn = sqlite3.connect("details.db")
                    conn.execute("UPDATE rentledger SET partyid = ?,rentreceive = ?,rentMonth = ?,chqdate = ?,chqnumber = ?,remark = ?,rentreceivedate = ?,updated = ? where id = ?",(partyId,cash,rentMonth,chqdate,chqno,desc,rentreceivedate,datetime.now(),pid))
                    conn.commit()
                    conn.close()
                    self.close()
                    QMessageBox.about(self,'Success!','Payment has been updated successfully!')
                    return
                except Exception as e:
                    print(e)
                    QMessageBox.warning(self,'Error!!','There has been an error, please try again or Consult Admin!!')

            conn = sqlite3.connect("details.db")
            conn.execute("INSERT INTO rentledger(partyid,rentreceive,rentMonth,chqdate,chqnumber,remark,rentreceivedate,added) values (?,?,?,?,?,?,?,?)",(partyId,cash,rentMonth,chqdate,chqno,desc,rentreceivedate,datetime.now()))
            conn.commit()
                
            buttonReply = QMessageBox.question(self, 'Success!!', "Rent has been saved successfully.\nDo you want to receive another rent?", \
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                self.lineEdit_9.clear()
                self.lineEdit_10.clear()
                self.lineEdit_11.clear()

                self.lineEdit_13.clear()

                maxId = maxIdInt('id','rentledger')
                print(f"printing maxid {maxId}")
                self.label_9.setText(str(maxId))
            else:
                self.close()
        conn.close()
    
    def deleterecord(self):
        if self.pushButton.text().endswith('UPDATE'):
            print(self.pid,'update')
            buttonReply = QMessageBox.question(self, 'CONFIRM DELETE?', "Are you sure you want to delete this Record?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                try:
                    conn = sqlite3.connect("details.db")
                    conn.execute("delete from rentledger where id = ?",(self.pid,))
                    conn.commit()
                    conn.close()
                    self.close()
                except Exception as e:
                    print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = ReceiveRent()
    sys.exit(app.exec_())
