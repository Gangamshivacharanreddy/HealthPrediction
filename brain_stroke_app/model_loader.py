# brain_stroke_app/model_loader.py
import pickle
import os
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, 'brain_stroke_app','models', 'brain_stroke_prediction.pkl')
model = None

def load_model():
    global model
    if model is None:
        try:
            with open(MODEL_PATH, 'rb') as file:
                model = pickle.load(file)
        except FileNotFoundError:
            print(f"Error: Model file not found at {MODEL_PATH}")
            raise  
    return model

def predict(data):
    loaded_model = load_model()
    return loaded_model.predict([data])[0]