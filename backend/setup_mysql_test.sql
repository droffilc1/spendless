-- Test that checks a script that prepares a MySQL server
CREATE DATABASE IF NOT EXISTS test_db;
CREATE USER IF NOT EXISTS 'test'@'localhost' IDENTIFIED BY 'test_pwd';
GRANT USAGE ON *.* TO 'test'@'localhost';
GRANT ALL ON hbnb_test_db.* TO 'test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'test'@'localhost';
