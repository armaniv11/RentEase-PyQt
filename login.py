

from dashboard import Dashboard
# from userprofile import UserProfile
from loginui import Ui_Login
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
import sqlite3
from datetime import datetime
import qtawesome
import sys
class Login(QDialog,Ui_Login):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui=Ui_Login()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        effect = QtWidgets.QGraphicsDropShadowEffect(self.frame)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        effect.setColor(QColor('white'))
        self.frame.setGraphicsEffect(effect)
        self.pushButton_6.clicked.connect(lambda:self.close())
        self.pushButton_3.clicked.connect(self.checkcredentials)
        self.esckey = QShortcut(QKeySequence('esc'), self)
        self.esckey.activated.connect(lambda:self.close())
        screen_width = QtWidgets.QDesktopWidget().screenGeometry().width()
        screen_height = QtWidgets.QDesktopWidget().screenGeometry().height()

        self.blockwidth = int(screen_width *0.7)
        self.blockheight = int(screen_height * 0.8)
        self.frame.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        
        # self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.textEdited.connect(lambda:self.auto_capital(self.lineEdit))
        self.lineEdit_2.textEdited.connect(lambda:self.auto_capital(self.lineEdit_2))
        #self.label_2.setText('ashu')
        self.show()
        self.oldPos = self.pos()

    def auto_capital(self,line_edit_object):
        # edit=line_edit_object
        text=line_edit_object.text()
        line_edit_object.setText(text.upper())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def checkcredentials(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        added = datetime.now().strftime("%y/%m/%d %H:%M")
        con=sqlite3.connect("details.db")
        cur=con.cursor()
        cur.execute("select * from loginusers")
        if len(cur.fetchall()) == 0:
            try:
                con.execute("INSERT INTO loginhistory(lastlogin,user) values (?,?)",(added,'Demo User'))
                con.commit()
            except Exception:
                QMessageBox.warning(self,'Alert!',"Problem with user! Contact Admin.")


            self.main=Dashboard()
            self.main.label_2.setText('Hi! Demo User')
            self.main.show()
            self.close()


        elif username=='':
            return QMessageBox.warning(self,'Alert!','Please provide Username!')
        elif password=='':
            return QMessageBox.warning(self,'Alert!','Please provide Password!')
        else:
            con=sqlite3.connect("details.db")
            cur=con.cursor()
            cur.execute("select * from loginusers where user=? and pass=?",(username,password))
            if len(cur.fetchall()) >0:
                # self.main.label_3.setText('Welcome! '+username.upper())
                cur.execute("SELECT lastlogin from loginhistory where user=? order by rowid desc limit 1",(username,))
                result = cur.fetchall()
                try:
                    lastlogin = str(result[0][0])
                except Exception:
                    lastlogin = ''


                # cursor = con.cursor()
                con.execute("INSERT INTO loginhistory(lastlogin,user) values (?,?)",(added,username))
                con.commit()
                self.close()


                self.main=Dashboard()
                self.main.label_2.setText('Welcome! '+username.upper())
                self.main.label_3.setText('Current Login: '+added)
                self.main.label_5.setText('Last Login: '+lastlogin)



                self.main.show()

            else:
                QMessageBox.warning(self, 'Error', 'Invalid Credentials!!')


            con.close()




    

if __name__ == "__main__":
    app=QApplication(sys.argv)
    app.setStyle('Fusion')
    window=Login()
    sys.exit(app.exec_())
