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
            print(f"Error de conexión: {error}")

    def cerrar_conexion(self):
        # Cierra la conexión con la base de datos.
        self.conn.close()
        print("Conexión cerrada")

class IngresoGastos:
    def __init__(self, conexion):
        # Recibe una instancia de 'ConexionBD' para interactuar con la base de datos.
        self.conexion = conexion

    def ingresar_gastos(self):
        # Solicita al usuario que ingrese el valor del gasto.
        ingresar_gasto = input("Ingresa el valor del gasto: ")
        # Solicita al usuario que ingrese su nombre de registro.
        nombre_usuario = input("Ingresa tu nombre de registro: ")
        # Solicita al usuario que ingrese su apellido de registro.
        apellido_usuario = input("Ingresa tu apellido de registro: ")
        
        # Busca el ID del usuario en la base de datos.
        self.conexion.cursor.execute(
            "SELECT usuario_ID FROM usuario WHERE nombre_usuario = ? AND apellido_usuario = ?", 
            (nombre_usuario, apellido_usuario)
        )
        usuario = self.conexion.cursor.fetchone()
        
        if usuario:
            # Si el usuario existe, obtiene su ID.
            usuario_id = usuario[0]
            # Inserta el gasto en la base de datos asociado al usuario.
            self.conexion.cursor.execute(
                "INSERT INTO gastos (gasto_usuario, usuario_ID) VALUES (?, ?)",
                (ingresar_gasto, usuario_id)
            )
            # Confirma los cambios en la base de datos.
            self.conexion.conn.commit()
            print(f"Gasto de {ingresar_gasto} insertado.")
        else:
            # Si el usuario no se encuentra, muestra un mensaje de error.
            print("Usuario no encontrado.")

# Especifica la ruta de la base de datos SQLite.
ruta_db = "C:/Users/POWER/gastos_control.db"
# Crea una instancia de 'ConexionBD' para manejar la conexión a la base de datos.
conexion = ConexionBD(ruta_db)
