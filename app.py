import streamlit as st
from PIL import Image
from ml import predict

st.title("Malaria Detection App")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Predict'):
        prediction = predict(image)
        if prediction < 0.5:
            st.success("Prediction: Uninfected")
        else:
            st.error("Prediction: Parasitized")
