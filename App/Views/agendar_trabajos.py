import tkinter as tk
from tkcalendar import Calendar

class AgendarTrabajos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Agendamiento de Trabajos")
        self.config(bg='#F0F0F0', width=480, height=500)
        #self.iconbitmap("DG.ico")

        self.marca_label = tk.Label(self, text="Marca:")
        self.marca_entry = tk.Entry(self)
        self.marca_label.grid(row=0, column=0)
        self.marca_entry.grid(row=0, column=1)


        self.modelo_label = tk.Label(self, text="Modelo:")
        self.modelo_entry = tk.Entry(self)
        self.modelo_label.grid(row=1, column=0)
        self.modelo_entry.grid(row=1, column=1)


        self.ano_label = tk.Label(self, text="Año:")
        self.ano_entry = tk.Entry(self)
        self.ano_label.grid(row=2, column=0)
        self.ano_entry.grid(row=2, column=1)


        self.patente_label = tk.Label(self, text="Patente:")
        self.patente_entry = tk.Entry(self)
        self.patente_label.grid(row=3, column=0)
        self.patente_entry.grid(row=3, column=1)


        self.nombre_cliente_label = tk.Label(self, text="Nombre Cliente:")
        self.nombre_cliente_entry = tk.Entry(self)
        self.nombre_cliente_label.grid(row=4, column=0)
        self.nombre_cliente_entry.grid(row=4, column=1)


        self.tipo_trabajo_label = tk.Label(self, text="Tipo de Trabajo:")
        self.tipo_trabajo_label.grid(row=5, column=0)






        # Crear lista para mostrar trabajos agendados
        self.lista_trabajos = tk.Listbox(self, width=80, height=10)
        self.lista_trabajos.grid(row=9, column=0, columnspan=2)
        # Colocar elementos en la ventana


        self.comentarios_label = tk.Label(self, text="Comentarios:")
        self.comentarios_label.grid(row=6, column=0)
        # Crear entrada de texto multi-línea para comentarios
        self.comentarios_text = tk.Text(self, width=30, height=5)


        def agregar_trabajo():
            # Función para agregar un trabajo a la lista
            marca = self.marca_entry.get()
            modelo = self.modelo_entry.get()
            ano = self.ano_entry.get()
            patente = self.patente_entry.get()
            nombre_cliente = self.nombre_cliente_entry.get()
            tipo_trabajo = self.tipo_trabajo_var.get()
            comentarios = self.comentarios_text.get(1.0, tk.END)

            fecha = self.fecha_cal.get_date()

            # Buscar el tiempo estimado para el tipo de trabajo seleccionado
            tiempo_estimado = next(
                (trabajo["tiempo_estimado"] for trabajo in self.tipos_de_trabajo if trabajo["nombre"] == tipo_trabajo), "")

            trabajo = f"Marca: {marca}, Modelo: {modelo}, Año: {ano}, Patente: {patente}, Nombre Cliente: {nombre_cliente}, Tipo Trabajo: {tipo_trabajo}, Tiempo Estimado: {tiempo_estimado}, Comentarios: {comentarios}, Fecha: {fecha}"
            self.lista_trabajos.insert(tk.END, trabajo)

            # Puedes agregar la lógica para guardar el trabajo en la base de datos aquí

        self.fecha_label = tk.Label(self, text="Fecha ejecución:")
        self.fecha_label.grid(row=7, column=0)
        # Calendario
        self.fecha_cal = Calendar(self)
        self.fecha_cal.grid(row=7, column=1)


        # Crear botón para agregar trabajo
        self.agregar_button = tk.Button(self, text="Agregar Trabajo", command=agregar_trabajo)
        self.agregar_button.grid(row=8, column=0, columnspan=2)



        self.tipos_de_trabajo = [
            {
                "nombre": "Ingrese trabajo a realizar",
                "tiempo_estimado": "0 minutos"
            },
            {
                "nombre": "Cambio de aceite y filtro",
                "tiempo_estimado": "45 minutos"
            },
            {
                "nombre": "Cambio de frenos (delanteros o traseros)",
                "tiempo_estimado": "2 horas"
            },
            {
                "nombre": "Cambio de neumáticos",
                "tiempo_estimado": "45 minutos"
            },
            {
                "nombre": "Cambio de bujías",
                "tiempo_estimado": "45 minutos"
            },
            {
                "nombre": "Cambio de batería",
                "tiempo_estimado": "30 minutos"
            },
            # Agrega los demás trabajos con sus descripciones y tiempos estimados aquí
        ]
        # Crear variable para el campo "Tipo de Trabajo"
        self.tipos_de_trabajo_nombres = [trabajo["nombre"] for trabajo in self.tipos_de_trabajo]
        self.tipo_trabajo_var = tk.StringVar(self)
        self.tipo_trabajo_var.set(self.tipos_de_trabajo_nombres[0])  # Establecer el valor inicial
        self.tipo_trabajo_menu = tk.OptionMenu(self, self.tipo_trabajo_var, *self.tipos_de_trabajo_nombres)
        self.tipo_trabajo_menu.grid(row=5, column=1)

