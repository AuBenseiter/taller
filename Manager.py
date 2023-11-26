import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

from App.Views.ingeniero_view import IngenieroView
from App.Views.login_view import LoginView
from App.Views.supervisor_view import SupervisorView
from App.Views.tecnico_view import TecnicoView


class ManagerView(QDialog):
    def setupUi(self, option_manager):
        option_manager.setObjectName("Dialog")
        option_manager.resize(588, 648)
        option_manager.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(option_manager)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(option_manager)
        self.frame.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(14, 149, 201, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border: 1px solid #003c5a;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 40, 91, 91))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./App/Images/logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.ingenieria = QtWidgets.QPushButton(self.frame)
        self.ingenieria.setGeometry(QtCore.QRect(160, 280, 281, 51))
        self.ingenieria.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ingenieria.setStyleSheet("QPushButton{\n"
"    background-color: rgba(0, 0, 0,0%);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(44, 132, 132);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(18, 69, 89);\n"
"}\n"
"\n"
"\n"
"")
        self.ingenieria.setDefault(False)
        self.ingenieria.setFlat(False)
        self.ingenieria.setObjectName("ingenieria")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(140, 190, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.supervisor = QtWidgets.QPushButton(self.frame)
        self.supervisor.setGeometry(QtCore.QRect(160, 470, 281, 51))
        self.supervisor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.supervisor.setStyleSheet("QPushButton{\n"
"    background-color: rgba(0, 0, 0,0%);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(44, 132, 132);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(18, 69, 89);\n"
"}")
        self.supervisor.setObjectName("supervisor")
        self.tecnico = QtWidgets.QPushButton(self.frame)
        self.tecnico.setGeometry(QtCore.QRect(160, 370, 281, 51))
        self.tecnico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tecnico.setStyleSheet("QPushButton{\n"
"    background-color: rgba(0, 0, 0,0%);\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(44, 132, 132);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgba(18, 69, 89);\n"
"}")
        self.tecnico.setObjectName("tecnico")
        self.salir = QtWidgets.QPushButton(self.frame)
        self.salir.setGeometry(QtCore.QRect(410, 570, 121, 41))
        self.salir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.salir.setStyleSheet("QPushButton{\n"
"    background-color: rgba(rgb(170, 58, 82));\n"
"    border-radius: 10px;\n"
"    border: 2px solid rgb(143, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(135, 0, 0);\n"
"}")
        self.salir.setObjectName("salir")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(option_manager)
        self.salir.clicked.connect(option_manager.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(option_manager)

        # Conecta los métodos de clic a los eventos de los botones
        self.ingenieria.clicked.connect(self.mostrar_ingeneria)
        self.tecnico.clicked.connect(self.mostrar_tecnico)
        self.supervisor.clicked.connect(self.mostrar_supervisor)
        self.salir.clicked.connect(option_manager.close)

    def mostrar_ingeneria(self):
        try:
            print("llamando a la vista de login")
            time.sleep(1)
            self.login_view = LoginView(None, self.mostrar_ingeneria_post_login)
            self.login_view.setModal(True)
            self.login_view.finished.connect(self.login_view.close)
            self.login_view.exec_()
        except Exception as e:
            print("No se pudo llamar a la vista login")
            print(f"Error en mostrar_ingeneria: {str(e)}")

    def mostrar_tecnico(self):
        try:
            login_view = LoginView(self, self.mostrar_tecnico_post_login)
            result = login_view.show()
            if result == QDialog.Accepted:
                # La función callback se llama desde el diálogo de inicio de sesión si las credenciales son correctas
                pass  # No es necesario hacer nada aquí, ya que la función callback se encargará de mostrar TecnicoView
        except Exception as e:
            print(f"Error en mostrar_tecnico: {str(e)}")

    def mostrar_supervisor(self):
        try:
            login_view = LoginView(self, self.mostrar_supervisor_post_login)
            result = login_view.show()
            if result == QDialog.Accepted:
                # La función callback se llama desde el diálogo de inicio de sesión si las credenciales son correctas
                pass  # No es necesario hacer nada aquí, ya que la función callback se encargará de mostrar SupervisorView
        except Exception as e:
            print(f"Error en mostrar_supervisor: {str(e)}")

    def mostrar_ingeneria_post_login(self):
        ingeniero_dialog = IngenieroView(self)
        ingeniero_dialog.setupUi(ingeniero_dialog)
        ingeniero_dialog.exec_()
        self.login_view.close()  # Cerrar la ventana de login  # Cerrar la ventana de login

    def mostrar_tecnico_post_login(self):
        tecnico_view = TecnicoView(self)
        tecnico_view.exec_()
        self.close()  # Cerrar la ventana de login

    def mostrar_supervisor_post_login(self):
        supervisor_view = SupervisorView(self)
        supervisor_view.exec_()
        self.close()  # Cerrar la ventana de login

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ingenieria.setText(_translate("Dialog", "Ingenieria"))
        self.label_2.setText(_translate("Dialog", "Selecciona una Opcion"))
        self.supervisor.setText(_translate("Dialog", "Supervisor"))
        self.tecnico.setText(_translate("Dialog", "Tecnico"))
        self.salir.setText(_translate("Dialog", "SALIR"))
