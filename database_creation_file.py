import sqlite3
connection=sqlite3.connect("hospital.db")
cursor=connection.cursor()
sql_command="""
create table patient(patient_id int primary key not null,patient_name char(50) not null,patient_details varchar(500) not null,patient_phone int ,patient_problem char(50) not null,prescription varchar(200),name_of_doctor char(50),treatement_given varchar(200) not null,bill_amount int not null,admitted_date date,discharge_date  date)"""
cursor.execute(sql_command)
connection.commit()