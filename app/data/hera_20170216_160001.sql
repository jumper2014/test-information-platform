-- MySQL dump 10.13  Distrib 5.5.53, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: hera
-- ------------------------------------------------------
-- Server version	5.5.53-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Feature_Test_Flow`
--

DROP TABLE IF EXISTS `Feature_Test_Flow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Feature_Test_Flow` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `feature_name` varchar(60) DEFAULT NULL,
  `demand` varchar(1) DEFAULT NULL,
  `test_schema` varchar(1) DEFAULT NULL,
  `review` varchar(1) DEFAULT NULL,
  `achieve` varchar(1) DEFAULT NULL,
  `environment` varchar(1) DEFAULT NULL,
  `execute` varchar(1) DEFAULT NULL,
  `report` varchar(1) DEFAULT NULL,
  `archive` varchar(1) DEFAULT NULL,
  `storing` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Feature_Test_Flow`
--

LOCK TABLES `Feature_Test_Flow` WRITE;
/*!40000 ALTER TABLE `Feature_Test_Flow` DISABLE KEYS */;
INSERT INTO `Feature_Test_Flow` VALUES (1,'start-channel接口性能 _张树伟','0','0','0','0','0','0','0','0','0'),(2,'SDK上异步http-dns_冒雨楠','0','0','0','0','0','0','0','0','0'),(3,'PUFF协议测试_顾泽豪','0','0','0','0','0','0','0','0','0'),(4,'SDK支持STUN水平扩展_张树伟','0','0','0','0','0','0','0','0','0'),(5,'cache-port接口性能_曾月天','0','0','0','0','0','0','0','0','0'),(6,'boss','0','0','0','0','0','0','0','0','0'),(7,'13','0','0','0','0','0','0','0','0','0'),(8,'31','0','0','0','0','0','0','0','0','0'),(9,'31','0','0','0','0','0','0','0','0','0'),(10,'2','0','0','0','0','0','0','0','0','0'),(11,'3','0','0','0','0','0','0','0','0','0'),(12,'3','0','0','0','0','0','0','0','0','0'),(13,'4','0','0','0','0','0','0','0','0','0'),(14,'5','0','0','0','0','0','0','0','0','0'),(15,'5','0','0','0','0','0','0','0','0','0'),(16,'6','0','0','0','0','0','0','0','0','0'),(17,'7','0','0','0','0','0','0','0','0','0'),(18,'dasd','0','0','0','0','0','0','0','0','0'),(19,'asd','0','0','0','0','0','0','0','0','0'),(20,'da','0','0','0','0','0','0','0','0','0'),(21,'asd','0','0','0','0','0','0','0','0','0'),(22,'ad','0','0','0','0','0','0','0','0','0'),(23,'ad','0','0','0','0','0','0','0','0','0');
/*!40000 ALTER TABLE `Feature_Test_Flow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feature_test_progress`
--

DROP TABLE IF EXISTS `feature_test_progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feature_test_progress` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `feature_name` varchar(60) DEFAULT NULL,
  `demand` varchar(1) DEFAULT NULL,
  `test_schema` varchar(1) DEFAULT NULL,
  `review` varchar(1) DEFAULT NULL,
  `achieve` varchar(1) DEFAULT NULL,
  `environment` varchar(1) DEFAULT NULL,
  `execute` varchar(1) DEFAULT NULL,
  `report` varchar(1) DEFAULT NULL,
  `archive` varchar(1) DEFAULT NULL,
  `storing` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=426 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feature_test_progress`
--

LOCK TABLES `feature_test_progress` WRITE;
/*!40000 ALTER TABLE `feature_test_progress` DISABLE KEYS */;
INSERT INTO `feature_test_progress` VALUES (419,'SDK上异步http-dns_冒雨楠','2','2','2','0','0','0','0','0','0'),(422,'cache-port接口性能_曾月天','2','2','2','2','2','2','2','2','2'),(423,'start-channel接口性能 _张树伟','2','2','2','1','0','0','0','0','0'),(424,'SDK支持STUN水平扩展_张树伟','2','2','2','2','2','2','2','2','2'),(425,'PUFF协议测试_顾泽豪','2','2','2','1','1','1','0','0','0');
/*!40000 ALTER TABLE `feature_test_progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `machines_info`
--

DROP TABLE IF EXISTS `machines_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `machines_info` (
  `ip` varchar(20) NOT NULL,
  `username` varchar(60) DEFAULT NULL,
  `passwd` varchar(30) DEFAULT NULL,
  `cpu` int(10) DEFAULT NULL,
  `memory` int(10) DEFAULT NULL,
  PRIMARY KEY (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `machines_info`
--

LOCK TABLES `machines_info` WRITE;
/*!40000 ALTER TABLE `machines_info` DISABLE KEYS */;
INSERT INTO `machines_info` VALUES ('192.168.1.155','root','rootPass',8,16),('192.168.1.156','root','rootPass',4,8),('192.168.1.157','root','rootPass',4,16),('192.168.1.158','root','rootPass',4,16),('192.168.1.159','root','rootPass',4,16),('192.168.1.160','root','rootPass',4,16),('192.168.1.161','root','rootPass',4,16),('192.168.1.162','root','rootPass',4,16);
/*!40000 ALTER TABLE `machines_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `passwd` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'root','rootPass');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-02-16 16:00:02
