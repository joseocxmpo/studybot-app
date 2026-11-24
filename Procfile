"""Función de predicción (Paso 2). No entrena: solo carga el modelo y predice."""
import joblib
import pandas as pd

_bundle = joblib.load("studybot_model.joblib")
MODEL, FEATURES = _bundle["model"], _bundle["features"]


def predecir(valores: dict):
    """valores: {nombre_columna: 0 o 1}. Devuelve (etiqueta, probabilidad_de_APTO)."""
    fila = pd.DataFrame([[float(valores[c]) for c in FEATURES]], columns=FEATURES)
    pred = int(MODEL.predict(fila)[0])
    p_apto = float(MODEL.predict_proba(fila)[0][list(MODEL.classes_).index(1)])
    return ("APTO" if pred == 1 else "NO APTO"), p_apto
