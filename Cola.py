import tkinter as tk
from tkinter import messagebox
from collections import deque

cola_llamadas = deque()

def encolar_llamada():
    nombre = entrada_nombre.get()
    if nombre:
        cola_llamadas.append(nombre)
        entrada_nombre.delete(0, tk.END)
        actualizar_estado()
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, ingresa un nombre.")

def atender_llamada():
    if cola_llamadas:
        atendido = cola_llamadas.popleft()
        messagebox.showinfo("Llamada atendida", f"Se está atendiendo a: {atendido}")
        actualizar_estado()
    else:
        messagebox.showinfo("Sin llamadas", "No hay llamadas en espera.")

def ver_frente():
    if cola_llamadas:
        messagebox.showinfo("Próxima llamada", f"Próximo en ser atendido: {cola_llamadas[0]}")
    else:
        messagebox.showinfo("Sin llamadas", "No hay llamadas en espera.")

def verificar_vacia():
    if not cola_llamadas:
        messagebox.showinfo("Cola vacía", "No hay llamadas en la cola.")
    else:
        messagebox.showinfo("Cola activa", "Hay llamadas esperando.")

def actualizar_estado():
    etiqueta_estado.config(text=f"Llamadas en espera: {len(cola_llamadas)}")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title(" Centro de Atención Telefónica")
ventana.geometry("800x800")

# Entrada
tk.Label(ventana, text="Nombre del cliente:").pack(pady=5)
entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.pack(pady=5)

# Botones
tk.Button(ventana, text=" Encolar llamada", command=encolar_llamada).pack(pady=15)
tk.Button(ventana, text=" Atender llamada", command=atender_llamada).pack(pady=15)
tk.Button(ventana, text=" Ver próxima llamada", command=ver_frente).pack(pady=15)
tk.Button(ventana, text=" Ver tamaño de la cola", command=actualizar_estado).pack(pady=15)
tk.Button(ventana, text=" ¿Cola vacía?", command=verificar_vacia).pack(pady=15)

# Estado
etiqueta_estado = tk.Label(ventana, text="Llamadas en espera: 0", font=("Arial", 12, "bold"))
etiqueta_estado.pack(pady=20)

ventana.mainloop()
