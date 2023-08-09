# Project: Classes August 7, 2023. Amadou, Diallo, Alex Lam, Sanketh Mekala, Winko Peng (Group 7). 
# Program Description:
# This program creates a Doctor / Patient Management System with five classes:
# Doctor Class: Represents a doctor with attributes like doctor_id, name, specialization, working_time, qualification, and room_number.
# Doctor_Manager Class: Manages a list of doctors, reads doctor information from "doctors.txt," and allows adding, editing, searching by ID and name, and displaying doctors.
# Patient CLass: Represents a patient with attributes like pid, name, disease, gender, and age.
# Patient_Manager Class: Manages a list of patients, reads patient information from "patients.txt," and allows adding, editing, searching by ID, and displaying patients.
# Management Class: The main class that displays the Doctor / Patient Management System menu, providing options to access Doctor and Patient submenus for various user inputs.

# The program's main menu allows users to navigate to the Doctor and Patient submenus. In the Doctor submenu, users can display, search, add, and edit doctor information. The Patient submenu enables similar application for patients.

# Create Doctor class
class Doctor:

    #Doctor object constructor 
    def __init__(self,doctor_id,name,specialization, working_time, qualification,room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time  = working_time
        self.qualification = qualification
        self.room_number = room_number

    # Getters
    def get_doctor_id(self):
        return self.doctor_id
    
    def get_name(self):
        return self.name
    
    def get_specialization(self):
        return self.specialization
    
    def get_working_time(self):
        return self.working_time
    
    def get_qualification(self):
        return self.qualification
    
    def get_room_number(self):
        return self.room_number 
    
    # Setters
    def set_doctor_id(self,new_id):
        self.doctor_id = new_id
    
    def set_name(self,new_name): 
        self.name = new_name
    
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
    
    def set_working_time(self,new_working_time):
        self.working_time = new_working_time
    
    def set_qualification(self, new_qualification):
        self.qualification = new_qualification
    
    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    # String method to return a string representation of the doctor object 
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"
    
# Create Doctor-Manager class
class Doctor_Manager:

    # Doctor Manager Constructor
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    # Format dr info method to format the doctor objects information to match the txt file
    def format_dr_info(self,doctor):
        return doctor.__str__()
    
    # Read from the doctor txt file, strip and split the data in the file to create a doctor object for each line in the file. Then append that object to the doctors list created in the constructor.
    def read_doctors_file(self):
        with open("Project-Classes-Group-7/doctors.txt", 'r') as file:
            for line in file:
                doctor_id, name ,specialization,working_time,qualification,room_number = line.strip().split('_')
                if name == 'name':
                    name = 'Name'
                if specialization == 'specilist':
                    specialization = 'Speciality'
                if qualification == 'qualification':
                    qualification = 'Qualification'

                try:
                    doctor_id = int(doctor_id)
                    room_number = int(room_number)
                except ValueError:
                    doctor_id= "Id"
                    room_number ="Room Number"
                doctor = Doctor(doctor_id,name,specialization,working_time, qualification,room_number)
                self.doctors.append(doctor)    

    # Prompts user to enter doctor infomotion than returns the inputs in one line.
    def enter_dr_info(self):
        print()
        doctor_id = input("Enter the doctor’s ID: ")
        name = input("Enter the doctor’s name: ")
        specility = input("Enter the doctor’s specility: ")
        work_time = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor’s qualification: ")
        room_number = input("Enter the doctor’s room number: ")
        doctor = Doctor(doctor_id,name,specility,work_time,qualification,room_number,)
        return doctor
        
    # Prompt user to input ID, Iterates over the for loop to check for that ID, returns that ID if found with .format spacing, if not prints can't find that id.
    def search_doctor_by_id(self):
        print()
        doctor_id = int(input("Enter the doctor ID: "))
        print()
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<15}".format('Id','Name','Speciality','Timing','Qualification','Room Number\n'))
                return self.display_doctor_info(doctor)
        else:

            return print("Can't find the doctor with the same ID on the system\n")

    # Prompt User to input a Doctor name, Iterates over the for loop to check for that name, returns that name along with the information if found with .format spacing if not prints can't find name.        
    def search_doctor_by_name(self):
        print()
        doctor_name = input("Enter the doctor Name: ")
        print()
        for doctor in self.doctors:
            if doctor.get_name() == doctor_name:
                print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<15}".format('Id','Name','Speciality','Timing','Qualification','Room Number \n'))
                return self.display_doctor_info(doctor)
        else:
            return print("Can't find the doctor with the same name on the system\n")
        
    # Displays the doctor object in a table like format with .format to space out the data.    
    def display_doctor_info(self,doctor): 
        print("{:<5}{:<20}{:<15}{:<15}{:<15}{:<15}".format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time().capitalize(), doctor.get_qualification(), doctor.get_room_number()))
        print()

    # Prompt user to enter the doctor ID they would like to edit, set a variable to none, then checks list to find that ID to store to variable set to noneD if variable doesn't == to none prompt user to edit otherwise print can't find ID. 
    def edit_doctor_info(self):
        found_doctor = None
        print()
        doctor_id = int(input("Please enter the id of the doctor that you want to edit their information: "))
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                found_doctor = doctor
                break   
               
        if found_doctor != None:
            new_name = input("Enter new Name: ")
            new_specialization = input("Enter new Specilist in: ")
            new_working_time = input("Enter new Timing: ")
            new_qualification = input("Enter new Qualification: ")
            new_room_number = input("Enter new Room number: ")
            found_doctor.set_name(new_name)
            found_doctor.set_specialization(new_specialization )
            found_doctor.set_working_time(new_working_time)
            found_doctor.set_qualification(new_qualification)
            found_doctor.set_room_number(new_room_number )
            self.write_list_of_doctors_to_file()
            print()
            print(f"Doctor whose ID is {doctor_id} has been edited \n")
        else:
            print(f"Cannot find the doctor with an ID of {doctor_id}")
            
    # Creates a for loop to iterate over each doctor object in the doctors list and uses the display doctor info function to diplay the object
    def display_doctor_list(self):
        for doctor in self.doctors: 
             self.display_doctor_info(doctor)

    # Write a doctor object to the doctors txt file in the correct formating using format_dr_info.
    def write_list_of_doctors_to_file(self):
        with open("Project-Classes-Group-7/doctors.txt", 'w') as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")

    # Calls the enter dr info which stores it in a variable as a new doctor, check to see if the id exists and print the id is already in use if the id already exists, else if it does not exist append the new doctor object to the doctors list and write the new doctor object to the file of doctors,print a message that the doctor has been added.
    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        for doctor in self.doctors:
            if int(new_doctor.get_doctor_id()) == doctor.get_doctor_id():
                print("That Doctor ID is already in use please select another ID\n")   
                break
        else:
            self.doctors.append(new_doctor)
            self.write_list_of_doctors_to_file()
            print()
            print(f'Doctor whose ID is {new_doctor.get_doctor_id()} has been added \n')

