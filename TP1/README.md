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

- [search_properties](#search_properties)

## Descripcion del problema elegido

El problema escogido para realizar este trabajo practico fue el de las "Torres de Hanoi". Este consiste en una cantidad positiva de discos (disks) de distinto peso y 3 postes (towers), donde uno de ellos es considerado el "poste destino" (destination tower). El objetivo del juego es que partiendo de una situacion inicial donde los discos estan apilados de mayor a menor peso en uno de los postes que no es el destino, apilarlos todos en este ultimo poste, movimiento unicamente los discos que estan en el tope de un poste, a otro donde en su tope haya un disco de peso mayor, o este vacio.

Algo importante a destacar es que si bien el juego considera el caso de todos los discos apilados en un poste que no sea el destino como unica situacion inicial, en nuestra implementacion permitimos que el estado inicial sea cualquier estado valido, es decir, todos los discos distribuidos entre los 3 postes, donde en cada uno esten apilados de mayor a menor peso.

## Requerimientos previos

Para la instalacion y ejecucion de este proyecto (explicados posteriormente), son necesarios los siguientes requerimientos :

- Python (Version **3.10** o superior)

## Instalacion y ejecucion

Una vez descargado el proyecto, y posicionado en la carpeta raiz del mismo, dentro de una terminal se ejecuta lo siguiente (tener en cuenta que los comandos que sean de la forma "pyhton . . .", en caso de no funcionar, deben hacerse de la forma "python3 . . .") :

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
$ pyhton app.py
```

Ejecutando de dicha forma, el programa buscara el archivo de configuracion en el directorio "./config". En caso de mover el archivo de configuracion a otro directorio, debe ejecutarse de alguna de estas dos formas :

```
$ pyhton app.py -c PATH_TO_CONFIG_FILE/config.json

$ pyhton app.py --config PATH_TO_CONFIG_FILE/config.json
```

Siendo PATH_TO_CONFIG_FILE el path hacia el archivo de configuracion

- Finalmente, para salir del virtual environment, debe ejecutarse

```
$ deactivate
```

## Guia de uso

Para la configuracion de parametros del proyecto, se utiliza el archivo "config.json", ubicado en la carpeta "config". Dicho archivo contiene una serie de parametros a configurar para arrancar el juego, separados en dos grandes partes : "search_properties" (propiedades de busqueda) y "game_properties" (propiedades del juego)

Ejemplo:

```
{
  "search_properties": {
    "search_method": "BPPV",
    "max_height_bppv": 4,
    "growth_factor_bppv": 1,
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

### search_properties

- "search_method" : Es un string que indica el metodo de busqueda utilizado. Los valores que puede tomar son :

- "BPP" = Busqueda primero en profundidad

- "BPA" = Busqueda primero a lo ancho

- "BPPV" = Busqueda primero en profundidad con altura variable sin retroceso

- "BPPVO" = Busqueda primero en profundidad con altura variable con retroceso

- "HL" = Busqueda heuristica local

- "HG" = Busqueda heuristica global

- "A*" = Busqueda por algoritmo A*

- "F" = Igual al A\*, pero con peso (weight) variable
