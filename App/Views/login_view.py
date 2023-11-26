import time

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog

from App.Controllers.login_controller import LoginController
from App.Sevices.login_service import LoginService


class LoginView(QDialog,QtWidgets.QWidget):
    def __init__(self, parent=None, callback=None):
        super(LoginView, self).__init__(parent)

        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 400, 200)

        layout = QtWidgets.QVBoxLayout()

        self.label_username = QtWidgets.QLabel("Usuario:")
        self.edit_username = QtWidgets.QLineEdit(self)

        self.label_password = QtWidgets.QLabel("Contraseña:")
        self.edit_password = QtWidgets.QLineEdit(self)
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.button_login = QtWidgets.QPushButton("Iniciar Sesión", self)
        self.button_login.clicked.connect(self.iniciar_sesion)

        layout.addWidget(self.label_username)
        layout.addWidget(self.edit_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.edit_password)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

        # Almacenar el callback proporcionado
        self.callback = callback

    def iniciar_sesion(self):
        # Llamar al controlador para iniciar sesión
        username = self.edit_username.text()
        password = self.edit_password.text()
        inicio: str = "Inicio de sesión."
        inicio_exitoso: str = "Inicio de sesión exitoso."
        time.sleep(1)
        print("Llamando a LoginController")
        time.sleep(1)
        if LoginController.iniciar_sesion(username, password):
            QtWidgets.QMessageBox.information(self, inicio, inicio_exitoso)
            # Llamar al callback si está definido
            if self.callback:
                self.callback()
        else:
            QtWidgets.QMessageBox.warning(self, inicio, inicio_exitoso)