import sqlite3
connection=sqlite3.connect("hospital.db")
cursor=connection.cursor()
a=["PATIENT_ID",'PATIENT_NAME','DETAILS:','PHONE','PROBLEM','PRESCRIPTION','DOCTOR NAME','TREATMENT','BILL','ADMISSION','DISCHARGE']
def printing_down():
		print("~"*60,end="\n")
def clear():
	for _ in range(65):
		print()
def low_clear():
	for _ in range(5):
		print()
def choose():
	choice=int(input("ENTER YOUR CHOICE.....S.NO:"))
	if (choice==0):
		clear()	
		inputs()
	elif (choice==1):
		clear()
		disp()
	elif (choice==2):
		clear()
		dispall()
	else:
		print("CHECK YOUR INPUT")
		choose()
def dispall():
	cursor.execute("select *from patient")
	data=cursor.fetchall()
	print("  ALL PATIENT RECORDS  ".center(60,"="))
	for i in range(len(data)):
		s=data[i]
		low_clear()
		for j in range(11):
				if(j<1):
					printing_down()
				print("|",a[j].center(20," "),"|",s[j],end='\n')
				printing_down()
	connection.commit()
	connection.close()
def disp():
	print("SEARCH RECORDS".center(60,"="))
	ide=int(input("ENTER THE PATIENT ID:"))
	info=("""select *from patient where(patient_id={id});""")
	command=info.format(id=ide)
	cursor.execute(command)
	result=cursor.fetchone()
	clear()
	printing_down()
	print("  PATIENT REPORT  ".center(60,"="))
	print("~"*60)
	for f in range(11):
		print("|",a[f].center(20," "),"|",result[f],end='\n')
		printing_down()
def inputs():
	printing_down()
	print("  ENTER THE DETAILS ".center(60,"="))
	printing_down()
	id=int(input("ENTER THE PATIENT ID:"))
	name=input("ENTER THE NAME:")
	phone=int(input("ENTER THE PHONE NUMBER:"))
	problem=input("ENTER THE PATIENT PROBLEM:")
	details=input("ENTER THE PATIENT DETAILS:")
	medicine=input("PATIENT PRESCRIPTION:")
	doc=input("ENTER THE DOCTOR NAME:")
	treat=input("ENTER THE TREATEMENT_NAME:")
	bill=int(input("ENTER THE BILL AMOUNT PAID:"))
	admit=input("ADMISSION DATE:")
	discharge=input("DISCHARGE DATE:")
	a=[(id,name,details,phone,problem,medicine,doc,treat,bill,admit,discharge)]
	connection=sqlite3.connect("hospital.db")
	cursor=connection.cursor()
	for p in a:
		my_command="""INSERT INTO patient values("{id}","{name}","{details}","{phone}","{problem}","{medicine}","{doc}","{treat}","{bill}","{admit}","{discharge}")"""
		sqlcom=my_command.format(id=p[0],name=p[1],details=p[2],phone=p[3],problem=p[4],medicine=p[5],doc=p[6],treat=p[7],bill=p[8],admit=p[9],discharge=p[10])
		cursor.execute(sqlcom)
	connection.commit()
	connection.close()
def intro():
	clear()
	printing_down()
	print("   VELLORE CMC   ".center(60,"="))
	print("   RECORDS MANAGEMENT   ".center(60,"="))
	printing_down()
	a=["UPDATE THE PATIENT RECORD","SEARCH THE PATIENT RECORDS","SEE ALL PATIENT RECORD"]
	print("|"," "*4,"S.NO"," "*3,"|","ACTIONS".center(40," "),"|")
	printing_down()
	for i in range(3):
		print("|"," "*5,i," "*5,"|",a[i].center(40),"|")
		printing_down()
intro()
choose()