import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from App.Controllers.ingeniero_controller import IngenieroController
from App.Controllers.supervisor_controller import SupervisorController
from App.Controllers.tecnico_controller import TecnicoController
from App.Credentials.static_credentials import StaticCredentials
from App.Views.login_view import LoginView


class InicioView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pantalla de Inicio")
        self.geometry("400x500")

        self.iconbitmap("DG.ico")

        self.image = Image.open("disiture_logo.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.logoLabel = tk.Label(self, image=self.photo)  # Corregir esta línea
        self.logoLabel.pack()

        self.image2 = Image.open("garege_logo.png")
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.logoLabel = tk.Label(self, image=self.photo2)  # Corregir esta línea
        self.logoLabel.pack()


        self.label = tk.Label(self, text="Seleccione su rol:")
        self.label.pack(pady=20)

        self.roles = ["Supervisor", "Técnico", "Ingeniero"]
        self.selected_role = tk.StringVar()
        self.selected_role.set(self.roles[0])

        for role in self.roles:
            tk.Radiobutton(self, text=role, variable=self.selected_role, value=role).pack()

        tk.Button(self, text="Ingresar", command=self.show_login_window).pack(pady=20)

    def show_login_window(self):
        selected_role = self.selected_role.get()

        def verificar_login(username, password):
            credentials = StaticCredentials.get_credentials(username)

            if credentials and credentials == password:
                if selected_role == "Supervisor":
                    SupervisorController(self.master)

                elif selected_role == "Técnico":
                    TecnicoController(self.master)
                elif selected_role == "Ingeniero":
                    IngenieroController(self.master)
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
        login_window = LoginView(verificar_login)
        login_window.mainloop()