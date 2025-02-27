CREATE DATABASE  IF NOT EXISTS `library` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `library`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `author`
--

DROP TABLE IF EXISTS `author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author` (
  `idauthor` int NOT NULL AUTO_INCREMENT,
  `author_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idauthor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author`
--

LOCK TABLES `author` WRITE;
/*!40000 ALTER TABLE `author` DISABLE KEYS */;
INSERT INTO `author` VALUES (1,'James Clear'),(2,'Harper Lee'),(3,'J. K. Rowling'),(4,'John Ronald Reuel Tolkien'),(5,'George Orwell');
/*!40000 ALTER TABLE `author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(45) DEFAULT NULL,
  `book_description` varchar(900) DEFAULT NULL,
  `book_code` varchar(45) DEFAULT NULL,
  `book_category` varchar(45) DEFAULT NULL,
  `book_author` varchar(45) DEFAULT NULL,
  `book_publisher` varchar(45) DEFAULT NULL,
  `book_price` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'To Kill a Mockingbird','To Kill a Mockingbird is a 1960 novel by American author Harper Lee. It became instantly successful after its release; in the United States, it is widely read in high schools and middle schools.','001','Bildungsroman','Harper Lee','HarperCollins',55),(2,'Atomic Habits','Atomic Habits by James Clear is a comprehensive, practical guide on how to change your habits and get 1% better every day. Using a framework called the Four Laws of Behavior Change, Atomic Habits teaches readers a simple set of rules for creating good habits and breaking bad ones.','002','nonfiction','James Clear','Penguin House',99),(3,'The Sorcerer\'s Stone','Harry Potter and the Sorcerer\'s Stone is a novel by J.K. Rowling about an 11-year-old boy who discovers he is a wizard and attends Hogwarts School of Witchcraft and Wizardry. The book explores themes of friendship, love, and good and evil.','003','fantasy literature','J. K. Rowling','Scholastic Corporation',60),(4,'The Lord of the Rings','The Lord of the Rings is a trilogy of epic fantasy adventure films directed by Peter Jackson, based on the novel The Lord of the Rings by English author J. R. R. Tolkien. The films are titled identically to the three volumes of the novel: The Fellowship of the Ring, The Two Towers, and The Return of the King.','004','Adventure','John Ronald Reuel Tolkien','Houghton Mifflin',120),(5,'1984','1984 is a dystopian novel by George Orwell that was published in 1949. It depicts a future where the government controls every aspect of people\'s lives, and where individuality is not permitted. The book is a warning about the dangers of totalitarianism and mass surveillance.','005','Dystopian Fiction','George Orwell','Secker & Warburg',30);
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `idcategory` int NOT NULL AUTO_INCREMENT,
  `category_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcategory`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Bildungsroman'),(2,'nonfiction'),(3,'fantasy literature'),(4,'Adventure'),(5,'Dystopian Fiction');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `idclients` int NOT NULL AUTO_INCREMENT,
  `client_name` varchar(45) DEFAULT NULL,
  `client_email` varchar(45) DEFAULT NULL,
  `client_passport_number` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idclients`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'Sky Lee','skylee@gmail.com','M29182938'),(2,'John Smiths','john333@gmail.com','N3921222'),(3,'Lionel Messi','bestatsoccer@gmail.com','M2921832'),(4,'Cristiano Ronaldo','soccergod@gmail.com','M9272613'),(5,'Dwayne Johnson','rock@gmail.com','M76273722'),(6,'Ryan Reynolds','secretsuperhero@gmail.com','M82837752');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dayoperations`
--

DROP TABLE IF EXISTS `dayoperations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dayoperations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_name` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `days` int DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `client` varchar(45) DEFAULT NULL,
  `to_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dayoperations`
--

LOCK TABLES `dayoperations` WRITE;
/*!40000 ALTER TABLE `dayoperations` DISABLE KEYS */;
INSERT INTO `dayoperations` VALUES (1,'To Kill a Mockingbird','Rent',4,'2025-02-28 00:00:00','Ryan Reynolds','2025-03-04 00:00:00'),(2,'Atomic Habits','Rent',9,'2025-02-28 00:00:00','Dwayne Johnson','2025-03-09 00:00:00'),(3,'1984','Rent',4,'2025-02-28 00:00:00','Lionel Messi','2025-03-04 00:00:00');
/*!40000 ALTER TABLE `dayoperations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publisher` (
  `idpublisher` int NOT NULL AUTO_INCREMENT,
  `publisher_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idpublisher`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher`
--

LOCK TABLES `publisher` WRITE;
/*!40000 ALTER TABLE `publisher` DISABLE KEYS */;
INSERT INTO `publisher` VALUES (1,'HarperCollins'),(2,'Penguin House'),(3,'Scholastic Corporation'),(4,'Houghton Mifflin'),(5,'Secker & Warburg');
/*!40000 ALTER TABLE `publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `idusers` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) DEFAULT NULL,
  `user_email` varchar(45) DEFAULT NULL,
  `user_password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idusers`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin@gmail.com','123');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-28 10:38:01
