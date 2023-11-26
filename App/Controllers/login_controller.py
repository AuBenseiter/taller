import time

from App.Models.login_model import LoginModel
from App.Sevices.login_service import LoginService


class LoginController:
    @staticmethod
    def iniciar_sesion(username, password):
        time.sleep(1)
        credenciales = LoginService.obtener_credenciales_usuario(username)
        print("Llamando a LoginService")
        time.sleep(1)
        print("Llamando a LoginModel")
        time.sleep(1)
        print("Comparando credenciales introducidas con credenciales de la base de datos")
        time.sleep(1)

        if credenciales and LoginModel.verificar_credenciales(username, password, credenciales):
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Inicio de sesión fallido.")
            return False

