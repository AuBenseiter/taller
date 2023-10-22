import unittest
import tkinter as tk
from tkcalendar import Calendar
from App.Views.agendar_trabajos import *
# Asegúrate de que la ruta sea correcta



class TestAgendarTrabajos(unittest.TestCase):




    # FalloFalloFalloFalloFalloFalloFalloFalloFalloFalloFalloFalloFalloFalloFalloFallo

    def test_agregar_trabajo_datos_validos(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Llenar los campos con datos válidos (puedes ajustar los valores según lo necesites)
        app.marca_entry.insert(0, "Toyota")
        app.modelo_entry.insert(0, "Camry")
        app.ano_entry.insert(0, "2022")
        app.patente_entry.insert(0, "ABC123")
        app.nombre_cliente_entry.insert(0, "Juan Pérez")
        app.tipo_trabajo_var.set("Cambio de aceite y filtro")  # Seleccionar un tipo de trabajo válido

        # Agregar trabajo
        app.agregar_button.invoke()

        # Verificar que el trabajo se haya agregado a la lista
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        trabajo_agregado = f"Marca: Toyota, Modelo: Camry, Año: 2022, Patente: ABC123, Nombre Cliente: Juan Pérez, Tipo Trabajo: Cambio de aceite y filtro,"
        self.assertIn(trabajo_agregado, lista_trabajos)
    def test_seleccionar_fecha_calendario(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Establecer una fecha en el calendario
        fecha_seleccionada = "2023-12-31"
        app.fecha_cal.set_date(fecha_seleccionada)

        # Obtener la fecha seleccionada del calendario
        fecha_calendario = app.fecha_cal.get_date()

        # Verificar que la fecha seleccionada coincide con la fecha establecida
        self.assertEqual(fecha_calendario, fecha_seleccionada)
    def test_verificar_trabajos_en_lista(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Datos de varios trabajos
        trabajos = [
            {
                "marca": "Toyota",
                "modelo": "Camry",
                "ano": "2022",
                "patente": "ABC123",
                "nombre_cliente": "Juan Pérez",
                "tipo_trabajo": "Cambio de aceite y filtro",
                "fecha": "2023-01-15",
                "comentarios": "Trabajo 1"
            },
            {
                "marca": "Honda",
                "modelo": "Civic",
                "ano": "2021",
                "patente": "XYZ789",
                "nombre_cliente": "María López",
                "tipo_trabajo": "Cambio de neumáticos",
                "fecha": "2023-02-20",
                "comentarios": "Trabajo 2"
            }
        ]

        # Agregar los trabajos a la lista
        for trabajo in trabajos:
            app.marca_entry.insert(0, trabajo["marca"])
            app.modelo_entry.insert(0, trabajo["modelo"])
            app.ano_entry.insert(0, trabajo["ano"])
            app.patente_entry.insert(0, trabajo["patente"])
            app.nombre_cliente_entry.insert(0, trabajo["nombre_cliente"])
            app.tipo_trabajo_var.set(trabajo["tipo_trabajo"])
            app.fecha_cal.set_date(trabajo["fecha"])
            app.comentarios_text.insert(tk.END, trabajo["comentarios"])
            app.agregar_button.invoke()

        # Verificar que los trabajos se hayan agregado a la lista
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        for trabajo in trabajos:
            trabajo_agregado = f"Marca: {trabajo['marca']}, Modelo: {trabajo['modelo']}, Año: {trabajo['ano']}, Patente: {trabajo['patente']}, Nombre Cliente: {trabajo['nombre_cliente']}, Tipo Trabajo: {trabajo['tipo_trabajo']}, Comentarios: {trabajo['comentarios']}, Fecha: {trabajo['fecha']}"
            self.assertIn(trabajo_agregado, lista_trabajos)

        # Cerrar la ventana principal
        app.destroy()
    def test_eliminar_trabajo_de_lista(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Datos de trabajo a eliminar
        trabajo_a_eliminar = {
            "marca": "Toyota",
            "modelo": "Camry",
            "ano": "2022",
            "patente": "ABC123",
            "nombre_cliente": "Juan Pérez",
            "tipo_trabajo": "Cambio de aceite y filtro",
            "fecha": "2023-01-15",
            "comentarios": "Trabajo a eliminar"
        }

        # Llenar los campos con los datos del trabajo a eliminar
        app.marca_entry.insert(0, trabajo_a_eliminar["marca"])
        app.modelo_entry.insert(0, trabajo_a_eliminar["modelo"])
        app.ano_entry.insert(0, trabajo_a_eliminar["ano"])
        app.patente_entry.insert(0, trabajo_a_eliminar["patente"])
        app.nombre_cliente_entry.insert(0, trabajo_a_eliminar["nombre_cliente"])
        app.tipo_trabajo_var.set(trabajo_a_eliminar["tipo_trabajo"])
        app.fecha_cal.set_date(trabajo_a_eliminar["fecha"])
        app.comentarios_text.insert(tk.END, trabajo_a_eliminar["comentarios"])

        # Agregar el trabajo a la lista
        app.agregar_button.invoke()

        # Verificar que el trabajo se haya agregado a la lista
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        trabajo_agregado = f"Marca: {trabajo_a_eliminar['marca']}, Modelo: {trabajo_a_eliminar['modelo']}, Año: {trabajo_a_eliminar['ano']}, Patente: {trabajo_a_eliminar['patente']}, Nombre Cliente: {trabajo_a_eliminar['nombre_cliente']}, Tipo Trabajo: {trabajo_a_eliminar['tipo_trabajo']}, Comentarios: {trabajo_a_eliminar['comentarios']}, Fecha: {trabajo_a_eliminar['fecha']}"
        self.assertIn(trabajo_agregado, lista_trabajos)

        # Eliminar el trabajo de la lista
        app.lista_trabajos.select_set(0)  # Seleccionar el primer trabajo en la lista
        app.eliminar_button.invoke()

        # Verificar que el trabajo haya sido eliminado de la lista
        lista_trabajos_actualizada = app.lista_trabajos.get(0, tk.END)
        self.assertNotIn(trabajo_agregado, lista_trabajos_actualizada)

        # Cerrar la ventana principal
        app.destroy()



    # AprobadaAprobadaAprobadaAprobadaAprobadaAprobadaAprobadaAprobadaAprobadaAprobada
    def test_interfaz_apertura(self):
        app = AgendarTrabajos()

        # Verificar que la ventana principal se abra con éxito
        self.assertTrue(app.winfo_exists())  # Verifica que la ventana exista
        self.assertEqual(app.title(), "Sistema de Agendamiento de Trabajos")  # Verifica el título de la ventana
    def test_interfaz_etiquetas(self):
        app = AgendarTrabajos()  # Crea una instancia de la aplicación

        # Verifica que las etiquetas se muestren correctamente
        self.assertTrue(app.winfo_exists())  # Verifica que la ventana exista
        self.assertEqual(app.title(), "Sistema de Agendamiento de Trabajos")  # Verifica el título de la ventana

        # Comprueba el contenido de etiquetas específicas
        marca_label = app.marca_label.cget("text")  # Obtiene el texto de la etiqueta de "Marca"
        self.assertEqual(marca_label, "Marca:")

        modelo_label = app.modelo_label.cget("text")  # Obtiene el texto de la etiqueta de "Modelo"
        self.assertEqual(modelo_label, "Modelo:")

        ano_label = app.ano_label.cget("text")  # Obtiene el texto de la etiqueta de "Año"
        self.assertEqual(ano_label, "Año:")

        patente_label = app.patente_label.cget("text")  # Obtiene el texto de la etiqueta de "Patente"
        self.assertEqual(patente_label, "Patente:")

        nombre_cliente_label = app.nombre_cliente_label.cget("text")  # Obtiene el texto de la etiqueta de "Nombre Cliente"
        self.assertEqual(nombre_cliente_label, "Nombre Cliente:")

        tipo_trabajo_label = app.tipo_trabajo_label.cget("text")  # Obtiene el texto de la etiqueta de "Tipo de Trabajo"
        self.assertEqual(tipo_trabajo_label, "Tipo de Trabajo:")
    def test_interfaz_campos_vacios(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Verificar que los campos de entrada estén inicialmente vacíos
        self.assertEqual(app.marca_entry.get(), "")  # Verificar el campo de "Marca"
        self.assertEqual(app.modelo_entry.get(), "")  # Verificar el campo de "Modelo"
        self.assertEqual(app.ano_entry.get(), "")  # Verificar el campo de "Año"
        self.assertEqual(app.patente_entry.get(), "")  # Verificar el campo de "Patente"
        self.assertEqual(app.nombre_cliente_entry.get(), "")  # Verificar el campo de "Nombre Cliente"
    def test_interfaz_menu_desplegable(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Verificar que el menú desplegable "Tipo de Trabajo" esté presente
        self.assertTrue(app.tipo_trabajo_menu.winfo_exists())

        # Verificar el valor inicial del menú desplegable
        self.assertEqual(app.tipo_trabajo_var.get(), "Ingrese trabajo a realizar")  # Verificar que sea el valor esperado
    def test_interfaz_boton_agregar(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Verificar que el botón "Agregar Trabajo" esté presente
        self.assertTrue(app.agregar_button.winfo_exists())

        # Verificar que el botón tenga el texto correcto
        self.assertEqual(app.agregar_button.cget("text"), "Agregar Trabajo")  # Verificar que el texto sea el esperado
    def test_agregar_trabajo_falta_datos(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Dejar campos de entrada en blanco (simulando datos incompletos)
        app.marca_entry.insert(0, "Toyota")
        app.modelo_entry.insert(0, "")  # Dejar el campo "Modelo" en blanco
        app.ano_entry.insert(0, "2022")
        app.patente_entry.insert(0, "ABC123")
        app.nombre_cliente_entry.insert(0, "Juan Pérez")
        app.tipo_trabajo_var.set("Cambio de aceite y filtro")  # Seleccionar un tipo de trabajo válido

        # Agregar trabajo
        app.agregar_button.invoke()

        # Verificar que el trabajo no se haya agregado a la lista
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        trabajo_agregado = f"Marca: Toyota, Modelo: , Año: 2022, Patente: ABC123, Nombre Cliente: Juan Pérez, Tipo Trabajo: Cambio de aceite y filtro,"
        self.assertNotIn(trabajo_agregado, lista_trabajos)
    def test_agregar_trabajo_fecha_pasada(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Llenar los campos con datos válidos (puedes ajustar los valores según lo necesites)
        app.marca_entry.insert(0, "Toyota")
        app.modelo_entry.insert(0, "Camry")
        app.ano_entry.insert(0, "2022")
        app.patente_entry.insert(0, "ABC123")
        app.nombre_cliente_entry.insert(0, "Juan Pérez")
        app.tipo_trabajo_var.set("Cambio de aceite y filtro")  # Seleccionar un tipo de trabajo válido

        # Establecer una fecha en el pasado
        app.fecha_cal.set_date("2022-01-01")

        # Agregar trabajo
        app.agregar_button.invoke()

        # Verificar que el trabajo no se haya agregado a la lista
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        trabajo_agregado = f"Marca: Toyota, Modelo: Camry, Año: 2022, Patente: ABC123, Nombre Cliente: Juan Pérez, Tipo Trabajo: Cambio de aceite y filtro,"
        self.assertNotIn(trabajo_agregado, lista_trabajos)
    def test_agregar_trabajo_varios_datos(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Datos de trabajos a agregar (puedes ajustar los valores según lo necesites)
        trabajos = [
            {
                "marca": "Toyota",
                "modelo": "Camry",
                "ano": "2022",
                "patente": "ABC123",
                "nombre_cliente": "Juan Pérez",
                "tipo_trabajo": "Cambio de aceite y filtro",
                "fecha": "2022-10-15"
            },
            {
                "marca": "Honda",
                "modelo": "Civic",
                "ano": "2021",
                "patente": "XYZ456",
                "nombre_cliente": "Ana López",
                "tipo_trabajo": "Cambio de frenos (delanteros o traseros)",
                "fecha": "2022-11-20"
            }
            # Agrega más trabajos con diferentes datos
        ]

        for trabajo in trabajos:
            # Llenar los campos con los datos del trabajo actual
            app.marca_entry.insert(0, trabajo["marca"])
            app.modelo_entry.insert(0, trabajo["modelo"])
            app.ano_entry.insert(0, trabajo["ano"])
            app.patente_entry.insert(0, trabajo["patente"])
            app.nombre_cliente_entry.insert(0, trabajo["nombre_cliente"])
            app.tipo_trabajo_var.set(trabajo["tipo_trabajo"])
            app.fecha_cal.set_date(trabajo["fecha"])

            # Agregar trabajo
            app.agregar_button.invoke()

            # Verificar que el trabajo se haya agregado a la lista
            lista_trabajos = app.lista_trabajos.get(0, tk.END)
            trabajo_agregado = f"Marca: {trabajo['marca']}, Modelo: {trabajo['modelo']}, Año: {trabajo['ano']}, Patente: {trabajo['patente']}, Nombre Cliente: {trabajo['nombre_cliente']}, Tipo Trabajo: {trabajo['tipo_trabajo']},"
            self.assertIn(trabajo_agregado, lista_trabajos)

            # Limpiar los campos para el próximo trabajo
            app.marca_entry.delete(0, tk.END)
            app.modelo_entry.delete(0, tk.END)
            app.ano_entry.delete(0, tk.END)
            app.patente_entry.delete(0, tk.END)
            app.nombre_cliente_entry.delete(0, tk.END)
    def test_fecha_pasada_calendario(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Establecer una fecha en el calendario en el pasado
        fecha_pasada = "2020-01-01"
        app.fecha_cal.set_date(fecha_pasada)

        # Intentar agregar un trabajo con la fecha en el pasado
        app.marca_entry.insert(0, "Toyota")
        app.modelo_entry.insert(0, "Camry")
        app.ano_entry.insert(0, "2022")
        app.patente_entry.insert(0, "ABC123")
        app.nombre_cliente_entry.insert(0, "Juan Pérez")
        app.tipo_trabajo_var.set("Cambio de aceite y filtro")

        # Agregar trabajo
        app.agregar_button.invoke()

        # Verificar que el trabajo no se haya agregado a la lista
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        trabajo_agregado = f"Marca: Toyota, Modelo: Camry, Año: 2022, Patente: ABC123, Nombre Cliente: Juan Pérez, Tipo Trabajo: Cambio de aceite y filtro,"
        self.assertNotIn(trabajo_agregado, lista_trabajos)
    def test_ingresar_comentarios_largos(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Datos de trabajo con comentarios largos
        trabajo = {
            "marca": "Toyota",
            "modelo": "Camry",
            "ano": "2022",
            "patente": "ABC123",
            "nombre_cliente": "Juan Pérez",
            "tipo_trabajo": "Cambio de aceite y filtro",
            "fecha": "2023-01-15",
            "comentarios": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam fringilla ipsum nec magna vestibulum,"
                          "eget fermentum felis congue. Nulla facilisi. Donec lacinia, purus nec mattis hendrerit, purus urna."
                          "Quisque rutrum orci vel nulla ultrices, in auctor neque aliquam. Sed quis metus vel libero."
                          "Suspendisse cursus erat quis euismod. Etiam eu quam et metus consectetur viverra. Nullam et augue."
        }

        # Llenar los campos con los datos del trabajo
        app.marca_entry.insert(0, trabajo["marca"])
        app.modelo_entry.insert(0, trabajo["modelo"])
        app.ano_entry.insert(0, trabajo["ano"])
        app.patente_entry.insert(0, trabajo["patente"])
        app.nombre_cliente_entry.insert(0, trabajo["nombre_cliente"])
        app.tipo_trabajo_var.set(trabajo["tipo_trabajo"])
        app.fecha_cal.set_date(trabajo["fecha"])
        app.comentarios_text.insert(tk.END, trabajo["comentarios"])

        # Agregar trabajo
        app.agregar_button.invoke()

        # Verificar que el trabajo se haya agregado a la lista
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        trabajo_agregado = f"Marca: {trabajo['marca']}, Modelo: {trabajo['modelo']}, Año: {trabajo['ano']}, Patente: {trabajo['patente']}, Nombre Cliente: {trabajo['nombre_cliente']}, Tipo Trabajo: {trabajo['tipo_trabajo']}, Comentarios: {trabajo['comentarios']}, Fecha: {trabajo['fecha']}"
        self.assertIn(trabajo_agregado, lista_trabajos)

        # Cerrar la ventana principal
        app.destroy()
    def test_agregar_trabajo_sin_comentarios(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Datos de trabajo sin comentarios
        trabajo = {
            "marca": "Toyota",
            "modelo": "Camry",
            "ano": "2022",
            "patente": "ABC123",
            "nombre_cliente": "Juan Pérez",
            "tipo_trabajo": "Cambio de aceite y filtro",
            "fecha": "2023-01-15",
            "comentarios": ""
        }

        # Llenar los campos con los datos del trabajo
        app.marca_entry.insert(0, trabajo["marca"])
        app.modelo_entry.insert(0, trabajo["modelo"])
        app.ano_entry.insert(0, trabajo["ano"])
        app.patente_entry.insert(0, trabajo["patente"])
        app.nombre_cliente_entry.insert(0, trabajo["nombre_cliente"])
        app.tipo_trabajo_var.set(trabajo["tipo_trabajo"])
        app.fecha_cal.set_date(trabajo["fecha"])
        app.comentarios_text.insert(tk.END, trabajo["comentarios"])

        # Agregar trabajo
        app.agregar_button.invoke()

        # Verificar que el trabajo NO se haya agregado a la lista
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        trabajo_agregado = f"Marca: {trabajo['marca']}, Modelo: {trabajo['modelo']}, Año: {trabajo['ano']}, Patente: {trabajo['patente']}, Nombre Cliente: {trabajo['nombre_cliente']}, Tipo Trabajo: {trabajo['tipo_trabajo']}, Comentarios: {trabajo['comentarios']}, Fecha: {trabajo['fecha']}"

        # Usamos self.assertTrue con una expresión negada
        self.assertTrue(trabajo_agregado not in lista_trabajos, "El trabajo no debería agregarse en esta prueba")

        # Cerrar la ventana principal
        app.destroy()
    def test_seleccionar_tipo_trabajo(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Tipos de trabajo a seleccionar
        tipos_de_trabajo = [
            "Cambio de aceite y filtro",
            "Cambio de frenos (delanteros o traseros)",
            "Cambio de neumáticos",
            "Cambio de bujías",
            "Cambio de batería"
        ]

        for tipo_trabajo in tipos_de_trabajo:
            # Seleccionar un tipo de trabajo en el menú desplegable
            app.tipo_trabajo_var.set(tipo_trabajo)

            # Verificar que el tipo de trabajo seleccionado coincida
            self.assertEqual(app.tipo_trabajo_var.get(), tipo_trabajo)

        # Cerrar la ventana principal
        app.destroy()
    def test_seleccionar_tipo_trabajo_predeterminado(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Tipo de trabajo predeterminado
        tipo_trabajo_predeterminado = "Ingrese trabajo a realizar"

        # Verificar que el tipo de trabajo predeterminado esté seleccionado al inicio
        self.assertEqual(app.tipo_trabajo_var.get(), tipo_trabajo_predeterminado)

        # Cerrar la ventana principal
        app.destroy()
    def test_agregar_gran_cantidad_trabajos(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Cantidad de trabajos a agregar
        cantidad_trabajos = 100  # Puedes ajustar este número según tus necesidades

        for i in range(cantidad_trabajos):
            # Generar datos de trabajo de forma dinámica
            trabajo = {
                "marca": f"Marca {i + 1}",
                "modelo": f"Modelo {i + 1}",
                "ano": f"Año {i + 1}",
                "patente": f"Patente {i + 1}",
                "nombre_cliente": f"Cliente {i + 1}",
                "tipo_trabajo": "Cambio de aceite y filtro",
                "fecha": "2023-01-15",
                "comentarios": f"Comentarios {i + 1}"
            }

            # Llenar los campos con los datos del trabajo
            app.marca_entry.insert(0, trabajo["marca"])
            app.modelo_entry.insert(0, trabajo["modelo"])
            app.ano_entry.insert(0, trabajo["ano"])
            app.patente_entry.insert(0, trabajo["patente"])
            app.nombre_cliente_entry.insert(0, trabajo["nombre_cliente"])
            app.tipo_trabajo_var.set(trabajo["tipo_trabajo"])
            app.fecha_cal.set_date(trabajo["fecha"])
            app.comentarios_text.insert(tk.END, trabajo["comentarios"])

            # Agregar el trabajo a la lista
            app.agregar_button.invoke()

        # Verificar que la cantidad de trabajos en la lista coincida
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        self.assertEqual(len(lista_trabajos), cantidad_trabajos)

        # Cerrar la ventana principal
        app.destroy()
    def test_manipular_lista_con_maximo_trabajos(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Establecer el número máximo de trabajos
        max_trabajos = 10

        for i in range(max_trabajos):
            # Generar datos de trabajo de forma dinámica
            trabajo = {
                "marca": f"Marca {i + 1}",
                "modelo": f"Modelo {i + 1}",
                "ano": f"Año {i + 1}",
                "patente": f"Patente {i + 1}",
                "nombre_cliente": f"Cliente {i + 1}",
                "tipo_trabajo": "Cambio de aceite y filtro",
                "fecha": "2023-01-15",
                "comentarios": f"Comentarios {i + 1}"
            }

            # Llenar los campos con los datos del trabajo
            app.marca_entry.insert(0, trabajo["marca"])
            app.modelo_entry.insert(0, trabajo["modelo"])
            app.ano_entry.insert(0, trabajo["ano"])
            app.patente_entry.insert(0, trabajo["patente"])
            app.nombre_cliente_entry.insert(0, trabajo["nombre_cliente"])
            app.tipo_trabajo_var.set(trabajo["tipo_trabajo"])
            app.fecha_cal.set_date(trabajo["fecha"])
            app.comentarios_text.insert(tk.END, trabajo["comentarios"])

            # Agregar el trabajo a la lista
            app.agregar_button.invoke()

        # Verificar que la cantidad de trabajos en la lista coincida con el número máximo
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        self.assertEqual(len(lista_trabajos), max_trabajos)

        # Intentar agregar un trabajo adicional y verificar que la cantidad de trabajos no aumente
        app.marca_entry.insert(0, "Marca Extra")
        app.modelo_entry.insert(0, "Modelo Extra")
        app.ano_entry.insert(0, "Año Extra")
        app.patente_entry.insert(0, "Patente Extra")
        app.nombre_cliente_entry.insert(0, "Cliente Extra")
        app.tipo_trabajo_var.set("Cambio de bujías")
        app.fecha_cal.set_date("2023-01-15")
        app.comentarios_text.insert(tk.END, "Comentarios Extra")
        app.agregar_button.invoke()

        lista_trabajos_despues = app.lista_trabajos.get(0, tk.END)
        self.assertEqual(len(lista_trabajos_despues), max_trabajos)  # La cantidad de trabajos no debe aumentar

        # Cerrar la ventana principal
        app.destroy()
    def test_datos_no_validos(self):
        # Crear una instancia de la aplicación
        app = AgendarTrabajos()

        # Ingresar datos no válidos en campos obligatorios
        app.marca_entry.insert(0, "")
        app.modelo_entry.insert(0, "Modelo Válido")
        app.ano_entry.insert(0, "Año Válido")
        app.patente_entry.insert(0, "Patente Válida")
        app.nombre_cliente_entry.insert(0, "Cliente Válido")

        # Tipo de trabajo inválido
        app.tipo_trabajo_var.set("Tipo Inválido")

        # Fecha pasada
        app.fecha_cal.set_date("2020-01-01")

        # Comentarios largos
        app.comentarios_text.insert(tk.END, "Estos son comentarios largos que exceden el límite de caracteres permitidos en los comentarios.")

        # Intentar agregar el trabajo
        app.agregar_button.invoke()

        # Verificar que la lista de trabajos esté vacía
        lista_trabajos = app.lista_trabajos.get(0, tk.END)
        self.assertEqual(len(lista_trabajos), 0)

        # Cerrar la ventana principal
        app.destroy()


if __name__ == '__main__':
    unittest.main()
