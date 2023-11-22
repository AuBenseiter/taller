
from PIL import Image, ImageTk
import tkinter as tk
from App.Views.agendar_trabajos import AgendarTrabajos


class SupervisorView(tk.Toplevel):

    def __init__(self, master):
        super().__init__()
        self.title("Disiture Garage - Supervisor")
        self.config(bg='#F0F0F0', width=480, height=500)
        self.iconbitmap("DG.ico")

        # Construir la ruta al archivo de imagen
        # -Saludo
        self.saludoLabel = tk.Label(self, text="Bienvenido nuevamente Supervisor Fulano")
        self.saludoLabel.pack()

        # -Crear nuevos usuarios
        self.btnCrearUsuario = tk.Button(self, text="Administración de Usuarios", width=23, height=4)
        self.btnCrearUsuario.pack(side="left")

        self.btn_agendar_trabajos = tk.Button(self, text="Agendar Trabajos", width=23, height=4, command=self.show_abrir_agendar_trabajos)
        self.btn_agendar_trabajos.pack(side="left")

        # -Reloj control
        self.btnAsistencia = tk.Button(self, text="Administración de Asistencia", width=23, height=4)
        self.btnAsistencia.pack(side="left")

        # -cerrar sesión/Cambiar de vistas
        self.btnSalir = tk.Button(self, text="Salir de esta vista", width=23, height=4)
        self.btnSalir.pack(side="left")

        # -Imagen
        self.image = Image.open("disiture_logo.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.logoLabel = tk.Label(self, image=self.photo)  # Corregir esta línea
        self.logoLabel.pack()

    def show_abrir_agendar_trabajos(self):
        ag_trb_window = AgendarTrabajos()
        ag_trb_window.mainloop()

