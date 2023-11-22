import tkinter as tk
from App.Views.agendar_trabajos import AgendarTrabajos


class SupervisorView(tk.Toplevel):

    def __init__(self, master):
        super().__init__()
        self.title("Disiture Garage - Supervisor")
        self.config(bg='#F0F0F0', width=480, height=500)
        #self.iconbitmap("DG.ico")

        # Construir la ruta al archivo de imagen


        self.saludoLabel = tk.Label(self, text="Bienvenido nuevamente Supervisor Fulano")
        self.saludoLabel.grid(row=1, column=0 )

        # -Crear nuevos usuarios
        self.btnCrearUsuario = tk.Button(self, text="Administración de Usuarios", width=23, height=4)
        self.btnCrearUsuario.grid(row=2, column=0, padx=25, pady=25)

        self.btn_agendar_trabajos = tk.Button(self, text="Agendar Trabajos", width=23, height=4, command=self.show_abrir_agendar_trabajos)
        self.btn_agendar_trabajos.grid(row=2, column=1, padx=25, pady=25)

        # -Reloj control
        self.btnAsistencia = tk.Button(self, text="Administración de Asistencia", width=23, height=4)
        self.btnAsistencia.grid(row=3, column=0, padx=25, pady=25)

        # -cerrar sesión/Cambiar de vistas
        self.btnSalir = tk.Button(self, text="Salir de esta vista", width=23, height=4)
        self.btnSalir.grid(row=3, column=1, padx=25, pady=25)

    def show_abrir_agendar_trabajos(self):

        ag_trb_window = AgendarTrabajos()
        ag_trb_window.mainloop()