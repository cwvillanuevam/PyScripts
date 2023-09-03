# 💫 Descripción / Description
Los archivos de este repositorio de scripts se crearon en lenguaje python por: Carlos Wyller Villanueva Machado utilizando el apoyo, ayuda y colaboración del software IA (you.com) y scripts libres de la web. Si desea explicaciones, detalles, colaborar con correcciones y/o comentarios, comunicarse con mi persona para las coordinaciones respectivas a:
vmcwyller@gmail.com;
cwvillanuevam@uni.pe

Me disculpo de antemano por cualquier inconveniente que mi apretada agenda pueda causar en la dilación de tiempos de actualización. Gracias a todos por su apoyo./

The files in this script repository were created in the Python language by Carlos Wyller Villanueva Machado, with the support, assistance, and collaboration of the AI software (you.com) and freely available scripts from the web. If you would like explanations, details, or if you'd like to collaborate by providing corrections and/or comments, please contact me for the respective coordination at:
vmcwyller@gmail.com;
cwvillanuevam@uni.pe

I apologize in advance for any inconvenience that my busy schedule may cause in terms of update delays. Thank you all for your support.

## 💻 Lineamientos para colaboración / Collaboration Guidelines.
1. Si desea corregir algún bug o actualizar algún archivo para agregarle funcionalidades:  
-Favor de buscar su sección en este archivo Readme.txt en la sección de documentación y/o editar el archivo Documentación.md para editar las funcionalidades y/o correcciones realizadas.  
-Continuamente se estará revisando los issues  para realizar la actualización de la documentación (por este motivo solicito se comuniquen con migo para poder tener conocimiento de los cambios y darle seguimiento).  
-En caso de agregar una funcionalidad no descrita en los hashtags existentes del archivo editado, agregarlo para facilitar la utilización y busqueda de los demás usuarios.  
-Mantener un script lo más limpio  posible, utilizando comentarios en ingles o español de preferencia.  
-agregar su información de contacto en la sección de colaboradores de este archivo y/o en el archivo   colaboladores.md.  
2. En caso de agregar un archivo al repositorio.  
-Agregar la documentación del mismo en la sección documentación del presente archivo Readme y/o agregarlo en el archivo Documentación.md Si desea puede dejar sus credenciales y/o social media para tener información de contacto.  
-Continuamente se estará revisando los issues  para realizar la actualización de la documentación (por este motivo solicito se comuniquen con migo para poder tener conocimiento de los cambios y darle seguimiento).  
-Tratar de usar los hashtags existentes en otros archivos o agregar uno nuevo en caso así se amerite. Esto facilitará la utilización y busqueda de los demás usuarios.  
-Mantener un script lo más limpio  posible, utilizando comentarios en ingles o español de preferencia.  
-agregar su información de contacto en la sección de colaboradores de este archivo y/o en el archivo colaboladores.md.  

/

1. If you want to fix a bug or update a file to add functionality:  
-Please search for your section in this Readme.md file under the documentation section and/or edit the Documentación.txt file to edit the functionality and/or corrections made.  
-Issues will be continuously reviewed to update the documentation (for this reason, I request you to contact me to be aware of the changes and follow up).  
-If you add functionality not described in the existing hashtags of the edited file, please add it to facilitate the use and search by other users.  
-Keep the script as clean as possible, using comments in English or Spanish preferably.  
-Add your contact information in the collaborators section of this file and/or in the colaboladores.md file.  
2. If you add a file to the repository:  
-Add its documentation to the documentation section of this Readme file and/or add it to the Documentación.md file. If you wish, you can leave your credentials and/or social media for contact information.  
-Issues will be continuously reviewed to update the documentation (for this reason, I request you to contact me to be aware of the changes and follow up).  
-Try to use existing hashtags in other files or add a new one if necessary. This will facilitate the use and search by other users.  
-Keep the script as clean as possible, using comments in English or Spanish preferably.  
-Add your contact information in the collaborators section of this file and/or in the colaboladores.md file.  

## 🏆 Colaboradores:
* you.com (IA) / you.com (AI) *



# ✍️ Documentación
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
