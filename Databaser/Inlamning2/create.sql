DROP SCHEMA IF EXISTS kt_inlamning2;

CREATE DATABASE kt_inlamning2;

USE kt_inlamning2;

/*
MariaDB [kt_inlamning2]> DESCRIBE bank_accounts;;
+------------+-------------+------+-----+---------------------+-------------------------------+
| Field      | Type        | Null | Key | Default             | Extra                         |
+------------+-------------+------+-----+---------------------+-------------------------------+
| id         | int(11)     | NO   | PRI | NULL                | auto_increment                |
| first_name | varchar(50) | YES  |     | NULL                |                               |
| last_name  | varchar(50) | YES  |     | NULL                |                               |
| holding    | int(11)     | YES  |     | NULL                |                               |
| created    | timestamp   | YES  |     | current_timestamp() |                               |
| modified   | timestamp   | YES  |     | current_timestamp() | on update current_timestamp() |
+------------+-------------+------+-----+---------------------+-------------------------------+
*/
CREATE TABLE bank_accounts (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  first_name varchar(50) DEFAULT NULL,
  last_name varchar(50) DEFAULT NULL,
  holding int DEFAULT NULL,
  created timestamp NULL DEFAULT current_timestamp(),
  modified timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
);

/*
MariaDB [kt_inlamning2]> DESCRIBE locations;
+----------+-------------+------+-----+---------------------+-------------------------------+
| Field    | Type        | Null | Key | Default             | Extra                         |
+----------+-------------+------+-----+---------------------+-------------------------------+
| id       | int(11)     | NO   | PRI | NULL                | auto_increment                |
| country  | varchar(50) | YES  |     | NULL                |                               |
| address  | varchar(50) | YES  |     | NULL                |                               |
| created  | timestamp   | YES  |     | current_timestamp() |                               |
| modified | timestamp   | YES  |     | current_timestamp() | on update current_timestamp() |
+----------+-------------+------+-----+---------------------+-------------------------------+
*/
CREATE TABLE locations (
  id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  country varchar(50) DEFAULT NULL,
  address varchar(50) DEFAULT NULL,
  created timestamp NULL DEFAULT current_timestamp(),
  modified timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
);

/*
MariaDB [kt_inlamning2]> DESCRIBE acc_loc_relation;
+-------------+---------+------+-----+---------+-------+
| Field       | Type    | Null | Key | Default | Extra |
+-------------+---------+------+-----+---------+-------+
| account_id  | int(11) | NO   | PRI | NULL    |       |
| location_id | int(11) | YES  | MUL | NULL    |       |
+-------------+---------+------+-----+---------+-------+
*/
CREATE TABLE acc_loc_relation (
    account_id int PRIMARY KEY,
    location_id int,
    FOREIGN KEY (account_id) REFERENCES bank_accounts(id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(id)
  );

LOAD DATA LOCAL INFILE './dump.sql.txt' INTO TABLE bank_accounts COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY "'";

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
        address LIKE 'Asteroid road%'
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
        address LIKE 'Comet road%'
    )
  );

SELECT
  b.id, b.first_name, b.last_name, b.holding, l.country, l.address
FROM
  bank_accounts b
  JOIN acc_loc_relation a ON b.id = a.account_id
  JOIN locations l ON l.id = a.location_id
WHERE
  l.country LIKE "SE";
