import catboost as cb
import pandas as pd

from flask import Flask, jsonify, request

# Carregamos o Modelo
model = cb.CatBoostClassifier()  # Link do CatBoost --> https://catboost.ai/
model.load_model("loan_catboost_model.cbm")

# Instanciamos app
app = Flask("default")


# Endpoint de previsão de setup
@app.route("/predict", methods=["POST"])
def predict():
    # Get o JSON fornecido
    X = request.get_json()
    # Ececutamos uma previsão
    preds = model.predict_proba(pd.DataFrame(X, index=[0]))[0, 1]
    # Output do JSON com previsão
    result = {"default_proba": preds}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host="0.0.0.0", port=8989)