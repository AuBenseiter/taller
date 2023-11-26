from App.Views.supervisor_view import SupervisorView


class SupervisorController:
    def __init__(self, master):
        self.master = master
        self.view = SupervisorView(master)
