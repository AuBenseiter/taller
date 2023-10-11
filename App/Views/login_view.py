import tkinter as tk
from tkinter import simpledialog, messagebox

class LoginView(tk.Tk):
    def __init__(self, verificar_callback):
        super().__init__()
        self.title("Inicio de Sesión")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Ingrese sus credenciales:")
        self.label.pack(pady=20)

        self.username = ""
        self.password = ""

        tk.Label(self, text="Usuario:").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Contraseña:").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.verificar_callback = verificar_callback

        tk.Button(self, text="Iniciar Sesión", command=self.login).pack(pady=20)

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

        if self.username and self.password:
            self.verificar_callback(self.username, self.password)
            self.destroy()
        else:
            messagebox.showerror("Error", "Credenciales requeridas")
