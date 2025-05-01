from flask import Blueprint, request, jsonify
import joblib
import numpy as np
import os
from flask_cors import CORS

predict_bp = Blueprint('predict', __name__)
CORS(predict_bp)

shared_path = "/app/shared"
model_path = os.path.join(shared_path, "models", "random_forest.pkl")
model = joblib.load(model_path)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['input']).reshape(1, -1)
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        return jsonify({'prediction': int(prediction), 'probability': float(probability)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    