import sys
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import matplotlib.pyplot as plt

def predict_image(image_path, model_path='models/cleanuncleanmodel.h5'):
    # Load the saved model
    model = load_model(model_path)

    # Load and preprocess the image
    img = cv2.imread(image_path)
    resize = tf.image.resize(img, (256, 256))

    # Predict the class
    yhat = model.predict(np.expand_dims(resize/255.0, 0))
    
    # Output the result
    if yhat > 0.5:
        print(f'Predicted class is dirty')
    else:
        print(f'Predicted class is clean')
    print(f"Rating on Unclean scale: {(yhat[0][0] * 100):.2f}")

    # Display the image
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

# If you want to pass the image path as a command-line argument
if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else 'sample_images/cleantest.jpg'
    predict_image(image_path)
