from App.Views.ingeniero_view import IngenieroView


class IngenieroController:
    def __init__(self, master):
        self.master = master
        self.view = IngenieroView(master)

