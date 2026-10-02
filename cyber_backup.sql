-- MySQL dump 10.13  Distrib 9.6.0, for Win64 (x86_64)
--
-- Host: localhost    Database: cyber
-- ------------------------------------------------------
-- Server version	9.6.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '8dd97aeb-117d-11f1-9e8e-0a0027000005:1-1418';

--
-- Table structure for table `incident`
--

DROP TABLE IF EXISTS `incident`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incident` (
  `incident_id` int NOT NULL AUTO_INCREMENT,
  `reporter_id` int NOT NULL,
  `category_id` int NOT NULL,
  `incident_title` varchar(150) NOT NULL,
  `description` text,
  `date_reported` datetime NOT NULL,
  `severity` enum('Low','Medium','High','Critical') NOT NULL,
  `current_status` varchar(50) NOT NULL,
  `location` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`incident_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incident`
--

LOCK TABLES `incident` WRITE;
/*!40000 ALTER TABLE `incident` DISABLE KEYS */;
INSERT INTO `incident` VALUES (1,101,1,'Phishing Email Reported','A student received an email requesting university login credentials through a suspicious link.','2026-08-01 09:15:00','Medium','Reported','Main Campus'),(2,102,2,'Malware Infection on Laptop','A staff laptop was detected running suspicious software after downloading an unknown file.','2026-08-02 11:30:00','High','Investigating','Faculty of Science and Technology'),(3,103,3,'Unauthorized Account Access','A student reported several unsuccessful login attempts followed by a successful login from an unknown location.','2026-08-03 14:20:00','High','Assigned','Main Campus'),(4,104,4,'Suspicious Network Traffic','Unusual outbound network traffic was detected from a computer connected to the university network.','2026-08-04 08:45:00','Critical','Investigating','ICT Department'),(5,105,1,'Phishing Message on WhatsApp','A staff member received a fraudulent message requesting confidential university information.','2026-08-05 16:10:00','Low','Closed','Administration Block'),(6,106,5,'Lost University Laptop','A university laptop was reported missing from an office.','2026-08-06 10:05:00','High','Reported','Library'),(7,107,6,'Data Breach Suspected','Unauthorized access to files containing sensitive university information was suspected.','2026-08-07 13:40:00','Critical','Investigating','ICT Department'),(8,108,2,'Virus Detected on Desktop','Antivirus software detected malware on a desktop computer used by a staff member.','2026-08-08 09:25:00','Medium','Resolved','Finance Department'),(9,109,3,'Suspicious Student Login','Multiple login attempts were detected on a student account from an unfamiliar device.','2026-08-09 15:35:00','Medium','Triaged','Main Campus'),(10,110,7,'Unauthorized System Access','An unauthorized user attempted to gain access to an internal university system.','2026-08-10 12:15:00','Critical','Assigned','Server Room'),(11,111,5,'Stolen Mobile Device','A university-owned mobile device was reported stolen.','2026-08-11 17:00:00','High','Closed','Student Residence'),(12,112,1,'Fake Password Reset Email','A user received a fake password reset email containing a suspicious web address.','2026-08-12 10:30:00','Low','Reported','Main Campus');
/*!40000 ALTER TABLE `incident` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  `unit_price` decimal(10,2) DEFAULT NULL,
  `order_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1,5,NULL,'2026-09-24 08:47:42'),(2,1,5,NULL,'2026-09-24 08:54:10'),(3,1,5,NULL,'2026-09-24 08:55:04'),(4,1,5,NULL,'2026-09-24 08:58:39');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `price_audit`
--

DROP TABLE IF EXISTS `price_audit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `price_audit` (
  `audit_id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `old_price` decimal(10,2) NOT NULL,
  `new_price` decimal(10,2) NOT NULL,
  `changed_by` varchar(100) NOT NULL,
  `changed_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`audit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `price_audit`
--

