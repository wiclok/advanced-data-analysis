# Advanced Data Analysis

Este proyecto realiza un analisis de datos avanzado utilizando Python, numpy, pandas y matplotlib, extrayendo información de una base de datos MySQL.

## Requisitos

Para ejecutar este programa, necesitarás:

- **Python 3.x**: Asegúrate de tener Python 3 instalado en tu sistema.
- **mysql-connector-python**: Librería para conectar Python con MySQL.
- **pandas**: Librería para la manipulación y análisis de datos.
- **numpy**: Librería para operaciones matemáticas y estadísticas.
- **matplotlib**: Librería para la creación de gráficos.
- **MySQL**: Un servidor de base de datos MySQL en funcionaminto.

## Instalación

1. **Clonar el repositorio**

Clona este repositorio en tu máquina local utilizando Git:

```sh
  https://github.com/wiclok/advanced-data-analysis.git
```

2. **Instalar Dependencias**

Navega al directorio del proyecto y crea un entorno virtual (opcional pero recomendado):

```sh
cd advanced-data-analysis
python -m venv venv
source venv/bin/activate
```

Luego, instala las dependencias necesarias:

```sh
pip install mysql-connector-python pandas numpy matplotlib
```

# Configuración

```
conn = mysql.connector.connect(
    host="tu_host",  # Por lo general, 'localhost'
    user="tu_usuario",
    password="tu_contraseña"
)
```

Asegúrate de reemplazar "tu_host", "tu_usuario" y "tu_contraseña" con los valores correspondientes para tu base de datos MySQL.

# Uso

1. **Ejecutar el Script**

Con el entorno virtual activado (si lo estás usando), ejecuta el script principal:

```sh
python main.py
```

El script realizará las siguientes acciones:

- Conexión a MySQL: Verifica si la conexión a la base de datos es exitosa.
- Creación de Base de Datos y Tabla: Crea la base de datos CompanyData y la tabla EmployeePerformance si no existen.
- Población de Datos: Inserta datos ficticios en la tabla.
- Extracción de Datos: Extrae los datos de la tabla a un DataFrame de pandas.
- Análisis de Datos: Calcula estadísticas y correlaciones.
- Visualización de Datos: Genera gráficos para visualizar los datos.

2. **Ver resultados**

Después de ejecutar el script, revisa la salida en la consola para ver las estadísticas calculadas y las correlaciones. También se generarán gráficos que se mostrarán en ventanas emergentes.