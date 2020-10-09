#########################################################################################
################################ Password Check Function ################################
#########################################################################################
def user_passcheck ():
	flag=0
	i=0	
	while i<=2 and flag==0:
		if i==0:
			password=input("Please enter your password : ")	
			if password=='1234':
					flag=1
					break					
			else:
				password=input("Please try again : ")
				
		elif password!="1234" and i!=2 :
			password=input("Please try again : ")
			
		elif password=='1234':
			flag=1
			break	
		i=i+1
		
	if flag==0 :
		print("Your password is incorrect for three times please try again later ")
	if flag==1 :
		print("                                          ##* Welcome Admin *## ")
#########################################################################################
############################### Patients Functions ######################################	
#########################################################################################

def add_patient(patients,id):
	name=input("Please enter the patient's Name : ")
	dep=input("Please enter the patient's Department : ")
	room=input("Please enter the patient's Room : ")
	doctor=input("Please enter the name of the doctor following the patient's case :")	
	condition=input("Please enter the patient's Condition : ")
	age=input("Please enter the patient's Age : ")
	gender=input("Please enter the patient's Gender : ")
	address=input("Please enter the patient's address : ")
	phone=input("Please enter the patient's Phone Number : ")

	patients[id]={'Name':name,'Department':dep,'Room':room,'Doctor':doctor,'Condition':condition,'Age':age,'Gender':gender,'Address':address,'Phone':phone,'ID':id}
	
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


def delete_patient(patients,id):
	patients.pop(id)	
	print("^_^_^_^_^_^ The Patient is Successfully Deleted ^_^_^_^_^_^")
	
def edit_patient(patients,id):
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	op=input('''To Edit the Patient's Name Press 1
To Edit the Patient's Department Press 2
To Edit the Patient's Room Press 3
To Edit the Patient's Doctor Press 4
To Edit the Patient's Condition Press 5
To Edit the Patient's Age Press 6
To Edit the Patient's Gender Press 7
To Edit the Patient's Address Press 8
To Edit the Patient's Phone Number Press 9     your Choice : ''')
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	if op=='1':
		name=input("Please enter the patient's Name : ")
		patients[id]['Name']=name
		display_patient(patients,id)
	elif op=='2':
		dep=input("Please enter the patient's Department : ")
		patients[id]['Department']=dep
		display_patient(patients,id)
	elif op=='3':
		room=input("Please enter the patient's Room : ")
		patients[id]['Room']=room
		display_patient(patients,id)
	elif op=='4':
		doctor=input("Please enter the name of the doctor following the patient's case :")
		patients[id]['Doctor']=doctor
		display_patient(patients,id)
	elif op=='5':
		condition=input("Please enter the patient's Condition : ")
		patients[id]['Condition']=condition
		display_patient(patients,id)
	elif op=='6':
		age=input("Please enter the patient's Age : ")
		patients[id]['Age']=age
		display_patient(patients,id)
	elif op=='7':
		gender=input("Please enter the patient's Gender : ")
		patients[id]['Gender']=gender
		display_patient(patients,id)
	elif op=='8':
		address=input("Please enter the patient's address : ")
		patients[id]['Address']=address
		display_patient(patients,id)
	elif op=='9':
		phone=input("Please enter the patient's Phone Number : ")
		patients[id]['Phone']=phone
		display_patient(patients,id)		
	else :
		print("**** Wrong Choice **** ")
		
def display_patient(patients,id):	
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	print("The patient of ID {} has the following data :".format(id))
	print("------------------------------------------------------")
	print("Name: {}".format(patients[id]['Name']))
	print("Department: {}".format(patients[id]['Department']))
	print("Room: {}".format(patients[id]['Room']))
	print("Doctor: {}".format(patients[id]['Doctor']))
	print("Condition: {}".format(patients[id]['Condition']))
	print("Age: {}".format(patients[id]['Age']))
	print("Gender: {}".format(patients[id]['Gender']))
	print("Address: {}".format(patients[id]['Address']))
	print("Phone Number: {}".format(patients[id]['Phone']))
	
