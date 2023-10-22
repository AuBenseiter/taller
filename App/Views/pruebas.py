import tkinter as tk
from PIL import Image, ImageTk

# Crear una instancia de la ventana principal
root = tk.Tk()
root.title("Mostrar Imagen")

# Cargar la imagen utilizando PIL
image = Image.open("../../disiture_logo.jpg")  # Asegúrate de que el archivo "disiture.jpg" esté en el mismo directorio que este script

# Convertir la imagen en un objeto PhotoImage
photo = ImageTk.PhotoImage(image)

# Crear una etiqueta para mostrar la imagen
label = tk.Label(root, image=photo)
label.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
