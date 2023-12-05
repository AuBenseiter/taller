from PyQt5 import QtCore, QtGui, QtWidgets
class option_view(QtWidgets.QDialog):
    def setupUi(self, main_window):
        # Define el estilo del botón en una variable
        button_style = "QPushButton{\n" \
                       "    background-color: rgba(0, 0, 0,0%);\n" \
                       "    border-radius: 10px;\n" \
                       "    border: 2px solid rgb(44, 132, 132);\n" \
                       "}\n" \
                       "QPushButton:hover{\n" \
                       "    color: rgb(255, 255, 255);\n" \
                       "    background-color: rgba(18, 69, 89);\n" \
                       "}\n"
        main_window.setObjectName("MainWindow")
        main_window.resize(623, 417)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 200, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(button_style)
        self.pushButton.setObjectName("pushButton")
        #boton 2
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 200, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(button_style)  # Fix this line
        self.pushButton_2.setObjectName("pushButton_2")
        #boton 3
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 200, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(button_style)  # Fix this line
        self.pushButton_3.setObjectName("pushButton_3")
        #label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 50, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        #main_window.setCentralWidget(self.centralwidget) #esto es las ventanas principales
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 21))
        self.menubar.setObjectName("menubar")
        #main_window.setMenuBar(self.menubar) #esto es las ventanas principales
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        #main_window.setStatusBar(self.statusbar) #esto es las ventanas principales

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    # Traducir los textos de la interfaz
    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ingresar Trabajo"))
        self.pushButton_2.setText(_translate("MainWindow", "Bodega"))
        self.pushButton_3.setText(_translate("MainWindow", "Agregar Usuario"))
        self.label.setText(_translate("MainWindow", "Elija una opcion"))
