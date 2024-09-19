'''
Programa que calcula la edad de un gato
y un perro con respecto a los años humanos
'''

import tkinter as tk
from tkinter import messagebox


# Función para calcular las edades
def calculate_pet_ages(humanYears):
    if humanYears == 1:
        catYears = 15
        dogYears = 15
    elif humanYears == 2:
        catYears = 15 + 9
        dogYears = 15 + 9
    else:
        catYears = 15 + 9 + (humanYears - 2) * 4
        dogYears = 15 + 9 + (humanYears - 2) * 5

    return {
        'humanYears': humanYears,
        'catYears': catYears,
        'dogYears': dogYears
    }


# Función que se ejecuta al presionar el botón o dar ENTER
def show_ages(event=None):
    try:
        # Obtener el valor ingresado por el usuario
        humanYears = int(entry.get())

        # Calcular las edades de gato y perro
        ages = calculate_pet_ages(humanYears)

        # Mostrar un mensaje emergente con el resultado y un ícono de información
        messagebox.showinfo("Resultado",
                            f"Años humanos: {ages['humanYears']}\n"
                            f"Años de gato: {ages['catYears']}\n"
                            f"Años de perro: {ages['dogYears']}",
                            icon='info')

        # Limpiar el campo de entrada después del cálculo
        entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")
        entry.delete(0, tk.END)


# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Años para Gatos y Perros")

# Etiqueta para indicar al usuario que ingrese los años
label = tk.Label(root, text="Ingresa los años humanos:")
label.pack(pady=10)

# Campo de entrada para los años humanos
entry = tk.Entry(root)
entry.pack(pady=5)

# Botón para calcular y mostrar las edades
button = tk.Button(root, text="Calcular", command=show_ages)
button.pack(pady=10)

# Vincular la tecla ENTER para que funcione igual que el botón
root.bind('<Return>', show_ages)

# Ejecutar el bucle principal de la ventana
root.mainloop()
