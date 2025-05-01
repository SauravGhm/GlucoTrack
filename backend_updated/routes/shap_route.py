from flask import Blueprint, request, jsonify
import joblib
import pandas as pd
import numpy as np

shap_bp = Blueprint('shap', __name__)
explainer = joblib.load('shared/models/shap_explainer.pkl')
X_test = pd.read_csv('shared/data/X_test_for_shap.csv')

@shap_bp.route('/shap', methods=['POST'])
def shap_explanation():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    shap_values = explainer.shap_values(features)[1][0]
    feature_names = X_test.columns.tolist()
    shap_dict = {name: round(val, 4) for name, val in zip(feature_names, shap_values)}
    return jsonify(shap_dict)

