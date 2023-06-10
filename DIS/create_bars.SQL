CREATE TABLE IF NOT EXISTS bars (
    id character(3),
    name character varying(20),
    city character varying(12),
    address character varying(30),
    beer double precision,
    wine double precision,
    cocktail double precision,
    rating double precision,
    table_booking boolean,
    happy_hour_start time without time zone,
    happy_hour_end time without time zone
);

COPY bars (ID, Name, City, Address, beer, wine, cocktail, Rating, Table_Booking, Happy_Hour_Start, Happy_Hour_End)
    FROM 'C:\Users\katja\OneDrive - University of Copenhagen\DIS\DIS_Group_Project\DIS\static\bars.csv'
    DELIMITER ',' NULL AS '' CSV HEADER;
