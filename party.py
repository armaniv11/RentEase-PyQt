


import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import QIcon, QPixmap
from datetime import datetime
from partyui import Ui_AddParty
import qtawesome as qta
from icondelegate import IconDelegate

class AddParty(QDialog,Ui_AddParty):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = Ui_AddParty()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_2.clicked.connect(lambda:self.close())
        effect = QtWidgets.QGraphicsDropShadowEffect(self.frame)
        effect.setOffset(0, 10)
        effect.setBlurRadius(20)
        effect.setColor(QColor('black'))
        self.frame.setGraphicsEffect(effect)
        screen_width = QtWidgets.QDesktopWidget().screenGeometry().width()
        screen_height = QtWidgets.QDesktopWidget().screenGeometry().height()

        # self.adjusted_size = screen_width / 4.4
        self.blockwidth = int(screen_width *0.9)
        self.blockheight = int(screen_height * 0.6)



        self.frame.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        self.onlyfloat = QtGui.QDoubleValidator()
        self.partyid = ''
        self.pushButton.clicked.connect(self.addparty)
        self.tableWidget.cellClicked.connect(self.cellclick)
        self.lineEdit_2.textEdited.connect(lambda:self.lineEdit_2.setText(self.lineEdit_2.text().upper()))
        self.lineEdit_4.textEdited.connect(lambda:self.lineEdit_4.setText(self.lineEdit_4.text().upper()))
        self.lineEdit_14.textEdited.connect(self.search)

      
        self.showMaximized()
        self.autoload()

    def search(self,value):
        print(value)
        conn = sqlite3.connect("details.db")
        cursor = conn.cursor()
        cursor.execute("SELECT partyid,partyname,gstin,pmobile,paddress FROM newparty where partyname like ? or paddress like ?",(value+'%',value+'%'))
        result = cursor.fetchall()
        conn.close()
        self.tableshow(result)

    def autoload(self):
        conn = sqlite3.connect("details.db")
        c = conn.cursor()
        c.execute("select partyid,partyname,pmobile,email,paddress,rent,leaseexpiry from newparty")
        res = c.fetchall()
        self.tableshow(res)
        conn.close()

    def tableshow(self,res):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate (res):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)

        header.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6,QtWidgets.QHeaderView.ResizeToContents)

        delegate = IconDelegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)
        for m in range(len(res)):
            status_item = QtWidgets.QTableWidgetItem()
            status_item.setIcon(qta.icon('fa.edit',color='grey'))
            self.tableWidget.setItem(m,7, status_item)
            status_ite = QtWidgets.QTableWidgetItem()
            status_ite.setIcon(qta.icon('mdi.delete-forever',color='red'))
            self.tableWidget.setItem(m,8 , status_ite)

    def addparty(self):
        btntext = self.pushButton.text()
        
        pname = self.lineEdit_2.text()
        paddress = self.lineEdit_4.text()
        # ptype = self.comboBox.currentText()
        pmob = self.lineEdit_5.text()
        gstin = self.lineEdit_6.text()
        email = self.lineEdit_9.text()
        rentamount = self.lineEdit_3.text()
        initialb = self.lineEdit_3.text()
        leaseExpiryDate = self.dateEdit_6.date().toString("yyyy-MM-dd")
        curdate = QDateTime.currentDateTime().toString()
        if pname == '':
            return QMessageBox.warning(self,'Alert!','Party Name cannot be empty!!')
        conn = sqlite3.connect("details.db")
        cursor = conn.cursor()
        cursor.execute("select count(partyname) from newparty where partyname = ?",(pname,))
        if cursor.fetchone()[0]>0:
            return QMessageBox.warning(self,'Alert!','Party Name already exists!!')

        if btntext=='UPDATE PARTY':
            try:
                conn = sqlite3.connect("details.db")
                conn.execute("update newparty set partyname=(?),partype=(?),paddress=(?),pmobile=(?),gstin=(?),pinitial=(?),initialtype=? where partyid=(?)",(pname,ptype,paddress,pmob,gstin,initialb,initialtype,self.partyid))
                conn.commit()
                message = QMessageBox.about(self,'Success','Party Updated Successfully')
                self.pushButton.setText("CREATE PARTY")
                conn.close()
                self.clearInputs()

            except sqlite3.IntegrityError:
                message = QMessageBox.about(self,'Alert!','Party Name Already Exists!')

        else:
            
            conn = sqlite3.connect("details.db")
            conn.execute("insert into newparty(partyname,paddress,pmobile,email,gstin,rent,leaseexpiry, added) values(?,?,?,?,?,?,?,?)",(pname,paddress,pmob,email, gstin,rentamount,leaseExpiryDate, curdate))
            conn.commit()
            conn.close()
            QMessageBox.about(self,'SUCCESS!!','PARTY CREATED SUCCESSFULY!!')
            self.clearInputs()
        conn.close()
        self.autoload()
    

    def clearInputs(self):
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_9.clear()
        
        
    def cellclick(self, row,column):
        if column==self.tableWidget.columnCount()-1:
            ite = self.tableWidget.item(row,0).text()
            itemname = self.tableWidget.item(row,1).text()

            buttonReply = QMessageBox.question(self, 'CONFIRM DELETE', "Are you sure you want to delete the Party?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                print(ite)
                conn = sqlite3.connect("details.db")
                conn.execute("delete from newparty where partyid=(?)",(ite,))
                conn.commit()
                conn.close()
                self.autoload()
        elif column==self.tableWidget.columnCount()-2:
            ite = self.tableWidget.item(row,0).text()
            itemname = self.tableWidget.item(row,1).text()
            conn = sqlite3.connect("details.db")
            c = conn.cursor()

            c.execute("select partyid,partyname,paddress,pmobile,email,gstin,rent,leaseexpiry from newparty where partyid=(?)",(ite,))
            result = c.fetchall()
            self.lineEdit_2.setEnabled(False)
            
            self.partyid = result[0][0]
            self.lineEdit_2.setText(str(result[0][1]))
            self.lineEdit_4.setText(str(result[0][2]))
            
            self.lineEdit_5.setText(str(result[0][3]))
            self.lineEdit_9.setText(str(result[0][4]))

            self.lineEdit_6.setText(str(result[0][5]))
            self.lineEdit_3.setText(str(result[0][6]))

            qdate = QtCore.QDate.fromString(result[0][7],'yyyy-MM-dd')
            print(qdate)

            self.dateEdit_6.setDate(qdate)

            self.pushButton.setText("UPDATE PARTY")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = AddParty()
    sys.exit(app.exec_())
