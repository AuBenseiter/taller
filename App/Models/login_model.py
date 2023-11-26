class LoginModel:
    @staticmethod
    def verificar_credenciales(username, password, credenciales_db):
        """
        Verifica las credenciales del usuario.

        :param username: Nombre de usuario ingresado.
        :param password: Contraseña ingresada.
        :param credenciales_db: Credenciales almacenadas en la base de datos.
        :return: True si las credenciales son correctas, False en caso contrario.
        """
        stored_username = credenciales_db.get("usuario")
        stored_password = credenciales_db.get("contrasenha")

        return username == stored_username and password == stored_password