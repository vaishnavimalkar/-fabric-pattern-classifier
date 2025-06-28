from flask import Flask, render_template, request
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# ✅ Adjusted model architecture to match saved weights (Flatten output = 57600)
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(120, 120, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),  # Output should now match what saved weights expect
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')  # Ensure you trained on 10 classes
])

# ✅ Load the trained weights
model.load_weights('model_cnn.h5')

# ✅ Update with your actual class labels
class_names = ['Chevron', 'Dots', 'Floral', 'Geometric', 'Houndstooth', 'Paisley', 'Striped', 'Plaid', 'Polka', 'Solid']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    # Save file
    file_path = os.path.join('static', file.filename)
    file.save(file_path)

    # ✅ Resize image to new input shape
    img = image.load_img(file_path, target_size=(120, 120))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    return render_template('result.html', prediction=predicted_class, img_path=file_path)

if __name__ == '__main__':
    app.run(debug=True)
