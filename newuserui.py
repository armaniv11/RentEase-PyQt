# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newuser.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewUser(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(973, 532)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(400, 400))
        self.frame.setMaximumSize(QtCore.QSize(1677215, 1667215))
        self.frame.setStyleSheet("QFrame{background-color: rgb(85, 85, 255);\n"
"border:6px solid grey;}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("QFrame{\n"
"border:none;\n"
"padding:10px;\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Team meeting_Monochromatic.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setStyleSheet("QFrame{background-color: none;\n"
"padding:20px;\n"
"padding-bottom:20px;\n"
"border:none;}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_4.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_5.setStyleSheet("border:none;\n"
"border-radius:8px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 7, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("font: 12pt \"Arial Unicode MS\";\n"
"border-radius:8px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 6, 1, 1, 3)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_6.setStyleSheet("border:none;\n"
"margin-bottom:0px;\n"
"border-radius:8px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 6, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setStyleSheet("border:none;\n"
"border-radius:8px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 5, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_9.setMinimumSize(QtCore.QSize(35, 30))
        self.pushButton_9.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_9.setStyleSheet("\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"\n"
"font: 87 14pt \"Arial Black\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"background:none;\n"
"margin-right:5px;\n"
"\n"
"\n"
"}")
        self.pushButton_9.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../contra_new/Icons/minimizeicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QtCore.QSize(42, 42))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_4.addWidget(self.pushButton_9, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("font: 12pt \"Arial Unicode MS\";\n"
"border:none;\n"
"border-radius:8px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 5, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setMinimumSize(QtCore.QSize(0, 100))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label_2.setStyleSheet("font: 87 24pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"padding:0;\n"
"border:none;\n"
"background:none;\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 3, 0, 1, 4)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_7.setStyleSheet("border:none;\n"
"border-radius:8px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 8, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("font: 12pt \"Arial Unicode MS\";\n"
"border-radius:8px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 7, 1, 1, 3)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_8.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_8.setStyleSheet("\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"\n"
"font: 87 14pt \"Arial Black\";\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"background:none;\n"
"\n"
"\n"
"}")
        self.pushButton_8.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../contra_new/Icons/closeicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(36, 36))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 0, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("font: 12pt \"Arial Unicode MS\";\n"
"border-radius:8px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_4.addWidget(self.lineEdit_3, 8, 1, 1, 3)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 65))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_3.setStyleSheet("QPushButton{background-color: rgb(85, 170, 255);\n"
"    \n"
"    background-color: rgb(255, 0, 127);\n"
"border-radius:8px;\n"
"\n"
"padding:0px;\n"
"\n"
"font: 87 10pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"border-radius5px;}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 9, 0, 1, 4)
        self.gridLayout_4.setRowMinimumHeight(5, 1)
        self.gridLayout_4.setRowMinimumHeight(6, 1)
        self.gridLayout_4.setRowMinimumHeight(7, 1)
        self.gridLayout_4.setRowMinimumHeight(8, 1)
        self.gridLayout_4.setRowMinimumHeight(9, 1)
        self.gridLayout_2.addWidget(self.frame_8, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.lineEdit_5)
        Dialog.setTabOrder(self.lineEdit_5, self.lineEdit_2)
        Dialog.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Dialog.setTabOrder(self.lineEdit_3, self.pushButton_3)
        Dialog.setTabOrder(self.pushButton_3, self.pushButton_8)
        Dialog.setTabOrder(self.pushButton_8, self.pushButton_7)
        Dialog.setTabOrder(self.pushButton_7, self.pushButton_6)
        Dialog.setTabOrder(self.pushButton_6, self.pushButton_5)
        Dialog.setTabOrder(self.pushButton_5, self.pushButton_4)
        Dialog.setTabOrder(self.pushButton_4, self.pushButton_9)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "Password"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "New User !"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Confirm Password"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Master Password"))
        self.pushButton_3.setText(_translate("Dialog", "ADD USER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_NewUser()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
