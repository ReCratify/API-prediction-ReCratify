import os
from tensorflow.keras.models import load_model

# Tentukan jalur ke model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'models', 'recratify_model.h5')

# Periksa apakah model ada di jalur tersebut
print(f"Checking if model exists at: {model_path}")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Muat model
print("Attempting to load the model...")
try:
    model = load_model(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