def display_allpatients(patients):

	for i in patients :
		print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		print("Name: {}".format(patients[i]['Name']))
		print("ID: {}".format(patients[i]['Name']))
		print("Department: {}".format(patients[i]['Department']))
		print("Room: {}".format(patients[i]['Room']))
		print("Doctor: {}".format(patients[i]['Doctor']))
		print("Condition: {}".format(patients[i]['Condition']))
		print("Age: {}".format(patients[i]['Age']))
		print("Gender: {}".format(patients[i]['Gender']))
		print("Address: {}".format(patients[i]['Address']))
		print("Phone Number: {}".format(patients[i]['Phone']))	

#####################################################################################################	
##################################### Doctors functions #############################################
#####################################################################################################

def add_doctor(doctors,id):	
	name=input("Please enter the Doctor's Name : ")
	dep=input("Please enter the Doctor's Department : ")
	address=input("Please enter the Doctor's address : ")
	phone=input("Please enter the Doctor's Phone Number : ")
	
	doctors[id]={'Name':name,'Department':dep,'Address':address,'Phone':phone,'ID':id,'Slots':'Not Available'}
	
	print("^_^_^_^_^_^ The Doctor is Successfully Added ^_^_^_^_^_^")	
def delete_doctor(doctors,id):
	doctors.pop(id)	
	print("^_^_^_^_^_^ The Doctor is Successfully Deleted ^_^_^_^_^_^")
	
def edit_doctor(doctors,id):	
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	op=input('''To Edit the Doctor's Name Press 1
To Edit the Doctor's Department Press 2
To Edit the Doctor's Address Press 3
To Edit the Doctor's Phone Number Press 4     your Choice : ''')
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	if op=='1':
		name=input("Please enter the Doctor's Name : ")
		doctors[id]['Name']=name
		display_doctor(doctors,id)
	elif op=='2':
		dep=input("Please enter the Doctor's Department : ")
		doctors[id]['Department']=dep
		display_doctor(doctors,id)
	elif op=='3':
		address=input("Please enter the Docotr's Address : ")
		doctors[id]['Address']=address
		display_doctor(doctors,id)
	elif op=='4':
		phone=input("Please enter the Doctor's Phone : ")
		patients[id]['Phone']=phone
		display_doctor(doctors,id)
	else :
		print("**** Wrong Choice **** ")

def display_doctor(doctors,id):		
		
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	print("The Doctor of ID {} has the following data :".format(id))
	print("------------------------------------------------------")	
	print("Name: {}".format(doctors[id]['Name']))
	print("Department: {}".format(doctors[id]['Department']))	
	print("Address: {}".format(doctors[id]['Address']))
	print("Phone Number: {}".format(doctors[id]['Phone']))	
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
def display_alldoctors(doctors):
	for i in doctors :
		print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		print("Name: {}".format(doctors[i]['Name']))
		print("Department: {}".format(doctors[i]['Department']))	
		print("Address: {}".format(doctors[i]['Address']))
		print("Phone Number: {}".format(doctors[i]['Phone']))
		print("ID: {}".format(doctors[i]['ID']))
#####################################################################################################	
################################# Booking appointments functions ####################################
#####################################################################################################		
def book_appointment(booked_appointments,available_appointments,department,doctor,id):
	print("                     ")
	print("The Slots available for doctor {} is :".format(doctor))
	print("'-'-'-'-'-'-'-'-'-'-'-''-'-'-'-'-'-'-'-'-'-'-'-'-'-'")
						
	for i in range(len(available_appointments[department][doctor])) :
		print(available_appointments[department][doctor][i])
								
	slot=input("Please enter the number of the slot you want to reserve            your Choice : ")
	while slot>str(len(available_appointments[department][doctor])) or slot<='0' :
		slot=input("The Slot you entered isn't available Please enter the number of the slot you want to reserve            your Choice : ")
					
	name=input("Please enter the patient's Name : ")
	gender=input("Please enter the patient's Gender : ")
	age=input("Please enter the patient's Age : ")
	newslot=int(slot)-1
	booked_appointments[id]={'Patient Name':name ,'Department':department ,'Doctor Name':doctor ,'Slot': available_appointments[department][doctor].pop(newslot) ,'Age':age ,'ID':id }
	print ("~~~~~~~~~~ The Reservation is Successfully Done ~~~~~~~~~~")
			
	print('ID : {}'.format(booked_appointments[id]['ID']))
	print("Patient's Name : {}".format(booked_appointments[id]['Patient Name']))
	print("Doctor's Name : {}".format(booked_appointments[id]['Doctor Name']))
	print("Department : {}".format(booked_appointments[id]['Department']))
	print("Slot : {}".format(booked_appointments[id]['Slot']))
	print("Age : {}".format(booked_appointments[id]['Age']))
			
	
