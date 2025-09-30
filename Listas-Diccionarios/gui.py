import tkinter as tk
from tkinter import messagebox
from database import agregar_estudiante, eliminar_estudiante, promedio_estudiante

def iniciar_gui():
    ventana = tk.Tk()
    ventana.title("Gestion de Estudiantes")
    ventana.geometry("800x600")
    ventana.configure(bg="white")

    # Funcion actualizar Listbox
    def actualizar_lista():
        listbox_estudiantes.delete(0, tk.END)
        conexion = __import__('sqlite3').connect('estudiantes.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre FROM estudiantes ORDER BY nombre")
        for row in cursor.fetchall():
            listbox_estudiantes.insert(tk.END, row[0])
        conexion.close()

    # FUncion agregar estudiante a la db
    def agregar():
        nombre = entry_nombre.get().strip()
        edad = entry_edad.get().strip()
        try:
            edad = int(edad)
        except ValueError:
            messagebox.showerror("Error", "Edad debe ser un numero entero.")
            return

        calificaciones = []
        for i in range(4):
            materia = entries_materias[i].get().strip()
            calificacion_str = entries_calificaciones[i].get().strip()
            if not materia:
                messagebox.showerror("Error", f"Ingrese el nombre de la materia {i+1}.")
                return
            try:
                calificacion = float(calificacion_str)
            except ValueError:
                messagebox.showerror("Error", f"Ingrese una calificacion numerica valida para '{materia}'.")
                return
            if not (0 <= calificacion <= 100):
                messagebox.showerror("Error", f"La calificacion de '{materia}' debe estar entre 0 y 100.")
                return
            calificaciones.append({'nombre': materia, 'calificacion': calificacion})

        agregar_estudiante(nombre, edad, calificaciones)
        messagebox.showinfo("Exito", f"Estudiante '{nombre}' agregado.")
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        for e in entries_materias + entries_calificaciones:
            e.delete(0, tk.END)
        actualizar_lista()

    # Funcion eliminar estudiante de la db
    def eliminar():
        nombre = entry_eliminar.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Ingrese el nombre del estudiante a eliminar.")
            return
        eliminado = eliminar_estudiante(nombre)
        if eliminado:
            messagebox.showinfo("Exito", f"Estudiante '{nombre}' eliminado correctamente.")
        else:
            messagebox.showwarning("Aviso", f"No se encontro un estudiante con el nombre '{nombre}'.")
        entry_eliminar.delete(0, tk.END)
        actualizar_lista()


    # Funcioncalcular promedio
    def calcular_promedio():
        nombre = entry_promedio.get().strip()
        if not nombre:
            messagebox.showerror("Error", "Ingrese el nombre del estudiante para calcular promedio.")
            return
        promedio = promedio_estudiante(nombre)
        if promedio is not None:
            messagebox.showinfo("Promedio", f"El promedio de '{nombre}' es: {promedio:.2f}")

    # Interfaz Grafica
    frame_form = tk.Frame(ventana, bg="white")
    frame_form.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

    tk.Label(frame_form, text="Agregar Estudiante", font=("Arial", 14, "bold"), bg="white").pack(pady=5)
    tk.Label(frame_form, text="Nombre:", bg="white").pack()
    entry_nombre = tk.Entry(frame_form)
    entry_nombre.pack()

    tk.Label(frame_form, text="Edad:", bg="white").pack()
    entry_edad = tk.Entry(frame_form)
    entry_edad.pack()

    tk.Label(frame_form, text="Materias y Calificaciones:", bg="white").pack(pady=5)
    entries_materias = []
    entries_calificaciones = []
    for i in range(4):
        frame = tk.Frame(frame_form, bg="white")
        frame.pack(pady=2)
        tk.Label(frame, text=f"Materia {i+1}:", bg="white").grid(row=0, column=0)
        e_materia = tk.Entry(frame)
        e_materia.grid(row=0, column=1)
        tk.Label(frame, text="Calificación:", bg="white").grid(row=0, column=2)
        e_calificacion = tk.Entry(frame, width=5)
        e_calificacion.grid(row=0, column=3)
        entries_materias.append(e_materia)
        entries_calificaciones.append(e_calificacion)

    tk.Button(frame_form, text="Agregar Estudiante", command=agregar).pack(pady=10)

    tk.Label(frame_form, text="Eliminar Estudiante", font=("Arial", 14, "bold"), bg="white").pack(pady=5)
    tk.Label(frame_form, text="Nombre:", bg="white").pack()
    entry_eliminar = tk.Entry(frame_form)
    entry_eliminar.pack()
    tk.Button(frame_form, text="Eliminar", command=eliminar).pack(pady=5)

    tk.Label(frame_form, text="Calcular Promedio", font=("Arial", 14, "bold"), bg="white").pack(pady=5)
    tk.Label(frame_form, text="Nombre:", bg="white").pack()
    entry_promedio = tk.Entry(frame_form)
    entry_promedio.pack()
    tk.Button(frame_form, text="Calcular Promedio", command=calcular_promedio).pack(pady=5)

 
    frame_lista = tk.Frame(ventana, bg="white")
    frame_lista.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

    tk.Label(frame_lista, text="Estudiantes Registrados", font=("Arial", 14, "bold"), bg="white").pack(pady=5)

    listbox_estudiantes = tk.Listbox(frame_lista, width=25, bg="white", highlightbackground="gray", borderwidth=2)
    listbox_estudiantes.pack(pady=5, fill=tk.Y)

    actualizar_lista()

    ventana.mainloop()
