import mod

patients=dict()
booked_appointments=dict()
doctors={'11':{'Name':'Ismail Mohamed','Department':'Cardiology','ID':'11','Phone':'01002024476','Address':'Street 100','Slots':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1:30 to 2pm']},
         '12':{'Name':'Osama Ahmed','Department':'Cardiology','ID':'12','Phone':'01118897765','Address':'Street 101','Slots':['slot1:From 1 to 1:30pm','slot2:From 2 to 2:30pm']},
		 '13':{'Name':'Hossam Noureldin','Department':'Neurology','ID':'13','Phone':'01155532765','Address':'Street 102','Slots':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm']},
		 '14':{'Name':'Ahmed Abdelaziz','Department':'Orthopedics','ID':'14','Phone':'01254454465','Address':'Street 103','Slots':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm']},
		 '15':{'Name':'Wael Mounir','Department':'Orthopedics','ID':'15','Phone':'01247736225','Address':'Street 104','Slots':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm']},
		 '16':{'Name':'Sherif Reda','Department':'Opthalmology','ID':'16','Phone':'0353525235225','Address':'Street 105','Slots':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm']},
		 '17':{'Name':'Alaa Badr','Department':'Opthalmology','ID':'17','Phone':'01555533335','Address':'Street 106','Slots':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm']},
		 }
available_appointments={
'Cardiology':{'Ismail Mohamed':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1:30 to 2pm'],
              'Osama Ahmed':['slot1:From 1 to 1:30pm','slot2:From 2 to 2:30pm']},

'Neurology':{'Hossam Noureldin':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm']},
'Orthopedics':{'Ahmed Abdelaziz':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm'],
               'Wael Mounir':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm']},
'Opthalmology':{'Sherif Reda':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm'],
				'Alaa Badr':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm']},

'Radiology':{'X-ray':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm','slot7:From 3 to 3:30','slot8:From 3:30 to 4pm'],				
            'MRI':['slot1:From 12 to 12:30','slot2:From 12:30 to 1pm','slot3:From 1 to 1:30pm','slot4:From 1:30 to 2pm','slot5:From 2 to 2:30pm','slot6:From 2:30 to 3pm','slot7:From 3 to 3:30','slot8:From 3:30 to 4pm']}}

departments=['Cardiology','Neurology','Orthopedics','Opthalmology','Radiology']
mod.retrieve_data(doctors,patients)			
while 1:
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	print('For Admin mode please enter 1 ') 
	print("For user mode please enter 2 ") 
	mode=input("To Exit the Program Please enter E      your choice: ")
	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
	if mode=='1':
		mod.user_passcheck()
		while 1:
			print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
			task=input('''To Manage the Data of the Patients Press 1
To Manage the Data of the Doctors Press 2
For Appointments Press 3     
To Return Back to the previous menu Press B      your choice :  ''')
			if task=='1':
				while 1:
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
					op=input('''To ADD Patient Press 1 
To Delete Patient Press 2 
To Edit Patient Data Press 3
To Display Patient's Data Press 4 
To Return Back to the previous menu Press B     your choice :  ''')
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
					if op=='1':
						id=input("Please enter the id : ")
						while id in patients :
							id=input("This Id already Existed please enter another one : ")
					
						mod.add_patient(patients,id)
					elif op=='2':
						id=input("Please enter the id : ")
						if id in patients :
							mod.delete_patient(patients,id)
						else:
							print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")
					elif op=='3':
						id=input("Please enter the id : ")
						if id in patients :
							mod.edit_patient(patients,id)
						else:
							print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")
					elif op=='4':
						id=input("Please enter the id : ")
						if id in patients :
							mod.display_patient(patients,id)
						else:
							print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")	
					elif op=='B':
						break
					else :
						print(" **** Wrong Choice **** ")
					mod.store_data(doctors,patients)
			elif task=='2':
				while 1:
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
					op=input('''To ADD Doctor Press 1 
To Delete Doctor Press 2 
To Edit Doctor Data Press 3
To Display Doctor's Data Press 4 
To Return Back to the previous menu Press B     your choice :  ''')
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
					if op=='1':
						id=input("Please enter the id : ")
						while id in doctors :
							id=input("This Id already Existed please enter another one : ")
					
						mod.add_doctor(doctors,id)
					elif op=='2':
						id=input("Please enter the id : ")
						if id in doctors :
							mod.delete_doctor(doctors,id)
						else:
							print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")
					elif op=='3':
						id=input("Please enter the id : ")
						if id in doctors :
							mod.edit_doctor(doctors,id)
						else:
							print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")
					elif op=='4':
						id=input("Please enter the id : ")
						if id in doctors :
							mod.display_doctor(doctors,id)
						else:
							print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")	
					elif op=='B':
						break
					else :
						print(" **** Wrong Choice **** ")
					mod.store_data(doctors,patients)
			elif task=='3':
				while 1:
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
					op=input('''To Book an Appointment Press 1
To Edit an appointment Press 2
To Cancel an appointment Press 3          
TO Return to the Previous menu Press B            your Choice : ''')
					if op=='1':
						id=input('please enter ID : ')
						if id in booked_appointments:
							id=input("The ID is already Existed Please enter another one : ")	
						else: 
							print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
							department=input('''For Cardiology Department Press 1
For Neurology Department press 2
For Orthopedics Department press 3
For Opthalmology Department press 4
For Radiology Department Press 5        
TO Return to the previous menu Press B             your choice : ''')
							if department =='1':
								department='Cardiology'
								print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
								doc=input('''To View Doctor Ismail Mohamed Slots Press 1 
To View Doctor Osama Ahmed Slots Press 2           your Choice :  ''')
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
								doc=input('''To View Doctor Ahmed Abdelaziz Slots Press 1 
To View Doctor Wael Mounir Slots Press 2           your Choice :  ''')
								if doc=='1':
									doctor='Ahmed Abdelaziz'
								elif doc=='2':
									doctor='Wael Mounir'
								else :
									print(" **** Wrong Choice **** ")							
							elif department =='4':
								department='Opthalmology'
								print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
								doc=input('''To View Doctor Sherif Reda Slots Press 1 
To View Doctor Alaa Badr Slots Press 2           your Choice :  ''')		
								if doc=='1':
									doctor='Sherif Reda'
								elif doc=='2':
									doctor='Alaa Badr'
								else :
									print(" **** Wrong Choice **** ")		
							elif department =='5':
								department='Radiology'
								print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
								doc=input('''To View X-ray Slots Press 1 
To View  MRI Slots Press 2           your Choice :  ''')		
								if doc=='1':
									doctor='X-ray'
								elif doc=='2':
									doctor='MRI'
								else :
									print(" **** Wrong Choice **** ")			
							else :
								print(" **** Wrong Choice **** ")		
						mod.book_appointment(booked_appointments,available_appointments,department,doctor,id)	
							
					elif op=='2':
						id=input("Please enter the reservation ID : ")
						if id in booked_appointments:
							mod.Edit_appointment(booked_appointments,available_appointments,id)
						else:
							print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")
					elif op=='3':
						id=input("Please enter appointment ID : ")
						if id in booked_appointments:
							mod.cancel_appointment(booked_appointments,available_appointments,id)
						else :
							print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")
							
					elif op=='B':
						break
					else :
						print(" **** Wrong Choice **** ")
			elif task=='B':
				break
			else:
				print("**** Wrong Choice**** ")
	elif mode=='2':
		print("##** Welcome User **## ")
		while 1:
			
			op=input('''To View all Departments in the Hospital Press 1 
To View All Doctors in Hospital in Details Press 2
To View All Patients in Hospital in Details Press 3 
To view Certain patient's Details Press 4
To View the Appointments of a Doctor Press 5         
To Return to the previous menu Press B               your Choice : ''')
			if op=='1':
				mod.view_departments(available_appointments)
				print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
			elif op=='2':
				mod.display_alldoctors(doctors)
				print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
			elif op=='3':
				mod.display_allpatients(patients)
				print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
			elif op=='4':
				id=input("Please enter the patient's ID : ")
				if id in patients :
					mod.display_patient(patients,id)
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
				else:
					print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")
			elif op=='5':
				id=input("Please enter the doctor's ID : ")
				if id in doctors:
					mod.display_doctorappointment(doctors,id)
					print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
				else:
					print(" *^*^*^*^*^*^*^*^* The ID you Entered is not existing *^*^*^*^*^*^*^*^*")
					
			elif op=='B':
				break
			else:
				print("**** Wrong Choice**** ")	
	elif mode=='E':
		break
	else:
		print("**** Wrong Choice**** ")