import sqlite3

DB_NAME = "estudiantes.db"

# Crear la base de datos y tablas
def crear_db():
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    # Tabla de estudiantes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    ''')
    
    # Tabla de calificaciones
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calificaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            estudiante_id INTEGER NOT NULL,
            nombre_materia TEXT NOT NULL,
            calificacion REAL NOT NULL,
            FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id) ON DELETE CASCADE
        )
    ''')
    
    conexion.commit()
    conexion.close()
    print("Base de datos y tablas creadas correctamente.")

# Funcion agregar un estudiante
def agregar_estudiante(nombre: str, edad: int, calificaciones: list):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    cursor.execute('INSERT INTO estudiantes (nombre, edad) VALUES (?, ?)', (nombre, edad))
    estudiante_id = cursor.lastrowid
    
    for c in calificaciones:
        cursor.execute(
            'INSERT INTO calificaciones (estudiante_id, nombre_materia, calificacion) VALUES (?, ?, ?)',
            (estudiante_id, c['nombre'], c['calificacion'])
        )
    
    conexion.commit()
    conexion.close()
    print(f"Estudiante '{nombre}' agregado correctamente.")

# Funcion eliminar estudiante
def eliminar_estudiante(nombre: str) -> bool:
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    cursor.execute('SELECT id FROM estudiantes WHERE nombre = ?', (nombre,))
    result = cursor.fetchone()
    if result:
        estudiante_id = result[0]
        cursor.execute('DELETE FROM estudiantes WHERE id = ?', (estudiante_id,))
        conexion.commit()
        conexion.close()
        return True
    else:
        conexion.close()
        return False


# Funcion obtener promedio estudiante
def promedio_estudiante(nombre: str):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()

    cursor.execute('SELECT id FROM estudiantes WHERE nombre = ?', (nombre,))
    result = cursor.fetchone()
    if not result:
        conexion.close()
        print(f"No se encontró un estudiante con el nombre '{nombre}'.")
        return None
    
    estudiante_id = result[0]
    cursor.execute('SELECT calificacion FROM calificaciones WHERE estudiante_id = ?', (estudiante_id,))
    calificaciones = cursor.fetchall()
    
    if not calificaciones:
        conexion.close()
        print(f"El estudiante '{nombre}' no tiene calificaciones registradas.")
        return None
    
    promedio = sum(c[0] for c in calificaciones) / len(calificaciones)
    conexion.close()
    return promedio
