import sqlite3

class ConexionBD:
    def __init__(self, base_datos):
        try:
            # Establece una conexión con la base de datos SQLite especificada por 'base_datos'.
            self.conn = sqlite3.connect(base_datos)
            # Crea un cursor para interactuar con la base de datos.
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            # Maneja cualquier error que ocurra durante la conexión.
            print(f"Error de conexión: {error}.")

    def cerrar_conexion(self):
        # Cierra la conexión con la base de datos.
        self.conn.close()
        print("Conexión cerrada")

class IngresoUsuario:
    def __init__(self, conexion):
        # Recibe una instancia de 'ConexionBD' para interactuar con la base de datos.
        self.conexion = conexion

    def ingresar_usuario(self):
        try:
            # Solicita al usuario que ingrese su nombre y apellido.
            nombre_usuario = input("Ingresa tu nombre: ")
            apellido_usuario = input("Ingresa tu apellido: ")
            # Inserta el nuevo usuario en la tabla 'usuario' de la base de datos.
            self.conexion.cursor.execute(
                "INSERT INTO usuario (nombre_usuario, apellido_usuario) VALUES (?, ?)",
                (nombre_usuario, apellido_usuario)
            )
            # Confirma (hace commit) la transacción en la base de datos.
            self.conexion.conn.commit()
            print(f"Usuario {nombre_usuario} {apellido_usuario} ingresado correctamente")
        except ValueError:
            # Maneja errores relacionados con la conversión de tipos de datos.
            print("Ingresa un valor adecuado.")
        except sqlite3.Error as error:
            # Maneja errores específicos de SQLite.
            print(f"Error en la base de datos: {error}.")

# Especifica la ruta de la base de datos SQLite.
ruta_db = "C:/Users/POWER/gastos_control.db"
# Crea una instancia de 'ConexionBD' para manejar la conexión a la base de datos.
conexion = ConexionBD(ruta_db)
