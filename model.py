from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Input
from tensorflow.keras.utils import to_categorical

# Cargar el dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train / 255.0
x_test = x_test / 255.0

# Convertir las etiquetas a una representación categórica
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Definir el modelo secuencial
model = Sequential([
    Input(shape=(32, 32, 3)),
    Flatten(),
    Dense(1000, activation='relu'),
    Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, batch_size=64, epochs=10, validation_data=(x_test, y_test))

# Guardar el modelo
model.save('cifar10_model.h5')


