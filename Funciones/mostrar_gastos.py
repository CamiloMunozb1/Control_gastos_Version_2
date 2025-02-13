import sqlite3
import pandas as pd

class ConexionBD:
    def __init__(self, base_datos):
        try:
            # Establece una conexión con la base de datos SQLite especificada por 'base_datos'.
            self.conn = sqlite3.connect(base_datos)
        except sqlite3.Error as error:
            # Captura y muestra cualquier error que ocurra durante la conexión.
            print(f"Error de conexión: {error}.")

    def cerrar_conexion(self):
        # Cierra la conexión con la base de datos.
        self.conn.close()
        print("Conexión cerrada.")

class MostrarGastos:
    def __init__(self, conexion):
        # Recibe una instancia de 'ConexionBD' para interactuar con la base de datos.
        self.conexion = conexion

    def mostrar_gasto(self):
        # Define una consulta SQL para obtener los nombres, apellidos y gastos de los usuarios.
        query = """
                SELECT usuario.nombre_usuario, usuario.apellido_usuario, gastos.gasto_usuario
                FROM usuario
                JOIN gastos ON usuario.usuario_ID = gastos.usuario_ID
                """
        # Ejecuta la consulta y almacena el resultado en un DataFrame de pandas.
        resultado_df = pd.read_sql_query(query, self.conexion.conn)
        if not resultado_df.empty:
            # Si el DataFrame no está vacío, imprime su contenido.
            print(resultado_df)
        else:
            # Si no se encontraron registros, muestra un mensaje indicándolo.
            print("No se encontraron registros.")


# Ruta a la base de datos SQLite.
ruta_db = "C:/Users/POWER/gastos_control.db"
# Crea una instancia de la conexión a la base de datos.
conexion = ConexionBD(ruta_db)

