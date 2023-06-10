CREATE TABLE IF NOT EXISTS ratings (
    id character(3),
    rating double precision,
    num_ratings int
);

COPY ratings (ID, rating, num_ratings)
    FROM 'C:\Users\katja\OneDrive - University of Copenhagen\DIS\DIS_Group_Project\DIS\static\ratings.csv'
    DELIMITER ',' NULL AS '' CSV HEADER;
