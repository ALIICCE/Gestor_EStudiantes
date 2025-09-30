# Gestor de Estudiantes

Este programa en **Python** permite manejar una lista de estudiantes almacenados en una **base de datos SQLite**. Cada estudiante tiene un **nombre**, una **edad** y una **lista de calificaciones** que corresponden a 4 materias.  

Cuenta con una interfaz grafica con **Tkinter**, donde se pueden realizar las siguientes acciones:

## Caracteristicas principales

- **Agregar estudiantes**: permite registrar un estudiante con su nombre, edad y calificaciones en 4 materias.
- **Eliminar estudiantes**: se puede eliminar a un estudiante de la base de datos por su nombre.
- **Listar estudiantes**: se muestra en la interfaz el listado de nombres de los estudiantes registrados.
- **Base de datos SQLite**: los datos se guardan en `estudiantes.db`.

---

## Requisitos

1. **Python 3.8 o superior**
2. TKinter generalmente viene instalado por defecto con Python, pero en algunas distribuciones Linux puedes ejecutar:
   sudo apt-get install python3-tk
