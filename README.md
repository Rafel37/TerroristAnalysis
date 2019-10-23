# Analisis de ataque terroristas a nivel mundial

En este proyecto se entrena un modelo para que te diga si un ataque terrorista tendrá exito en un lugar 
y fecha especifico.

## Descripción:

Dataset que se ha usado en el proyecto:

https://www.kaggle.com/START-UMD/gtd

## Archivos:
```
+ README.md : Descripción del proyecto

+ Machine Learning.ipynb : En este notebook normalizo los datos del dataset modificado y entreno un modelo 
                           con un RandomForestClassifier.
                           Finalmente pruebo el modelo a través de un input donde se introduce la ciudad y 
                           la fecha para que te responda si el ataque tendría exito o no.

+ code 
    ┬
    │  
    ├── + Main.py : fichero principal desde el que se llaman a las demás clases y sus funciones.  
    │  
    ├── + Paths.py : fichero en el que se guardan las rutas de lectura del dataset y guardado del   
    │                dataset final.
    ├── + ImportExport.py : clase dónde se guardan las funciones para descargar el csv, leerlo y   
    │                       exportar el nuevo csv final.  
    └── + RowsAnalysis.py : clase dónde se amacenan las funciones para saber el número de columnas 
                            del dataset, sacar la cantidad de nulos en cada columna del dataset y 
                            seleccionar las columnas con las que queremos trabajar del dataset.  
 + dataset 
    ┬
    │                        
    └── + AnalisisDatos.ipynb : jupyter notebook para saber los valores de los dataset tanto del 
                                inicial como del modificado, en este caso solo me interesaba el
                                numero de registros.
                            
                            
                            
+ Tests.ipynb : jupyter notebook para hacer pruebas sobre el dataset, más especificamente sobre 
                las columnas y como cambiar sus nombre, la solución final fue duplicarlas con
                el nombre modificado y quedarme con la nueva columna creada.
```
