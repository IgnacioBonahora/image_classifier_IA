import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import tensorflow as tf

def main():
    st.title("clasificador de imagenes")
    st.write("Carga una imagen para obtener la prediccion de la IA")

    file = st.file_uploader("carga una imagen")

    if file:
        image = Image.open(file)
        st.image(image, use_column_width= True)

        resized_image = image.resize((32,32))
        img_array = np.array(resized_image) / 25
        img_array = img_array.reshape((1,32,32,3))

        model = tf.keras.models.load_model('cifar10_model.h5')

        predictions = model.predict(img_array)

        cifar10_classes = ['airplane','automobile','bird','cat','dog','deer','frog','horse','ship','truck']

        fig,ax = plt.subplots()
        y_pos = np.arange(len(cifar10_classes))
        ax.barh(y_pos,predictions[0],align='center')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(cifar10_classes)
        ax.set_xlabel('probabilidad')
        ax.set_title('prediccion de imagenes')
        st.pyplot(fig)
    else:
        st.text('no has cargado una imagen')

main()