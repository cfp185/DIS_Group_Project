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
