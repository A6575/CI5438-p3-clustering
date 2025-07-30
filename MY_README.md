# Proyecto 2 - Redes Neuronales

## Activación del entorno virtual

1. **Crear el entorno virtual:**
	```bash
	python3 -m venv env
	```

2. **Activar el entorno virtual:**
	- En Linux/Mac:
	  ```bash
	  source env/bin/activate
	  ```
	- En Windows:
	  ```bash
	  env\Scripts\activate
	  ```

3. **Instalar las librerías desde `requirements.txt`:**
	```bash
	pip install -r requirements.txt
	```
>[!NOTE]
> Para desactivar el entorno virtual:
> ```bash
> deactivate
> ```

## Ejecución del proyecto

El desarrollo del proyecto se llevó a cabo íntegramente en Jupyter Notebook, utilizando Visual Studio Code junto con la extensión oficial [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) para su ejecución y visualización.

La organización del repositorio es la siguiente:

- [x] img/
- [x] src/
- [x] MY_README.md
- [x] README.md
- [x] requirements.txt

- En la carpeta `img/` se encuentran los gráficos e imagenes generadas durante el desarrollo del proyecto:
  - En la carpeta `parte_2-1/` se encuentran las imágenes generadas durante la parte 2.1 del proyecto:
	- `iris_kmeans_k=2.png`
	- `iris_kmeans_k=3.png`
	- `iris_kmeans_k=4.png`
	- `iris_kmeans_k=5.png`
  - En la carpeta `parte_2-2/` se encuentran las imágenes generadas durante la parte 2.2 del proyecto:
    - `imagen1.png`: foto de paleta de colores.
	- En `imagen1/` se encuentran las imágenes generadas para `imagen1.png`:
      - En `comparacion/` se encuentran las imágenes generadas junto con la imagen original, para comparación de resultados:
		- `imagen1_K[2].png`
		- `imagen1_K[4].png`
		- `imagen1_K[8].png`
		- `imagen1_K[16].png`
		- `imagen1_K[32].png`
		- `imagen1_K[64].png`
		- `imagen1_K[128].png`
      - `imagen1_K[2].jpg`
      - `imagen1_K[4].jpg`
      - `imagen1_K[8].jpg`
      - `imagen1_K[16].jpg`
	  - `imagen1_K[32].jpg`
	  - `imagen1_K[64].jpg`
	  - `imagen1_K[128].jpg`
- En la carpeta `src/` se encuentran los scripts y notebooks desarrollados para la resolución de las distintas etapas del proyecto:
  - Parte 1: `clustering.py`
  - Parte 2: `resultados_parte2-1.ipynb`
  - Parte 3: `resultados_parte2-2.ipynb`

Para consultar la resolución de cada sección, se recomienda acceder a los archivos correspondientes dentro de la carpeta `src` y ejecutar las celdas de los notebooks en el orden establecido.

>[!IMPORTANT]
> Si es primera vez utilizando Jupyter en VSCode habrá un símbolo a la derecha que indica `Select Kernel` alli deberá usar el del environment. Una vez seleccionado, debera tratar de ejecutar una celda, le sandrá un aviso de que debe instalar un componente adicional de Kernel, debe aceptar dicha instalacion y podra ejecutar las celdas del Jupyter.

## Alternativas si no se puede usar VSCode

- **Jupyter Notebook en el navegador:**  
 Instalar Jupyter con `pip install notebook` y ejecutar `jupyter notebook` en la terminal. Se abrirá una interfaz web donde se pueden abrir y ejecutar los notebooks.
- **JupyterLab:**  
 Instalar con `pip install jupyterlab` y ejecutar `jupyter lab` para una experiencia más avanzada.
- **Google Colab:**  
 Subir el notebook a [Google Colab](https://colab.research.google.com/) para ejecutarlo en la nube (puede requerir instalar dependencias manualmente).
- **Exportar a .py:**  
 Desde Jupyter o VSCode, es posible exportar el notebook como archivo `.py` y ejecutarlo como un script de Python tradicional.