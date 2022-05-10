# 72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022

## TP 3 : Perceptron Simple y Multicapa

### Instituto Tecnológico de Buenos Aires (ITBA)

## Autores (Equipo "Termos")

- [Agustin Tormakh](https://github.com/atormakh) - Legajo 60041
- [Valentino Riera Torraca](https://github.com/vriera) - Legajo 60212
- [Igal Leonel Revich](https://github.com/irevich) - Legajo 60390

## Indice

- [72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022](#7227-sistemas-de-inteligencia-artificial-1er-cuatrimestre-2022)
  - [TP 3 : Perceptron simple y multicapa](#tp-3--perceptron-simple-y-multicapa)
    - [Instituto Tecnológico de Buenos Aires (ITBA)](#instituto-tecnológico-de-buenos-aires-itba)
  - [Autores (Equipo "Termos")](#autores-equipo-termos)
  - [Indice](#indice)
  - [Descripcion del problema](#descripcion-del-problema)
  - [Requerimientos previos](#requerimientos-previos)
  - [Instalacion y ejecucion](#instalacion-y-ejecucion)
  - [Guia de uso](#guia-de-uso)
    - [Archivos de configuracion](#archivos-de-configuracion)
      - [Parametros generales](#parametros-generales)
      - [neural_net](#neural_net)
      - [backtracking](#backtracking)
    - [Salida del programa](#salida-del-programa)
      - [Por consola](#por-consola)
      - [Graficos](#graficos)
    - [Ejecucion con Jupyter Notebook](#ejecucion-con-jupyter-notebook)
  - [Ejemplos de configuracion](#ejemplos-de-configuracion)
    - [Ejemplo 1 : Ejecucion con parametros para ejercicio 1](#ejemplo-1--ejecucion-con-los-parametros-para-el-ejercicio-1)
    - [Ejemplo 2 : Ejecucion con parametros para ejercicio 2](#ejemplo-2--ejecucion-con-los-parametros-para-el-ejercicio-2)
    - [Ejemplo 3 : Ejecucion con parametros para ejercicio 3](#ejemplo-3--ejecucion-con-los-parametros-para-el-ejercicio-33)

## Descripcion del problema

El objetivo de este trabajo es utilizar perceptrones simples y multicapa con aprendizaje para minimizar el error para diferentes datos de entrada. Se utiliza el metodo de backtracking para entrenar a la red en que se minimice el error.

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
  $ python app.py -t train.txt -o result.txt
  ```

  Siendo <i>train.txt</i> el conjunto de entrenamiento y <i>result.txt</i> la salida esperada. Estos archivos son obligatorios, y al pasarse al programa, se construiran conjuntos de entrenamientos y salida como una lista de listas, donde cada sublista es un array de elementos formados los pertenecientes a cada linea de los distintos archivos, separados por un espacio. Estos deben ser numeros decimales

  Ejecutando de dicha forma, el programa buscara el archivo de configuracion en el directorio "./config". En caso de mover el archivo de configuracion a otro directorio, debe ejecutarse de alguna de estas dos formas :

  ```
  $ python app.py -c PATH_TO_CONFIG_FILE/config.json -t train.txt -o result.txt

  $ python app.py --configPath PATH_TO_CONFIG_FILE/config.json --trainSetFile train.txt --outputSetFile output.txt
  ```

  Siendo PATH_TO_CONFIG_FILE el path hacia el archivo de configuracion

- Finalmente, para salir del virtual environment, debe ejecutarse

  ```
  $ deactivate
  ```

Cabe aclarar que estas instrucciones de ejecucion sirven unicamente para entrenar una red neuronal con las caracteristicas especificadas en el config.json (explicado en la seccion siguiente), y utilizando un trainingSet y resultSet determinados e interpretados como se explico recientemente. Para ejecutarse los respectivos ejercicios del trabajo practico ofrecemos un Jupyter notebook con distintas celdas de codigo correspondientes a los distintos ejercicios, explicadas en la seccion [Ejecucion con Jupyter Notebook](#ejecucion-con-jupyter-notebook)

## Guia de uso

### Archivos de configuracion

Para la configuracion de parametros del proyecto, se utiliza el archivo "config.json", ubicado en la carpeta "config". Dicho archivo contiene una serie de parametros a configurar para arrancar el algoritmo.

#### Parametros generales

Estos parametros son optativos y no son parte de las propiedades de los algoritmos geneticos ni del problema (es decir que abarcan a todo el algoritmo en general). Estos son :

- "random_seed" : Es un numero (entero o decimal), que sera utilizado como "semilla" de los distinos metodos random a usar dentro del algoritmo. Este sirve para repetir exactamente los mismos experimentos y obtener los mismos resultados al utilizar la misma semilla. De no incluirse en el json, el proceso se vuelve completamente aleatorio y no se aseguran los mismos resultados
- "max_epochs": Es un entero mayor que 0 que representa un limite superior que se le pone a algoritmo para que corte despues de esta cantidad de epocas en el caso de que no haya llegado a minimizar el error en el rango que se lo requiere.
- "max_tolerance_exponent": Es un numero entero que representa el exponente al cual 10 elevado al mismo de menor que el error actual de la red, que se utilizara como criterio de corte para el algoritmo.

#### neural_net

- "architecture" : Es un array de enteros, con longitud indeterminada en donde el primer elemento indica la cantidad de parametros de entrada tiene cada elemento del dataset que se le vaya a propagar a la red. Los elementos del medio son la cantidad de perceptrones que tendra cada capa oculta. El ultimo elemento del array indica la cantidad de salidas que tendra el programa, es importante que este numero sea el mismo que el numero de elementos que tiene cada entrada del resultset.
- "activation_function" : Es un objeto que contiene 1 o 2 parametros correspondientes a la funcion de activacion, estos son:
  - "type": Es un string que indica que funcion de activacion se desea tomar, las opciones posibles son:
    - "SIGMOIDAL": funcion logistica
    - "STEP": funcion escalon
    - "TANH": tangente hiperbolica
    - "LINEAL": funcion lineal que pasa por el origen
  - "beta": Es un float entre (0,1] que se le puede pasar como parametro a las funciones "SIGMOIDAL" y "TANH"

#### backtracking

- "learning_rate": Es un float que puede ir entre (0,1] que se utiliza al momento de calcular los cambios en los pesos que se le van a ir aplicando a los perceptrones en cada iteracion.

### Salida del programa

Al ejecutarse el programa se produce en linea de comando los resultados del entrenamiento de la red, explicados en detalle en la siguiente seccion. A su vez, se muestra el grafico de Error vs Epoch, que muestra como evoluciona el error de la red en cada epoca.

#### Por consola

Al ejecutarse un algoritmo determinado, por consola se observara una salida con las siguientes propiedades :

- "Configuration parameters" : Los parametros utilizados para el algoritmo del perceptron explicados previamente en <a href="#archivos-de-configuracion">archivos de configuracion</a>
- "Error" : El error de entrenamiento
- "Epoch" : La epoca donde corto el entrenamiento
- "Execution time" : El tiempo de ejecucion del algoritmo en segundos

#### Graficos

El grafico a mostrar consiste en el error en funcion de las epocas, y este se visualiza al finalizar el algoritmo. En caso de ejecutar el ejercicio 1 con Jupyter (explicado en la seccion posterior), se guarda en el directorio "results/graphs" un .gif con la animacion del plano de separacion del perceptron.

### Ejecucion con Jupyter Notebook

Dada la naturaleza diversa de los ejercicios que se piden implementar para el TP, se opto por crear metodos generales para utilizar redes neuronales, y hacer una implementacion de la resolucion customizada a las necesidades de cada ejercicio. Esto mismo se realizo un Jupyter Notebook, con la premisa de solo incluir funciones cuyo nombre sea auto explicativo y de alto nivel, lo cual nos permite en pocas lineas sintetizar la resolucion de un problema.

Para ello se comienza importando arriba de todo las dependencias que necesiten cualquiera de los ejercicios. Posterior a eso, se encuentran las celdas de cada ejercicio junto con su titulo, subtitulos y bloques de codigo, los cuales en general resultan en la generacion de un grafico pertinente a lo que pide el ejercicio.

## Ejemplos de configuracion

### Ejemplo 1 : Ejecucion con los parametros para el ejercicio 1

```json
{
  "neural_net": {
    "architecture": [2, 1],
    "activation_function": {
      "type": "STEP"
    }
  },
  "backtracking": {
    "learning_rate": 0.001
  },
  "max_epochs": 100,
  "max_tolerance_exponent": -12,
  "random_seed": 11
}
```

### Ejemplo 2 : Ejecucion con los parametros para el ejercicio 2

```json
{
  "random_seed": 11,
  "neural_net": {
    "architecture": [3, 1],
    "activation_function": {
      "type": "SIGMOIDAL",
      "beta": 0.6
    }
  },
  "backtracking": {
    "learning_rate": 0.01
  },
  "max_epochs": 300,
  "max_tolerance_exponent": -5
}
```

### Ejemplo 3 : Ejecucion con los parametros para el ejercicio 3.3

```json
{
  "neural_net": {
    "architecture": [35, 15, 15, 15, 10],
    "activation_function": {
      "type": "SIGMOIDAL",
      "beta": 0.45
    }
  },
  "backtracking": {
    "learning_rate": 0.1
  },
  "max_epochs": 100,
  "max_tolerance_exponent": -12
}
```

Para mas ejemplos, en la carpeta <i>config</i> hay ejemplos para los distintos configs que se utilizan para cada ejercicio.
