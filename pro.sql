create database project;
use project;
create table doctor(
     doc_name char(20) NOT NULL,
     qualification char(20) NOT NULL,
     phn_no varchar(10) NOT NULL UNIQUE,
	 age int NOT NULL,
     CHECK (age >= 24),
     regis_no int PRIMARY KEY,
     doc_id int NOT NULL UNIQUE,
     fees int not null
    );
create table patient(
 aadhar_no varchar(12) NOT NULL PRIMARY KEY,
 pat_name char(20) NOT NULL,
 phn_no varchar(10) NOT NULL UNIQUE,
 age int NOT NULL,
 CHECK (age <=100)
 );
 
 create table patient_history(
	weight int,
    height int,
    blood_grp varchar(4),
    CHECK (weight <= 700 and weight > 2),
    CHECK (height >= 40 and height <= 300),
    aadhar_no varchar(12) not null PRIMARY KEY ,
    foreign key(aadhar_no) REFERENCES patient(aadhar_no) ON DELETE cascade
    );
create table patient_diease(
	aadhar_no varchar(12)  ,
    disease varchar(20),
    FOREIGN KEY(aadhar_no) REFERENCES patient_history(aadhar_no) ON DELETE CASCADE
    );
create table appointment(
	app_date date NOT NULL,
    check (app_date > sysdate()),
    doc_id int,
    aadhar_no varchar(12) NOT NULL PRIMARY KEY ,
	pat_name char(20) NOT NULL,
	phn_no varchar(10) NOT NULL UNIQUE,
	age int NOT NULL,
	CHECK (age <=100),
     app_status int not null ,
     check( app_status =0 or app_status=1),
     fees int default null
    );
    
    
create table billing(
aadhar_no varchar(12) NOT NULL ,
doc_id int,
pat_name char(20) NOT NULL,
age int NOT NULL,
FOREIGN KEY(aadhar_no) REFERENCES patient(aadhar_no),
fees int default null
);



create table vaccine (
    aadhar_no varchar(12) NOT NULL PRIMARY KEY  , 
    no_of_dose int ,
    CHECK (no_of_dose <= 3) ,
    name_of_vaccine varchar (20),
    FOREIGN KEY(aadhar_no) REFERENCES patient(aadhar_no)
    );
    
delimiter $$
Create Trigger insert_patient  
AFTER INSERT ON appointment FOR EACH ROW  
BEGIN   
INSERT INTO patient VALUES (new.aadhar_no, new.pat_name,   
new.phn_no, new.age); 
END;
$$
