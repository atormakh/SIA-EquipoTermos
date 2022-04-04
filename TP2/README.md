# 72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022

## TP 2 : Algoritmos geneticos

### Instituto Tecnológico de Buenos Aires (ITBA)

## Autores (Equipo "Termos")

- [Agustin Tormakh](https://github.com/atormakh) - Legajo 60041
- [Valentino Riera Torraca](https://github.com/vriera) - Legajo 60212
- [Igal Leonel Revich](https://github.com/irevich) - Legajo 60390

## Indice

- [72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022](#7227-sistemas-de-inteligencia-artificial-1er-cuatrimestre-2022)
  - [TP 2 : Algoritmos geneticos](#tp-2--algoritmos-geneticos)
    - [Instituto Tecnológico de Buenos Aires (ITBA)](#instituto-tecnológico-de-buenos-aires-itba)
  - [Autores (Equipo "Termos")](#autores-equipo-termos)
  - [Indice](#indice)
  - [Descripcion del problema elegido](#descripcion-del-problema-elegido)
  - [Requerimientos previos](#requerimientos-previos)
  - [Instalacion y ejecucion](#instalacion-y-ejecucion)
  - [Guia de uso](#guia-de-uso)
    - [Archivos de configuracion](#archivos-de-configuracion)
      - [Parametros generales](#parametros-generales)
      - [genetic_properties](#genetic_properties)
      - [problem_properties](#problem_properties)
    - [Salida del programa](#salida-del-programa)
      - [Por consola](#por-consola)
      - [Por archivo](#por-archivo)
    - [Consideraciones adicionales](#consideraciones-adicionales)
  - [Ejemplos de configuracion](#ejemplos-de-configuracion)
    - [Ejemplo 1 :](#ejemplo-1-)
    - [Ejemplo 2 :](#ejemplo-2-)
    - [Ejemplo 3 :](#ejemplo-3-)

## Descripcion del problema elegido

El problema escogido para realizar este trabajo practico fue el primero que figura en el enunciado, el cual consiste en las mediciones de un reactivo a partir de un conjunto de valores de entrada ξ<sup>k</sup>, y cuyo resultado es un conjunto de valores ζ<sup>k</sup>, k = 1,2,3.

En este se busca aproximar los valores de salida para otras posibles entradas, por una funcion F(W,w,w<sub>0</sub>,ξ), donde W es un vector de tres coordenadas de numeros reales, w es una matriz de dimension 2 × 3 de numeros reales, y w<sub>0</sub> = (w<sub>01</sub>,w<sub>02</sub>) tambien de numeros reales, definiendose dicha funcion a partir de otra funcion g(x) que figura en el enunciado.A su vez, tambien se define una funcion de error que indica la diferencia entre los valores de ζ<sup>n</sup> y los calculados por la funcion F(W,w,w0,ξ)

El objetivo de este problema es utilizar algoritmos geneticos para calcular los valores de W, w y w0 que minimizan el error recientemente mencionado, para los datos de entrada ξ<sup>1</sup>, ξ<sup>2</sup>, ξ<sup>3</sup>

Para ello se decidio modelar a cada individuo de la poblacion de la siguiente manera : X = [W<sub>0</sub>,W<sub>1</sub>,W<sub>2</sub>,w<sub>11</sub>,w<sub>12</sub>,w<sub>13</sub>,w<sub>21</sub>,w<sub>22</sub>,w<sub>23</sub>,w<sub>01</sub>,w<sub>02</sub>], donde cada elemento del individuo es un <i>gen</i> del mismo

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

Para la configuracion de parametros del proyecto, se utiliza el archivo "config.json", ubicado en la carpeta "config". Dicho archivo contiene una serie de parametros a configurar para arrancar el algoritmo. Todos estos son obligatorios a menos que se especifique lo contrario. Se componen de 2 parametros generales, y luego se separan en dos grandes partes : "genetic_properties" (propiedades de algoritmo genetico) y "problem_properties" (propiedades del problema)

#### Parametros generales

Estos parametros son optativos y no son parte de las propiedades de los algoritmos geneticos ni del problema (es decir que abarcan a todo el algoritmo en general). Estos son :

- "all" : Es un string que indica que se ejecutaran todos los metodos de una determinada categoria, con todos los otros parametros fijos. Los valores que puede tomar son :
  - "SELECTION" = Se ejecutaran todos los metodos de seleccion disponibles (boltzmann,elite,rank,ruleta,torneos y truncada)
  - "CROSS" = Se ejecutaran todos los metodos de cruza disponibles (multiple, simple y uniforme)
  - "MUTATION" = Se ejecutaran todos los metodos de mutacion disponibles (es decir, se ejecutara un algoritmo por cada distribucion posible, siendo estas la gaussiana y la uniforme)
  - "FINISH_CONDITION" = Se ejecutaran todos los criterios de corte disponibles (solucion aceptable, contenido, cantidad de generaciones y tiempo)

  Algo importante a tener en cuenta de este parametro es que al setearse en el config.json, luego cada metodo a ejecutar utilizara el archivo de configuracion correspondiente dentro del directorio "config/exampleConfigs/CATEGORIA", siendo categoria el valor seteado en el parametro "all" en minusculas (por ejemplo, si se seteo en el config.json "all":"CROSS", luego cada metodo de cruza usara su json correspondiente dentro de la carpeta config/exampleConfigs/cross). Con lo cual, en caso de querer cambiarse alguno de los otros parametros que quedan fijos, estos deben cambiarse en el archivo de configuracion correspondiente y no el principal (por ejemplo, en el ejemplo anterior, si para la cruza multiple se quisiera que utilice el metodo de seleccion elite, debe modificarse el parametro correspondiente en el archivo de configuracion "multipleCross.json" y no en el "config.json")

- "random_seed" : Es un numero (entero o decimal), que sera utilizado como "semilla" de los distinos metodos random a usar dentro del algoritmo. Este sirve para repetir exactamente los mismos experimentos y obtener los mismos resultados al utilizar la misma semilla. De no incluirse en el json, el proceso se vuelve completamente aleatorio y no se aseguran los mismos resultados
  
#### genetic_properties

- "population_size" : Es un entero positivo que indica la cantidad de individuos que tendra cada generacion. Se requiere que sea mayor que 1 (caso contrario en caso de realizar el algoritmo sin reemplazo no se podra seleccionar 2 padres distintos para la nueva poblacion)
- "max_range_gen" : Es un entero positivo que determina el rango en el cual se tomara cada gen de los individuos de la generacion 0 (es decir que si por ejemplo toma como valor 10, cada gen tendra un valor aleatorio entre -10 y 10)
- "replacement" : Es un booleano (true/false) que indica si tanto la seleccion de padres del algoritmo como los distintos metodos de seleccion se haran con o sin reemplazo. Cabe aclarar que en estos ultimos es siempre y cuando exista la posibilidad en el metodo de seleccion elegido (ya que por ejemplo el metodo de seleccion ruleta o rank estan hechos para hacerse con reemplazo, con lo cual funcionaran asi aunque este parametro este en false)
- "cross" : Es un objeto que contiene distintos parametros correspondientes a los diferentes metodos de cruza. Estos son : 
  - "method" : Es un string que indica el metodo de cruza a utilizarse. Los valores que puede tomar son : 
    - "SIMPLE" = Cruza simple
    - "MULTIPLE" = Cruza multiple
    - "UNIFORM" = Cruza uniforme
  - "index_count" = Es un parametro obligatorio <b>unicamente</b> en caso de utilizar la cruza multiple. Es un entero positivo que indica la cantidad de indices a tomar en la cruza multiple. Este debe ir de 2 a 11 (limites incluidos)
- "mutation" : Es un objeto que contiene distintos parametros correspondientes a las diferentes mutaciones a aplicar. Estos son :
  - "method" : Es un string que indica la distribucion de probabilidad a utilizar en la mutacion. Sus valores posibles son :
    - "GAUSSIAN" : Distribucion Gaussiana
    - "UNIFORM" : Distribucion Uniforme
  - "probability" : Es un numero decimal que indica la probabilidad con la que ejecutara la mutacion. Esta debe estar entre 0 y 1 (limites incluidos)
  - "sigma" : Es un parametro obligatorio <b>unicamente</b> en caso de utilizar distribucion gaussiana. Es un numero decimal positivo que indica el valor del parametro utilizado para dicha distribucion
  - "a" : Es un parametro obligatorio <b>unicamente</b> en caso de utilizar distribucion uniforme. Es un numero decimal positivo que indica el valor del parametro utilizado para dicha distribucion
- "selection" : Es un objeto que contiene distintos parametros correspondientes a los diferentes metodos de seleccion. Estos son :
  - "method" : Es un string que indica el metodo de seleccion a utilizarse. Los valores que puede tomar son : 
    - "ELITE" = Metodo de seleccion <i>elite</i>
    - "RANK" = Metodo de seleccion <i>rank</i>
    - "ROULETTE" = Metodo de seleccion <i>ruleta</i>
    - "TOURNAMENTS" = Metodo de seleccion <i>torneos</i>
    - "TRUNCATED" = Metodo de seleccion <i>truncada</i>
    - "BOLTZMANN" = Metodo de seleccion <i>de Boltzmann</i>
  - "k" : Es un parametro obligatorio <b>unicamente</b> en caso de utilizar seleccion de Boltzmann o truncada. Si bien utilizan el mismo parametro, para cada uno signifca algo diferente y posee distintos requisitos :
    - En caso utilizar <i>Boltzmann</i> : 
      - Signifcado : Es el "k" correspondiente al e<sup>-kt</sup> dentro de la funcion de temperatura T(t).
      - Requisitos : Debe ser un numero entero o decimal entre 0 y 1 (limites incluidos)
    - En caso utilizar <i>Truncada</i> : 
      - Signifcado : Es la cantidad de malos individuos que descartara en el metodo (es decir, descartara a los peores "k")
      - Requisitos : Debe ser un numero entero y menor o igual al tamaño de poblacion indicado previamente ("poblation_size")
  - "u" : Es un parametro obligatorio <b>unicamente</b> en caso de utilizar seleccion por torneos. Es un numero decimal que indica el valor de umbral utilizado en dicho metodo, y debe estar entre 0.5 y 1 (limites incluidos)
  - "T0" : Es un parametro obligatorio <b>unicamente</b> en caso de utilizar seleccion de Boltzmann. Es un numero entero o decimal que indica la temperatura inicial que utilizara dicho metodo.
  - "Tc" : Es un parametro obligatorio <b>unicamente</b> en caso de utilizar seleccion de Boltzmann. Es un numero entero o decimal que indica la temperatura limite que utilizara dicho metodo, y esta debe ser menor o igual que la temperatura inicial previamente definida ("T0")
- "finish_condition" : Es un objeto que contiene distintos parametros correspondientes a los diferentes criterios de corte. Estos son :
  - "method" : Es un string que indica el criterio de corte a utilizarse. Los valores que puede tomar son : 
    - "GENERATION_SIZE" = Por cantidad de generaciones. Termina al generarse una cantidad "n" de generaciones (sin contar la generacion 0)
    - "TIME" = Por tiempo. Termina si el tiempo de ejecucion iguala o supera un tiempo limite
    - "CONTENT" = Por contenido. Termina si el maximo fitness no varia en una cantidad "n" de generaciones
    - "ACCEPTABLE_SOLUTION" = Por solucion aceptable. Termina si encuentra un individuo cuyo error sea cercano a 0 con una tolerancia especifica
  - "max_generation_size" : Parametro obligatorio <b>unicamente</b> en caso de utilizar el criterio de corte por cantidad de generaciones y por contenido. Es un numero entero positivo que corresponde al limite "n" de generaciones
  - "max_execution_time" : Parametro obligatorio <b>unicamente</b> en caso de utilizar el criterio de corte por tiempo. Es un numero entero positivo que indica el tiempo limite de ejecucion del algoritmo en segundos
  - "max_tolerance_exponent" : Parametro obligatorio <b>unicamente</b> en caso de utilizar el criterio de corte por solucion aceptable. Es un numero entero negativo y menor que 0 que corresponde al exponente de la tolerancia de error utilizada, de forma tal que la cota de error utilizada sea 10<sup>max_tolerance_exponent</sup>. Por ejemplo si esta se define como -8, la tolerancia utilizada para ver la cercania del error con 0 seria 10<sup>-8</sup>. Cabe aclarar que en caso de ingresarse y utilizar el criterio de corte por contenido, dicha tolerancia tambien sera utilizada, pero para dicho criterio este parametro no es obligatorio dado que en caso de no ingresarse, utiliza una tolerancia de error default (1e-9 o 10<sup>-9</sup>)
  
#### problem_properties

- "epsilon" : Es un objeto que contiene los valores correspondientes a la entrada de los reactivos (es decir que seria el ξ<sup>k</sup> mencionado en  la <a href="#descripcion-del-problema-elegido">descripcion del problema elegido</a> previamente ). Se compone de :
  - "epsilon_1" : Array de 3 numeros decimales (Seria ξ<sup>1</sup>)
  - "epsilon_2" : Array de 3 numeros decimales (Seria ξ<sup>2</sup>)
  - "epsilon_3" : Array de 3 numeros decimales (Seria ξ<sup>3</sup>)

- "c" : Es un array de 3 numeros enteros (ya que debe tener el mismo tamaño que los valores de entrada) que contiene los resultados del reactivo (es decir que seria el ζ<sup>k</sup> mencionado en  la <a href="#descripcion-del-problema-elegido">descripcion del problema elegido</a> previamente). Los valores pertenecientes a este array deben ser unicamente 0 o 1

### Salida del programa


#### Por consola


#### Por archivo

### Consideraciones adicionales

## Ejemplos de configuracion

### Ejemplo 1 : 

```
{

}
```

### Ejemplo 2 : 

```
{

}
```

### Ejemplo 3 : 

```
{

}
```

Para mas ejemplos, en la carpeta <i>exampleConfigs</i> hay ejemplos para los distintos metodos de seleccion y cruza, y los distintos tipos de mutacion y criterios de corte
