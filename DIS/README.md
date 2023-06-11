<h1>Readme</h1>
<h2>Introduction</h2>

Welcome to Sip'N'Save! Discover the best spots to enjoy your favorite beverages in Copenhagen, Odense, or Aarhus. Whether you're a wine connoisseur, a cocktail enthusiast, or a beer lover, we've got you covered. With our intuitive interface, you can easily find the perfect place to quench your thirst.

Want to secure a table beforehand? No problem! Simply let us know your preferred city, beverage of choice, and whether you'd like to make a table booking. We'll provide you with a comprehensive list of options tailored to your preferences.

Please note that the dataset used in Sip'N'Save is entirely fictional and should not be relied upon for real-world purposes. The information provided is for entertainment purposes only.

One unique feature of Sip'N'Save is the ability to rate and review the bars you visit. Curious to see how your feedback affects the overall rating of a bar? Leave your honest review and observe the impact on its reputation.

In addition to helping you find the perfect place to indulge, we prioritize your budget by sorting the results from cheapest to most expensive. By saving money on your drinks, you can enjoy your favorite beverages even more.

Get ready to embark on a delightful journey through the vibrant nightlife of Copenhagen, Odense, or Aarhus. Explore, savor, and share your experiences with the Sip'N'Save community. Let's raise a glass and toast to unforgettable moments!

<h2>How to run the code</h2>

(1) Run the code below to install the dependencies.
>$ pip install -r requirements.txt

(2) Create a new database - this can be done through PgAdmin or through psql.
(Use an existing user and password or create a new one by loggin in as superuser and typing 
>$ CREATE USER xxx WITH LOGIN CREATEDB PASSWORD 'yyy' ;
Make sure the user has privileges to access the database and tables in it or consider just using your postgres user.)

You might need to set your system path to the pg .bin and .lib folders for psql to be recognized as command.
>$ createdb -U username -h localhost database_name

(3) Then run the .SQL files to create the necessary tables. In psql you can run:
>$ psql -U username -d database_name -f file.sql
IMPORTANT: In the 'create_bars.SQL' and 'create_ratings.SQL' change the directory to the full path of the 'create_bars' file. 

(3) In the app.py-file, set the parameters of the connection (line 7) to match the database name, username and password

(4) Run Web-App
>$ python src/app.py

<h2>Link to the E/R Diagram</h2>
https://github.com/cfp185/DIS_Group_Project/blob/c93d78cdcce14010c86dc666790e0279f5c4917a/DIS/ER.png

