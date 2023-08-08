from doctor_management_class import Doctor_Manager
from Patient_Manager import Patient_Manager

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