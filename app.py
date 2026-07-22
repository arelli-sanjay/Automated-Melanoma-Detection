#!/usr/bin/env python
import os
import sys

from flask import Flask, request, jsonify, send_file, render_template
from io import BytesIO
from PIL import Image, ImageOps
import base64
import urllib.parse

import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import tensorflow as tf

# Flask utils
from flask import redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

# Load your trained model globally
MODEL_PATH = os.path.join("model", "skin.h5")
model = load_model(MODEL_PATH, compile=False)

@app.route("/")
@app.route("/first")
def first():
    return render_template('first.html')
    
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/chart")
def chart():
    return render_template('chart.html')

@app.route("/performance")
def performance():
    return render_template('performance.html')

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload_file():
    print("Hello - Upload endpoint reached")
    print(request.files)
    out_pred = None
    out_prob = None
    processed_file = None
    
    try:
        # Read and process the image
        img = Image.open(BytesIO(request.files['imagefile'].read())).convert('RGB')
        img = ImageOps.fit(img, (224, 224), Image.LANCZOS)  # Changed ANTIALIAS to LANCZOS (updated PIL)
        
        # Call Function to predict
        out_pred, out_prob = predict(img)
        out_prob = out_prob * 100
        
        print(f"Prediction: {out_pred}, Probability: {out_prob}")
        
        # Convert image to base64 for display
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        png_output = base64.b64encode(img_io.getvalue()).decode('utf-8')
        processed_file = png_output
        
        danger = "danger"
        if out_pred == "Benign melanoma lesion":
            danger = "success"
        
        return render_template('result.html', 
                               out_pred=out_pred, 
                               out_prob=out_prob, 
                               processed_file=processed_file,
                               danger=danger)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        error_msg = f"Please choose a valid image file! Error: {str(e)}"
        return render_template('index.html', error_msg=error_msg)

def predict(img):
    try:
        # Preprocess the image
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Make prediction using the global model
        pred = model.predict(img_array)
        print(pred)
        
        # Get the prediction class
        pred_class = np.argmax(pred, axis=1)[0]
        
        if pred_class == 0:
            out_pred = "Benign melanoma lesion"
        elif pred_class == 1:
            out_pred = "Malignant melanoma lesion"
        else:
            out_pred = "Unknown"
        
        return out_pred, float(np.max(pred))
    
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return "Error in prediction", 0.0

if __name__ == '__main__':
    app.run(debug=True)
