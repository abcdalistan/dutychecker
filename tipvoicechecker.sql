DROP SCHEMA IF EXISTS `staffer` ;

CREATE SCHEMA IF NOT EXISTS `staffer` DEFAULT CHARACTER SET utf8 ;
USE `staffer`;

DROP TABLE IF EXISTS `staffer`.`stafferinfo` ;
CREATE TABLE IF NOT EXISTS `staffer`.`stafferinfo` (
  `student_number` varchar(50) NOT NULL ,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `program` VARCHAR(45) NOT NULL,
  `position` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`student_number`))
ENGINE = InnoDB;

DROP TABLE IF EXISTS `staffer`.`schedules` ;
CREATE TABLE IF NOT EXISTS `staffer`.`schedules` (
  `student_number` varchar(45) NOT NULL ,
  `start_time` time not NULL,
  `end_time` time not NULL,
  `day` varchar(45) not NULL,
  `semester` varchar(45) not NULL,
  `academic_year` varchar(45) not NULL,
  foreign key (`student_number`) references `stafferinfo`(`student_number`)
  )
ENGINE = InnoDB;

DROP TABLE IF EXISTS `staffer`.`fine` ;
CREATE TABLE IF NOT EXISTS `staffer`.`fine` (
  `fine_ID` int ,
  `no_of_duty` int null ,
  `total_fine` decimal NULL,
  primary key (`fine_ID`))
ENGINE = InnoDB;

DROP TABLE IF EXISTS `staffer`.`loginstaff` ;
CREATE TABLE IF NOT EXISTS `staffer`.`loginstaff` (
  `student_number` varchar(50) NOT NULL ,
  `login_time` time NULL,
  `logout_time` time NULL,
  `status` varchar(45) NULL,
  `date` date NULL,
  `fine_ID` int NULL, 
  foreign key (`student_number`) references `stafferinfo`(`student_number`),
  foreign key (`fine_ID`) references `fine`(`fine_ID`)
  )
ENGINE = InnoDB;

DROP TABLE IF EXISTS `staffer`.`adminlogin` ;
CREATE TABLE IF NOT EXISTS `staffer`.`adminlogin` (
  `username` varchar(45) not null,
  `password` varchar(45) not null
  )
ENGINE = InnoDB;

