


import sys
import platform
from tracemalloc import start
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import QIcon, QPixmap
from datetime import datetime

import qtawesome
from rent_recordsui import Ui_RentRecords
from PyQt5.QtGui import QPainter
from PyQt5.QtPrintSupport import QPrinter
from icondelegate import IconDelegate
from receive_rent import ReceiveRent

from shared_classes import SharedClasses


class RentRecord(QDialog,Ui_RentRecords):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = Ui_RentRecords()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(lambda:self.close())
        effect = QtWidgets.QGraphicsDropShadowEffect(self.frame)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        effect.setColor(QColor('black'))
        self.frame.setGraphicsEffect(effect)
        self.onlyfloat = QtGui.QDoubleValidator()
        self.selectedParty = ''
        self.pushButton_13.clicked.connect(self.rentRecord)
        self.pushButton_14.clicked.connect(self.partyRentRecord)
        self.pushButton_12.clicked.connect(self.dateSearch)


        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5,QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(7,QtWidgets.QHeaderView.ResizeToContents)
        self.lineEdit_14.textEdited.connect(self.search)
        self.tableWidget.cellClicked.connect(self.cellclick)
       
        self.pushButton_8.setIcon(qtawesome.icon('mdi.printer',color='white'))
        self.pushButton_9.setIcon(qtawesome.icon('mdi.database-export',color='white'))
        self.pushButton_8.clicked.connect(self.handle_preview)
        self.pushButton_9.clicked.connect(self.print_widget)
        
        self.autoLoad()

        self.showMaximized()
        
        


    

    def closewindow(self):
        self.close()

    def handle_print(self):
        printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
        printer.setPaperSize(QPrinter.A4)
        printer.setPageSize(QPrinter.A4)
        printer.setOrientation(QPrinter.Portrait)
        
        printer.setPageMargins(10, 10, 10, 10, QPrinter.Millimeter)

        dialog = QtPrintSupport.QPrintDialog(printer, self)
        if dialog.exec_() == QtPrintSupport.QPrintDialog.Accepted:
            self.handle_paint_request(printer)

    def handle_preview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handle_paint_request)
        dialog.exec_()
    
    # def handle_paint_request(self, printer):
    #     document = QtGui.QTextDocument()
    #     cursor = QtGui.QTextCursor(document)
    #     table = cursor.insertTable(self.tableWidget.rowCount(), self.tableWidget.columnCount())

    #     for row in range(table.rows()):
    #         for col in range(table.columns()):
    #             it = self.tableWidget.item(row, col)
    #             if it is not None:
    #                 cursor.insertText(it.text())
    #             cursor.movePosition(QtGui.QTextCursor.NextCell)
    #     document.print_(printer)

    def handle_paint_request(self, printer):
        painter = QtGui.QPainter(printer)
        # painter.setViewport(self.fr)
        painter.setWindow(self.tableWidget.rect())                        
        self.tableWidget.render(painter)
        painter.end()
        print('printed')
        


    def print_widget(self):
        # widget = QLabel('Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        # widget.setFont(font)
        # widget.resize(256, 256)
        # widget.setWordWrap(True)
        # Print options
        # self.frame.setGeometry(QtCore.QRect(0, 0, 821, 1031))
        # self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 791, 961))

        widget = self.tableWidget
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOrientation(QPrinter.Portrait)
        printer.setPaperSize(QPrinter.A4)
        printer.setPageSize(QPrinter.A4)
        printer.setPageMargins(5, 5, 5, 5, QPrinter.Millimeter)
        # Setting the margins and then calling setFullPage() will discard the margins.
        # printer.setFullPage(True)
        printer.setOutputFormat(QPrinter.PdfFormat)
        filename,_ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', '', ".pdf(*.pdf)")

        printer.setOutputFileName(filename)
         
        # Render/Paint it
        painter = QPainter()
        painter.begin(printer)
         
        # Establish scaling transform
        scaleX = printer.pageRect().width() / widget.rect().width() 
        scaleY = printer.pageRect().height() / widget.rect().width()
        # useScale2 = min(scaleX)
        # useScale = max(scaleY)
        painter.scale(scaleX, scaleY)
         
        widget.render(painter)
        painter.end()
        QMessageBox.about(self,'Success!','PDF has been created successfully!')
        # self.close()

    def search(self,value):
        print(value)
        conn = sqlite3.connect("details.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id,newparty.partyname,chqnumber,chqdate,\
            remark,rentreceivedate,rentMonth,rentreceive from rentledger LEFT JOIN newparty ON \
                rentledger.partyid = newparty.partyid where newparty.partyname like ? or rentledger.rentMonth like ?",(value+'%',value+'%'))
        
        result = cursor.fetchall()
        conn.close()
        self.tableshow(result)

    def autoLoad(self):
        parties = SharedClasses().partyDict
        self.comboBox.clear()
        for key in parties:
            self.comboBox.addItem(key)
        self.dateEdit_4.setDate(QtCore.QDate.currentDate())
        self.dateEdit_5.setDate(QtCore.QDate.currentDate())
        
        
    def partyRentRecord(self):
        selectedParty = self.comboBox.currentText()
        print(SharedClasses.partyDict[selectedParty])
        
        conn = sqlite3.connect("details.db")
        c = conn.cursor()
        c.execute("SELECT id,newparty.partyname,chqnumber,chqdate,\
            remark,rentreceivedate,rentMonth,rentreceive from rentledger LEFT JOIN newparty ON \
                rentledger.partyid = newparty.partyid where rentledger.partyid = ? order by id desc",(SharedClasses.partyDict[selectedParty],))
        result = c.fetchall()
        self.tableshow(result)
        conn.close()
    
    def dateSearch(self):
        startDate = self.dateEdit_4.date().toString('yyyy-MM-dd')
        endDate = self.dateEdit_5.date().toString('yyyy-MM-dd')
        conn = sqlite3.connect("details.db")
        c = conn.cursor()
        c.execute("SELECT id,newparty.partyname,chqnumber,chqdate,\
            remark,rentreceivedate,rentMonth,rentreceive from rentledger LEFT JOIN newparty ON \
                rentledger.partyid = newparty.partyid where rentledger.rentreceivedate >=? and rentledger.rentreceivedate  <= ? order by id desc",(startDate,endDate))
        result = c.fetchall()
        self.tableshow(result)
        conn.close()


    def rentRecord(self):
        conn = sqlite3.connect("details.db")
        c = conn.cursor()
        c.execute("SELECT id,newparty.partyname,chqnumber,chqdate,\
            remark,rentreceivedate,rentMonth,rentreceive from rentledger LEFT JOIN newparty ON \
                rentledger.partyid = newparty.partyid order by id desc")
        result = c.fetchall()
        self.tableshow(result)
        conn.close()

    def tableshow(self,result):
        self.tableWidget.setRowCount(0)
        j = 0
        colCount = self.tableWidget.columnCount()
        for row_number, row_data in enumerate (result):
            # self.progressBar.setValue = 0
            j = j+1
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                if column_number==colCount -2: 
                    # print(f"printing col number {column_number} {resLength}")
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
                    # item.setTextAlignment()

                    
                self.tableWidget.setItem(row_number, column_number, item)
            self.progressBar.setValue(int(j*100/len(result)))
            
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)

        header.setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5,QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(7,QtWidgets.QHeaderView.ResizeToContents)

        delegate = IconDelegate(self.tableWidget)
        self.tableWidget.setItemDelegate(delegate)
        for m in range(len(result)):
            status_item = QtWidgets.QTableWidgetItem()
            status_item.setIcon(qtawesome.icon('fa.edit',color='grey'))
            self.tableWidget.setItem(m,colCount-1, status_item)
        credittot = debittot = running = 0

        for i,j in enumerate(result):
            print(i,j)
            credittot = credittot+j[colCount-2]
        self.label_27.setText('Rs. '+ str(credittot))
    
    def cellclick(self, row,column):

        
        if column == self.tableWidget.columnCount() - 1:
            id = self.tableWidget.item(row,0).text()
            self.main = ReceiveRent()
            self.main.show()
            self.main.clickload(id)
            

        # trans = self.tableWidget.item(row,4).text()
        # print(id,trans)
        # if trans=='RECEIVE':
        #     self.main = Credit()
        #     self.main.show()
        #     self.main.clickload(id)
        # elif trans=='BALANCEPAY':
        #     self.main = Pay()
        #     self.main.show()
        #     self.main.clickload(id)
        # elif trans.startswith('PURCHASE'):
        #     self.main = Purchase()
        #     self.main.show()
        #     self.main.clickload(id)


    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = RentRecord()
    sys.exit(app.exec_())
