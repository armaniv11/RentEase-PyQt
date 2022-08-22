# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'due_paid_rent.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DuePaidRent(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1403, 679)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(-1, -1, 4, 4)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("QFrame{background-color: rgb(255, 255, 255);\n"
"border:1px solid black;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_3.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 85, 127);\n"
"border:2px solig grey;\n"
"border-radius:8;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(4, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_13.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_13.setMaximumSize(QtCore.QSize(1677315, 16777215))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 130, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Arial Black\";\n"
"border:2px solid grey;}\n"
"QPushButton:hover{\n"
"background-color: rgb(88, 88, 88);\n"
"border:2px solid white;}\n"
"\n"
"\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_5.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_5.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 85, 127);\n"
"border:2px solig grey;\n"
"border-radius:8;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(4, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 85, 127);\n"
"border:2px solig grey;\n"
"border-radius:8;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(4, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(0, 45))
        self.label_6.setStyleSheet("background-color: rgb(52, 167, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_27 = QtWidgets.QLabel(self.frame_4)
        self.label_27.setMinimumSize(QtCore.QSize(0, 50))
        self.label_27.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.label_27.setText("")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout.addWidget(self.label_27)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_2.addWidget(self.frame_4, 4, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 212, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 113, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.tableWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("\n"
"color: rgb(0, 0, 0);\n"
"alternate-background-color: rgb(240, 240, 240);\n"
"border:none;")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(29)
        self.tableWidget.verticalHeader().setMinimumSectionSize(26)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 1, 4, 3)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 85, 127);\n"
"border:2px solig grey;\n"
"border-radius:8;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(4, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 45))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 85, 127);\n"
"font: 75 12pt \"Arial Narrow\";\n"
"selection-background-color: rgb(85, 85, 127);\n"
"selection-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 130, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Arial Black\";\n"
"border:2px solid grey;}\n"
"QPushButton:hover{\n"
"background-color: rgb(88, 88, 88);\n"
"border:2px solid white;}\n"
"\n"
"\n"
"")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_4.addWidget(self.pushButton_14)
        self.gridLayout_2.addWidget(self.frame_6, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("border:none;\n"
"color: rgb(91, 91, 91);\n"
"font: 87 16pt \"Arial Black\";\n"
"padding-left:20;\n"
"")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 130, 80);\n"
"color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Arial Black\";\n"
"border:2px solid grey;}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 127);\n"
"border:2px solid white;}")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(400, 45))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_14.setStyleSheet("font: 75 11pt \"Tahoma\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(76, 76, 76);\n"
"border:2px solid grey;\n"
"border-radius:0;")
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setClearButtonEnabled(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_2.addWidget(self.lineEdit_14, 0, 2, 1, 1)
        self.label.raise_()
        self.frame_4.raise_()
        self.tableWidget.raise_()
        self.frame_3.raise_()
        self.pushButton.raise_()
        self.frame_5.raise_()
        self.lineEdit_14.raise_()
        self.frame_6.raise_()
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_13.setText(_translate("Dialog", "DUE RENTS THIS MONTH"))
        self.pushButton_8.setText(_translate("Dialog", "PRINT"))
        self.pushButton_9.setText(_translate("Dialog", "EXPORT"))
        self.label_6.setText(_translate("Dialog", "Total"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "TENANT"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "DUE MONTH"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "RENT AMT."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "RENT HISTORY"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.comboBox.setItemText(0, _translate("Dialog", "JANUARY"))
        self.comboBox.setItemText(1, _translate("Dialog", "FEBRUARY"))
        self.comboBox.setItemText(2, _translate("Dialog", "MARCH"))
        self.comboBox.setItemText(3, _translate("Dialog", "APRIL"))
        self.comboBox.setItemText(4, _translate("Dialog", "MAY"))
        self.comboBox.setItemText(5, _translate("Dialog", "JUNE"))
        self.comboBox.setItemText(6, _translate("Dialog", "JULY"))
        self.comboBox.setItemText(7, _translate("Dialog", "AUGUST"))
        self.comboBox.setItemText(8, _translate("Dialog", "SEPTEMBER"))
        self.comboBox.setItemText(9, _translate("Dialog", "OCTOBER"))
        self.comboBox.setItemText(10, _translate("Dialog", "NOVEMBER"))
        self.comboBox.setItemText(11, _translate("Dialog", "DECEMBER"))
        self.pushButton_14.setText(_translate("Dialog", "SEARCH"))
        self.label.setText(_translate("Dialog", "DUE RENTS"))
        self.pushButton.setText(_translate("Dialog", "X"))
        self.lineEdit_14.setPlaceholderText(_translate("Dialog", "Search Here"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DuePaidRent()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
