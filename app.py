from pathlib import Path
from flask import Flask, render_template, request
import joblib
import pandas as pd


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


# prediction-----------------
model = joblib.load(Path("artifacts/model_trainer/model.joblib"))

@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        try:
            input_data = {key: float(value) for key, value in request.form.items()}
        
            feature_columns = [
                    "fixed acidity", "volatile acidity", "citric acid", "residual sugar", 
                    "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", 
                    "pH", "sulphates", "alcohol"
                ]
            df = pd.DataFrame([input_data], columns=feature_columns)
            
            prediction = model.predict(df)
            
            return render_template("index.html", prediction=prediction[0])
            
        except Exception as e:
            return render_template("index.html", error=str(e))
    
    return render_template("index.html", prediction=None)


if __name__=="__main__":
    app.run(
        host="0.0.0.0", port=5000, debug=True
    )