def Edit_appointment (booked_appointments,available_appointments,id)	:

	doctorname=booked_appointments[id]['Doctor Name']
	department=booked_appointments[id]['Department']
	slot=booked_appointments[id]['Slot']
	available_appointments[department][doctorname].append(slot)
	available_appointments[department][doctorname].sort()
	
				
	view_appointments(available_appointments)	
		
		
	department=input('''For Cardiology Department Press 1
For Neurology Department press 2
For Orthopedics Department press 3
For Opthalmology Department press 4
For Radiology Department Press 5        your choice : ''')	
	if department =='1':
		department='Cardiology'
		print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		doc=input('''To Select Doctor Ismail Mohamed Slots Press 1 
To Select Doctor Osama Ahmed Slots Press 2           your Choice :  ''')
		if doc=='1':
				doctor='Ismail Mohamed'
		elif doc=='2':
			doctor='Osama Ahmed'
								
		else :
			print(" **** Wrong Choice **** ")
									
							
	elif department =='2':
		department='Neurology'
		doctor='Hossam Noureldin'
								
	elif department =='3':
		department='Orthopedics'
		print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		doc=input('''To Select Doctor Ahmed Abdelaziz Slots Press 1 
To Select Doctor Wael Mounir Slots Press 2           your Choice :  ''')
		if doc=='1':
			doctor='Ahmed Abdelaziz'
		elif doc=='2':
			doctor='Wael Mounir'
								
		else :
			print(" **** Wrong Choice **** ")							
							
	elif department =='4':
		department='Opthalmology'
		print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		doc=input('''To Select Doctor Sherif Reda Slots Press 1 
To Select Doctor Alaa Badr Slots Press 2           your Choice :  ''')		
		if doc=='1':
			doctor='Sherif Reda'
		elif doc=='2':
			doctor='Alaa Badr'
								
		else :
			print(" **** Wrong Choice **** ")		
						
	elif department =='5':
		department='Radiology'
		print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
		doc=input('''To Select X-ray Slots Press 1 
To Select MRI Slots Press 2           your Choice :  ''')		
		if doc=='1':
			doctor='X-ray'
		elif doc=='2':
			doctor='MRI'
								
		else :
			print(" **** Wrong Choice **** ")	
		
		
	else :
		print(" **** Wrong Choice **** ")		
	
	print("                     ")
	print("The Slots available for doctor {} is :".format(doctor))
	print("'-'-'-'-'-'-'-'-'-'-'-''-'-'-'-'-'-'-'-'-'-'-'-'-'-'")					
	for i in range(len(available_appointments[department][doctor])) :
		print(available_appointments[department][doctor][i])
								
	slot=input("Please enter the number of the slot you want to reserve            your Choice : ")
	while slot>str(len(available_appointments[department][doctor])) or slot<='0' :
		slot=input("The Slot you entered isn't available Please enter the number of the slot you want to reserve            your Choice : ")
					
	name=input("Please enter the patient's Name : ")
	gender=input("Please enter the patient's Gender : ")
	age=input("Please enter the patient's Age : ")
	newslot=int(slot)-1
	booked_appointments[id]={'Patient Name':name ,'Department':department ,'Doctor Name':doctor ,'Slot': available_appointments[department][doctor].pop(newslot) ,'Age':age ,'ID':id }
	print ("~~~~~~~~~~ The Reservation is Successfully Done ~~~~~~~~~~")
			
	print('ID : {}'.format(booked_appointments[id]['ID']))
	print("Patient's Name : {}".format(booked_appointments[id]['Patient Name']))
	print("Doctor's Name : {}".format(booked_appointments[id]['Doctor Name']))
	print("Department : {}".format(booked_appointments[id]['Department']))
	print("Slot : {}".format(booked_appointments[id]['Slot']))
	print("Age : {}".format(booked_appointments[id]['Age']))
	
