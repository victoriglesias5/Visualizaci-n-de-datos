A lo largo del presente escrito, vamos a reflejar los requerimientos necesarios para lanzar nuestro streamlit y el contenido que podrá encontrar en el mismo.
En primer lugar, debido al elevado peso de nuestro dataset, debemos de decir que nos ha sido imposible hacer una subida de nuestro streamlit. Debido a esta dificultad, es necesario que el usuario que desee lanzar el programa instale el paquete de archivos completos que encontrará en nuestro Github. El paquete de archivos consiste en lo siguiente:
-	Car_Crash.mp3
-	Codigo_streamlit.py
-	Foto.jpg
-	Leyenda.md
-	Foto_conclusion.jpg
-	Requirements.txt
Una vez descargados los archivos, y ubicados todos en la misma ubicación dentro del dispositivo en el cual vamos a lanzar el programa, podemos comenzar la ejecución del mismo.
Nos gustaría recomendar al usuario la ejecución del mismo en un entorno virtual. Para correr el mismo deberá de acudir a su terminal y poner lo siguiente:
-	cd  + ruta en la que desea correr el entorno virtual (la cual deberá ser la misma en la cual se ubican los archivos anteriormente instalados).
-	python -m venv venv ( Forma de crear el entorno virtual)
-	pip install -r .\requirements.txt ( Recomendable tener un archivo de texto donde se detallen las distintas herramientas a instalar y las versiones )
-	.\venv\Scripts\activate ( Comando para levantar el entorno virtual y comenzar a trabajar dentro del mismo )
Una vez hecho lo anterior, ya solo quedaría lanzar el streamlit. Hemos de entender que este paso anterior referente al entorno virtual no es del todo necesario y puede ser omitido. Finalmente, la forma de abrir el streamlit con o sin trabajar dentro de un entorno virtual es la siguiente:
-	streamlit run Codigo_streamlit.py ( Al correr el código se ha de esperar a que se abra una ventana de Google con el streamlit )
Bien, una vez llegados a este punto ya tendremos nuestro streamlit lanzado. Por lo que podremos interactuar con él.
Al abrirse tendremos una página llamada portada. En la cual hay un audio que debe de ser activado pulsando el icono de play para escucharlo. Para ir pasando entre las diferentes páginas del trabajo, hemos de dirigirnos al lateral izquierdo de nuestras pantallas y clicar donde nos pone “Seleccionar Apartado” y elegir entre las diferentes opciones ordenadas en orden lógico para que la experiencia goce de cohesión global.
En cuanto a la interactividad de las gráficas, vemos que existen las diferentes funcionalidades:
-	Ampliar la gráfica usando los iconos que aparecen en la parte superior del gráfico cuando el cursor se encuentra encima del gráfico.
-	Ver valores concretos posando el cursor sobre un punto concreto del gráfico.
-	Seleccionar ciertas áreas del gráfico para hacer un estudio más concreto de las partes de mayor interés.
Por último, aclarar que a lo largo del presente documento, se va a abordar la evolución y las características tanto de los propios siniestros como de las respuestas de la autoridad pertinente en Reino Unido en el periodo comprendido entre los años 2006-2014. Haciendo un análisis visual y concienzudo para lograr desentrañar las características de los mismos y sacar conclusiones sobre la manera óptima de paliar esta lacra.
