from flask import Flask, render_template, url_for


app = Flask(__name__)

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

@app.route("/liar")
def liar():
    return render_template(
        "liar.html"
    )
