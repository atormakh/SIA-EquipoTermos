# 72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022

## Ej obligatorio 1 : Metodos de optimizacion no lineal

### Instituto Tecnológico de Buenos Aires (ITBA)

## Autores (Equipo "Termos")

- [Agustin Tormakh](https://github.com/atormakh) - Legajo 60041
- [Valentino Riera Torraca](https://github.com/vriera) - Legajo 60212
- [Igal Leonel Revich](https://github.com/irevich) - Legajo 60390

## Indice

- [72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022](#7227-sistemas-de-inteligencia-artificial-1er-cuatrimestre-2022)
  - [Ej obligatorio 1 : Metodos de optimizacion no lineal](#ej-obligatorio-1--metodos-de-optimizacion-no-lineal)
    - [Instituto Tecnológico de Buenos Aires (ITBA)](#instituto-tecnológico-de-buenos-aires-itba)
  - [Autores (Equipo "Termos")](#autores-equipo-termos)
  - [Indice](#indice)
  - [Descripcion del problema](#descripcion-del-problema)
  - [Requerimientos previos](#requerimientos-previos)
  - [Instalacion y ejecucion](#instalacion-y-ejecucion)
  - [Guia de uso](#guia-de-uso)
    - [Archivos de configuracion](#archivos-de-configuracion)
      - [Parametros generales](#parametros-generales)
      - [optimization_properties](#optimization_properties)
      - [problem_properties](#problem_properties)
    - [Salida del programa](#salida-del-programa)
      - [Por consola](#por-consola)
      - [Graficos](#graficos)
  - [Ejemplos de configuracion](#ejemplos-de-configuracion)
    - [Ejemplo 1 : Metodo de Gradientes conjugados (CG)](#ejemplo-1--metodo-de-gradientes-conjugados-cg)
    - [Ejemplo 2 : Metodo de ADAM, con una seed=10 para el random](#ejemplo-2--metodo-de-adam-con-una-seed10-para-el-random)
    - [Ejemplo 3 : Ejecucion de todos los metodos de optimizacion con una seed=10](#ejemplo-3--ejecucion-de-todos-los-metodos-de-optimizacion-con-una-seed10)

## Descripcion del problema

El problema es el mismo que se eligio para el TP 2 de la materia, el cual
consistia en las mediciones de un reactivo a partir de un conjunto de valores de entrada ξ<sup>k</sup>, y cuyo resultado es un conjunto de valores ζ<sup>k</sup>, k = 1,2,3.

En este se buscaba aproximar los valores de salida para otras posibles entradas, por una funcion F(W,w,w<sub>0</sub>,ξ), donde W es un vector de tres coordenadas de numeros reales, w es una matriz de dimension 2 × 3 de numeros reales, y w<sub>0</sub> = (w<sub>01</sub>,w<sub>02</sub>) tambien de numeros reales, definiendose dicha funcion a partir de otra funcion g(x) que figuraba en el enunciado.A su vez, tambien se definia una funcion de error que indica la diferencia entre los valores de ζ<sup>n</sup> y los calculados por la funcion F(W,w,w0,ξ)

El objetivo de este ejercicios es utilizar ciertos metodos de optimizacion no lineal vistos en clase para calcular los valores de W, w y w<sub>0</sub> que minimizan el error recientemente mencionado, para los datos de entrada ξ<sup>1</sup>, ξ<sup>2</sup>, ξ<sup>3</sup>

Los metodos a utilizar son: 
  - Gradiente descendiente (GD)
  - Gradientes conjugados (CG)
  - Adam

## Requerimientos previos

Para la instalacion y ejecucion de este proyecto (explicados posteriormente), son necesarios los siguientes requerimientos :

- Python (Version **3.8** o superior)

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

Para la configuracion de parametros del proyecto, se utiliza el archivo "config.json", ubicado en la carpeta "config". Dicho archivo contiene una serie de parametros a configurar para arrancar el algoritmo. Todos estos son obligatorios a menos que se especifique lo contrario. Este posee un parametro general, y luego se separan en dos grandes partes : "optimization_properties" (propiedades de algoritmo de optimizacion) y "problem_properties" (propiedades del problema)

#### Parametros generales

Estos parametros son optativos y no son parte de las propiedades de los algoritmos de optimizacion ni del problema (es decir que abarcan a todo el algoritmo en general). Estos son :

- "random_seed" : Es un numero (entero o decimal), que sera utilizado como "semilla" de los distinos metodos random a usar dentro del algoritmo. Este sirve para repetir exactamente los mismos experimentos y obtener los mismos resultados al utilizar la misma semilla. De no incluirse en el json, el proceso se vuelve completamente aleatorio y no se aseguran los mismos resultados
  
#### optimization_properties

- "method" : Es un string que indica el metodo de optimizacion utilizado. Los valores que puede tomar son :
  - "GD" = Gradiente descendiente
  - "CG" = Gradientes conjugados
  - "ADAM" = Adam
  - "ALL" = Ejecuta todos los metodos de optimizacion mencionados anteriormente
- "max_range_gen" : Es un entero positivo que determina el rango en el cual se tomaran los valores de W, w y w<sub>0</sub> para el conjunto inicial (es decir que si por ejemplo toma como valor 10, cada uno tendra un valor aleatorio entre -10 y 10)
  
#### problem_properties

- "epsilon" : Es un objeto que contiene los valores correspondientes a la entrada de los reactivos (es decir que seria el ξ<sup>k</sup> mencionado en  la <a href="#descripcion-del-problema">descripcion del problema</a> previamente ). Se compone de :
  - "epsilon_1" : Array de 3 numeros decimales (Seria ξ<sup>1</sup>)
  - "epsilon_2" : Array de 3 numeros decimales (Seria ξ<sup>2</sup>)
  - "epsilon_3" : Array de 3 numeros decimales (Seria ξ<sup>3</sup>)

- "c" : Es un array de 3 numeros enteros (ya que debe tener el mismo tamaño que los valores de entrada) que contiene los resultados del reactivo (es decir que seria el ζ<sup>k</sup> mencionado en  la <a href="#descripcion-del-problema">descripcion del problema</a> previamente). Los valores pertenecientes a este array deben ser unicamente 0 o 1

### Salida del programa

Al ejecutarse el programa se produce una salida por consola. A su vez, en caso de utilizar el ALL en el "method", se producen 2 graficos, cuyo contenido se especificara posteriormente

#### Por consola

Al ejecutarse un algoritmo determinado, por consola se observara una salida con las siguientes propiedades :

- "Configuration parameters" : Los parametros utilizados para el algoritmo genetico explicados previamente en <a href="#archivos-de-configuracion">archivos de configuracion</a>
- "Solution" : Contiene las distintas componentes de la solucion encontrada por el algoritmo, estas son :
  - "Optimal individual" : Es el individuo optimo (es decir, el que minimiza la funcion de error). En este se pueden observar sus respectivos valores, y ciertas propiedades como :
    - "F(i)": El valor de la funcion F(W,w,w0,ξ) enunciada en la <a href="#descripcion-del-problema">descripcion del problema</a> de los valores del individuo optimo
    - "E(i)" : El error del invidivuo optimo
- "Execution time" : El tiempo de ejecucion del algoritmo en segundos

#### Graficos



## Ejemplos de configuracion

### Ejemplo 1 : Metodo de Gradientes conjugados (CG)

```json
{ 
    "optimization_properties": {
      "method": "CG",
      "max_range_gen":10
    },
    "problem_properties": {
      "epsilon": {
        "epsilon_1": [4.4793, -4.0765, -4.0765],
        "epsilon_2": [-4.1793, -4.9218, 1.7664],
        "epsilon_3": [-3.9429, -0.7689, 4.883]
      },
      "c": [0, 1, 1]
    }
}
  
```

### Ejemplo 2 : Metodo de ADAM, con una seed=10 para el random

```json
{ 
    "random_seed" : 10,
    "optimization_properties": {
      "method": "ADAM",
      "max_range_gen":10
    },
    "problem_properties": {
      "epsilon": {
        "epsilon_1": [4.4793, -4.0765, -4.0765],
        "epsilon_2": [-4.1793, -4.9218, 1.7664],
        "epsilon_3": [-3.9429, -0.7689, 4.883]
      },
      "c": [0, 1, 1]
    }
}
  
```

### Ejemplo 3 : Ejecucion de todos los metodos de optimizacion con una seed=10

```json
{ 
    "random_seed" : 10,
    "optimization_properties": {
      "method": "ALL",
      "max_range_gen":10
    },
    "problem_properties": {
      "epsilon": {
        "epsilon_1": [4.4793, -4.0765, -4.0765],
        "epsilon_2": [-4.1793, -4.9218, 1.7664],
        "epsilon_3": [-3.9429, -0.7689, 4.883]
      },
      "c": [0, 1, 1]
    }
}
  
```

Para mas ejemplos, en la carpeta <i>exampleConfigs</i> hay ejemplos para los distintos metodos de seleccion y cruza, y los distintos tipos de mutacion y criterios de corte
