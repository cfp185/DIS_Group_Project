CREATE TABLE IF NOT EXISTS bars(
id char(3),
type char(20),
gender char(20),
skin_tone char(30),
count int,
accessories char(10000),
CONSTRAINT nft_pk PRIMARY KEY (id));

copy  Attributes(id,type,gender, skin_tone, count, accessories)
            from 'C:\Users\katja\Downloads\nft-crypto-punk\nft-crypto-punk\tmp\attributes.csv'
            delimiter ','
            CSV HEADER;