# Define patient class
class Patient:

    # Constructor 
    def __init__(self, pid, name, disease, gender,age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    # Getters
    def get_pid (self):
        return self.pid
    
    def get_name (self):
        return self.name
    
    def get_disease (self):
        return self.disease
    
    def get_gender (self):
        return self.gender
    
    def get_age (self):
        return self.age
    
    # Setters
    def set_pid(self, new_pid):
        self.pid = new_pid
    
    def set_name(self, new_name):
        self.name = new_name
    
    def set_disease (self, new_disease):
        self.disease = new_disease
    
    def set_gender (self, new_gender):
        self.gender = new_gender
    
    def set_age (self, new_age):
        self.age = new_age
    
    # String method to return a string representation of the doctor object 
    def __str__(self):
        return f'{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}'

# Define patient manager class   
class Patient_Manager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    # formatts getters into one sentence with under scores as space
    def format_patient_info_for_file(self,patient):
        return patient.__str__()

    # Enter patient info method that allows the user to create a patient object
    def enter_patient_info(self):
        print()
        pid = input("Enter the patient ID: ")
        name = input("Enter the patient name: ")
        disease = input("Enter the patient's disease: ")
        gender = input("Enter the gender of the patient: ")
        age = input("Enter the patient's age: ")
        patient_info = Patient(pid,name,disease,gender,age)
        return patient_info

    # Read patients txt file and create a patient object with specific properties for each line in the file.
    def read_patients_file(self):
        with open("Project-Classes-Group-7/patients.txt", 'r') as file:
            for line in file:
                pid, name, disease, gender, age = line.strip().split('_')
                try:
                    age = int(age)
                    pid = int(pid)
                except ValueError:
                    age = "Age"
                    pid = "ID"
                patient = Patient(pid,name,disease,gender,age)
                self.patients.append(patient)
    
    # Searchs for a patient object based on the id entered in the user input and displays
    def search_patient_by_id(self):
        print()
        patient_id = input("Enter a patient ID: ")
        print()
        for patient in self.patients:
            if int(patient_id) == patient.get_pid():
                print("{:<5}{:<20}{:<15}{:<15}{:<15}".format('PID','Name','Disease','Gender','Age\n'))
                return self.display_patient_info(patient)
        else:
            print("Can't find the Patient with the same id on the system \n")

    # Display patient info method to display and format a patient object in the correct format of the output file.
    def display_patient_info(self,patient):
        print("{:<5}{:<20}{:<15}{:<15}{:<15}".format(patient.get_pid(), patient.get_name(), patient.get_disease(), patient.get_gender(),patient.get_age()))
        print()

    # Edit patient info method to edit a specific patient object from the patiens list and then update and write that objects properties to the patients txt file.
    def edit_patient_info_by_id(self):
        found_patient = None
        print()
        patient_id = input("Please enter the id of the patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_pid() == int(patient_id):
                found_patient= patient
                break      
        if found_patient != None:
            new_name = input("Enter new Name: ")
            new_disease = input("Enter new disease: ")
            new_gender = input("Enter new gender: ")
            new_age = input("Enter new age: ")
            found_patient.set_name(new_name)
            found_patient.set_disease(new_disease)
            found_patient.set_gender(new_gender)
            found_patient.set_age(new_age)
            self.write_list_of_patients_to_file()
            print()
            print(f"Patient whose ID is {patient_id} has been edited \n")
        else:
            print(f"Cannot find the patient with an ID of {patient_id}")
            
    # Display patient list method that iterates over the patient list and correctly displays each patient objct using the display patient info function       
    def display_patient_list(self):
        for patient in self.patients: 
            self.display_patient_info(patient)
            
    # Write list of patients method which writes and formats a patient object to the patients.txt file 
    def write_list_of_patients_to_file(self):
        with open('Project-Classes-Group-7/patients.txt', 'w') as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient) + "\n")
    
    # Calls the enter patient info which stores it in a variable as a new patient, check to see if the id exists and print the id is already in use if the id of that patient already exists. Else if it does not exist append the new patient object to the patients list and write the new patient object to the patients.txt file and print a message that the patient has been added 
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        for patient in self.patients:
            if int(new_patient.get_pid()) == patient.get_pid():
                print("That Patient ID is already in use please select another ID")   
                break 
        else:
            self.patients.append(new_patient)
            self.write_list_of_patients_to_file()
            print()
            print(f'Patient whose ID is {new_patient.get_pid()} has been added \n')
            
            
