# Prueba de evaluación continua 4, Programación para la ciencia de datos

* **Autor: Francisco Jesús Frías Tenza**
* **

Este el es proyecto final de la asignatura _Programación para la ciencia de datos_.
Vamos a proceder con una explicación de sus componentes.

## Árbol de archivos
```
.
├── data
│   ├── nics-firearm-background-checks.csv
│   └── us-state-populations.csv
├── data_analysis
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── utils.cpython-310.pyc
│   └── utils.py
├── data_fetching
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── utils.cpython-310.pyc
│   └── utils.py
├── data_grouping
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── utils.cpython-310.pyc
│   └── utils.py
├── data_processing
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── utils.cpython-310.pyc
│   └── utils.py
├── __init__.py
├── LICENSE.md
├── main.py
├── makedirs
├── README.md
├── requirements.txt
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   │   └── tests.cpython-310.pyc
│   └── tests.py
├── tree.txt
└── venv
    ├── pyvenv.cfg
    ├── bin ...
    ├── 

12 directories, 29 files
```

En los archivos del tipo _utils.py_ encontramos principalmente
las funciones que se nos pide en la práctica.

### Data

En esta carpeta hallamos todos los datos que vamos a emplear
en el análisis.

* nics-firearms-background-checks.csv: dataset con los datos de registros de armas
* us-state-populations.csv: dataset con la población de los estados de EEUU

### Data_analysis

En esta carpeta, dentro del archivo _utils.py_, encontramos las siguientes funciones.

* _time_evoltion_ **(Ejercicio 4.1)**: dibuja una función de evolución temporal de los permisos de armas
* _calculate_relative_values_ **(Ejercicio 5.4)**: calcula valores porcentuales de permisos de armas
* _analyze_permit_ **(Ejercicio 5.5)**: corrige valores discrepantes de un dataset.

### Data_fetching

En esta carpeta, se encuentran las funciones de limpieza y de captura de datos.

* _read_csv_ **(Ejercicio 1.1)**: leer un fichero CSV
* _clean_csv_ **(Ejercicio 1.2)**: limpia un dataset CSV eliminando las columnas innecesarias
* _rename_cols_ **(Ejercicio 1.3)**: renombrar una columnas
* _clean_states_ **(Ejercicio 5.2)**: limpia registros de estados no válidos en el dataset _us-state-populations.csv_

### Data_grouping

En esta carpeta, se encuentras las funciones de agrupación.

* _group_by_state_and_year_ **(Ejercicio 3.1)**: función que agrupa el primer dataset por año y estado de la unión.
* _print_biggest_handguns_ **(Ejercicio 3.2)**: muestra por pantalla el estadp y año con más armas de cinto registradas.
* _print_biggest_longguns_ **(Ejercicio 3.3)**: muestra por pantalla el estado y año con más armas largas registradas
* _group_by_state_ **(Ejercicio 5.1)**: recibe el input de la primera función de esta sección, desagrupa y agrupa solo por estado.

### Data_processing

Aquí encontramos las funciones de procesamiento estándares para los datasets.

* _breakdown_date_ **(Ejercicio 2.1)**: despliega la fecha del dataset en mes y año.
* _erase_month_ **(Ejercicio 2.2)**: deja caer la columna con fechas.
* _merge_datasets_ **(Ejercicio 5.3)**: combina los dos datasets por estado.

### Tests

Aquí están los diversos tests para varios de los procesos

* _TestFetching_: prueba las funciones de obtención de datos.
* _TestCleanCSV_: prueba las funciones de limpieza de datos.
* _TestDataProcessing_: prueba las funciones sobre el procesamiento de datos.
* _TestDataGrouping_: prueba las funciones que agrupan los datos
* _TestCleanMerge_: pruebas las funciones que combinan y luego limpian los dos sets de datos.

## Instalación

Para realizar la instalación vamos a seguir estos pasos.

### Por PyCharm

1. En primer lugar, hemos de descomprimir el proyecto si no lo hemos hecho ya.
2. Posteriormente, hemos de abrirlo con Pycharm como proyecto desde la carpeta que sale al descomprimir (Se recomienda hacerlo desde el Escritorio).
3. Pycharm debería de darnos la opción instantáneamente de crear un entorno virtual, donde le daríamos a aceptar. En caso contrario, si no aparece esta ventana, sigánse estos pasos. 
   4. Entrar en la terminal integrada dentro de Pycharm y escribir el siguiente comando. `$ virtualenv venv`. Esto creará un entorno virtual en la carpeta del proyecto.
   5. En caso de que no esté instalado virtualenv, se deberá instalar con `$ pip install virtualenv`
   6. Posteriormente se ha de activar con el comando `$ source venv/bin/activate`. También se puede escribir sencillamente `$ venv/bin/activate`.
7. Con el entorno activado, hemos de proceder al siguiente punto. Se han de instalar las librerías. Ya viene por defecto un archivo `requirements.txt` con todas las librerías requisito a instalar. Por tanto se ha de ejecutar el siguiente comando `pip install -r requirements.txt`
8. Con esto, el entorno debería estar funcionando y las librerías correctamente instaladas.

### Desde Terminal

1. En este caso, hemos de empezar por ejecutar `$ cd` hasta la carpeta donde de se encuentra este proyecto.
2. Posteriormente ejecutamos `$ virtualenv venv` y si no está instalado, instalarlo con `$ pip install virtualenv`.
3. Activamos el entorno virtual con el comando `$ source venv/bin/activate`.
4. Y finalmente ejecutamos `$ python main.py`

**ACLARACIÓN** Es posible que usando `pip`, salte un error de no haberse encontrado dicho manager dependiendo del proceso de instalación de python que se haya llevado a cabo. En ese caso, empléese los comandos anteriores con la forma `$ python -m pip ...` o `$ py3 -m pip ...` en su defecto. 