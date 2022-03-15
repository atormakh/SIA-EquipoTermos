# 72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022

## TP 1 : Metodos de Busqueda

### Instituto Tecnológico de Buenos Aires (ITBA)

## Autores (Equipo "Termos")

- [Agustin Tormakh](https://github.com/atormakh) - Legajo 60041
- [Valentino Riera Torraca](https://github.com/vriera) - Legajo 60212
- [Igal Leonel Revich](https://github.com/irevich) - Legajo 60390

## Indice

- [72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022](#7227-sistemas-de-inteligencia-artificial-1er-cuatrimestre-2022)
  - [TP 1 : Metodos de Busqueda](#tp-1--metodos-de-busqueda)
    - [Instituto Tecnológico de Buenos Aires (ITBA)](#instituto-tecnológico-de-buenos-aires-itba)
  - [Autores (Equipo "Termos")](#autores-equipo-termos)
  - [Indice](#indice)
  - [Descripcion del problema elegido](#descripcion-del-problema-elegido)
  - [Requerimientos previos](#requerimientos-previos)
  - [Instalacion y ejecucion](#instalacion-y-ejecucion)
  - [Guia de uso](#guia-de-uso)
    - [Archivos de configuracion](#archivos-de-configuracion)
      - [search_properties](#search_properties)
      - [game_properties](#game_properties)
    - [Salida del programa](#salida-del-programa)
      - [Por consola](#por-consola)
      - [Por archivo](#por-archivo)
  - [Ejemplos de configuracion](#ejemplos-de-configuracion)
    - [Ejemplo 1 : Configuracion para BPA, con 7 discos y poste destino = 3](#ejemplo-1--configuracion-para-bpa-con-7-discos-y-poste-destino--3)
    - [Ejemplo 2 : Configuracion para A\*, usando FHF como funcion heuristica, 7 discos y poste destino = 2](#ejemplo-2--configuracion-para-a-usando-fhf-como-funcion-heuristica-7-discos-y-poste-destino--2)
    - [Ejemplo 3 : Configuracion para BPPVO, usando 5 como altura maxima inicial, 2 como factor de crecimiento, 7 discos y poste destino = 1](#ejemplo-3--configuracion-para-bppvo-usando-5-como-altura-maxima-inicial-2-como-factor-de-crecimiento-7-discos-y-poste-destino--1)

## Descripcion del problema elegido

El problema escogido para realizar este trabajo practico fue el de las "Torres de Hanoi". Este consiste en una cantidad positiva de discos (disks) de distinto peso y 3 postes (towers), donde uno de ellos es considerado el "poste destino" (destination tower). El objetivo del juego es que partiendo de una situacion inicial donde los discos estan apilados de mayor a menor peso en uno de los postes que no es el destino, apilarlos todos en este ultimo poste, movimiento unicamente los discos que estan en el tope de un poste, a otro donde en su tope haya un disco de peso mayor, o este vacio.

Algo importante a destacar es que si bien el juego considera el caso de todos los discos apilados en un poste que no sea el destino como unica situacion inicial, en nuestra implementacion permitimos que el estado inicial sea cualquier estado valido, es decir, todos los discos distribuidos entre los 3 postes, donde en cada uno esten apilados de mayor a menor peso.

## Requerimientos previos

Para la instalacion y ejecucion de este proyecto (explicados posteriormente), son necesarios los siguientes requerimientos :

- Python (Version **3.10** o superior)

## Instalacion y ejecucion

Una vez descargado el proyecto, y posicionado en la carpeta raiz del mismo, dentro de una terminal se ejecuta lo siguiente (tener en cuenta que los comandos que sean de la forma "python . . .", en caso de no funcionar, deben hacerse de la forma "python3 . . .") :

- Primero, para verificar que la version de Python corresponda con la especificada anteriormente, ejecutar

```
$ python --version
```

- Luego, para introducirse en el virtual environment del proyecto debe ejecutatse lo siguiente, dependiendo del sistema operativo utilizado

  - Linux/Mac

```
$ python -m venv venv/ (o python3 -m venv venv/ )

$ source venv/bin/activate
```

- Windows

```
$ pip install virtualenv

$ virtualenv --python PATH_TO_PYTHON venv (Siendo PATH_TO_PYTHON el path donde se encuentra el python.exe)

$ .\venv\Scripts\activate
```

- Una vez realizado esto, se descargan las dependencias a utilizar mediante el siguiente comando

```
$ pip install -r requirements.txt
```

- Una vez hecho esto, el proyecto esta listo para ser ejecutado. Para hacer esto en la terminal debe introducirse lo siguiente

```
$ python app.py
```

Ejecutando de dicha forma, el programa buscara el archivo de configuracion en el directorio "./config". En caso de mover el archivo de configuracion a otro directorio, debe ejecutarse de alguna de estas dos formas :

```
$ python app.py -c PATH_TO_CONFIG_FILE/config.json

$ python app.py --configPath PATH_TO_CONFIG_FILE/config.json
```

    Siendo PATH_TO_CONFIG_FILE el path hacia el archivo de configuracion

- Finalmente, para salir del virtual environment, debe ejecutarse

```
$ deactivate
```

## Guia de uso

### Archivos de configuracion

Para la configuracion de parametros del proyecto, se utiliza el archivo "config.json", ubicado en la carpeta "config". Dicho archivo contiene una serie de parametros a configurar para arrancar el juego, separados en dos grandes partes : "search_properties" (propiedades de busqueda) y "game_properties" (propiedades del juego)

#### search_properties

- "search_method" : Es un string que indica el metodo de busqueda utilizado. Los valores que puede tomar son :
  - "BPP" = Busqueda primero en profundidad
  - "BPA" = Busqueda primero a lo ancho
  - "BPPV" = Busqueda primero en profundidad con altura variable sin retroceso
  - "BPPVO" = Busqueda primero en profundidad con altura variable con retroceso
  - "HL" = Busqueda heuristica local
  - "HG" = Busqueda heuristica global
  - "A*" = Busqueda por algoritmo A*
  - "F" = Igual al A\*, pero con peso (weight) variable
  - "ALL" = Ejecuta todos los metodos de busqueda mencionados anteriormente
- "heuristic_function" : Es un string que indica la funcion heuristica a utilizar. Es obligatoria en caso de usar metodos de busqueda informados. Los valores que puede tomar son :
  - "FHF" = Primera funcion heuristica (admisible)
  - "SHF" = Segunda funcion heuristica (admisible)
  - "THF" = Tercera funcion heuristica (no admisible)
- "max_height_bppv" : Es un entero positivo que indica la primera maxima altura con la cual se explorara en los algoritmos BPPV y BPPVO recientemente mencionados. En caso de utilizar alguno de ellos, este parametro es obligatorio
- "growth_factor_bppv" : Es un entero positivo que indica cuanto va a aumentarse la altura para buscar la proxima solucion en caso de no haber sido previamente encontrada en los algoritmos BPPV y BPPVO recientemente mencionados. En caso de utilizar alguno de ellos, este parametro es obligatorio
- "weight" : Es un decimal positivo que se ocupa de ponderar la funcion f(), al utilizar el metodo de busqueda "F". Este debe estar en un rango de 0 a 1 (ambos extremos inclusive)

#### game_properties

- "disk_count" : Es un entero positivo que indica la cantidad de discos a utilizar. Su rango debe ser de 3 a 10 (ambos extremos inclusive)
- "initial_state" : Indica el estado inicial del juego. Esta compuesto por los 3 postes
  - "tower_1"
  - "tower_2"
  - "tower_3"
    Para ser un estado inicial valido debe cumplir las siguientes condiciones :
  - En caso de no estar vacio, cada poste debe contener un conjunto de enteros positivos ordenados descendentemente
  - Los elementos de todas los postes deben estar en el rango de 1 a la cantidad de discos especificada en el parametro anterior (ambos extremos inclusive)
  - La suma de los elementos de todas los postes debe ser igual a la cantidad de discos especificada en el parametro anterior
- "destination_tower" : Es un entero positivo que indica el poste destino del juego. Debe estar en el rango de 1 a 3 (ambos extremos inclusive)

En caso de que alguno de los parametros no cumpla las indicaciones previamente mencionadas, se mostrara en la consola un mensaje de error correspondiente

Algo importante a aclarar es que en caso de ejecutar el metodo de busqueda "ALL", para su funcionamiento este provee un archivo JSON de configuracion para cada metodo de busqueda ejecutado, con los mismos parametros mencionados anteriormente. Por ende, si en caso de ejecutarse de dicho modo se quisiera que cada metodo de busqueda se ejecute con parametros diferentes, lo que debe hacerse es dirigirse a la carpeta "exampleConfigs", y cambiar los parametros que correspondan (Por ejemplo, si se quisiera que en el ALL, el BPA corra con distinto estado inicial que el resto, debe modificarse el parametro correspondiente en el BPA.json)

### Salida del programa

Al ejecutarse un metodo de busqueda se producen 2 tipos de salidas : Por consola y por archivo. A su vez, por cada uno se grafica el arbol utilizado en un archivo .html, que podra ser visualizado en el navegador de preferencia. En caso de no abrise automaticamente, para verlo puede ejecutarse el siguiente comando :

```
$open graph.html
```

Siendo graph el grafico del arbol correspondiente al metodo de busqueda utilizada

#### Por consola

Al ejecutarse un metodo de busqueda determinado, por consola se observara una salida con las siguientes propiedades :

- "Configuration parameters" : Los parametros correspondientes al archivo de configuracion mecionado previamente
- "Search result" : Resultado de la busqueda, que indica si encontro una solucion ("Success") o no ("Fail")
- "Solution" : En caso de haber encontrado una solucion, contiene todos los estados desde el que etiqueta a la raiz del arbol correspondiente, hasta el estado objetivo
- "Solution cost" : El costo de la solucion
- "Solution height" : La profundidad de la solucion
- "Expanded nodes count" : Cantidad de nodos expandidos
- "Frontier nodes count" : Cantidad de nodos frontera
- "Execution time" : Tiempo de procesamiento (en segundos)

#### Por archivo

Ademas de la salida por consola mencionada anteriormente, tambien se produce una salida a dos archivos CSV, dentro de la carpeta "stats" :

- Al csv correspondiente al metodo ejecutado (por ejemplo BPP.csv)
- A un csv global (global.csv) con las estadisticas de todos los metodos de busqueda ejecutados
  Ambos documentos contienen las siguientes entradas :
  - "method" : Metodo de busqueda utilizado
  - "diskCount" : Cantidad de discos
  - "executionTime" : Tiempo de procesamiento (en segundos)
  - "solutionHeight" : Profundidad de la solucion
  - "expandedNodes" : Cantidad de nodos expandidos
  - "frontierNodes" : Cantidad de nodos frontera
  - "heuristic" : Funcion heuristica utilizada, entre las mencionadas previamente (o "None" en caso de usar un metodo de busqueda no informado

## Ejemplos de configuracion

### Ejemplo 1 : Configuracion para BPA, con 7 discos y poste destino = 3

```
{
  "search_properties": {
    "search_method": "BPA"
  },
  "game_properties": {
    "disk_count": 7,
    "initial_state": {
      "tower_1": [7,6,5,4,3,2,1],
      "tower_2": [],
      "tower_3": []
    },
    "destination_tower": 3
  }
}
```

### Ejemplo 2 : Configuracion para A\*, usando FHF como funcion heuristica, 7 discos y poste destino = 2

```
{
  "search_properties": {
    "search_method": "A*",
    "heuristic_function": "FHF"
  },
  "game_properties": {
    "disk_count": 7,
    "initial_state": {
      "tower_1": [7,6,5],
      "tower_2": [],
      "tower_3": [4,3,2,1]
    },
    "destination_tower": 2
  }
}
```

### Ejemplo 3 : Configuracion para BPPVO, usando 5 como altura maxima inicial, 2 como factor de crecimiento, 7 discos y poste destino = 1

```
{
  "search_properties": {
    "search_method": "BPPVO",
    "max_height_bppv": 5,
    "growth_factor_bppv": 2
  },
  "game_properties": {
    "disk_count": 7,
    "initial_state": {
      "tower_1": [],
      "tower_2": [7,6],
      "tower_3": [5,4,3,2,1]
    },
    "destination_tower": 2
  }
}
```

Para mas ejemplos, en la carpeta exampleConfigs hay ejemplos para distintos metodos de busqueda
