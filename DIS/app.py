from flask import Flask, render_template, url_for, request, flash, redirect
import psycopg2
import datetime

app = Flask(__name__)

conn = psycopg2.connect(
    database='test',
    user='postgres',
    password='1sa63lla'
)
cursor = conn.cursor()

@app.route("/login", methods=['POST', 'GET'])
def login():
    cur = conn.cursor()
    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']
        cur.execute(f'''select * from users where username = '{new_username}' ''')
        unique = cur.fetchall()
        flash('Account created!')
        if  len(unique) == 0:
            cur.execute(f'''INSERT INTO users(username, password) VALUES ('{new_username}', '{new_password}')''')
            flash('Account created!')
            conn.commit()
            return render_template(url_for("drink_type"))
        else: 
            flash('Username already exists!')


    return render_template("login.html")


# @app.route('/login', methods=['POST'])
# def do_admin_login():
#     cur = conn.cursor()
#     username = request.form['username']
#     password = request.form['password'] 

#     insys = f''' SELECT * from users where username = '{username}' and password = '{password}' '''

#     cur.execute(insys)

#     ifcool = len(cur.fetchall()) != 0

#     if ifcool:
#         session['logged_in'] = True
#         session['username'] = username
#     else:
#         flash('wrong password!')
#     return redirect(url_for("home"))

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
        print(rdrink == 'beer')
        time=datetime.datetime.now().hour
        barquery = f"SELECT * FROM bars WHERE city = '{rcity}' AND {rdrink} IS NOT NULL"
        if rtable:
            barquery += " AND table_booking = true"
        barquery += f" ORDER BY LEAST ({rdrink})"
        # params= [rcity, rdrink, rdrink]
        cursor.execute(barquery)
        rows = cursor.fetchall()
        drinkcol=0
        if rdrink == f" {rdrink}":
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

# @app.route("/login")
# def login():
#     return render_template(
#         "login.html"
#     )

@app.route("/toobad")
def too_bad():
    return render_template(
        "toobad.html"
    )

if __name__ == '__main__':
    app.debug=True
    app.run(port=5001)