from App.Views.calendario_personal import CalendarioPersonal


class AgendarTrabajosController:
    def __init__(self, master):
        self.master = master
        self.view = CalendarioPersonal(master)

