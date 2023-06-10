from flask import Flask, render_template, url_for, request
import psycopg2
import datetime

app = Flask(__name__)
app.config


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
        city=request.form["city"]
        drink=request.form["drink"]
        table=request.form["table"]
        time=datetime.datetime.now().hour
        print(city)
    return render_template(
        "result.html"
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

@app.route("/login")
def login():
    return render_template(
        "login.html"
    )

@app.route("/toobad")
def too_bad():
    return render_template(
        "toobad.html"
    )

if __name__ == '__main__':
    app.debug=True
    app.run(port=5001)
    
    conn = psycopg2.connect(
        # host='localhost',
        port='5001',
        database='bars',
        user='wkl712',
        password='1234'
    )
    cursor = conn.cursor()