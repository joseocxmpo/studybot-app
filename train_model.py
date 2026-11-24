"""Entrena el modelo StudyBot y lo guarda en studybot_model.joblib (Paso 1).

La aplicación web NO usa este script: solo carga el archivo .joblib ya generado.
"""
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

FEATURES = [
    "silencio", "sombra", "aire_acondicionado", "soporte_para_trabajar", "asientos",
    "asientos_comodos", "enchufes", "flujo_personas", "banos_cerca", "cafeteria_cerca",
    "internet_wifi",
]

df = pd.read_csv("Dataset v1.0.csv")
X, y = df[FEATURES], df["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Exactitud en prueba:", accuracy_score(y_test, model.predict(X_test)))

# Se guarda el modelo junto con el orden exacto de las columnas.
joblib.dump({"model": model, "features": FEATURES}, "studybot_model.joblib")

# Verificación: recargar y predecir.
bundle = joblib.load("studybot_model.joblib")
print("Predicción de prueba:", bundle["model"].predict(X_test.iloc[[0]]))
