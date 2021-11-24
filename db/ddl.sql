DROP database pes_interconnect2;
CREATE database pes_interconnect2;

\c pes_interconnect2

CREATE TABLE Club
(
  Club_ID INT NOT NULL,
  Name VARCHAR(25) NOT NULL,
  PRIMARY KEY (Club_ID)
);


CREATE TABLE Staff
(
  Employee_ID INT NOT NULL,
  Email_ID VARCHAR(35) NOT NULL,
  Name VARCHAR(20) NOT NULL,
  Type VARCHAR(25) NOT NULL,
  PRIMARY KEY (Employee_ID)
);


CREATE TABLE Section
(
  Room_no INT NOT NULL,
  Floor INT NOT NULL,
  Name VARCHAR(1) NOT NULL,
  PRIMARY KEY (Name)
);

CREATE TABLE Teacher
(
  Employee_ID INT NOT NULL,
  Email_ID VARCHAR(35) NOT NULL,
  Name VARCHAR(20) NOT NULL,
  Phone_No BIGINT NOT NULL,
  Address VARCHAR(50) NOT NULL,
  Club_ID INT,
  PRIMARY KEY (Employee_ID),
  FOREIGN KEY (Club_ID) REFERENCES Club(Club_ID)
);


CREATE TABLE Course
(
  Course_code INT NOT NULL,
  Name VARCHAR(50) NOT NULL,
  Credits INT NOT NULL,
  Type VARCHAR(10) NOT NULL,
  Employee_ID INT NOT NULL,
  PRIMARY KEY (Course_code),
  FOREIGN KEY (Employee_ID) REFERENCES Teacher(Employee_ID)
);


CREATE TABLE Department
(
  Name VARCHAR(50) NOT NULL,
  Email_ID VARCHAR(35) NOT NULL,
  Dept_ID INT NOT NULL,
  Phone_No BIGINT NOT NULL,
  Floors VARCHAR(5) NOT NULL,
  Employee_ID INT NOT NULL,
  PRIMARY KEY (Dept_ID),
  FOREIGN KEY (Employee_ID) REFERENCES Teacher(Employee_ID)
);


CREATE TABLE Student
(
  Name VARCHAR(20) NOT NULL,
  SRN INT NOT NULL,
  Address VARCHAR(50) NOT NULL,
  Phone_NO BIGINT NOT NULL,
  CGPA FLOAT NOT NULL,
  Email_ID VARCHAR(35) NOT NULL,
  Section VarChar(1) NOT NULL,
  Dept_ID INT NOT NULL,
  Mentor_ID INT NOT NULL,
  PRIMARY KEY (SRN), 
  FOREIGN KEY (Section) REFERENCES Section(Name),
  FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID),
  FOREIGN KEY (Mentor_ID) REFERENCES Teacher(Employee_ID)
);



CREATE TABLE consists
(
  Club_ID INT NOT NULL,
  SRN INT NOT NULL,
  PRIMARY KEY (Club_ID, SRN),
  FOREIGN KEY (Club_ID) REFERENCES Club(Club_ID),
  FOREIGN KEY (SRN) REFERENCES Student(SRN)
);


CREATE TABLE teaches
(
  Employee_ID INT NOT NULL,
  Course_code INT NOT NULL,
  Dept_ID INT NOT NULL,
  PRIMARY KEY (Employee_ID, Course_code),
  FOREIGN KEY (Employee_ID) REFERENCES Teacher(Employee_ID),
  FOREIGN KEY (Course_code) REFERENCES Course(Course_code),
  FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID)
);


CREATE TABLE opts
(
  SRN INT NOT NULL,
  Course_code INT NOT NULL,
  PRIMARY KEY (SRN, Course_code),
  FOREIGN KEY (SRN) REFERENCES Student(SRN),
  FOREIGN KEY (Course_code) REFERENCES Course(Course_code)
);


CREATE TABLE managed_by
(
  Dept_ID INT NOT NULL,
  Employee_ID INT NOT NULL,
  PRIMARY KEY (Dept_ID, Employee_ID),
  FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID),
  FOREIGN KEY (Employee_ID) REFERENCES Staff(Employee_ID)
);


CREATE TABLE offers
(
  Dept_ID INT NOT NULL,
  Course_code INT NOT NULL,
  PRIMARY KEY (Dept_ID, Course_code),
  FOREIGN KEY (Dept_ID) REFERENCES Department(Dept_ID),
  FOREIGN KEY (Course_code) REFERENCES Course(Course_code)
);


CREATE TABLE tutors
(
  Employee_ID INT NOT NULL,
  Name VARCHAR(20) NOT NULL,
  PRIMARY KEY (Employee_ID, Name),
  FOREIGN KEY (Employee_ID) REFERENCES Teacher(Employee_ID),
  FOREIGN KEY (Name) REFERENCES Section(Name)
);
