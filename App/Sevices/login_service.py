class LoginService:
    @staticmethod
    def obtener_credenciales_usuario(username):
        try:
            # Aquí puedes agregar la lógica para obtener las credenciales de un usuario desde la base de datos
            # Por ahora, estamos usando credenciales estáticas como ejemplo
            credenciales_db = {
                "usuario": "usuario",
                "contrasenha": "usuario"
                # Aquí podrías tener más información, como roles, etc.
            }

            return credenciales_db
        except Exception as e:
            print(f"Error al obtener las credenciales: {str(e)}")
            return None
