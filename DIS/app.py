from flask import Flask, render_template, url_for, request
import psycopg2
import datetime

app = Flask(__name__)

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
        barquery = "SELECT * FROM bars WHERE city = %s AND %s IS NOT NULL"
        if rtable:
            barquery += " AND table_booking = true"
        barquery += " ORDER BY LEAST (%s)"
        params= [rcity, rdrink, rdrink]
        cursor.execute(barquery, params)
        rows = cursor.fetchall()
        drinkcol = 6
        if rdrink == 'beer':
            drinkcol = 4
        elif rdrink == 'wine':
            drinkcol == 5
        else: 
            drinkcol == 6
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

if __name__ == '__main__':
    app.debug=True
    app.run(port=5001)