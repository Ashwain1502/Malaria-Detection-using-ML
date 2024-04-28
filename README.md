# IQ_Gateway
This is the task given by IQ gateway for the interview process.

# Malaria Detection System
This project is aimed at detecting malaria in blood smear images using deep learning techniques. Malaria is a life-threatening disease caused by parasites transmitted to humans through the bites of infected female Anopheles mosquitoes. Early detection of malaria is crucial for effective treatment and prevention of complications.

# Overview
The project utilizes a convolutional neural network (CNN) architecture to classify blood smear images as infected or uninfected with malaria parasites. The CNN model is trained on a dataset consisting of thousands of annotated blood smear images obtained from patients diagnosed with malaria.

# Features
* Data Augmentation: The training data is augmented using techniques such as rotation, shear, and zoom to improve model generalization.
* Transfer Learning: Transfer learning is employed by utilizing a pre-trained VGG19 model as a feature extractor.
* Model Training: The CNN model is trained using TensorFlow and Keras, with binary cross-entropy as the loss function and Adam optimizer.
* Model Evaluation: The trained model is evaluated on a separate validation dataset to assess its performance in terms of accuracy and loss metrics.
* Prediction: The model is capable of predicting whether a given blood smear image is infected or uninfected with malaria parasites.
* Sample Visualization: Sample images from the dataset are visualized to illustrate the differences between infected and uninfected blood smear images.

# Requirements
* TensorFlow
* Keras
* OpenCV
* Matplotlib
* Seaborn
* Usage

# Clone the repository to your local machine:
[git clone https://github.com/Ashwain1502/Malaria-Detection-using-ML.git]

# Navigate to the project directory:

Run the Jupyter Notebook malaria-cells-classification-cnn.ipynb to train the model and perform predictions.

Contributors
Ashwani Kumar (ashwink1502@gmail.com)
