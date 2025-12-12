from flask import Flask, jsonify
import pandas as pd

app = Flask("Mini API del Trabajo Final")

roi_por_genero = pd.read_csv("roi_por_genero.csv")
directores_rating = pd.read_csv("directores_rating.csv")

@app.route("/")
def home():
    return jsonify({
        "mensaje": "Mini API del Trabajo Final – Lenguajes 2025",
        "endpoints": ["/top_generos_roi", "/top_directores_rating"]
    })

@app.route("/top_generos_roi")
def top_generos_roi():
    return jsonify(roi_por_genero.head(10).to_dict(orient="records"))

@app.route("/top_directores_rating")
def top_directores_rating():
    top = directores_rating.sort_values("rating", ascending=False).head(10)
    return jsonify(top.to_dict(orient="records"))

app.run()