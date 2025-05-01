# trainer/main.py

import subprocess

print("Running EDA...")
subprocess.run(["python", "EDA.py"], check=True)

print("Running model training...")
subprocess.run(["python", "model_training.py"], check=True)