# Define Managment Class
class Management:
    
    # Display menu method to display the Hospital managment system menu, which allows the user to enter a value to display the doctors and patient menus. Inside each doctor and patient menu the user can enter a specific value to call on each patient or doctor mangment class and perform a specific operation depending on what the user enters. These menus will keep looping and taking user input until the user enters the correct value to exit the program, which prints a thank you message. 
    def display_menu():
        while True: 
            print("Welcome to Alberta Hospital (AH) Managment system ")
            print("Select from the following options, or select 3 to stop: ")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit")
            
            main_menu = input(">>> ")
            print()
            if main_menu == "1":
                while True:
                        print("Doctor Menu")
                        print("1 - Display Doctors list")
                        print("2 - Search for doctor by ID")
                        print("3 - Search for doctor by name")
                        print("4 - Add doctor")
                        print("5 - Edit doctor info")
                        print("6 - Back to the Main Menu")

                        doctor_menu = input(">>> ")
                        if doctor_menu == "1":
                            Doctor_Manager().display_doctor_list()
                        elif doctor_menu == "2":
                            Doctor_Manager().search_doctor_by_id()
                        elif doctor_menu == "3":
                            Doctor_Manager().search_doctor_by_name()
                        elif doctor_menu == "4":
                            Doctor_Manager().add_dr_to_file()
                        elif doctor_menu == "5":
                            Doctor_Manager().edit_doctor_info()
                        elif doctor_menu == "6":
                            break
                                              
            elif main_menu == "2":
                    while True:   
                        print("Patient Menu")     
                        print("1 - Display patients list")
                        print("2 - Search for patient by ID")
                        print("3 - Add patient")
                        print("4 - Edit patient info")
                        print("5 - Back to Main Menu")

                        patient_menu = input(">>> ")
                        
                        if patient_menu == "1":
                            Patient_Manager().display_patient_list()
                        
                        elif patient_menu == "2":
                            Patient_Manager().search_patient_by_id()
                        
                        elif patient_menu == "3":
                            Patient_Manager().add_patient_to_file()

                        elif patient_menu == "4":
                            Patient_Manager().edit_patient_info_by_id()

                        elif patient_menu == "5":
                            break
                    
            elif main_menu == "3":
                print("Thanks for using the program. Bye!")
                break

# set the managment class to a variable and call the display_menu() method which displays the main menu of the program
main = Management
main.display_menu()