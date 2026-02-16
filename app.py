import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :
@app.get("/paris")
def api_paris():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()

    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])

    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]

    return jsonify(result)
@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")
@app.route("/histogramme")
def histogramme():
    return render_template("histogramme.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.get("/atelier")
def api_atelier():
    
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8014&longitude=2.1301&hourly=relative_humidity_2m"
    response = requests.get(url)
    data = response.json()

    humidities = data.get("hourly", {}).get("relative_humidity_2m", [])

    # On prend seulement les 7 premiers jours (24h x 7 = 168 valeurs)
    first_week = humidities[:168]

    # Calcul moyenne humidité
    if len(first_week) > 0:
        average_humidity = sum(first_week) / len(first_week)
    else:
        average_humidity = 0

    result = {
        "humidite_moyenne": round(average_humidity, 2),
        "reste": round(100 - average_humidity, 2)
    }

    return jsonify(result)
@app.route("/atelier")
def page_atelier():
    return render_template("atelier.html")


# Ne rien mettre après ce commentaire
    
