# Credentials/static_credentials.py
class StaticCredentials:
    @staticmethod
    def get_credentials(username):
        # Aquí puedes definir las credenciales estáticas para diferentes roles
        if username == "qwe":
            return "qwe"
        elif username == "tecnico":
            return "tecnico_password"
        elif username == "ingeniero":
            return "ingeniero_password"
        else:
            return None