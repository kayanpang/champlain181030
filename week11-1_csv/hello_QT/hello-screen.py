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
        self.btm_ok.setGeometry(QtCore.QRect(400, 250, 75, 23))
        self.btm_ok.setObjectName("btm_ok")
        self.labelresult = QtWidgets.QLabel(HelloWorld)
        self.labelresult.setGeometry(QtCore.QRect(70, 200, 101, 51))
        self.labelresult.setObjectName("labelresult")
        self.label = QtWidgets.QLabel(HelloWorld)
        self.label.setGeometry(QtCore.QRect(50, 40, 161, 31))
        self.label.setObjectName("label")

        self.retranslateUi(HelloWorld)
        QtCore.QMetaObject.connectSlotsByName(HelloWorld)

    def retranslateUi(self, HelloWorld):
        _translate = QtCore.QCoreApplication.translate
        HelloWorld.setWindowTitle(_translate("HelloWorld", "Dialog"))
        self.btm_ok.setText(_translate("HelloWorld", "ok"))
        self.labelresult.setText(_translate("HelloWorld", "<html><head/><body><p><span style=\" font-size:12pt;\">x</span></p></body></html>"))
        self.label.setText(_translate("HelloWorld", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter your name</span></p></body></html>"))

    def button_pressed(self):
        self.label_result.setText(self.edit_inputname.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HelloWorld = QtWidgets.QDialog()
    ui = Ui_HelloWorld()
    ui.setupUi(HelloWorld)
    HelloWorld.show()
    sys.exit(app.exec_())

