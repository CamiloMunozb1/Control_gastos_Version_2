from Funciones.Ingreso_usuario import conexionBD, ingreso_usuario
from Funciones.ingreso_gastos import conexionBD, ingreso_gastos
from Funciones.eliminar_gastos import conexionBD, eliminacion_gastos
ruta = "C:/Users/POWER/gastos_control.db"
conexion = conexionBD(ruta)


while True:

    # MENU DEL INDEX PARA EL USUARIO.

    print(
        """
            Bienvenido al control de gastos, elije una opcion:
            1. Ingreso de nuevo usuario.
            2. Ingreso de gastos.
            3. Eliminar gastos.
            4. Mostrar gastos.
            5. Salir
        """
    )

    try:
        
        # INGRESO DE USUARIO PARA INGRESAR UNA OPCION.

        usuario = int(input("Ingresa una opcion: "))

        # CONDICIONALES CON LA FUNCION IMPORTADA PARA USARSE.

        if usuario == 1:
            ingreso = ingreso_usuario(conexion)
            ingreso.ingresar_usuario()
        elif usuario == 2:
            gasto = ingreso_gastos(conexion)
            gasto.ingresar_gastos()
        elif usuario == 3:
            eliminar = eliminacion_gastos(conexion)
            eliminar.eliminar_gastos()
        elif usuario == 4:
            print("Proxima actualizacion")
        else:

            # SALIDA DEL PROGRAMA.

            print("Gracias por usar el controlador de gastos, cuida tus ganancias.")
            break

    # MANEJO DE ERROES.
    
    except ValueError:
        print("Error de digitacion, volver a intentar")