# CIFAR-10 Image Classifier with Streamlit

Este proyecto es un clasificador de imágenes entrenado con el dataset CIFAR-10. Utiliza un modelo de redes neuronales con **TensorFlow** para predecir la categoría de una imagen entre las 10 clases disponibles (avión, coche, perro, gato, etc.). La interfaz gráfica ha sido desarrollada con **Streamlit** para facilitar la interacción del usuario.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las dependencias necesarias. Te re recomiendo crear un entorno virtual para aislar el entorno de desarrollo.

### Crear y activar un entorno virtual

1. Crea un entorno virtual:

   - En Windows:
     ```bash
     python -m venv mi_entorno
     ```
   - En macOS/Linux:
     ```bash
     python3 -m venv mi_entorno
     ```

2. Activa el entorno virtual:

   - En Windows:
     ```bash
     mi_entorno\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source mi_entorno/bin/activate
     ```

### Instalar dependencias

Una vez activado el entorno virtual, instalar las dependencias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt

```
# ejecutar la app

```bash
streamlit run APP.py

```
Esto abrirá la aplicación en tu navegador, aca podes cargar imágenes y ver las predicciones del modelo.
El archivo cifar10_model.h5 tiene que estar en el mismo directorio que el archivo APP.py para que la aplicación funcione correctamente.
