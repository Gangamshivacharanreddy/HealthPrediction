# predict/model_loader.py
import pickle
import os
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'predict', 'models', 'heart_disease_model.pkl')
model = None

def load_model():
    global model
    if model is None:
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)  # Indented line
    return model

def predict(data):
    loaded_model = load_model()
    return loaded_model.predict([data])[0]