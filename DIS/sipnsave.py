from flask import Flask, render_template, url_for


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

@app.route("/result")
def result():
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
