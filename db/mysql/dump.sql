-- MySQL dump 10.13  Distrib 5.5.55, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: unam_biblioteca
-- ------------------------------------------------------
-- Server version	5.5.55-0+deb8u1

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
-- Table structure for table `ADM_ACCOUNTS`
--

DROP TABLE IF EXISTS `ADM_ACCOUNTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_ACCOUNTS` (
  `ID` varchar(32) NOT NULL,
  `USER_ID` varchar(32) NOT NULL,
  `LIBRARY_ID` varchar(32) NOT NULL,
  `ACCOUNT` varchar(32) NOT NULL,
  `PASSWORD` varchar(256) NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `adm_accounts_pk` (`ID`),
  KEY `ADM_ACCOUNTS_ID_index` (`ID`),
  KEY `adm_users_adm_accounts_fk` (`USER_ID`),
  KEY `lib_library_adm_accounts_fk` (`LIBRARY_ID`),
  CONSTRAINT `adm_users_adm_accounts_fk` FOREIGN KEY (`USER_ID`) REFERENCES `ADM_USERS` (`ID`),
  CONSTRAINT `lib_library_adm_accounts_fk` FOREIGN KEY (`LIBRARY_ID`) REFERENCES `LIB_LIBRARY` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_ACCOUNTS`
--

LOCK TABLES `ADM_ACCOUNTS` WRITE;
/*!40000 ALTER TABLE `ADM_ACCOUNTS` DISABLE KEYS */;
/*!40000 ALTER TABLE `ADM_ACCOUNTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_CLIENTS`
--

DROP TABLE IF EXISTS `ADM_CLIENTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_CLIENTS` (
  `ID` varchar(32) NOT NULL,
  `NAME` varchar(128) NOT NULL,
  `TOKEN` varchar(256) NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ADM_CLIENTS_TOKEN_uindex` (`TOKEN`),
  UNIQUE KEY `ADM_CLIENTS_NAME_uindex` (`NAME`),
  KEY `ADM_CLIENTS_ID_index` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_CLIENTS`
--

LOCK TABLES `ADM_CLIENTS` WRITE;
/*!40000 ALTER TABLE `ADM_CLIENTS` DISABLE KEYS */;
INSERT INTO `ADM_CLIENTS` VALUES ('33ca8c20fc3207a5e31f85b11ffdd886','CLIENT_ANDROID','40a60830-6047-11e7-8d1d-0071cc2af855',1,0,0,'2017-07-03 18:26:12',NULL),('f5ee9cf27aa09fea3055f6ca8214fecc','CLIENT_WEB','4fd411b4-4e52-11e7-9ca5-0071cc2af855',1,0,0,'2017-06-10 22:01:49','2017-06-10 22:01:49');
/*!40000 ALTER TABLE `ADM_CLIENTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_DEVICES`
--

DROP TABLE IF EXISTS `ADM_DEVICES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_DEVICES` (
  `ID` varchar(32) NOT NULL,
  `NAME` varchar(32) NOT NULL,
  `USER_ID` varchar(32) NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ADM_DEVICES_ID_index` (`ID`),
  KEY `adm_users_adm_devices_fk` (`USER_ID`),
  CONSTRAINT `adm_users_adm_devices_fk` FOREIGN KEY (`USER_ID`) REFERENCES `ADM_USERS` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_DEVICES`
--

LOCK TABLES `ADM_DEVICES` WRITE;
/*!40000 ALTER TABLE `ADM_DEVICES` DISABLE KEYS */;
/*!40000 ALTER TABLE `ADM_DEVICES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_SESSIONS`
--

DROP TABLE IF EXISTS `ADM_SESSIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_SESSIONS` (
  `USER_ID` varchar(32) NOT NULL,
  `CLIENT_ID` varchar(32) NOT NULL,
  `TOKEN` varchar(256) NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `EXPIRATION_TIME` datetime NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`USER_ID`,`CLIENT_ID`),
  UNIQUE KEY `ADM_SESSIONS_TOKEN_uindex` (`TOKEN`),
  UNIQUE KEY `adm_sessions_pk` (`USER_ID`,`CLIENT_ID`),
  KEY `ADM_SESSIONS_USER_ID_index` (`USER_ID`),
  KEY `adm_clients_adm_sessions_fk` (`CLIENT_ID`),
  CONSTRAINT `adm_clients_adm_sessions_fk` FOREIGN KEY (`CLIENT_ID`) REFERENCES `ADM_CLIENTS` (`ID`),
  CONSTRAINT `adm_users_adm_sessions_fk` FOREIGN KEY (`USER_ID`) REFERENCES `ADM_USERS` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_SESSIONS`
--

LOCK TABLES `ADM_SESSIONS` WRITE;
/*!40000 ALTER TABLE `ADM_SESSIONS` DISABLE KEYS */;
/*!40000 ALTER TABLE `ADM_SESSIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADM_USERS`
--

DROP TABLE IF EXISTS `ADM_USERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ADM_USERS` (
  `ID` varchar(32) NOT NULL,
  `SCHOOL_ID` varchar(32) NOT NULL,
  `NAME` varchar(256) NOT NULL,
  `LASTNAME` varchar(256) NOT NULL,
  `MAIL` varchar(128) NOT NULL,
  `PASSWORD` varchar(256) NOT NULL,
  `ACCOUNT_NUMBER` varchar(16) DEFAULT NULL,
  `GENRE` varchar(16) NOT NULL,
  `PHONE` varchar(16) DEFAULT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ADM_USERS_MAIL_uindex` (`MAIL`),
  KEY `lib_school_adm_users_fk` (`SCHOOL_ID`),
  CONSTRAINT `lib_school_adm_users_fk` FOREIGN KEY (`SCHOOL_ID`) REFERENCES `LIB_SCHOOLS` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADM_USERS`
--

LOCK TABLES `ADM_USERS` WRITE;
/*!40000 ALTER TABLE `ADM_USERS` DISABLE KEYS */;
/*!40000 ALTER TABLE `ADM_USERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_BOOKS`
--

DROP TABLE IF EXISTS `LIB_BOOKS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_BOOKS` (
  `ID` varchar(32) NOT NULL,
  `LIBRARY_ID` varchar(32) NOT NULL,
  `CLASSIFICATION` varchar(64) NOT NULL,
  `AUTHOR` varchar(128) NOT NULL,
  `TITLE` varchar(256) NOT NULL,
  `YEAR` varchar(8) NOT NULL,
  `NUMBER_SYSTEM` varchar(32) NOT NULL,
  `ISBN` varchar(64) NOT NULL,
  `COPIES` int(11) NOT NULL,
  `ON_LOAN` int(11) NOT NULL,
  `CLASSIFICATION_DEWEY` varchar(64) DEFAULT NULL,
  `PUBLICATION_DATA` varchar(128) DEFAULT NULL,
  `DESCRIPTION` varchar(256) DEFAULT NULL,
  `SERIE` varchar(256) DEFAULT NULL,
  `COURSES` varchar(256) DEFAULT NULL,
  `TYPE` int(11) NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `lib_library_lib_books_fk` (`LIBRARY_ID`),
  KEY `LIB_BOOKS_TITLE_index` (`TITLE`),
  KEY `LIB_BOOKS_AUTHOR_index` (`AUTHOR`),
  KEY `LIB_BOOKS_CLASSIFICATION_index` (`CLASSIFICATION`),
  CONSTRAINT `lib_library_lib_books_fk` FOREIGN KEY (`LIBRARY_ID`) REFERENCES `LIB_LIBRARY` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_BOOKS`
--

LOCK TABLES `LIB_BOOKS` WRITE;
/*!40000 ALTER TABLE `LIB_BOOKS` DISABLE KEYS */;
INSERT INTO `LIB_BOOKS` VALUES ('c6944b8b9de87982540d577a3855f15e','97af4cc61899e3c6ddefe0791ed6c49d','QA76.9O35 J55','Jiménez de Parga, Carlos','UML : aplicaciones en Java y C++','2015','001773113','9788499645162',2,0,NULL,'Paracuellos de Jarama, Madrid : Ra-Ma, [2015]','411 páginas : ilustraciones',NULL,NULL,0,1,0,'2017-06-12 02:24:01','2017-06-12 02:24:01');
/*!40000 ALTER TABLE `LIB_BOOKS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_BORROW_BOOKS`
--

DROP TABLE IF EXISTS `LIB_BORROW_BOOKS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_BORROW_BOOKS` (
  `ID` varchar(32) NOT NULL,
  `BOOK_ID` varchar(32) NOT NULL,
  `USER_ID` varchar(32) NOT NULL,
  `TAKE_TIME` datetime NOT NULL,
  `EXPIRATION_TIME` datetime NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  `RENOVATIONS` int(11) NOT NULL,
  `MULCT` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `LIB_BORROW_BOOKS_TAKE_TIME_index` (`TAKE_TIME`),
  KEY `LIB_BORROW_BOOKS_EXPIRATION_TIME_index` (`EXPIRATION_TIME`),
  KEY `lib_books_lib_borrow_books_fk` (`BOOK_ID`),
  KEY `adm_users_lib_borrow_books_fk` (`USER_ID`),
  CONSTRAINT `adm_users_lib_borrow_books_fk` FOREIGN KEY (`USER_ID`) REFERENCES `ADM_USERS` (`ID`),
  CONSTRAINT `lib_books_lib_borrow_books_fk` FOREIGN KEY (`BOOK_ID`) REFERENCES `LIB_BOOKS` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_BORROW_BOOKS`
--

LOCK TABLES `LIB_BORROW_BOOKS` WRITE;
/*!40000 ALTER TABLE `LIB_BORROW_BOOKS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LIB_BORROW_BOOKS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_FAVORITES_BOOKS`
--

DROP TABLE IF EXISTS `LIB_FAVORITES_BOOKS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_FAVORITES_BOOKS` (
  `BOOK_ID` varchar(32) NOT NULL,
  `USER_ID` varchar(32) NOT NULL,
  `LAST_SYNC` datetime NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`BOOK_ID`,`USER_ID`),
  UNIQUE KEY `lib_books_favorites_pk` (`BOOK_ID`,`USER_ID`),
  KEY `LIB_BOOKS_FAVORITES_BOOK_ID_index` (`BOOK_ID`),
  KEY `adm_users_lib_books_favorites_fk` (`USER_ID`),
  CONSTRAINT `adm_users_lib_books_favorites_fk` FOREIGN KEY (`USER_ID`) REFERENCES `ADM_USERS` (`ID`),
  CONSTRAINT `lib_books_lib_books_favorites_fk` FOREIGN KEY (`BOOK_ID`) REFERENCES `LIB_BOOKS` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_FAVORITES_BOOKS`
--

LOCK TABLES `LIB_FAVORITES_BOOKS` WRITE;
/*!40000 ALTER TABLE `LIB_FAVORITES_BOOKS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LIB_FAVORITES_BOOKS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_LIBRARY`
--

DROP TABLE IF EXISTS `LIB_LIBRARY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_LIBRARY` (
  `ID` varchar(32) NOT NULL,
  `CLASS_NAME` varchar(32) NOT NULL,
  `NAME` varchar(64) NOT NULL,
  `DIVISION` varchar(128) NOT NULL,
  `ENTITY` varchar(128) NOT NULL,
  `KEY` varchar(32) NOT NULL,
  `WEBSITE` varchar(128) NOT NULL,
  `ADDRESS` varchar(256) NOT NULL,
  `TELEPHONE` varchar(64) NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_LIBRARY`
--

LOCK TABLES `LIB_LIBRARY` WRITE;
/*!40000 ALTER TABLE `LIB_LIBRARY` DISABLE KEYS */;
INSERT INTO `LIB_LIBRARY` VALUES ('420e721f804699a43f1ba8d9f264369b','Central','Biblioteca Central','Dirección General de Bibliotecas','Biblioteca Central','BC','http://informatica.dgbiblio.unam.mx:8991/','Edif. de Biblioteca Central, Circuito Escolar, Ciudad Universitaria, delegación Coyoacán C.P. 04510 México D.F.','56221658',1,0,0,'2017-06-10 14:39:45','2017-06-10 14:39:45'),('97af4cc61899e3c6ddefe0791ed6c49d','Aragon','Jesús Reyes Heroles','Facultad de Estudios Superiores Aragón','FES Aragón','ARA','http://biblioteca-fes.aragon.unam.mx:8991/F/','Av. Rancho Seco S/N, colonia Impulsora , municipio Nezahualcóyotl C.P. 57130 Estado de México','56231069',1,0,0,'2017-06-09 20:28:28','2017-06-09 20:28:28');
/*!40000 ALTER TABLE `LIB_LIBRARY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_LIBRARY_PARAMETERS`
--

DROP TABLE IF EXISTS `LIB_LIBRARY_PARAMETERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_LIBRARY_PARAMETERS` (
  `LIBRARY_ID` varchar(32) NOT NULL,
  `FIELD` varchar(64) NOT NULL,
  `VALUE` longblob,
  PRIMARY KEY (`LIBRARY_ID`,`FIELD`),
  KEY `LIB_LIBRARY_PARAMETERS_FIELD_index` (`FIELD`),
  KEY `LIB_LIBRARY_PARAMETERS_LIBRARY_ID_index` (`LIBRARY_ID`),
  CONSTRAINT `LIB_LIBRARY_PARAMETERS_LIB_LIBRARY_ID_fk` FOREIGN KEY (`LIBRARY_ID`) REFERENCES `LIB_LIBRARY` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_LIBRARY_PARAMETERS`
--

LOCK TABLES `LIB_LIBRARY_PARAMETERS` WRITE;
/*!40000 ALTER TABLE `LIB_LIBRARY_PARAMETERS` DISABLE KEYS */;
INSERT INTO `LIB_LIBRARY_PARAMETERS` VALUES ('97af4cc61899e3c6ddefe0791ed6c49d','books','l0801'),('97af4cc61899e3c6ddefe0791ed6c49d','magazine','p0801'),('97af4cc61899e3c6ddefe0791ed6c49d','thesis','t0801');
/*!40000 ALTER TABLE `LIB_LIBRARY_PARAMETERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_NOTIFICATIONS`
--

DROP TABLE IF EXISTS `LIB_NOTIFICATIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_NOTIFICATIONS` (
  `ID` varchar(32) NOT NULL,
  `DEVICE_ID` varchar(32) NOT NULL,
  `MESSAGE` longblob NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `LAST_NOTIFICATION_TIME` datetime DEFAULT NULL,
  `NEXT_NOTIFICATION_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `LIB_NOTIFICATIONS_LAST_NOTIFICATION_TIME_index` (`LAST_NOTIFICATION_TIME`),
  KEY `LIB_NOTIFICATIONS_NEXT_NOTIFICATION_TIME_index` (`NEXT_NOTIFICATION_TIME`),
  KEY `adm_devices_lib_notifications_fk` (`DEVICE_ID`),
  CONSTRAINT `adm_devices_lib_notifications_fk` FOREIGN KEY (`DEVICE_ID`) REFERENCES `ADM_DEVICES` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_NOTIFICATIONS`
--

LOCK TABLES `LIB_NOTIFICATIONS` WRITE;
/*!40000 ALTER TABLE `LIB_NOTIFICATIONS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LIB_NOTIFICATIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_NOTIFICATIONS_PARAMETERS`
--

DROP TABLE IF EXISTS `LIB_NOTIFICATIONS_PARAMETERS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_NOTIFICATIONS_PARAMETERS` (
  `NOTIFICATION_ID` varchar(32) NOT NULL,
  `FIELD` varchar(64) NOT NULL,
  `VALUE` longblob,
  PRIMARY KEY (`NOTIFICATION_ID`,`FIELD`),
  KEY `LIB_NOTIFICATIONS_PARAMETERS_ID_index` (`NOTIFICATION_ID`),
  KEY `LIB_NOTIFICATIONS_PARAMETERS_FIELD_index` (`FIELD`),
  CONSTRAINT `LIB_NOTIFICATIONS_PARAMETERS_LIB_NOTIFICATIONS_ID_fk` FOREIGN KEY (`NOTIFICATION_ID`) REFERENCES `LIB_NOTIFICATIONS` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_NOTIFICATIONS_PARAMETERS`
--

LOCK TABLES `LIB_NOTIFICATIONS_PARAMETERS` WRITE;
/*!40000 ALTER TABLE `LIB_NOTIFICATIONS_PARAMETERS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LIB_NOTIFICATIONS_PARAMETERS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_PROFESSIONS`
--

DROP TABLE IF EXISTS `LIB_PROFESSIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_PROFESSIONS` (
  `ID` varchar(32) NOT NULL,
  `SCHOOL_ID` varchar(32) NOT NULL,
  `PROFESSION` varchar(64) NOT NULL,
  `ACTIVE` tinyint(4) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `lib_school_lib_professions_fk` (`SCHOOL_ID`),
  CONSTRAINT `lib_school_lib_professions_fk` FOREIGN KEY (`SCHOOL_ID`) REFERENCES `LIB_SCHOOLS` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_PROFESSIONS`
--

LOCK TABLES `LIB_PROFESSIONS` WRITE;
/*!40000 ALTER TABLE `LIB_PROFESSIONS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LIB_PROFESSIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_SCHOOLS`
--

DROP TABLE IF EXISTS `LIB_SCHOOLS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_SCHOOLS` (
  `ID` varchar(32) NOT NULL,
  `NAME` varchar(64) NOT NULL,
  `ADDRESS` varchar(128) DEFAULT NULL,
  `WEBSITE` varchar(128) DEFAULT NULL,
  `MAIL` varchar(128) DEFAULT NULL,
  `TELEPHONE` varchar(16) DEFAULT NULL,
  `ACTIVE` tinyint(1) NOT NULL,
  `TYPE` int(11) NOT NULL,
  `STATUS` int(11) NOT NULL,
  `LATITUDE` double DEFAULT NULL,
  `LONGITUDE` double DEFAULT NULL,
  `CREATION_TIME` datetime NOT NULL,
  `UPDATE_TIME` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_SCHOOLS`
--

LOCK TABLES `LIB_SCHOOLS` WRITE;
/*!40000 ALTER TABLE `LIB_SCHOOLS` DISABLE KEYS */;
INSERT INTO `LIB_SCHOOLS` VALUES ('2398aa6a722d171da04ca3806e6b2d4d','FES Aragón',NULL,NULL,NULL,NULL,1,1,1,NULL,NULL,'2017-06-11 00:38:26','2017-06-11 00:38:26'),('b50339a10e1de285ac99d4c3990b8693','None',NULL,NULL,NULL,NULL,1,0,1,NULL,NULL,'2017-07-13 01:44:06','2017-07-13 01:44:10');
/*!40000 ALTER TABLE `LIB_SCHOOLS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIB_USERS_PROFESSIONS`
--

DROP TABLE IF EXISTS `LIB_USERS_PROFESSIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIB_USERS_PROFESSIONS` (
  `USER_ID` varchar(32) NOT NULL,
  `PROFESSION_ID` varchar(32) DEFAULT NULL,
  KEY `LIB_USERS_PROFESSIONS_LIB_PROFESSIONS_ID_fk` (`PROFESSION_ID`),
  KEY `LIB_USERS_PROFESSIONS_ADM_USERS_ID_fk` (`USER_ID`),
  CONSTRAINT `LIB_USERS_PROFESSIONS_ADM_USERS_ID_fk` FOREIGN KEY (`USER_ID`) REFERENCES `ADM_USERS` (`ID`),
  CONSTRAINT `LIB_USERS_PROFESSIONS_LIB_PROFESSIONS_ID_fk` FOREIGN KEY (`PROFESSION_ID`) REFERENCES `LIB_PROFESSIONS` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIB_USERS_PROFESSIONS`
--

LOCK TABLES `LIB_USERS_PROFESSIONS` WRITE;
/*!40000 ALTER TABLE `LIB_USERS_PROFESSIONS` DISABLE KEYS */;
/*!40000 ALTER TABLE `LIB_USERS_PROFESSIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEC_PERMISSIONS`
--

DROP TABLE IF EXISTS `SEC_PERMISSIONS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEC_PERMISSIONS` (
  `ROLE_ID` varchar(32) NOT NULL,
  `URI_ID` varchar(32) NOT NULL,
  `VERB_ID` varchar(32) NOT NULL,
  PRIMARY KEY (`ROLE_ID`,`URI_ID`,`VERB_ID`),
  UNIQUE KEY `sec_permissions_pk` (`ROLE_ID`,`URI_ID`,`VERB_ID`),
  KEY `sec_uris_sec_permissions_fk` (`URI_ID`),
  KEY `sec_verbs_sec_permissions_fk` (`VERB_ID`),
  CONSTRAINT `sec_roles_sec_permissions_fk` FOREIGN KEY (`ROLE_ID`) REFERENCES `SEC_ROLES` (`ID`),
  CONSTRAINT `sec_uris_sec_permissions_fk` FOREIGN KEY (`URI_ID`) REFERENCES `SEC_URIS` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `sec_verbs_sec_permissions_fk` FOREIGN KEY (`VERB_ID`) REFERENCES `SEC_VERBS` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEC_PERMISSIONS`
--

LOCK TABLES `SEC_PERMISSIONS` WRITE;
/*!40000 ALTER TABLE `SEC_PERMISSIONS` DISABLE KEYS */;
INSERT INTO `SEC_PERMISSIONS` VALUES ('2e40ad879e955201df4dedbf8d479a12','06bdcf95aafda840b1d04322636de293','a02439ec229d8be0e74b0c1602392310');
/*!40000 ALTER TABLE `SEC_PERMISSIONS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEC_ROLES`
--

DROP TABLE IF EXISTS `SEC_ROLES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEC_ROLES` (
  `ID` varchar(32) NOT NULL,
  `ROLE` varchar(32) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEC_ROLES`
--

LOCK TABLES `SEC_ROLES` WRITE;
/*!40000 ALTER TABLE `SEC_ROLES` DISABLE KEYS */;
INSERT INTO `SEC_ROLES` VALUES ('033bd94b1168d7e4f0d644c3c95e35bf','TEST'),('2e40ad879e955201df4dedbf8d479a12','USER'),('73acd9a5972130b75066c82595a1fae3','ADMIN'),('ff3e179b3cc64393841107ccba0d6e48','MONITOR');
/*!40000 ALTER TABLE `SEC_ROLES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEC_URIS`
--

DROP TABLE IF EXISTS `SEC_URIS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEC_URIS` (
  `ID` varchar(32) NOT NULL,
  `URI` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEC_URIS`
--

LOCK TABLES `SEC_URIS` WRITE;
/*!40000 ALTER TABLE `SEC_URIS` DISABLE KEYS */;
INSERT INTO `SEC_URIS` VALUES ('06bdcf95aafda840b1d04322636de293','/users');
/*!40000 ALTER TABLE `SEC_URIS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEC_USERS_ROLES`
--

DROP TABLE IF EXISTS `SEC_USERS_ROLES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEC_USERS_ROLES` (
  `USER_ID` varchar(32) NOT NULL,
  `ROLE_ID` varchar(32) NOT NULL,
  PRIMARY KEY (`USER_ID`,`ROLE_ID`),
  UNIQUE KEY `sec_users_roles_pk` (`USER_ID`,`ROLE_ID`),
  KEY `sec_roles_sec_users_roles_fk` (`ROLE_ID`),
  CONSTRAINT `adm_users_sec_users_roles_fk` FOREIGN KEY (`USER_ID`) REFERENCES `ADM_USERS` (`ID`),
  CONSTRAINT `sec_roles_sec_users_roles_fk` FOREIGN KEY (`ROLE_ID`) REFERENCES `SEC_ROLES` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEC_USERS_ROLES`
--

LOCK TABLES `SEC_USERS_ROLES` WRITE;
/*!40000 ALTER TABLE `SEC_USERS_ROLES` DISABLE KEYS */;
/*!40000 ALTER TABLE `SEC_USERS_ROLES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SEC_VERBS`
--

DROP TABLE IF EXISTS `SEC_VERBS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SEC_VERBS` (
  `ID` varchar(32) NOT NULL,
  `VERB` varchar(32) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SEC_VERBS`
--

LOCK TABLES `SEC_VERBS` WRITE;
/*!40000 ALTER TABLE `SEC_VERBS` DISABLE KEYS */;
INSERT INTO `SEC_VERBS` VALUES ('164dd62adb30ca051b5289672a572f9b','OPTIONS'),('32f68a60cef40faedbc6af20298c1a1e','DELETE'),('3e75383a5992a6d15fb81e872e46e256','PUT'),('63bc9a3997d66d835d9f3ec29451407d','PATCH'),('7528035a93ee69cedb1dbddb2f0bfcc8','GET'),('a02439ec229d8be0e74b0c1602392310','POST'),('e15e216fc1c639f787b1231ecdfa1bf8','HEAD');
/*!40000 ALTER TABLE `SEC_VERBS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-14  3:59:32
