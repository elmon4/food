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

@app.route("/rezepteAlphabetisch", methods=["GET"])
def rezepteAlphabetisch():
    if request.method == "GET":
        #TODODDODOD
        return render_template("rezeptHinzufügen.html")


@app.route("/rezeptHinzufügen", methods=["GET", "POST"])
def rezeptHinzufügen():
    if request.method == "POST":
        portionen = request.form.get("portionen")
        name = request.form.get("name")
        vorgehen = request.form.get("vorgehen")
        anzahlZutaten = int(request.form.get("zutatCount"))
        saison = request.form.get("saison")
        kategorie = request.form.get("kategorie")
        zutaten = {}
        print(f"Anzahl Zutaten: {anzahlZutaten}")
        for i in range(anzahlZutaten):
            aktuelleZutat=request.form.get("zutat"+str(i))
            aktuelleMenge=request.form.get("menge"+str(i))
            zutaten[aktuelleZutat] = aktuelleMenge
        db.execute("INSERT INTO rezept (kategorie, name, portionen, saisonalität, vorgehen) VALUES (?, ?, ?, ?, ?)", kategorie, name, portionen, saison, vorgehen)
        rezeptID = db.execute("SELECT id FROM rezept WHERE name = ?", name)[0]["id"]
        for key in zutaten:
            if key is not None:
                aktuelleZutat = key
                aktuelleMenge = zutaten[key]
                result = db.execute("SELECT * FROM zutat WHERE name = ?", aktuelleZutat)
                if len(result) == 0:
                    db.execute("INSERT INTO zutat (name) VALUES(?)", aktuelleZutat)
                zutatID = db.execute("SELECT id FROM zutat WHERE name = ?", aktuelleZutat)[0]["id"]
                db.execute("INSERT INTO zutatInRezept(rezeptID, zutatID, menge) VALUES(?,?,?)", rezeptID, zutatID, aktuelleMenge)
        return render_template("rezeptHinzufügen.html")
    else:
        return render_template("rezeptHinzufügen.html")

    #TODO: Daten in sql übertragen, probeweise ausgeben!!
    #TODO: rezepte Anzeigen lassen inkl. Zutaten, checken was falsch läuft in der Datenbank


if __name__ == '__main__':
    app.run()
