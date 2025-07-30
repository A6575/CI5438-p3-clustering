[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QQtMa8CD)
### CI5438 - AJ2025

# Proyecto 3


## Clustering
#### Prof. Ivette Carolina Martínez



### Resumen
El clustering o aglomeración  es una un subconjunto de algoritmos de aprendizaje no supervisado. Hay dos tipos de clustering: el jerárquico el no jerárquico. El algoritmo k-means es el más usado del los no jerarquicos. El objetivo de este proyecto es que el estudiante implemente dicho algoritmo y se familiarice con su uso. Para ello se pide que implementen k-means en el lenguaje imperativo de su preferencia; para luego evaluar esa implementación sobre dos problemas: la compresión de una imágen, y el cómo separar los ejemplos (con etiquetas conocidas) del Iris Dataset .

 


### Descripción

#### Parte 1
Implemente el algoritmo de k-means en el lenguaje imperativo de su preferencia.

#### Parte 2
Pruebe su algoritmo sobre los siguientes dominios de aplicación:

2.1. Para explorar los datos del conjunto Iris Data Set [1]:
   
	1.1. Pruebe para K = {2,3,4, 5}.
   
   	- Visualice si los clusters encontrados coinciden de alguna manera con las etiquetas de los ejemplos.

   	- Describa y discuta sus resultados.
	
 	1.2. Para K = 2 y K = 3, Calcule la diferencia entre los clusters y las etiquetas reales.

   	- Describa y discuta sus resultados.
	
	- Nota: Recuerden que el resultado de K-means depende a la inicialización, por lo que deben probar varias corridas para el mismo K (mínimo 5). Deben reportar los resultados de cada corrida (del ejercicio 1.2), los promedios, el mejor caso y el peor caso.

2.2. Para realizar la compresión de una imagen de su preferencia.
	- El proceso de compresión está descrito en las láminas "Clustering and The k-means Algorithm" 
 (Disponibles como clustering-1.pdf en el Canvas Instructure del curso.

	- En este caso cada pixel en la imagen original es un ejemplo, que será asignado en la imagen comprimida al cluster k_i . K será el número de colores en la imagen comprimida.

 	- Pruebe para K= {2, 4, 8, 16, 32, 64, 128}.
  	- Guarde las imagenes resultantes (y la original) en una carpeta. Si el nombre de la original es Imagen.png , el de las resultantes debe ser Imagen K[NumeroK].png
   	- Discuta sus resultados. Son distinguibles los elementos de la imágen general en la comprimida? Cómo afecta el K al tamaño de las imágenes generadas?



### Entrega:

* Deberán subir al repositorio de su tarea un archivo su repuesta a las actividades, en formato PDF, el archivo debe llevar por nombre "Reporte.pdf". El reporte deberá estar en el formato Wenneker Assignment [2].



* Su informe además de incluir las respuestas a cada una de las actividades planteadas en la descripción debe incluir los siguientes elementos: 
  1. Resumen.
  2. Detalles de implementacion/experimentacion. (Lenguaje usado, detalles del algoritmo, selección de colores, etc). 
  3. Presentacion y discusion de los resultados (En base a los elementos requridos para cada dominio)
  4. Conclusiones
  5. Referencias

* Fecha de entrega: Lunes 14 de Julio 2025, hasta la media noche.

#### Referencias
 

[1] Fisher, R.A. (1936) *Iris Data Set* [Data Set]. Disponible en: https://archive.ics.uci.edu/ml/datasets/iris [Fecha de consulta 22 de Marzo 2023].

[2] LaTeX Templates."Wenneker Assignment". disponible en: https://www.latextemplates.com/template/wenneker-assignment (consultado el 29/04/2025).
