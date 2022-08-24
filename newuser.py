from PyQt5.QtWidgets import QApplication, QDial, QDialog, QMainWindow, QMessageBox, QShortcut

# from dashboard import Dashboard
# from userprofile import UserProfile
from newuserui import Ui_NewUser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor,QKeySequence
from PyQt5.QtCore import QPoint
import sqlite3
from datetime import datetime
import sys
import platform
class NewUser(QDialog,Ui_NewUser):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui=Ui_NewUser()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        effect = QtWidgets.QGraphicsDropShadowEffect(self.frame)
        effect.setOffset(0, 0)
        effect.setBlurRadius(20)
        effect.setColor(QColor('black'))
        self.frame.setGraphicsEffect(effect)
        self.pushButton_8.clicked.connect(lambda:self.close())
        # self.pushButton_2.clicked.connect(self.createuser)
        self.databasename = ''
        screen_width = QtWidgets.QDesktopWidget().screenGeometry().width()
        screen_height = QtWidgets.QDesktopWidget().screenGeometry().height()

        self.blockwidth = int(screen_width * 0.7)
        self.blockheight = int(screen_height*0.7)
        self.frame.setMinimumSize(QtCore.QSize(self.blockwidth, self.blockheight))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.textEdited.connect(lambda:self.auto_capital(self.lineEdit))
        self.lineEdit_2.textEdited.connect(lambda:self.auto_capital(self.lineEdit_2))
        self.lineEdit_3.textEdited.connect(lambda:self.auto_capital(self.lineEdit_3))
        self.lineEdit_5.textEdited.connect(lambda:self.auto_capital(self.lineEdit_5))
        self.esckey = QShortcut(QKeySequence('esc'), self)
        self.esckey.activated.connect(lambda:self.close())
        self.pushButton_3.clicked.connect(self.createuser)
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

    def createuser(self):
        username = self.lineEdit.text()
        password = self.lineEdit_5.text()
        confirm = self.lineEdit_2.text()
        master = self.lineEdit_3.text()
        added = datetime.now()
        if username=='':
            QMessageBox.warning(self,'Alert!','Please Provide Username!')
        elif password=='':
            QMessageBox.warning(self,'Alert!','Please Provide Password!')
        elif master!='12345678':
            QMessageBox.warning(self,'Alert!','Incorrect Master Password!')
        elif password!=confirm:
            QMessageBox.warning(self,'Alert!','Passwords do not match!')
        else:
            conn = sqlite3.connect('details.db')

            conn.execute("INSERT into loginusers(user,pass,added) values (?,?,?)",(username,password,added))
            conn.commit()
            QMessageBox.about(self,'Success',f'New User with username {username} has been created successfully!')
            self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    app.setStyle('Fusion')
    window=NewUser()
    sys.exit(app.exec_())
