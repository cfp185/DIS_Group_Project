from flask import Flask, render_template, url_for, request, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
import psycopg2
import datetime

app = Flask(__name__)
app.secret_key = 'shh'

conn = psycopg2.connect(
    database='test',
    user='postgres',
    password='1sa63lla'
)
cursor = conn.cursor()

@app.route("/")
def front_page():
    return render_template(
        "frontpage.html",
    )


@app.route("/drink")
def drink_type():
    return render_template(
        "drinktype.html"
    )

@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        cursor = conn.cursor()
        rcity=request.form["city"]
        rdrink=request.form["drink"]
        rtable=request.form["table"]
        time=datetime.datetime.now().hour
        barquery = f"SELECT bars.*, ratings.rating FROM bars LEFT OUTER JOIN ratings ON bars.id=ratings.id WHERE bars.city = '{rcity}' AND bars.{rdrink} IS NOT NULL"
        if rtable:
            barquery += " AND bars.table_booking = true"
        barquery += f" ORDER BY LEAST ({rdrink})"
        cursor.execute(barquery)
        rows = cursor.fetchall()
        if 'beer' == f"{rdrink}":
            drinkcol = 4
        elif 'wine' == f"{rdrink}":
            drinkcol = 5
        else: 
            drinkcol = 6
    return render_template(
        "result.html", rows=rows, drinkcol = drinkcol, drink = rdrink
    )

@app.route("/areyousure")
def are_you_sure():
    return render_template(
        "areyousure.html"
    )

@app.route("/mind")
def mind():
    return render_template(
        "mind.html"
    )

@app.route("/rate", methods=["POST"])
def rate():
    return render_template(
        "rate.html", id=request.form["id"]#, name=request.form["name"], address=request.form["address"]
    )

if __name__ == '__main__':
    app.debug=True
    app.run(port=5001)