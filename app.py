from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///app.db")

@app.route("/")
def index():
    return render_template("layout.html")


@app.route("/rezeptHinzufügen", methods=["GET", "POST"])
def rezeptHinzufügen():
    if request.method == "POST":
        name = request.form.get("name")
        vorgehen = request.form.get("vorgehen")
        anzahlZutaten = request.form.get("zutatCount")
        zutaten = {}
        for i in range(anzahlZutaten-1):
            aktuelleZutat=request.form.get("zutat"+i)
            aktuelleMenge=request.form.get("menge"+1)
            zutaten[aktuelleZutat] = aktuelleMenge
        return render_template("rezeptHinzufügen.html")
    else:
        return render_template("rezeptHinzufügen.html")

    #TODO: Daten in sql übertragen, probeweise ausgeben!!

if __name__ == '__main__':
    app.run()
