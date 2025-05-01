import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib
import shap
import os

shared_path = "/app/shared"
data_path = os.path.join(shared_path, "data", "processed_data.csv")

# Load dataset
df = pd.read_csv(data_path)

# Features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, os.path.join(shared_path, "models", "random_forest.pkl"))

# Evaluate model
preds = model.predict(X_test)
print(classification_report(y_test, preds))
print('ROC-AUC:', roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))

# SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
joblib.dump(explainer, os.path.join(shared_path, "models", "shap_explainer.pkl"))
X_test.to_csv(os.path.join(shared_path, "data", "X_test_for_shap.csv"), index=False)
