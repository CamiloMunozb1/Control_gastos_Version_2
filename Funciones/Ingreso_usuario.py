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

class ingreso_usuario:
    def __init__(self, conexion):
        self.conexion = conexion

    def ingresar_usuario(self):
        nombre_usuario = str(input("Ingresa tu nombre: "))
        apellido_usuario = str(input("Ingresa tu apellido: "))
        self.conexion.cursor.execute("INSERT INTO usuario (nombre_usuario,apellido_usuario) VALUES (?,?)",(nombre_usuario,apellido_usuario))
        self.conexion.conn.commit()
        print(f"Usuario {nombre_usuario} {apellido_usuario} ingresado correctamente")

ruta_db = "C:/Users/POWER/gastos_control.db"
conexion = conexionBD(ruta_db)
