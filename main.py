
from UI.destinationUI import DestinationUI

import string
from UI.voyageUI import VoyageUI
from UI.page import Page
from UI.employeeUI import EmployeeUI
from UI.airplaneUI import AirplaneUI
from datetime import datetime
import os
import pathlib

#a = VoyageUI()
#a.get_all_voyages_after_current_date()


# VALID_THREE= ["1","2","3"]

class User(Page):
    def __init__(self):
        self.employeeUI = EmployeeUI()
        self.destinationUI = DestinationUI()
        self.voyageUI = VoyageUI()
        self.airplaneUI = AirplaneUI()

        super().__init__()

    def Home(self):

        options = ["1. Staff manager", "2. Planning manager", "3. Exit"]

        self.show_page(options)
        user_input = input().strip()
      
        chose_back = False
        while not chose_back:
            self.first_pick = user_input
            if user_input == "1":   # Staff manager
                chose_back = self.Staff_manager()
            elif user_input == "2": # Planning manager
                chose_back = self.Planning_manager()
            elif user_input == "3": # Exit
                # Return "True" to end the outside loop (in this case the loop in the main program)
                return True                 
            else:                   # Invalid input
                self.valid = False
                return False
        
        return False    #Continue outside loop

    def Staff_manager(self):
        """
        Displays the option screen for a staff manager.

        Options: Man flights, lists of work force and manage work force

        """

        header = "Staff manager"
        options = ["1. Man flights", "2. Workforce information", "3. Manage workforce", "4. Back"]

        self.show_page(options, header)
        
        user_input = input().strip()

        chose_back = False
        while not chose_back:

            if user_input == "4":       # Back
                # return "True" so the loop displaying the screen ends.
                return True
            elif user_input == "1":     # Man flights
                chose_back = self.voyageUI.man_voyage_SM()
            elif user_input == "2":     # Workforce information
                chose_back = self.Workforce_information()
            elif user_input == "3":     # Manage workforce
                chose_back = self.manage_workforce()
            else:                       # Invalid input
                # set valid to false to display an error message
                self.valid = False
                return False
        # Return "False" to display this screen again
        return False
    
    def manage_workforce(self):
        
        header = "Manage workforce"
        options = [ "1. Register a new airplane",
                    "2. Register a new employee",
                    "3. Edit employee",
                    "4. Back"]

        self.show_page(options, header)

        user_input = input().strip()

        chose_back = False

        if not chose_back:

            if user_input == "4":       # Back
                return True
            elif user_input == "1":     # Register new airplane
                chose_back == self.airplaneUI.register_airplane()
            elif user_input == "2":     # Register a new employee
                chose_back == self.employeeUI.register_employee()
            elif user_input == "3":     # Edit employee
                chose_back == self.employeeUI.edit_employee()
            else:                       # Invalid input
                self.valid = False
                return False
            
        return False

    def Planning_manager(self):

        header = "Planning manager"
        options = ["1. Manage voyages", "2. Voyage informations", "3. Manage destinations", "4. Back"]
        self.show_page(options, header)

        user_input = input().strip()

        chose_back = False
        if not chose_back:
            
            if user_input == "4":       # Back
                return True
            elif user_input == "1":     # Manage voyages
                chose_back = self.manage_voyages()

            elif user_input == "2":     # Voyage information
                chose_back = self.list_of_voyages()

            elif user_input == "3":     # Manage destinations
                chose_back = self.manage_destinations()
            else:                       # Invalid input
                # set valid to false to display a "... valid input..." message
                self.valid = False
                return False

        return False

    def manage_voyages(self):
        header = "Manage voyages"
        options = ["1. Register a new voyage", "2. Edit a voyage", "3. Cancel a voyage", "4. Back"]
        self.show_page(options, header)

        voyage_pick = input().strip()

        chose_back = False
        if not chose_back:
            if voyage_pick == "4":      # Back
                return True

            elif voyage_pick == "1":     # Register a new voyage
                chose_back = self.voyageUI.register_voyage_PM()

            elif voyage_pick == "2":     # Edit a voyage
                chose_back = self.edit_voyage_information()


            elif voyage_pick == "3":    # Cancel a voyage
                chose_back = self.voyageUI.cancel_voyage()
            else:
                self.valid = False
                return False

        return False

    def edit_voyage_information(self):
        edit_header = "Edit voyage"
        edit_options = ["1. Edit voyage date", "2. Edit destination","3. Back"]
        self.show_page(edit_options,edit_header)
        user_input_str = input().strip()

        chooseBack = False
        if not chooseBack:
            if user_input_str =="1": # edit voyage date
                chooseBack = self.voyageUI.edit_voyage_date()

            elif user_input_str == "2": # edit destination
                """ þarf að klára """
                chooseBack == self.destinationUI.edit_destination()

            elif user_input_str == "3":
                chooseBack == True

            else:
                self.valid = False
        return True


    def list_of_voyages(self):
        
        options = ["1. List all voyages",
                "2. List by day",
                "3. List by week",
                "4. Back"]

        self.show_page(options)
        user_input = input().strip()
        chose_back = False

        if not chose_back:
            if user_input == "4":
                return True

            elif user_input == "1":
                
                chose_back = self.voyageUI.print_all_voyages()

            elif user_input == "2":
                
                chose_back = self.voyageUI.list_voyage_day()

            elif user_input == "3":
                chose_back = self.voyageUI.print_list_voyage_by_week()
            else: 
                self.valid = False
                return False

        return False


    def manage_destinations(self):
        header = "Manage destinations"
        options = [ "1. Voyage repetions",
                    "2. Edit contact information",
                    "3. Register destination",
                    "4. Back "]

        self.show_page(options,header)
        user_input = input().strip()

        chose_back = False
        while not chose_back:
            if user_input == "4":
                return True
            elif user_input == "1":
                True

            elif user_input == "2":
                chose_back = self.destinationUI.edit_destination()

            elif user_input == "3":
                chose_back = self.destinationUI.register_destination()   # Endalaus loopa
            else:
                self.valid = False
                return False

        return False

    def Workforce_information(self):
        
        header = "Workforce information"
        options = [ "1. List of all airplanes",
                "2. List of all employees",
                "3. List of all flight attendants",
                "4. List of all pilots",
                "5. List of all available employees at a given time",
                "6. List of all busy employees at a given time",
                "7. Print week of employee",
                "8. Back"]
        
        self.show_page(options, header)

        user_input = input().strip()

        chose_back = False
        while not chose_back:

            if user_input == "8":
                return True
            elif user_input == "1":
                chose_back = self.airplaneUI.list_all_airplanes()
            elif user_input == "2":
                chose_back = self.employeeUI.get_all_employees()    # Endalaus loopa
            elif user_input == "3":
                chose_back = self.employeeUI.list_all_flight_attendants()   # Endalaus loopa
            elif user_input == "4":
                chose_back = self.employeeUI.list_all_pilots()  # Endalaus loopa
            elif user_input == "5":
                chose_back = self.employeeUI.available_employees()  # Festist inní
            elif user_input == "6":
                chose_back = self.employeeUI.busy_employees()   # Festist inní
            elif user_input == "7":
                chose_back = self.employeeUI.get_employee()     # Festist hérna inni, ekki hægt að fara til baka
            else: 
                self.valid = False
                return False
        
        return False




# user = VoyageUI()

# user.man_voyage_SM()
user = User()


user = User()
exit = False
while(not exit):
    user_selection = user.Home()
    exit = user_selection


"""

# if user.first_pick == "1":
#     user.Staff_manager()

# elif user.first_pick== "2":
#     user.Planning_manager()

#print("home window: {} second_window: {}".format(user.first_pick,user.second_pick))


# print(user)
<<<<<<< HEAD
=======

>>>>>>> f695626c1ece5cb54fb996be1d7cb0ea735a91d3
"""