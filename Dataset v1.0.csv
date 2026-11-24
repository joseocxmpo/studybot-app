from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# El modelo ya entrenado se carga una sola vez al iniciar. No hay fit() en la app.
bundle = joblib.load("studybot_model.joblib")
model, FEATURES = bundle["model"], bundle["features"]

ETIQUETAS = {
    "silencio": "Silencio", "sombra": "Sombra", "aire_acondicionado": "Aire acondicionado",
    "soporte_para_trabajar": "Soporte para trabajar (mesa)", "asientos": "Asientos",
    "asientos_comodos": "Asientos cómodos", "enchufes": "Enchufes",
    "flujo_personas": "Flujo alto de personas", "banos_cerca": "Baños cerca",
    "cafeteria_cerca": "Cafetería cerca", "internet_wifi": "Internet / WiFi",
}


@app.route("/", methods=["GET", "POST"])
def index():
    resultado, prob, error, valores = None, None, None, {}
    if request.method == "POST":
        try:
            for c in FEATURES:
                raw = request.form.get(c, "").strip()
                v = float(raw)            # falla si no es numérico
                if v not in (0.0, 1.0):
                    raise ValueError(f"'{ETIQUETAS[c]}' debe ser 0 o 1.")
                valores[c] = int(v)
        except ValueError as e:
            msg = str(e)
            error = msg if "debe ser" in msg else "Todos los campos deben ser numéricos (0 o 1)."
            valores = {}
        else:
            fila = pd.DataFrame([[valores[c] for c in FEATURES]], columns=FEATURES)
            pred = int(model.predict(fila)[0])
            prob = float(model.predict_proba(fila)[0][list(model.classes_).index(1)])
            resultado = "APTO" if pred == 1 else "NO APTO"
    return render_template("index.html", features=FEATURES, etiquetas=ETIQUETAS,
                           resultado=resultado, prob=prob, error=error, valores=valores)


if __name__ == "__main__":
    app.run(debug=False)
