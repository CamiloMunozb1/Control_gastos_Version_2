# Importación de clases desde módulos específicos dentro del paquete 'Funciones'.
# Se importa la clase 'conexionBD' desde cada módulo para establecer la conexión a la base de datos.
from Funciones.Ingreso_usuario import ConexionBD, IngresoUsuario
from Funciones.ingreso_gastos import ConexionBD, IngresoGastos
from Funciones.eliminar_gastos import ConexionBD, EliminacionGastos
from Funciones.mostrar_gastos import ConexionBD, MostrarGastos

# Definición de la ruta de la base de datos.
ruta = "C:/Users/POWER/gastos_control.db"

# Creación de una instancia de la clase 'conexionBD' para manejar la conexión a la base de datos.
conexion = ConexionBD(ruta)

# Bucle principal que mantiene el programa en ejecución hasta que el usuario decida salir.
while True:

    # Menú principal que se muestra al usuario con las opciones disponibles.
    print(
        """
            Bienvenido al control de gastos, elije una opción:
            1. Ingreso de nuevo usuario.
            2. Ingreso de gastos.
            3. Eliminar gastos.
            4. Mostrar gastos.
            5. Salir
        """
    )

    try:
        # Solicitud al usuario para que ingrese una opción del menú.
        usuario = int(input("Ingresa una opción: "))

        # Condicionales que ejecutan funciones basadas en la opción seleccionada por el usuario.
        if usuario == 1:
            # Opción 1: Ingreso de un nuevo usuario.
            # Se crea una instancia de 'ingreso_usuario' y se llama al método 'ingresar_usuario'.
            ingreso = IngresoUsuario(conexion)
            ingreso.ingresar_usuario()
        elif usuario == 2:
            # Opción 2: Ingreso de un nuevo gasto.
            # Se crea una instancia de 'ingreso_gastos' y se llama al método 'ingresar_gastos'.
            gasto = IngresoGastos(conexion)
            gasto.ingresar_gastos()
        elif usuario == 3:
            # Opción 3: Eliminación de un gasto existente.
            # Se crea una instancia de 'eliminacion_gastos' y se llama al método 'eliminar_gastos'.
            eliminar = EliminacionGastos(conexion)
            eliminar.eliminar_gastos()
        elif usuario == 4:
            # Opción 4: Mostrar todos los gastos registrados.
            # Se crea una instancia de 'mostrar_gastos' y se llama al método 'mostrar_gasto'.
            mostrar = MostrarGastos(conexion)
            mostrar.mostrar_gasto()
        elif usuario == 5:
            # Opción 5: Salir del programa.
            print("Gracias por usar el controlador de gastos, cuida tus ganancias.")
            break
        else:
            # Manejo de entradas que no corresponden a ninguna opción válida del menú.
            print("Ingresa un valor numérico adecuado del 1 al 5.")

    except ValueError:
        # Manejo de errores en caso de que el usuario ingrese un valor no numérico.
        print("Error de digitación, por favor intenta de nuevo.")
