from PyQt5 import QtCore, QtGui, QtWidgets
class IngenieroView(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(966, 835)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(80, 90, 801, 271))
        self.calendarWidget.setObjectName("calendarWidget")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(80, 490, 801, 241))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(630, 750, 251, 31))
        self.pushButton.setStyleSheet("border-radius: 15px;\n"
"background-color:rgb(137, 206, 206);\n"
"color: white;\n"
"font: 16px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 410, 161, 51))
        self.pushButton_2.setStyleSheet("border-radius: 20px;\n"
"background-color:rgb(137, 206, 206);\n"
"color: white;\n"
"font: 16px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(180, 10, 631, 61))
        self.label.setStyleSheet("font-size: 24pt;\n"
"background: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid;")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Guardar Cambios"))
        self.pushButton_2.setText(_translate("Dialog", "Añadir Nueva Tarea"))
        self.label.setText(_translate("Dialog", "TAREAS"))
