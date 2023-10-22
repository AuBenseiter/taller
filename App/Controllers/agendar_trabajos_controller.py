from App.Views.agendar_trabajos import AgendarTrabajos


class AgendarTrabajosController:
    def __init__(self, master):
        self.master = master
        self.view = AgendarTrabajos(master)

