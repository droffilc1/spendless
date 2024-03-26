-- MySQL dump

-- Drop database
DROP DATABASE IF EXISTS dev_db;

-- Create database + user if doesn't exist
CREATE DATABASE IF NOT EXISTS dev_db;
CREATE USER IF NOT EXISTS 'dev'@'localhost' IDENTIFIED BY 'dev_pwd';
GRANT ALL ON dev_db.* TO 'dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'dev'@'localhost';
FLUSH PRIVILEGES;

USE dev_db;

-- Table structure for table `categories`
DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `id` VARCHAR(60) PRIMARY KEY,
  `name` VARCHAR(50) UNIQUE NOT NULL
);

-- Add sample data to categories
LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES
('1', 'Food'),
('2', 'Transportation'),
('3', 'Entertainment');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

-- Table structure for table `users`
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` VARCHAR(60) PRIMARY KEY,
  `username` VARCHAR(50) UNIQUE NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `password` VARCHAR(100) NOT NULL
);

-- Add sample data to users
LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
('1', 'john_doe', 'johndoe@john.com', 'password123'),
('2', 'jane_smith', 'janedoe@john.com', 'password456');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

-- Table structure for table `expenses`
DROP TABLE IF EXISTS `expenses`;
CREATE TABLE `expenses` (
  `id` VARCHAR(60) PRIMARY KEY,
  `amount` FLOAT NOT NULL,
  `description` VARCHAR(255),
  `category_id` VARCHAR(60),
  `user_id` VARCHAR(60) NOT NULL,
  FOREIGN KEY (`category_id`) REFERENCES `categories`(`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);

-- Add sample data to expenses
LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES
('1', 20.50, 'Lunch with friends', '1', '1'),
('2', 15.75, 'Bus fare', '2', '2');
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;