LOCK TABLES `price_audit` WRITE;
/*!40000 ALTER TABLE `price_audit` DISABLE KEYS */;
/*!40000 ALTER TABLE `price_audit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock_qty` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Exercise Book',2500.00,100),(2,'Ballpoint Pen',500.00,200),(3,'Scientific Calculator',45000.00,10);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vw_five_most_recent_incidents`
--

DROP TABLE IF EXISTS `vw_five_most_recent_incidents`;
/*!50001 DROP VIEW IF EXISTS `vw_five_most_recent_incidents`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_five_most_recent_incidents` AS SELECT 
 1 AS `incident_id`,
 1 AS `incident_title`,
 1 AS `date_reported`,
 1 AS `severity`,
 1 AS `current_status`,
 1 AS `location`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_high_and_critical_incidents`
--

DROP TABLE IF EXISTS `vw_high_and_critical_incidents`;
/*!50001 DROP VIEW IF EXISTS `vw_high_and_critical_incidents`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_high_and_critical_incidents` AS SELECT 
 1 AS `incident_id`,
 1 AS `incident_title`,
 1 AS `severity`,
 1 AS `current_status`,
 1 AS `date_reported`,
 1 AS `location`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_incident_count_by_severity`
--

DROP TABLE IF EXISTS `vw_incident_count_by_severity`;
/*!50001 DROP VIEW IF EXISTS `vw_incident_count_by_severity`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_incident_count_by_severity` AS SELECT 
 1 AS `severity`,
 1 AS `total_incidents`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_incidents_missing_location`
--

DROP TABLE IF EXISTS `vw_incidents_missing_location`;
/*!50001 DROP VIEW IF EXISTS `vw_incidents_missing_location`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_incidents_missing_location` AS SELECT 
 1 AS `incident_id`,
 1 AS `incident_title`,
 1 AS `severity`,
 1 AS `current_status`,
 1 AS `date_reported`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_incidents_reported_after_august_7`
--

DROP TABLE IF EXISTS `vw_incidents_reported_after_august_7`;
/*!50001 DROP VIEW IF EXISTS `vw_incidents_reported_after_august_7`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_incidents_reported_after_august_7` AS SELECT 
 1 AS `incident_id`,
 1 AS `incident_title`,
 1 AS `date_reported`,
 1 AS `severity`,
 1 AS `current_status`,
 1 AS `location`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `vw_phishing_incidents`
--

DROP TABLE IF EXISTS `vw_phishing_incidents`;
/*!50001 DROP VIEW IF EXISTS `vw_phishing_incidents`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vw_phishing_incidents` AS SELECT 
 1 AS `incident_id`,
 1 AS `incident_title`,
 1 AS `description`,
 1 AS `severity`,
 1 AS `current_status`,
 1 AS `date_reported`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vw_five_most_recent_incidents`
--

/*!50001 DROP VIEW IF EXISTS `vw_five_most_recent_incidents`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_five_most_recent_incidents` AS select `incident`.`incident_id` AS `incident_id`,`incident`.`incident_title` AS `incident_title`,`incident`.`date_reported` AS `date_reported`,`incident`.`severity` AS `severity`,`incident`.`current_status` AS `current_status`,`incident`.`location` AS `location` from `incident` order by `incident`.`date_reported` desc limit 5 */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_high_and_critical_incidents`
--

/*!50001 DROP VIEW IF EXISTS `vw_high_and_critical_incidents`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_high_and_critical_incidents` AS select `incident`.`incident_id` AS `incident_id`,`incident`.`incident_title` AS `incident_title`,`incident`.`severity` AS `severity`,`incident`.`current_status` AS `current_status`,`incident`.`date_reported` AS `date_reported`,`incident`.`location` AS `location` from `incident` where (`incident`.`severity` in ('High','Critical')) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_incident_count_by_severity`
--

/*!50001 DROP VIEW IF EXISTS `vw_incident_count_by_severity`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_incident_count_by_severity` AS select `incident`.`severity` AS `severity`,count(0) AS `total_incidents` from `incident` group by `incident`.`severity` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_incidents_missing_location`
--

/*!50001 DROP VIEW IF EXISTS `vw_incidents_missing_location`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_incidents_missing_location` AS select `incident`.`incident_id` AS `incident_id`,`incident`.`incident_title` AS `incident_title`,`incident`.`severity` AS `severity`,`incident`.`current_status` AS `current_status`,`incident`.`date_reported` AS `date_reported` from `incident` where (`incident`.`location` is null) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_incidents_reported_after_august_7`
--

/*!50001 DROP VIEW IF EXISTS `vw_incidents_reported_after_august_7`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_incidents_reported_after_august_7` AS select `incident`.`incident_id` AS `incident_id`,`incident`.`incident_title` AS `incident_title`,`incident`.`date_reported` AS `date_reported`,`incident`.`severity` AS `severity`,`incident`.`current_status` AS `current_status`,`incident`.`location` AS `location` from `incident` where (`incident`.`date_reported` > '2026-08-07 00:00:00') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `vw_phishing_incidents`
--

/*!50001 DROP VIEW IF EXISTS `vw_phishing_incidents`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vw_phishing_incidents` AS select `incident`.`incident_id` AS `incident_id`,`incident`.`incident_title` AS `incident_title`,`incident`.`description` AS `description`,`incident`.`severity` AS `severity`,`incident`.`current_status` AS `current_status`,`incident`.`date_reported` AS `date_reported` from `incident` where (`incident`.`incident_title` like '%Phishing%') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-02 13:38:07
