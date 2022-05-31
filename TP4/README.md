# 72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022

## TP 4 : Metodos de aprendizaje no supervisado

### Instituto Tecnológico de Buenos Aires (ITBA)

## Autores (Equipo "Termos")

- [Agustin Tormakh](https://github.com/atormakh) - Legajo 60041
- [Valentino Riera Torraca](https://github.com/vriera) - Legajo 60212
- [Igal Leonel Revich](https://github.com/irevich) - Legajo 60390

## Indice

- [72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022](#7227-sistemas-de-inteligencia-artificial-1er-cuatrimestre-2022)
  - [TP 4 : Metodos de aprendizaje no supervisado](#tp-4--metodos-de-aprendizaje-no-supervisado)
    - [Instituto Tecnológico de Buenos Aires (ITBA)](#instituto-tecnológico-de-buenos-aires-itba)
  - [Autores (Equipo "Termos")](#autores-equipo-termos)
  - [Indice](#indice)
  - [Descripcion del problema](#descripcion-del-problema)
    - [Ejercicio 1](#ejercicio-1)
    - [Ejercicio 2](#ejercicio-2)
  - [Requerimientos previos](#requerimientos-previos)
  - [Instalacion y ejecucion](#instalacion-y-ejecucion)
  - [Guia de uso](#guia-de-uso)
    - [Ejecucion con Jupyter Notebook](#ejecucion-con-jupyter-notebook)
      - [Kohonen](#kohonen)
      - [Regla de oja](#regla-de-oja)
      - [Hopfield](#hopfield)
  - [Ejemplos de configuracion](#ejemplos-de-configuracion)
    - [Ejemplo 1 : Ejecucion con parametros para Kohonen](#ejemplo-1--ejecucion-con-parametros-para-kohonen)
    - [Ejemplo 2 : Ejecucion con parametros para Regla de Oja](#ejemplo-2--ejecucion-con-parametros-para-regla-de-oja)
    - [Ejemplo 3 : Ejecucion con parametros para Hopfield](#ejemplo-3--ejecucion-con-parametros-para-hopfield)


## Descripcion del problema

En este trabajo practico se contaban con distintos problemas dependiendo del ejercicio en cuestion. A continuacion se enuncian los mismos para cada uno:

### Ejercicio 1

Al igual que el ejercicio obligatorio 2, se cuenta con un archivo csv (<i>europe.csv</i>) con con características económicas, sociales y geográficas de 28 países de Europa, las cuales son:
- Area
- GDP
- Inflacion
- Expectativa de vida
- Fuerzas armadas
- Crecimiento de la poblacion
- Desempleo

El objetivo de este ejercicio, en el caso del item a, consiste en procesar dichos datos mediante una red de Kohonen, y analizar la agrupacion generada por la misma teniendo en cuenta sus diversos parametros. En cuanto al item b, se debe aplicar la Regla de Oja a partir de estos datos, con el objetivo de calcular una aproximacion de la primera componente principal de cada pais, y compararla con la calculada en el ejercicio obligatorio

### Ejercicio 2

Para este ejercicio, primero debian armarse distintas matrices de 5x5 con 1s y -1s, donde cada una representa una letra del alfabeto.

Una vez hecho eso, el objetivo consiste en utilizar la red de Hopfield con 4 de esas letras como "patrones almacenados", y pasarle una ellas donde previamente se le aplico ruido con cierta probabilidad, y a partir de ello, ver si converge a uno de los patrones, o termina siendo un estado espureo

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

- <i>kohonen_nb.ipynb</i> (Ejercicio 1a)
- <i>oja_nb.ipynb</i> (Ejercicio 1b)
- <i>hopfield.ipynb</i> (Ejercicio 2)

A continuacion se explicaran las instrucciones generales para ejecutar cualquiera de los 3, y posteriormente por cada uno se especificaran sus respectivos parametros de configuracion, situados para cada notebook en la segunda celda de codigo

### Ejecucion con Jupyter Notebook

Para cada uno de los ejercicios se comienza importando arriba de todo las dependencias necesarias. Posterior a eso, se encuentran las celdas correspondientes a cada notebook junto con su titulo, subtitulos y bloques de codigo. Cada celda se ejecuta con el boton de <i>Execute cell</i>, y tambien pueden ejecutarse todos los bloques de forma secuencial mediante el boton <i>Run all</i>. En caso de que se quiera limpiar las salidas de ejecuciones anteriores, apretar el boton <i>Clear ouputs of all cells</i>

Algo importante a tener en cuenta es que algunas celdas de codigo para poder ser ejecutadas con exito necesitan la ejecucion de celdas anteriores, con lo cual, a la hora de probar la ejecucion de una determinada celda de codigo, tener en cuenta dichas dependencias, y en dicho caso, ejecutar la celda previa que corresponda

Como se dijo anteriormente, cada uno de los notebook posee sus propios parametros de configuracion, los cuales son explicados a continuacion:

#### Kohonen

La celda de codigo correspondiente a la configuracion posee un diccionario llamado <i>kohonenProperties</i> con las siguientes propiedades:

- "seed" : Indica la semilla a utilizar para los random ejecutados a lo largo del ejercicio. Este parametro es optativo, y en caso de no setearse, en cada ejecucion se tomara una distinta al azar.
- "maxEpochs" : Numero entero que indica la maxima cantidad de epocas que se entrenara a la red
- "k" : Numero natural que indica la dimension de la matriz de neuronas de salida (k x k)
- "r0" : Numero natural que indica el radio inicial a utilizar
- "initialLearningRate" : Numero decimal que indica la taza de aprendizaje inicial a utilizar

#### Regla de oja

La celda de codigo correspondiente a la configuracion posee un diccionario llamado <i>ojaProperties</i> con las siguientes propiedades:

- "seed" : Indica la semilla a utilizar para los random ejecutados a lo largo del ejercicio. Este parametro es optativo, y en caso de no setearse, en cada ejecucion se tomara una distinta al azar.
- "epochs" : Numero entero que indica la cantidad de epocas que se entrenara a la red
- "learningRate" : Numero decimal que indica la taza de aprendizaje a utilizar

#### Hopfield

La celda de codigo correspondiente a la configuracion posee un diccionario llamado <i>hopfieldProperties</i> con las siguientes propiedades:

- "seed" : Indica la semilla a utilizar para los random ejecutados a lo largo del ejercicio. Este parametro es optativo, y en caso de no setearse, en cada ejecucion se tomara una distinta al azar.
- "noiseProbability" : Numero decimal entre 0 y 1 que indica la probabilidad de ruido a utilizar
- "lettersCombo" : Array de 4 letras que indica los patrones que almacenara la red

## Ejemplos de configuracion

### Ejemplo 1 : Ejecucion con parametros para Kohonen

```python
kohonenProperties = {
    'maxEpochs':3500,
    'k':4,
    'r0':4,
    'initialLearningRate':0.1
}
```

### Ejemplo 2 : Ejecucion con parametros para Regla de Oja

```python
ojaProperties = {
    'seed':10,
    'epochs':5000,
    'learningRate':0.0001
}
```

### Ejemplo 3 : Ejecucion con parametros para Hopfield

```python
hopfieldProperties = {
    'noiseProbability':0.2,
    'lettersCombo': ['v','t','r','q'],
}
```



