# Proyecto Individual N°1 #
<h1>Machine Learning Operations</h1>

Bienvenidos a este proyecto individual realizado en el Bootcamp de Data Science de HENRY.</p>
En este trabajo nos meteremos en la piel de un MLops Engineer al tomar 3 archivos JSON provistos por la empresa Valve Corporation, creadora de la plataforma Steam, de donde se basa el proyecto.
<hr>

# Contexto
Steam es una plataforma gratuita en la que los usuarios pueden comprar juegos, hacer reseñas sobre los mismos, trabajar en mods en la workshop, interactuar entre los usuarios y muchísimas cosas más.
<p>
Con más de 20 años de trayectoria, Steam ha adquirido un catálogo de juegos y aplicaciones inmenso y una base de usuarios aún más grande. Luego de trabajar sobre esto, vengo a presentarte mi proyecto.
<hr>

# Requisitos
El proceso de análisis, conversión de datos y creación de tablas que consumirán las funciones de la API fueron creadas en Google Colab.

La creación de las funciones y endpoints para la API fue creada en el Editor de código Visual Studio Code.

Dicho esto, los únicos requisitos serían las librerías especificadas en el archivo **__requirements.txt__**.
<hr>

# Instrucciones de uso

1. Clona este repositorio de GitHub.
2. Si se quiere visualizar el proceso de transformación y recorrer las celdas, lo recomendable es cargar las siguientes carpetas en Google Drive:

   - ML model
   - Raw data (contiene un archivo .zip que debe descomprimirse antes)
   - Refined data (contiene un archivo .zip que debe descomprimirse antes)
   - Process

   Para no tener problemas con las rutas, se recomienda poner estos archivos en una carpeta llamada Proyecto Steam.

3. Instala las librerías pertinentes especificadas en el requirements.txt con el comando `pip install -r requirements.txt`.
4. Para correr la API en local, abre una terminal en el archivo *main.py* y ejecuta el comando `python3 -m uvicorn main:app --reload`. Espera a que se levante y ve al siguiente [enlace](http://127.0.0.1:8000/docs).
5. La API se encuentra lista para ser consumida en Render, solo hay que visitar el siguiente [enlace](https://trabajoprac1.onrender.com/docs).

# Contenido

El repositorio está ordenado en carpetas que contienen los diversos archivos y los procesos que se fueron aplicando. A continuación, la explicación de estas:

- ## ML model:
  Se divide en dos archivos, creacion_data (donde se toman los datos de otros CSV para crear la tabla con los datos útiles) y creacion_modelo (transformaciones finales e implementación del modelo para probarlo).

- ## Raw data:
  Aquí están los archivos crudos, los datos con los cuales fue posible empezar todo esto (por temas de tamaño un archivo se encuentra en .zip).

- ## Process:
  Aquí se almacenan los archivos que contienen los procesos que se fueron aplicando a las tablas. Consta de dos archivos, conversion_datos (toma los archivos de raw data y se crean las primeras tablas refinadas que servirán para la creación de las funciones) y análisis y creación funciones (trabaja sobre los archivos de refined data, donde se exploran más a fondo y se crean las tablas que serán consumidas por las funciones).

- ## Refined data:
  Se almacenan los archivos que contienen las tablas refinadas producto del trabajo de conversion_datos.

# API

El proyecto cuenta con la implementación de una API con 6 funciones:

- `PlayTimeGenre()`: Devuelve el año con más horas jugadas para un género específico.
- `UserForGenre()`: Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
- `UsersRecommend()`: Proporciona información sobre los usuarios que recomiendan un juego.
- `UsersNotRecommend()`: Proporciona información sobre los usuarios que no recomiendan un juego.
- `SentimentAnalysis()`: Realiza análisis de sentimientos en las reseñas de los usuarios.

# Contacto

Si el proyecto fue de su agrado y quedaron dudas y/o sugerencias, no dude en contactarme.

- Nombre: Colanoni Lucas
- Teléfono: +54 3436 447764
- Correo Electrónico: lucascolantoni@hotmail.com
