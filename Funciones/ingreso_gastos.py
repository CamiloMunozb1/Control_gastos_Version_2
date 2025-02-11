import sqlite3

class conexionBD:
    def __init__(self, base_datos):
        try:
            self.conn = sqlite3.connect(base_datos)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error de conexion: {error}")

    def cerrar_conexion(self):
        self.conn.close()
        print("Conexion cerrada")

class ingreso_gastos:
    def __init__(self, conexion):
        self.conexion = conexion

    def ingresar_gastos(self):
        ingresar_gasto = str(input("Ingresa el valor del gasto: "))
        nombre_usuario = str(input("Ingresa tu nombre de registro: "))
        apellido_usuario = str(input("Ingresa tu apellido de registro: "))
        self.conexion.cursor.execute("SELECT usuario_ID FROM usuario WHERE nombre_usuario = ? AND apellido_usuario = ?", (nombre_usuario, apellido_usuario))
        usuario = self.conexion.cursor.fetchone()
        if usuario:
            usuario_id = usuario[0]
            self.conexion.cursor.execute("INSERT INTO gastos (gasto_usuario, usuario_ID) VALUES (?,?)",(ingresar_gasto, usuario_id))
            self.conexion.conn.commit()
            print(f"Gasto {ingresar_gasto} insertado.")
        else:
            print("Usuario no encontrado.")

ruta_db = "C:/Users/POWER/gastos_control.db"
conexion = conexionBD(ruta_db)

