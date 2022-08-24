


from os import rename
import sys
import platform
from xmlrpc.client import DateTime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtPrintSupport
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtGui import QIcon, QPixmap
from datetime import datetime

import qtawesome
from appConstants import AppConstants
from due_paid_rentui import Ui_DuePaidRent
from PyQt5.QtGui import QPainter
from PyQt5.QtPrintSupport import QPrinter

from shared_classes import SharedClasses


class DuePaidRent(QDialog,Ui_DuePaidRent):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = Ui_DuePaidRent()
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
        self.siteid = ''
        self.startMonth = 'June'
        self.startYear = 2022
        self.currentMonth = ''
        self.currentYear = ''
        # self.monthsMap = {}
        self.monthsList = ['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
        self.monthsMap = {'JANUARY':'01','FEBRUARY':'02','MARCH':'03','APRIL':'04','MAY':'05','JUNE':'06','JULY':'07','AUGUST':'08','SEPTEMBER':'09','OCTOBER':'10','NOVEMBER':'11','DECEMBER':'12'}
        
        self.pushButton_13.clicked.connect(self.rentRecord)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3,QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(4,QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(5,QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(7,QtWidgets.QHeaderView.ResizeToContents)
        self.lineEdit_14.textEdited.connect(self.search)
        self.tableWidget.cellClicked.connect(self.cellclick)
       
        self.pushButton_8.setIcon(qtawesome.icon('mdi.printer',color='white'))
        self.pushButton_9.setIcon(qtawesome.icon('mdi.database-export',color='white'))
        self.pushButton_8.clicked.connect(self.handle_preview)
        self.pushButton_9.clicked.connect(self.print_widget)

        self.autoload()

        self.showMaximized()
        
        
    def closewindow(self):
        self.close()

    
    def autoload(self):
        self.currentMonth = datetime.now().month
        self.currentYear = datetime.now().year
        print(self.currentMonth)
        print(self.currentYear)






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
    
    def dueRentLoad(self):
        conn = sqlite3.connect("details.db")
        cursor = conn.cursor()
        cursor.execute("SELECT rentledger.id,newparty.partyname, \
                ledger.partyid = newparty.partyid LEFT JOIN newsite ON ledger.siteid = newsite.siteid where (ledger.transtype!='CASH' AND ledger.transtype!='BANK' AND \
                    ledger.transtype!='PURCHASE TOTAL' and newparty.partyname like ?)",(value+'%',))
        result = cursor.fetchall()


    def search(self,value):
        print(value)
        # conn = sqlite3.connect("details.db")
        # cursor = conn.cursor()
        # cursor.execute("SELECT ledger.transid,ledger.date,(CASE WHEN newsite.sitename is null THEN '' ELSE newsite.sitename END),\
        #     newparty.partyname,transtype,material,value,transport,debit,credit from ledger LEFT JOIN newparty ON \
        #         ledger.partyid = newparty.partyid LEFT JOIN newsite ON ledger.siteid = newsite.siteid where (ledger.transtype!='CASH' AND ledger.transtype!='BANK' AND \
        #             ledger.transtype!='PURCHASE TOTAL' and newparty.partyname like ?)",(value+'%',))
        # result = cursor.fetchall()
        # conn.close()
        # self.tableshow(result)

        
        


    def rentRecord(self):
        print("printing current Month")

        partydict = SharedClasses().partyDict

        conn = sqlite3.connect("details.db")
        c = conn.cursor()

        # list of due rents
        dueRents = []
        # print(AppConstants.CURRENTYEAR)
        # while ()
        # print(SharedClasses().partyDict)
        for party in partydict:
            print(party)
            # Starting Year Check
            self.startYear = AppConstants.STARTYEAR

            while self.startYear<=AppConstants.CURRENTYEAR:
                print(f"prinitng month and year {self.startYear}")
                # print()
                # print(AppConstants.CURRENTYEAR)


                if self.startYear < AppConstants.CURRENTYEAR:
                    startMonthIndex = 0
                    lastMonthIndex = 12
                   
                else:
                    startMonthIndex = self.monthsMap[AppConstants.STARTMONTH]
                    lastMonthIndex = AppConstants.CURRENTMONTH
                    

                print("Printing index")
                print(startMonthIndex)
                print(lastMonthIndex)
                # return
                paidMonths = self.findMonthRent(partydict[party])
                findMonths = []
                for i in range(int(startMonthIndex),lastMonthIndex - 1):
                    findMonths.append(int(i))
                print(findMonths)
                paidMonthsIndex = []
                for i in paidMonths:
                    for j in i:
                        print(j)
                        paidMonthsIndex.append(int(self.monthsMap[j]))
                print("printing paidmonthsindex")
                print(paidMonthsIndex)
                unpaidMonthsIndex =  [x for x in findMonths if x not in paidMonthsIndex]
                print("printing unpaid months")
                print(unpaidMonthsIndex)
                c.execute("SELECT partyid,partyname,paddress,rent from newparty where partyname=?",(party,))
                result = c.fetchone()
                initialResult = list(result)
                
                for unpaid in unpaidMonthsIndex:
                    listResult = []
                    listResult =  listResult + initialResult
                    # listResult = initialResult
                    print("poriting initial result")
                    print(initialResult)
                    print(listResult)
                    print(self.monthsList[unpaid])
                    listResult.append(self.monthsList[unpaid])
                    dueRents.append(listResult)
                    # listResult = []
                
                print(dueRents)

                



                # print(findMonths)
                # return
                # for i in self.monthsList:
                #     print(f"PRINTING {i}")

                #     if self.monthsMap[str(i[0])] in findMonths:

                #         print("FoUND")
                #     else:
                #         print("Not Found")

                
                # print(paidMonths)



                # print(startMonthIndex)
                self.startYear = self.startYear + 1
                


            # print(j)
        
         
        
        
        self.tableshow(dueRents)

        conn.close()

    def findMonthRent(self,partyId):
        conn = sqlite3.connect("details.db")
        c = conn.cursor()
        c.execute("SELECT distinct rentMonth from rentledger where partyid = ?",(partyId,))
        result = c.fetchall()
        return result

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
                # if column_number==colCount -1: 
                #     # print(f"printing col number {column_number} {resLength}")
                #     item.setTextAlignment(Qt.AlignRight)
                self.tableWidget.setItem(row_number, column_number, item)
            self.progressBar.setValue(int(j*100/len(result)))
            
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)

        header.setSectionResizeMode(2,QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(3,QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(4,QtWidgets.QHeaderView.Stretch)
        # header.setSectionResizeMode(5,QtWidgets.QHeaderView.ResizeToContents)
        # header.setSectionResizeMode(7,QtWidgets.QHeaderView.ResizeToContents)
        credittot = debittot = running = 0

        # for i,j in enumerate(result):
        #     print(i,j)
        #     credittot = credittot+j[6]
        # self.label_27.setText('Rs. '+ str(credittot))
    
    def cellclick(self, row,column):
        id = self.tableWidget.item(row,0).text()
        trans = self.tableWidget.item(row,4).text()
        print(id,trans)
        if trans=='RECEIVE':
            self.main = Credit()
            self.main.show()
            self.main.clickload(id)
        elif trans=='BALANCEPAY':
            self.main = Pay()
            self.main.show()
            self.main.clickload(id)
        elif trans.startswith('PURCHASE'):
            self.main = Purchase()
            self.main.show()
            self.main.clickload(id)


    
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = DuePaidRent()
    sys.exit(app.exec_())
