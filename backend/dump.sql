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
  `id` VARCHAR(36) PRIMARY KEY,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `name` VARCHAR(50) UNIQUE NOT NULL
);

-- Add sample data to categories
LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES
('05b0b99c-f10e-4e3a-88d1-b3187d6998ee', NOW(), NOW(), 'Food'), -- Updated id to match the specified format
('2b9e95f2-524b-43eb-b1cf-33c8dbf02b8d', NOW(), NOW(), 'Transportation'), -- Updated id to match the specified format
('7e39ff7a-5a56-4da2-8228-d0ed35473f4d', NOW(), NOW(), 'Entertainment'); -- Updated id to match the specified format
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

-- Table structure for table `users`
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` VARCHAR(36) PRIMARY KEY,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `username` VARCHAR(50) UNIQUE NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `password` VARCHAR(100) NOT NULL
);

-- Add sample data to users
LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
('a67e5e80-759d-4c51-8596-288c7260d18f', NOW(), NOW(), 'john_doe', 'johndoe@john.com', 'password123'), -- Updated id to match the specified format
('42fd2057-7618-4ff2-a2b3-18b4d7d12e90', NOW(), NOW(), 'jane_smith', 'janedoe@john.com', 'password456'); -- Updated id to match the specified format
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

-- Table structure for table `expenses`
DROP TABLE IF EXISTS `expenses`;
CREATE TABLE `expenses` (
  `id` VARCHAR(36) PRIMARY KEY,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `amount` FLOAT NOT NULL,
  `description` VARCHAR(255),
  `category_id` VARCHAR(36),
  `user_id` VARCHAR(36) NOT NULL,
  FOREIGN KEY (`category_id`) REFERENCES `categories`(`id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`)
);

-- Add sample data to expenses
LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES
('b725ae9e-4d53-462d-82f1-8eefaa735c4b', NOW(), NOW(), 20.50, 'Lunch with friends', '05b0b99c-f10e-4e3a-88d1-b3187d6998ee', 'a67e5e80-759d-4c51-8596-288c7260d18f'), -- Updated id to match the specified format
('e1c54ec7-fc4b-4da4-b78c-7269cc7af93e', NOW(), NOW(), 15.75, 'Bus fare', '2b9e95f2-524b-43eb-b1cf-33c8dbf02b8d', '42fd2057-7618-4ff2-a2b3-18b4d7d12e90'); -- Updated id to match the specified format
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;
