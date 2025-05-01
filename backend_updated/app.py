from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins (for development)

# If using blueprints
from routes.predict_route import predict_bp
from routes.shap_route import shap_bp

app.register_blueprint(predict_bp)
app.register_blueprint(shap_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)