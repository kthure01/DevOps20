USE mysql;

DROP SCHEMA IF EXISTS db_inlamning2;

CREATE DATABASE db_inlamning2;

USE db_inlamning2;

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

CREATE TABLE acc_loc_relation (
    id int PRIMARY KEY AUTO_INCREMENT,
    account_id int,
    location_id int,
    FOREIGN KEY (account_id) REFERENCES bank_accounts(id),
    FOREIGN KEY (location_id) REFERENCES locations(id)
  );

LOAD DATA LOCAL INFILE './dump2.txt' INTO TABLE bank_accounts COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY "'";

INSERT INTO
  locations (country, address)
VALUES
  ('SE', 'Vimmerbygatan 20'),
  ('US', 'Asteroid road 5'),
  ('US', 'Comet road 41'),
  ('SE', 'Brunnsgatan 7');

INSERT INTO
  bank_accounts (first_name, last_name, holding)
VALUES
  ('Corbin', 'Hauck', 345674);
  
INSERT INTO
  acc_loc_relation (account_id, location_id)
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
  acc_loc_relation (account_id, location_id)
VALUES
  (
    LAST_INSERT_ID(),
    (
      SELECT
        id
      FROM
        locations
      WHERE
        address LIKE 'Asteroid%'
    )
  );

INSERT INTO
  bank_accounts (first_name, last_name, holding)
VALUES
  ('Eldon', 'McCartan', 234246);

INSERT INTO
  acc_loc_relation (account_id, location_id)
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
  acc_loc_relation (account_id, location_id)
VALUES
  (
    LAST_INSERT_ID(),
    (
      SELECT
        id
      FROM
        locations
      WHERE
        address LIKE 'Comet%'
    )
  );

SELECT
  *
FROM
  bank_accounts b
  JOIN acc_loc_relation a ON b.id = a.account_id
  JOIN locations l ON l.id = a.location_id
WHERE
  l.country LIKE "SE";

