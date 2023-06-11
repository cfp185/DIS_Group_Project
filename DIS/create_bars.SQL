CREATE TABLE IF NOT EXISTS bars (
    id character(3),
    name character varying(30),
    city character varying(12),
    address character varying(30),
    beer double precision,
    wine double precision,
    cocktail double precision,
    table_booking boolean
);

COPY bars (ID, Name, City, Address, beer, wine, cocktail, Table_Booking)
    FROM 'C:\Users\katja\OneDrive - University of Copenhagen\DIS\DIS_Group_Project\DIS\static\bars.csv'
    WITH (FORMAT csv, DELIMITER ',', NULL '', HEADER, ENCODING 'UTF8');

