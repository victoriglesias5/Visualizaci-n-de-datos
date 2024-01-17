A lo largo del presente escrito, vamos a reflejar los requerimientos necesarios para lanzar nuestro streamlit y el contenido que podrá encontrar en el mismo.
En primer lugar, debido al elevado peso de nuestro dataset, nos hemos encontrado con numerosos problemas a la hora de crear nuesra aplicación de Streamlit. Debido a esta dificultad, tuvimos que informarnos sobre esta situación, y llegamos a la conclusión de que era necesario usar Git LFS (Git LFS es una extensión de Git que mejora la manipulación de archivos grandes). Tuvimos que seguir los siguientes pasos:
1. Clonar nuestro repositorio de Github en nuestro PC ("git clone https://github.com/tu_usuario/tu_repositorio.git").
2. Instalar LFS ("git LFS install")
3. Especificar los tipos de archivos con los que queremos trabajar en LFS, sto generará un archivo .gitattributes que especifica qué archivos deben ser gestionados por Git LFS. ("git lfs track "*.csv"")
4. Añadir y hacer commit de tus cambios ("git add .; git commit -m "Iniciar Git LFS y añadir configuración"")
5. Empujar los cambios a tu repositorio de GitHub ("git push origin tu_rama")

Para que la aplicación de Streamlit pueda funcionar, además de cargar el archivo .csv que se va a analizar, es necesario que en el repositorio se encuentre el siguiente paquete de archivos:
-	Car_Crash.mp3
-	Codigo_streamlit.py
-	Foto.jpg
-	Leyenda.md
-	Foto_conclusion.jpg
-	Requirements.txt

Una vez llegados a este punto, creamos nuestra aplicación de Streamlit la cual genera el siguiente enlace con el que podreis interactuar con la misma: [Visita nuestro Streamlit](https://visualizaci-n-de-datos-wqtxditdpzt2qqycbzh8na.streamlit.app/).
Al abrirse tendremos una página llamada portada. En la cual hay un audio que debe de ser activado pulsando el icono de play para escucharlo. Para ir pasando entre las diferentes páginas del trabajo, hemos de dirigirnos al lateral izquierdo de nuestras pantallas y clicar donde nos pone “Seleccionar Apartado” y elegir entre las diferentes opciones ordenadas en orden lógico para que la experiencia goce de cohesión global.
En cuanto a la interactividad de las gráficas, vemos que existen las diferentes funcionalidades:
-	Ampliar la gráfica usando los iconos que aparecen en la parte superior del gráfico cuando el cursor se encuentra encima del gráfico.
-	Ver valores concretos posando el cursor sobre un punto concreto del gráfico.
-	Seleccionar ciertas áreas del gráfico para hacer un estudio más concreto de las partes de mayor interés.
Por último, aclarar que a lo largo del presente documento, se va a abordar la evolución y las características tanto de los propios siniestros como de las respuestas de la autoridad pertinente en Reino Unido en el periodo comprendido entre los años 2006-2014. Haciendo un análisis visual y concienzudo para lograr desentrañar las características de los mismos y sacar conclusiones sobre la manera óptima de paliar esta lacra.
