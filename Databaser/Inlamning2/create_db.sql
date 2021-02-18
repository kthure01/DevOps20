/* Denna fil går att ladda in i MaruaDB med: mysql -u root -p  < create_db.sql
   Den skapar upp hela exempeldatabasen och kör de frågor som
   efterfrågas i inlämningsuppgiften. Visar även CRUD-exempel.
*/

/* Tar bort databasen om den finns */
DROP DATABASE IF EXISTS kt_inlamning2;

CREATE DATABASE kt_inlamning2;

USE kt_inlamning2;

/* 2 st tabeller från inlämningsuppgift 1 */
CREATE TABLE bank_accounts (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name varchar(50) DEFAULT NULL,
  last_name varchar(50) DEFAULT NULL,
  holding int DEFAULT NULL,
  created timestamp NULL DEFAULT current_timestamp(),
  modified timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
);

CREATE TABLE locations (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  country varchar(50) DEFAULT NULL,
  address varchar(50) DEFAULT NULL,
  created timestamp NULL DEFAULT current_timestamp(),
  modified timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
);

/*
  Tabell från inlämningsuppgift 2.
  Brukar själv, nästan alltid, lägga in en id-kolumn, men enl uppgift så skulle vi inte göra detta.
*/
CREATE TABLE acc_loc_relations (
    account_id int PRIMARY KEY,
    location_id int,
    FOREIGN KEY (account_id) REFERENCES bank_accounts(id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

/* Läser in data, från filen dump.sql.txt, till tabellen bank_accounts */
LOAD DATA LOCAL INFILE './bank_accounts.csv' INTO TABLE bank_accounts COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY "'";

/* Lägger in uppgiftens bifogade data till tabellen locations */
INSERT INTO
  locations (country, address)
VALUES
  ('SE', 'Vimmerbygatan 20'),
  ('US', 'Asteroid road 5'),
  ('US', 'Comet road 41'),
  ('SE', 'Brunnsgatan 7');

/* Skapar några ny konton enl bifogad data */
INSERT INTO
  bank_accounts (first_name, last_name, holding)
VALUES
  ('Corbin', 'Hauck', 345674);
  
/*
  Lägger in relationerna mellan bank_accounts och locations i tabellen acc_loc_relations.
  Använder mig av LAST_INSERT_ID() för att få id't på den senast skapade bank_accounts
  och en SELECT-fråga för att få fram location id.
*/
INSERT INTO
  acc_loc_relations (account_id, location_id)
VALUES
  (
    LAST_INSERT_ID(),
    (
      SELECT
        id
      FROM
        locations
      WHERE
        address LIKE 'Brunnsgatan%'
    )
  );

INSERT INTO
  bank_accounts (first_name, last_name, holding)
VALUES
  ('Vanya', 'Worsell', 9879855);

INSERT INTO
  acc_loc_relations (account_id, location_id)
VALUES
  (
    LAST_INSERT_ID(),
    (
      SELECT
        id
      FROM
        locations
      WHERE
        address LIKE 'Asteroid road%'
    )
  );

INSERT INTO
  bank_accounts (first_name, last_name, holding)
VALUES
  ('Eldon', 'McCartan', 234246);

INSERT INTO
  acc_loc_relations (account_id, location_id)
VALUES
  (
    LAST_INSERT_ID(),
    (
      SELECT
        id
      FROM
        locations
      WHERE
        address LIKE 'Vimmerbygatan%'
    )
  );

INSERT INTO
  bank_accounts (first_name, last_name, holding)
VALUES
  ('Ingunna', 'Castellucci', 23423);

INSERT INTO
  acc_loc_relations (account_id, location_id)
VALUES
  (
    LAST_INSERT_ID(),
    (
      SELECT
        id
      FROM
        locations
      WHERE
        address LIKE 'Comet road%'
    )
  );



SELECT "===============================================================" AS '';

/*
   En query för att plocka ut de adresser där country="SE"
*/
SELECT "En query för att plocka ut de adresser med country=SE" AS ' ';

/*
SELECT-frågan i del 3 av uppgiften.
*/
SELECT
  b.id, b.first_name, b.last_name, b.holding, l.country, l.address
FROM
  bank_accounts b
  JOIN acc_loc_relations a ON b.id = a.account_id
  JOIN locations l ON l.id = a.location_id
WHERE
  l.country LIKE "SE";


SELECT "===============================================================" AS '';
SELECT "Visar CRUD" AS '';
SELECT "CREATE: INSERT INTO bank_accounts (first_name, last_name, holding) VALUES ('Kent', 'Thureson', 1234567890)" AS '';
INSERT INTO bank_accounts (first_name, last_name, holding) VALUES ('Kent', 'Thureson', 67890); 
SELECT * FROM bank_accounts WHERE id > 1003;


SELECT "===============================================================" AS '';
SELECT "READ: SELECT * FROM bank_accounts WHERE last_name LIKE 'Thureson'" AS '';
SELECT * FROM bank_accounts WHERE id > 1003;


SELECT "===============================================================" AS '';
SELECT "UPDATE: UPDATE bank_accounts SET last_name = 'Thureson updated' WHERE last_name LIKE 'Thureson'" AS '';
UPDATE bank_accounts SET last_name = 'Thureson updated' WHERE last_name LIKE 'Thureson';
SELECT * FROM bank_accounts WHERE id > 1003;


SELECT "===============================================================" AS '';
SELECT "DELETE: DELETE FROM bank_accounts WHERE last_name LIKE 'Thureson%'" AS '';
DELETE FROM bank_accounts WHERE last_name LIKE 'Thureson%';
SELECT * FROM bank_accounts WHERE id > 1003;


