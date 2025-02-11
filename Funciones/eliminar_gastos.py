import sqlite3

class conexionBD:
    def __init__(self, base_datos):
        try:
            self.conn = sqlite3.connect(base_datos)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error de conexion: {error}.")

    def cerrar_conexion(self):
        self.conn.close()
        print("Conexion cerrada.")

class eliminacion_gastos:
    def __init__(self, conexion):
        self.conexion = conexion
    def eliminar_gastos(self):
        gasto_eliminar = str(input("Ingresa el gasto a eliminar: "))
        nombre_usuario = str(input("Ingresa el nombre de registro: "))
        apellido_usuario = str(input("Ingresa el apellido del registro: "))
        self.conexion.cursor.execute("SELECT usuario_ID FROM usuario WHERE nombre_usuario = ? AND apellido_usuario = ?",(nombre_usuario, apellido_usuario))
        usuario = self.conexion.cursor.fetchone()
        if usuario:
            usuario_id = usuario[0]
            self.conexion.cursor.execute("DELETE FROM gastos WHERE gasto_usuario = ? AND usuario_ID = ?",(gasto_eliminar, usuario_id))
            self.conexion.conn.commit()
            print("Gasto eliminado.")
        else:
            print("Usuario no encontrado.")

ruta_db = "C:/Users/POWER/gastos_control.db"
conexion = conexionBD(ruta_db)