def cancel_appointment(booked_appointments,available_appointments,id):
	doctorname=booked_appointments[id]['Doctor Name']
	department=booked_appointments[id]['Department']
	slot=booked_appointments[id]['Slot']
	available_appointments[department][doctorname].append(slot)
	available_appointments[department][doctorname].sort()
	booked_appointments.pop(id)
	print("*~*~*~*~*~*~*~*~*~*~*~*The Reservation is Successfully Canceled*~*~*~*~*~*~*~*~*~*~*~*")


# def view_availableappointments(available_appointments)	:	
		
		
		
		
# def view_Bookedappointments(available_appointments)	:	
		
def view_appointments(available_appointments):	
	departments=list(available_appointments.keys())
				
	for i in range(len(departments)):
		print(departments[i]+' :')
		print('----------------')
	
		doctors=list(available_appointments[departments[i]].keys())
		for j in range(len(doctors)):
			print('**'+doctors[j])
		
			for k in range(len(available_appointments[departments[i]][doctors[j]])) :
				print(available_appointments[departments[i]][doctors[j]][k])
			
		print("##########################################")
		
def view_departments(available_appointments):
		departments=list(available_appointments.keys())
				
		for i in range(len(departments)):
			print(departments[i]+' :')
			print('----------------')
	
			doctors=list(available_appointments[departments[i]].keys())
			for j in range(len(doctors)):
				print(doctors[j])	
		
			print("      ")
		
def display_doctorappointment(doctors,id):
	print("The doctor choose is DR.{}:".format(doctors[id]['Name']))
	print('-----------------------------------------')
	print(doctors[id]['Slots'])	
		
#####################################################################################################	
############################################ Data Base ##############################################
#####################################################################################################		
def store_data(doctors,patients):
	import csv
#####################Store data of the doctors ####################
	
	fields=['Name','Department','Address','Phone','ID','Slots']
	with open('data_doctors.csv','w') as csvfile:
		csvwriter=csv.DictWriter(csvfile, fieldnames=fields)
		csvwriter.writeheader()
		for i in doctors :
	
			csvwriter.writerow({'Name':doctors[i]['Name'],'Department':doctors[i]['Department'],'Address':doctors[i]['Address'],'Phone':doctors[i]['Phone'],'ID':doctors[i]['ID'],'Slots':doctors[i]['Slots']})
 
 #####################Store data of the Patients#################### 
	fields=['Name','Department','Room','Doctor','Condition','Age','Gender','Address','Phone','ID']
	with open('data_patients.csv','w') as csvfile:
		csvwriter=csv.DictWriter(csvfile, fieldnames=fields)
		csvwriter.writeheader()
		for i in patients :
	
			csvwriter.writerow({'Name':patients[i]['Name'],'Department':patients[i]['Department'],'Room':patients[i]['Room'],'Doctor':patients[i]['Doctor'],'Condition':patients[i]['Condition'],'Age':patients[i]['Age'],'Address':patients[i]['Address'],'Phone':patients[i]['Phone'],'ID':patients[i]['ID']})				
	

def retrieve_data(doctors,patients)	:	
	import csv
#####################Retrieve data of the doctors ####################
	rows=[]
	with open('data_doctors.csv','r') as csvfile:
		csvreader=csv.DictReader(csvfile)
		for row in csvreader :
			ID=row['ID']
			doctors[ID]=dict(row)	
		
 #####################Retrieve data of the Patients#################### 		
	rows=[]
	with open('data_patients.csv','r') as csvfile:
		csvreader=csv.DictReader(csvfile)
		for row in csvreader :
			ID=row['ID']
			patients[ID]=dict(row)		
		
		
		
		