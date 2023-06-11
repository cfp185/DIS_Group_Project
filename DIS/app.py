from flask import Flask, render_template, url_for, request, flash, make_response
import psycopg2
import sys
import importlib

app = Flask(__name__)

conn = psycopg2.connect(
    database='dbname', 
    user='postgres', 
    password='password',
    options='-c client_encoding=utf8'  
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

@app.route("/result", methods=['POST', 'get'])
def result():
    rows = []
    if request.method in ['POST', 'get']:
        cursor = conn.cursor()
        rcity=request.form["city"]
        rdrink=request.form["drink"]
        rtable=request.form["table"]
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
    response = make_response(render_template("result.html", rows=rows, drinkcol=drinkcol, drink=rdrink))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response
    # return render_template(
    #     "result.html", rows=rows, drinkcol = drinkcol, drink = rdrink
    # )
 
@app.route('/update_rating', methods=['POST'])
def update_rating():
    cursor = conn.cursor()

    id = request.form.get('id')
    thisrating = 'rating_' + id
    new_rating = float(request.form.get(thisrating))
    name = request.form.get('name')

    #Get rating data from database
    get_rating = f"SELECT rating, num_ratings FROM ratings WHERE id='{id}'"
    cursor.execute(get_rating)
    old_data = cursor.fetchone()

    if old_data is not None:
        existing_rating, num_ratings = old_data
        new_num_ratings = num_ratings+1
        upd_rating = (existing_rating*num_ratings+new_rating)/(new_num_ratings)
        rounded_value = round(upd_rating, 1)
        #If there is already a rating update the row
        rating_query = f"UPDATE ratings SET rating = {rounded_value}, num_ratings = {new_num_ratings} WHERE id='{id}'"
    else: 
        #If there is no existing rating insert a new row.
        rating_query = f"INSERT INTO ratings (id, rating, num_ratings) VALUES ('{id}', '{new_rating}', 1)"
    cursor.execute(rating_query)
    conn.commit()
    return render_template("thanks_rating.html", name=name)

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