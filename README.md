# web_scraping_metrocuadrado
Recolector de datos de inmuebles de Metro Cuadrado
Para correr este programa es necesario contar con Google Chrome. Adicionalmente, es necesario descargar un chrome driver de la misma versión del Google Chrome que se tenga instalado así como del mismo sistema operativo con el que trabaja la computadora que va a correr este programa.
La función que se corre es la llamada "data_normalization". Las funciones "get_all_links" y "get_all_data" son funciones que alimentan "data_normalization", siendo esta última la que corre todo en conjunto reuniendo a su vez los datos en un mismo documento.
En "chromedriver_path" se debe escribir la ruta en la que quedó descargado el Chrome Driver en los archivos del computador.
El programa te va a solicitar dos inputs: ciudad y tipo de inmueble. Los datos recolectados dependerán de ambos inputs. Ejemplo: ciudad = bogota y tipo_inmueble = oficina generará la recolección de datos sobre oficinas en Bogotá.
El programa al final va a retornar un archivo xlsx llamado all_data. En este archivo podrás encontrar la información relevante para cada inmueble publicado en el portal Metrocuadrado.
