# src/main.py

import tkinter as tk
from tkinter import messagebox
from base64_encoder import text_to_base64

def convert_and_display():
    """Función para convertir el texto de entrada y mostrar el resultado."""
    input_text = entry.get()
    if input_text:
        base64_encoded = text_to_base64(input_text)
        output_label.config(text=f'Resultado: {base64_encoded}')
    else:
        messagebox.showwarning("Advertencia", "Por favor, introduce un texto.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Conversor a Base64")

# Etiqueta de entrada
entry_label = tk.Label(root, text="Introduce el texto:")
entry_label.pack(pady=10)

# Campo de entrada
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Botón para convertir
convert_button = tk.Button(root, text="Convertir", command=convert_and_display)
convert_button.pack(pady=20)

# Etiqueta para mostrar el resultado
output_label = tk.Label(root, text="Resultado:")
output_label.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
