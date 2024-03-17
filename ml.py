import numpy as np
from keras.preprocessing.image import img_to_array, load_img
import tensorflow as tf

img_width, img_height = 150, 150  # Adjust these values based on your model's input size

def load_model():
    return tf.keras.models.load_model("malaria-cnn-v1.keras")

def preprocess_image(image):
    img = image.resize((img_width, img_height))
    img = img_to_array(img) / 255.0
    img = img.reshape((1,) + img.shape)
    return img

def predict(image):
    model = load_model()
    preprocessed_img = preprocess_image(image)
    prediction = model.predict(preprocessed_img)
    return prediction[0][0]
