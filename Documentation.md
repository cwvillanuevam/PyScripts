# ✍️ Documentación / Documentation
## Summary.py
#Analisis #IA #SubDirectorio #MicrosoftWord / # Analysis #AI #SubDirectory #MSWord  
El archivo Summary.py se encarga de sintetizar todos los archivos encontrados en una sub carpeta de la carpeta de tu proyecto, de esta manera lee archivos word y aplicando la libreria NLTK para hacer síntesis de datos. De modo tal que usando tokenización puede sintetizar de que tratan los archivos. También copia las tablas de los archivos de la subcarpeta en el archivo word de sintesis. En caso de encontrar errores en la lectura de las tablas aplicar el script chtr.py para determinar que tablas contienen errores en los archivos  word. Recordar que python empieza los conteos con indice 0, no 1.  
/  
The file Summary.py is responsible for synthesizing all the files found in a subfolder of your project folder. This way, it reads word files and applies the NLTK library to perform data summarization. By using tokenization, it can synthesize what the files are about. It also copies the tables from the subfolder files into the summary word file. In case there are errors in reading the tables, the script chtr.py is applied to determine which tables contain errors in the word files. Remember that Python starts counting with index 0, not 1.  

## chtr.py
#Analisis #ReporteDeFallas #SubDirctorio #MicrosoftWord / #Analysis #FailureReport #SubDirectory #MSWord  
El archivo chtr.py se encarga de revisar en lote archivos word de una subcarpeta para determinar si las tablas que contien dichos archivo pueden ser leídas usando python o requieren acciones manuales para ajustar la cantidad de celdas que la tabla presenta. Cada vez que encuentre una falla en la lectura de las tablas se reportara el número de tabla (en índice usado por python) "/" La cantidad total de tablas del archivo. file: el nombre del archivo word donde se encuentra la tabla que presenta errores.  
/  
The file chtr.py is responsible for batch-checking Word files within a subfolder to determine if the tables in those files can be read using Python or if they require manual actions to adjust the number of cells in the table. Each time it encounters a failure in reading the tables, it will report the table number (using Python's indexing) "/" the total number of tables in the file. It will also report the name of the Word file where the table with errors is located.  

## readImg.py
#ProcesamientoDeImagenes #ImagenATexto / #ImageProcessing #ImageToText  
El archivo readImg.py se encarga de realizar un procesamiento de la lectura de imagenes que tengan información alfanumérica de manera simple. Lamento de antemano mi falta de conocimiento de más detalles del procesamiento de imagenes alfanuméricas, trataré de incrementar el expertise en la medida de lo posible.  
/  
The file readImg.py is responsible for performing image processing for reading images that contain alphanumeric information in a simple way. I apologize in advance for my lack of knowledge about the details of alphanumeric image processing, but I will try to increase my expertise as much as possible.  
