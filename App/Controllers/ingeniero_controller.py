import time
from PyQt5.QtCore import QObject

from App.Views.calendario_view import CalendarioView
from App.Views.ingeniero_view import IngenieroView

class IngenieroController(QObject):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.view = IngenieroView(master)

        # Conectar señales y ranuras
        self.view.ingresar_trabajo_signal.connect(self.ingresar_trabajo)
        self.view.mostrar_bodega_signal.connect(self.mostrar_bodega)
        self.view.agregar_usuario_signal.connect(self.agregar_usuario)

    def ingresar_trabajo(self):
        try:
            print("Botón 'Ingresar Trabajo' presionado")
            time.sleep(1)
            print("Llamando a CalendarioView")
            time.sleep(1)
            calendario_dialog = CalendarioView()
            calendario_dialog.setupUi(calendario_dialog)
            calendario_dialog.exec_()
        except Exception as e:
            print(f"Error al procesar 'Ingresar Trabajo': {str(e)}")

    def mostrar_bodega(self):
        try:
            print("Botón 'Bodega' presionado")
            # Aquí va el código para 'Mostrar Bodega'
        except Exception as e:
            print(f"Error al procesar 'Mostrar Bodega': {str(e)}")

    def agregar_usuario(self):
        try:
            print("Botón 'Agregar Usuario' presionado")
            # Aquí va el código para 'Agregar Usuario'
        except Exception as e:
            print(f"Error al procesar 'Agregar Usuario': {str(e)}")

