# import library
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import os
# from tensorflow import keras
# from keras.models import load_model
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as tfImage

# from keras import layers, models, optimizers, losses, metrics 

# initiation flask
app = Flask(__name__)

# initiation tf model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'recratify_model.h5')

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

model = load_model(model_path)

# processing image
def prepare_image(image, size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(size)
    image = tfImage.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    return image

# route
@app.route('/predict', methods=['POST'])
def waste_prediction():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    try:
        image = Image.open(file.stream)
        processed_image = prepare_image(image, size=(224, 224))
        prediction = model.predict(processed_image)[0]
        # result = prediction[0]

        prediction_class = np.argmax(prediction)

        label_mapping = {
            0: 'battery',
            1: 'organic-waste',
            2: 'brown-glass',
            3: 'cardbox',
            4: 'clothes',
            5: 'green-glass',
            6: 'metal',
            7: 'paper',
            8: 'plastic-bottle',
            9: 'shoes',
            10: 'trash',
            11: 'white-glass'
        }
        label_prediction = label_mapping[prediction_class]

        confidence = float(prediction[np.argmax(prediction)].item())

        return jsonify({
            'response': {
                'error': False,
                'code': 200,
                'message': 'Waste successful predict!',
                'data': {
                    'label': label_prediction,
                    'confidence': confidence
                }
            }
        })
    except Exception as err:
        return jsonify({'error': str(err)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
