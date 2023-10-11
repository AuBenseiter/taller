from App.Views.tecnico_view import TecnicoView

class TecnicoController:
    def __init__(self, master):
        self.master = master
        self.view = TecnicoView(master)
