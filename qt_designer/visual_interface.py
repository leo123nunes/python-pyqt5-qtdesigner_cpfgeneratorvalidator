# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.linedit_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.linedit_cpf.setGeometry(QtCore.QRect(9, 21, 281, 25))
        self.linedit_cpf.setObjectName("linedit_cpf")
        self.btn_generate_cpf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate_cpf.setGeometry(QtCore.QRect(9, 64, 281, 25))
        self.btn_generate_cpf.setObjectName("btn_generate_cpf")
        self.btn_validate_cpf = QtWidgets.QPushButton(self.centralwidget)
        self.btn_validate_cpf.setGeometry(QtCore.QRect(9, 107, 281, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_validate_cpf.sizePolicy().hasHeightForWidth())
        self.btn_validate_cpf.setSizePolicy(sizePolicy)
        self.btn_validate_cpf.setObjectName("btn_validate_cpf")
        self.linedit_display = QtWidgets.QLineEdit(self.centralwidget)
        self.linedit_display.setGeometry(QtCore.QRect(9, 150, 281, 41))
        self.linedit_display.setObjectName("linedit_display")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_generate_cpf.setText(_translate("MainWindow", "Generate cpf"))
        self.btn_validate_cpf.setText(_translate("MainWindow", "Validate cpf"))
