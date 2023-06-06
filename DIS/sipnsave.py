from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def front_page():
    return render_template(
        "frontpage.html",
    )
