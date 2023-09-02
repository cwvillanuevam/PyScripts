Los archivos de este repositorio de scripts se crearon en lenguaje python por: Carlos Wyller Villanueva Machado utilizando el apoyo, ayuda y colaboración del software IA (you.com) y scripts libres de la web. Si desea explicaciones, detalles, colaborar con correcciones y/o comentarios, comunicarse con mi persona para las coordinaciones respectivas a:
vmcwyller@gmail.com
cwvillanuevam@uni.pe
Me disculpo de antemano por cualquier inconveniente que mi apretada agenda pueda causar en la dilación de tiempos de actualización. Gracias a todos por su apoyo.

Lineamientos para colaboración.
1. Si desea corregir algún bug o actualizar algún archivo para agregarle funcionalidades:
-Favor de buscar su sección en este archivo Readme.txt en la sección de documentación y/o editar el archivo Documentación.txt para editar las funcionalidades y/o correcciones realizadas.
-Continuamente se estará revisando los issues  para realizar la actualización de la documentación (por este motivo solicito se comuniquen con migo para poder tener conocimiento de los cambios y darle seguimiento).
-En caso de agregar una funcionalidad no descrita en los hashtags existentes del archivo editado, agregarlo para facilitar la utilización y busqueda de los demás usuarios.
-Mantener un script lo más limpio  posible, utilizando comentarios en ingles o español de preferencia.
-agregar su información de contacto en la sección de colaboradores de este archivo y/o en el archivo colaboladores.txt
2. En caso de agregar un archivo al repositorio.
-Agregar la documentación del mismo en la sección documentación del presente archivo Readme y/o agregarlo en el archivo Documentación.txt Si desea puede dejar sus credenciales y/o social media para tener información de contacto.
-Continuamente se estará revisando los issues  para realizar la actualización de la documentación (por este motivo solicito se comuniquen con migo para poder tener conocimiento de los cambios y darle seguimiento).
-Tratar de usar los hashtags existentes en otros archivos o agregar uno nuevo en caso así se amerite. Esto facilitará la utilización y busqueda de los demás usuarios.
-Mantener un script lo más limpio  posible, utilizando comentarios en ingles o español de preferencia.
-agregar su información de contacto en la sección de colaboradores de este archivo y/o en el archivo colaboladores.txt

Colaboradores:



Documentación
Summary.py
#Analisis #IA #SubDir #Word
El archivo Summary.py se encarga de sintetizar todos los archivos encontrados en una sub carpeta de la carpeta de tu proyecto, de esta manera lee archivos word y aplicando la libreria NLTK para hacer síntesis de datos. De modo tal que usando tokenización puede sintetizar de que tratan los archivos. También copia las tablas de los archivos de la subcarpeta en el archivo word de sintesis. En caso de encontrar errores en la lectura de las tablas aplicar el script chtr.py para determinar que tablas contienen errores en los archivos  word. Recordar que python empieza los conteos con indice 0, no 1.

chtr.py
#Analisis #ReporteDeFallas #SubDir #Word
El archivo chtr.py se encarga de revisar en lote archivos word de una subcarpeta para determinar si las tablas que contien dichos archivo pueden ser leídas usando python o requieren acciones manuales para ajustar la cantidad de celdas que la tabla presenta. Cada vez que encuentre una falla en la lectura de las tablas se reportara el número de tabla (en índice usado por python) / La cantidad total de tablas del archivo. file: el nombre del archivo word donde se encuentra la tabla que presenta errores.

readImg.py
#ProcesamientoDeImagenes #ImagenATexto
El archivo readImg.py se encarga de realizar un procesamiento de la lectura de imagenes que tengan información alfanumérica de manera simple. Lamento de antemano mi falta de conocimiento de más detalles del procesamiento de imagenes alfanuméricas, trataré de incrementar el expertise en la medida de lo posible.