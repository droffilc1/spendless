-- Prepares a MySQL server
CREATE DATABASE IF NOT EXISTS dev_db;
CREATE USER IF NOT EXISTS 'dev'@'localhost' IDENTIFIED BY 'dev_pwd';
GRANT USAGE ON *.* TO 'dev'@'localhost';
GRANT ALL ON hbnb_dev_db.* TO 'dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'dev'@'localhost';
