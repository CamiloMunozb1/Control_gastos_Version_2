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
        print("Conexión cerrada.")

class EliminacionGastos:
    def __init__(self, conexion):
        # Recibe una instancia de 'ConexionBD' para interactuar con la base de datos.
        self.conexion = conexion

    def eliminar_gastos(self):
        try:
            # Solicita al usuario que ingrese el valor del gasto a eliminar.
            gasto_eliminar = input("Ingresa el gasto a eliminar: ")
            # Solicita al usuario que ingrese su nombre de registro.
            nombre_usuario = input("Ingresa el nombre de registro: ")
            # Solicita al usuario que ingrese su apellido de registro.
            apellido_usuario = input("Ingresa el apellido del registro: ")

            # Busca el ID del usuario en la base de datos.
            self.conexion.cursor.execute(
                "SELECT usuario_ID FROM usuario WHERE nombre_usuario = ? AND apellido_usuario = ?",
                (nombre_usuario, apellido_usuario)
            )
            usuario = self.conexion.cursor.fetchone()

            if usuario:
                # Si el usuario existe, obtiene su ID.
                usuario_id = usuario[0]
                # Elimina el gasto asociado al usuario en la base de datos.
                self.conexion.cursor.execute(
                    "DELETE FROM gastos WHERE gasto_usuario = ? AND usuario_ID = ?",
                    (gasto_eliminar, usuario_id)
                )
                # Confirma los cambios en la base de datos.
                self.conexion.conn.commit()
                print("Gasto eliminado.")
            else:
                # Si el usuario no se encuentra en la base de datos.
                print("Usuario no encontrado.")
        except ValueError:
            # Maneja errores relacionados con valores incorrectos.
            print("Ingresa un valor adecuado.")
        except sqlite3.Error as error:
            # Maneja errores relacionados con la base de datos.
            print(f"Error de base de datos: {error}.")

# Ruta a la base de datos SQLite.
ruta_db = "C:/Users/POWER/gastos_control.db"
# Crea una instancia de la conexión a la base de datos.
conexion = ConexionBD(ruta_db)
