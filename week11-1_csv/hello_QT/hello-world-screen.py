# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelloWorld.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HelloWorld(object):
    def setupUi(self, HelloWorld):
        HelloWorld.setObjectName("HelloWorld")
        HelloWorld.resize(722, 530)
        self.edit_inputname = QtWidgets.QLineEdit(HelloWorld)
        self.edit_inputname.setGeometry(QtCore.QRect(50, 90, 113, 20))
        self.edit_inputname.setObjectName("edit_inputname")
        self.btm_ok = QtWidgets.QPushButton(HelloWorld)
        self.btm_ok.setGeometry(QtCore.QRect(400, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btm_ok.setFont(font)
        self.btm_ok.setObjectName("btm_ok")
        self.labelresult = QtWidgets.QLabel(HelloWorld)
        self.labelresult.setGeometry(QtCore.QRect(70, 200, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelresult.setFont(font)
        self.labelresult.setObjectName("labelresult")
        self.label = QtWidgets.QLabel(HelloWorld)
        self.label.setGeometry(QtCore.QRect(50, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(HelloWorld)
        QtCore.QMetaObject.connectSlotsByName(HelloWorld)

        self.btm_ok.clicked.connect(self.button_pressed)

    def retranslateUi(self, HelloWorld):
        _translate = QtCore.QCoreApplication.translate
        HelloWorld.setWindowTitle(_translate("HelloWorld", "Dialog"))
        self.btm_ok.setText(_translate("HelloWorld", "ok"))
        self.labelresult.setText(_translate("HelloWorld", "x"))
        self.label.setText(_translate("HelloWorld", "Enter your name"))

    def button_pressed(self):

        self.labelresult.setText(self.edit_inputname.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelloWorld = QtWidgets.QDialog()
    ui = Ui_HelloWorld()
    ui.setupUi(HelloWorld)
    HelloWorld.show()
    sys.exit(app.exec_())
# this part will be generated when you input -x in the pyuic5 line
# in pycharm, right click the directory and choose open in terminal, input pyuic5 -x filename.ui > filename.py
