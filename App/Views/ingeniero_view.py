from PyQt5 import QtCore, QtGui, QtWidgets
from App.Views.options_view import option_view

class IngenieroView(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self, *args, **kwargs):
        try:
            # Tu código de inicialización de la interfaz aquí

            # Crear una instancia de OptionView
            self.option_view_instance = option_view()
            # Llamar a la función setupUi de option_view
            self.option_view_instance.setupUi(self)

            # Ahora puedes acceder a los elementos de option_view como atributos de self.option_view_instance
            self.option_view_instance.pushButton.clicked.connect(self.ingresar_trabajo)
            self.option_view_instance.pushButton_2.clicked.connect(self.mostrar_bodega)
            self.option_view_instance.pushButton_3.clicked.connect(self.agregar_usuario)
        except Exception as e:
            print(f"Error en setupUi de IngenieroView: {str(e)}")

    def ingresar_trabajo(self):
        try:
            print("Botón 'Ingresar Trabajo' presionado")
            # Aquí va el código para 'Ingresar Trabajo'
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

    # Otros métodos y funciones según sea necesario
