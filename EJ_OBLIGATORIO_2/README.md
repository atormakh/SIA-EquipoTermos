# 72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022

## Ej obligatorio 2 : Analisis de componentes principales

### Instituto Tecnológico de Buenos Aires (ITBA)

## Autores (Equipo "Termos")

- [Agustin Tormakh](https://github.com/atormakh) - Legajo 60041
- [Valentino Riera Torraca](https://github.com/vriera) - Legajo 60212
- [Igal Leonel Revich](https://github.com/irevich) - Legajo 60390

## Indice

- [72.27 Sistemas de Inteligencia Artificial 1er cuatrimestre 2022](#7227-sistemas-de-inteligencia-artificial-1er-cuatrimestre-2022)
  - [Ej obligatorio 2 : Analisis de componentes principales](#ej-obligatorio-2--analisis-de-componentes-principales)
    - [Instituto Tecnológico de Buenos Aires (ITBA)](#instituto-tecnológico-de-buenos-aires-itba)
  - [Autores (Equipo "Termos")](#autores-equipo-termos)
  - [Indice](#indice)
  - [Descripcion del problema](#descripcion-del-problema)
  - [Requerimientos previos](#requerimientos-previos)
  - [Instalacion y ejecucion](#instalacion-y-ejecucion)
  - [Guia de uso](#guia-de-uso)
    - [Archivos de configuracion](#archivos-de-configuracion)
    - [Ejecucion con Jupyter Notebook](#ejecucion-con-jupyter-notebook)


## Descripcion del problema

El problema consiste en que se posee un archivo csv (<i>europe.csv</i>) con con características económicas, sociales y geográficas de 28 países de Europa, las cuales son:
- Area
- GDP
- Inflacion
- Expectativa de vida
- Fuerzas armadas
- Crecimiento de la poblacion
- Desempleo

El objetivo del ejercicio es calcular las componentes principales para los distintos paises mediante el metodo de PCA utilizando alguna libreria, y realizar diversos analisis de la primera componente calculada

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

- Una vez hecho esto, el proyecto esta listo para ser ejecutado. Para hacer esto se deben seguir las instrucciones indicadas en la seccion [Ejecucion con Jupyter Notebook](#ejecucion-con-jupyter-notebook)

## Guia de uso

### Archivos de configuracion

Para este ejercicio se decidio no disponer de un archivo de configuracion

### Ejecucion con Jupyter Notebook

Al igual que en el TP 3, para este ejercicio se adopto la practica de utilizar un Jupyter Notebook para probar diversos casos de interes, una vez procesado los datos del csv y calculadas las componentes principales.

Por ende, para ejecutar el ejercicio se comienza importando arriba de todo las dependencias que necesiten cualquiera de los ejercicios. Posterior a eso, se encuentran las celdas de cada ejercicio junto con su titulo, subtitulos y bloques de codigo, los cuales en general resultan en la generacion de un grafico pertinente al caso a analizar. Cada celda se ejecuta con el boton de <i>Execute cell</i>, y tambien pueden ejecutarse todos los bloques de forma secuencial mediante el boton <i>Run all</i>. En caso de que se quiera limpiar las salidas de ejecuciones anteriores, apretar el boton <i>Clear ouputs of all cells</i>

Algo importante a tener en cuenta es que algunas celdas de codigo para poder ser ejecutadas con exito necesitan la ejecucion de celdas anteriores, con lo cual, a la hora de probar la ejecucion de una determinada celda de codigo, tener en cuenta dichas dependencias, y en dicho caso, ejecutar la celda previa que corresponda



