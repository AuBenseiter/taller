from App.Models.usuario_model import UsuarioModel

class TecnicoModel(UsuarioModel):
    def __init__(self, username, password):
        super().__init__(username, password)