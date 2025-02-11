## Control de Gastos - Versión 2
Bienvenido a la versión 2 de la aplicación "Control de Gastos". En esta actualización, he optimizado el código utilizando Programación Orientada a Objetos (POO) para mejorar la estructura, mantenibilidad y escalabilidad del proyecto.

## Descripción
"Control de Gastos" es una aplicación diseñada para ayudarte a gestionar tus finanzas personales de manera eficiente. Permite registrar usuarios, ingresar gastos asociados a cada usuario, eliminar gastos y visualizar un resumen de los mismos.

## Características
- **Gestión de Usuarios**: Registro de nuevos usuarios con nombre y apellido.
- **Registro de Gastos**: Asociación de gastos específicos a usuarios registrados.
- **Eliminación de Gastos**: Capacidad para eliminar gastos previamente registrados.
- **Visualización de Gastos**: Muestra una lista de gastos asociados a cada usuario.

## Tecnologías Utilizadas
- **Lenguaje de Programación**: Python
- **Base de Datos**: SQLite
- **Bibliotecas**:
  - `sqlite3`: Para la gestión de la base de datos.
  - `pandas`: Para la manipulación y visualización de datos en formato tabular.

## Estructura del Proyecto
El proyecto está organizado de la siguiente manera:

control_gastosV2/ ├── Funciones/ │ ├── ingreso_usuario.py │ ├── ingreso_gastos.py │ ├── eliminar_gastos.py │ └── mostrar_gastos.py ├── index.py └── README.md

- **Funciones/**: Contiene módulos específicos para cada funcionalidad principal de la aplicación.
- **index.py**: Archivo principal que ejecuta la aplicación y maneja la interacción con el usuario.
- **README.md**: Este archivo, que proporciona información general sobre el proyecto.
   
## Uso
Al ejecutar la aplicación, se presentará un menú interactivo con las siguientes opciones:

Ingreso de nuevo usuario: Permite registrar un nuevo usuario en la base de datos.
Ingreso de gastos: Permite ingresar un gasto asociado a un usuario existente.
Eliminar gastos: Permite eliminar un gasto específico de un usuario.
Mostrar gastos: Muestra una lista de todos los gastos registrados, asociados a sus respectivos usuarios.
Salir: Cierra la aplicación.
Sigue las instrucciones en pantalla para navegar por las opciones y gestionar tus gastos de manera efectiva.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar o ampliar las funcionalidades de esta aplicación:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -am 'Agrega nueva funcionalidad').
Sube tus cambios al repositorio (git push origin feature/nueva-funcionalidad).
Abre un Pull Request para revisión.

## Licencia
Este proyecto está bajo la Licencia MIT.

