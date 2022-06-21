# 72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022

## TP 5 : Deep Learning

### Instituto Tecnológico de Buenos Aires (ITBA)

## Autores (Equipo "Termos")

- [Agustin Tormakh](https://github.com/atormakh) - Legajo 60041
- [Valentino Riera Torraca](https://github.com/vriera) - Legajo 60212
- [Igal Leonel Revich](https://github.com/irevich) - Legajo 60390

## Indice

- [72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022](#7227-sistemas-de-inteligencia-artificial-1er-cuatrimestre-2022)
  - [TP 5 : Deep Learning](#tp-5--deep-learning)
    - [Instituto Tecnológico de Buenos Aires (ITBA)](#instituto-tecnológico-de-buenos-aires-itba)
  - [Autores (Equipo "Termos")](#autores-equipo-termos)
  - [Indice](#indice)
  - [Descripcion del problema](#descripcion-del-problema)
    - [Ejercicio 1.A](#ejercicio-1.A)
    - [Ejercicio 1.B](#ejercicio-1.B)
    - [Ejercicio 2](#ejercicio-2)
  - [Requerimientos previos](#requerimientos-previos)
  - [Instalacion y ejecucion](#instalacion-y-ejecucion)
  - [Guia de uso](#guia-de-uso)
    - [Archivos de configuracion](#archivos-de-configuracion)
    - [Ejecucion con Jupyter Notebook](#ejecucion-con-jupyter-notebook)
  - [Ejemplos de configuracion](#ejemplos-de-configuracion)
    - [Ejemplo 1 : Ejecucion con 3 capas ocultas entre encoder y decoder](#ejemplo-1--ejecucion-con-3-capas-ocultas-entre-encoder-y-decoder)
    - [Ejemplo 2 : Ejecucion con 1 capa oculta entre encoder y decoder](#ejemplo-ejecucion-con-arquitecturas-con-1-capa-oculta-entre-encoder-y-decoder)

## Descripcion del problema

En este trabajo practico se implementa un autoencoder con librerias de optimizacion.

### Ejercicio 1.A

Implementar un autoencoder basico para aprender un dataset de letras de tamano 7x5 y explorar el espacio latente generado.

### Ejercicio 1.B

Implementar un denoising autoencoder para eliminar ruido del dataset de letras de tamano 7x5.

### Ejercicio 2

Explorar la capacidad generativa del autoencoder, y solucionar el problema de representacion del espacio latente (Autoencoder variacional)

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

- Una vez hecho esto, el proyecto esta listo para ser ejecutado. Para hacer esto se deben seguir las instrucciones indicadas en la siguiente seccion [Guia de uso](#guia-de-uso)

## Guia de uso

Para ejecutar los ejercicios del trabajo practico, se cuentan con los siguientes Jupyter notebook, uno para cada red, y por ende para su ejercicio correspondiente:

- <i>TP5.ipynb</i> (Ejercicio 1a y 1b)
- <i>Vae.ipynb</i> (Ejercicio 2)

Para la configuracion de parametros del proyecto, ambos utilizan el archivo "config.json", ubicado en la carpeta "config". Dicho archivo contiene una serie de parametros a configurar para arrancar la ejecucion correspondiente.

A continuacion se explicara la estructura de dicho archivo, y las instrucciones generales para ejecutar cualquiera de los 2 notebook.

### Archivos de configuracion

El config.json cuenta con los siguientes parametros:

- "random_seed" : Es un numero (entero o decimal), que sera utilizado como "semilla" de los distinos metodos random a usar dentro del algoritmo. Este sirve para repetir exactamente los mismos experimentos y obtener los mismos resultados al utilizar la misma semilla. De no incluirse en el json, el proceso se vuelve completamente aleatorio y no se aseguran los mismos resultados
- "max_epochs": Es un entero mayor que 0 que representa un limite superior que se le pone a algoritmo para que corte despues de esta cantidad de epocas en el caso de que no haya llegado a minimizar el error en el rango que se lo requiere.
- "font": Indica la font a utilizar. Este puede tomar los siguientes valores:
  - FONT1
  - FONT2
  - FONT3
- "noise_probability": Es un numero (decimal) entre 0 y 1, que se utiliza para indicar la probabilidad uniforme con la cual se modifical al caracter con el cual se entrena.
- "noise_range": Es un numero positivo que indica el rango limite en el cual se tomara el numero con distribucion uniforme para agregarle ruido a las letras.

- "neural_net:

  - "architecture" : Es un array de enteros, con longitud indeterminada en donde el primer elemento indica la cantidad de parametros de entrada tiene cada elemento del dataset que se le vaya a propagar a la red. Los elementos del medio son la cantidad de perceptrones que tendra cada capa oculta. El ultimo elemento del array indica la cantidad de salidas que tendra el programa, es importante que este numero sea el mismo que el numero de elementos que tiene cada entrada del resultset. Dado que se trata de un autoencoder, a diferencia del TP 3, debe cumplir los siguientes requisitos adicionales:
    - Debe tener longitud impar
    - Debe ser espejada
  - "activation_function" : Es un objeto que contiene la descripcion de la funcion de activacion que se usa para :
    - encoder
    - latent_space
    - decoder
    en donde para especificar esta configuracion se deben indicar 1 o 2 parametros correspondientes a la funcion de activacion, estos son:
    - "type": Es un string que indica que funcion de activacion se desea tomar, las opciones posibles son:
      - "SIGMOIDAL": funcion logistica
      - "STEP": funcion escalon
      - "TANH": tangente hiperbolica
      - "LINEAL": funcion lineal que pasa por el origen
      - "RELU": funcion constante en 0 en los negativos y lineal pasando por el origen, a partir de que x se vuelve positivo
    - "beta": Es un float entre (0,1] que se le puede pasar como parametro a las funciones "SIGMOIDAL" y "TANH"

### Ejecucion con Jupyter Notebook

Para cada uno de los ejercicios se comienza importando arriba de todo las dependencias necesarias. Posterior a eso, se encuentran las celdas correspondientes a cada notebook junto con su titulo, subtitulos y bloques de codigo. Cada celda se ejecuta con el boton de <i>Execute cell</i>, y tambien pueden ejecutarse todos los bloques de forma secuencial mediante el boton <i>Run all</i>. En caso de que se quiera limpiar las salidas de ejecuciones anteriores, apretar el boton <i>Clear ouputs of all cells</i>

Algo importante a tener en cuenta es que algunas celdas de codigo para poder ser ejecutadas con exito necesitan la ejecucion de celdas anteriores, con lo cual, a la hora de probar la ejecucion de una determinada celda de codigo, tener en cuenta dichas dependencias, y en dicho caso, ejecutar la celda previa que corresponda

Como se dijo anteriormente, cada uno de los notebook posee sus propios parametros de configuracion, los cuales son explicados a continuacion:

## Ejemplos de configuracion

### Ejemplo 1 : Ejecucion con arquitecturas con 3 capas ocultas entre encoder y decoder

```json
{
  "random_seed": 11,
  "neural_net": {
    "architecture": [35, 25, 15, 10, 2, 10, 15, 25, 35],
    "activation_function": {
      "encoder": {
        "type": "RELU"
      },
      "latent_space": {
        "type": "LINEAL"
      },
      "decoder": {
        "type": "SIGMOIDAL",
        "beta": 0.8
      }
    }
  },
  "max_epochs": 1000,
  "font": "FONT2",
  "noise_probability": 0.1
}
```

### Ejemplo 2 : Ejecucion con arquitecturas con 1 capa oculta entre encoder y decoder

```json
{
  "neural_net": {
    "architecture": [35, 10, 2, 10, 35],
    "activation_function": {
      "encoder": {
        "type": "RELU"
      },
      "latent_space": {
        "type": "LINEAL"
      },
      "decoder": {
        "type": "SIGMOIDAL",
        "beta": 0.8
      }
    }
  },
  "max_epochs": 1000,
  "font": "FONT2",
  "noise_probability": 0.1
}
```
