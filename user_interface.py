
from UI.destinationUI import DestinationUI

import string
from UI.voyageUI import VoyageUI
from UI.page import Page
from UI.employeeUI import EmployeeUI
from UI.airplaneUI import AirplaneUI
import os
import pathlib


VALID_THREE= ["1","2","3"]

class User(Page):
    def __init__(self, first_pick=None, second_pick=None, valid=True):
        self.valid_inputs = []
        self.first_pick = first_pick
        self.second_pick = second_pick
        self.valid = valid

        self.employeeUI = EmployeeUI()
        self.destinationUI = DestinationUI()
        self.voyageUI = VoyageUI()
        self.airplaneUI = AirplaneUI()

    def __str__(self):
        return "First pick:{}, second pick: {}".format(str(self.first_pick), str(self.second_pick))

    def Home(self):

        self.valid_inputs = ["1", "2"]

        self.header()
        print("1. Staff manager\n2. Planning manager\n3. Exit")
        self.footer()

        # Read_key() reads key_down and key_up events seperately. Since there's no use for the 
        # "key_up" I don't assign it to a variable but I write it here to keep it from interfering
        # with the program and for clarifications.
        user_input = input().strip()

        # Debug, remove before turn in
        print(user_input)


        if user_input in self.valid_inputs:
            chose_back = False
            self.first_pick = user_input
            if user_input == "1":

                while not chose_back:
                    chose_back = self.Staff_manager()

                return False
            else:

                while not chose_back:
                    chose_back = self.Planning_manager()

                return False
        else:
            if user_input == "4":
                # Return "True" to end the outside loop (in this case the loop in the main program) displaying the screen.
                return True
            else:
                self.valid = False
                return False

    def Staff_manager(self):
        """
        Displays the option screen for a staff manager.

        Options: Man flights, lists of work force and manage work force

        """
        self.valid_inputs = ["1", "2", "3"]

        
        self.header()
        print("1. Man flights \n2. Workforce information\n3. Manage work force\n4. Back")
        self.footer()
        

        user_input = input().strip()
        print(user_input)

        if user_input not in self.valid_inputs:

            if user_input == "4":
                # return "True" so the loop displaying the screen ends.
                return True

            else:
                # set valid to false to display a "... valid input..." message
                self.valid = False
                # Return "False" to display the screen again
                return False

        else:
            if user_input == "1":
                chose_back = False
                """Man flights"""
                while not chose_back:

                    chose_back = self.voyageUI.man_voyage_SM()

                return False
                print("MAN FLIGHTS")
                # svo man flights

            elif user_input == "2":
                """List of work force"""

                print("List of work force".upper())
                #svo list of work force


            elif user_input == "3":
                """Manage work force"""

                print("Manage work force".upper())
                #svo manage work force

        

    def Planning_manager(self):

        self.valid_inputs = ["1", "2", "3"]

        
        self.header()
        print("1. Manage voyages\n2. Voyage informations\n3. Manage destinations\n4. Back")
        self.footer()
        

        user_input = input().strip()
        print(user_input)
        
        chose_back = False
        while not chose_back:
            

            if user_input == "4":
                # return "True" so the loop displaying the screen ends.
                return True
            
            
            elif user_input == "1":

                chose_back = self.manage_voyages()

            elif user_input == "2":
                
                chose_back = self.list_of_voyages()

            elif user_input == "3":
                
                chose_back = self.manage_destinations()

            else:
                # set valid to false to display a "... valid input..." message
                self.valid = False
                # Return "False" to display the screen again
                return False

        return False

    def manage_voyages(self):

        self.header()
        voyage_pick = input("1. Register a new voyage\n2. Edit a voyage\n3. Cancel a voyage\n4. Back ").strip()
        self.footer()

        chose_back = False
        while not chose_back:

            if voyage_pick == "4":
                
                return True

            elif voyage_pick =="1":
                chose_back = self.voyageUI.register_new_voyage_PM()

            elif voyage_pick =="2":
                pass
                # chose_back = self.voyageUI.edit_voyage()
                # edit a voyage

            elif voyage_pick == "3":
                chose_back = self.voyageUI.cancel_voyage()
                #Cancel a voyage
        return False            

    def list_of_voyages(self):
        pass

    def manage_destinations(self):
        pass


    def Workforce_information(self):
        
        self.header()
        print(  "1. List of all airplanes\n" + \
                "2. List of all employees\n" + \
                "3. List of all flight attendants\n" + \
                "4. List of all pilots\n" + \
                "5. List of all available employees at a given time\n" + \
                "6. List of all busy employees at a given time\n" + \
                "7. Find an employee\n" + \
                "8. Back")
        self.footer()

        user_input = input().strip()

        chose_back = False
        while not chose_back:

            if user_input == "8":
                return True

            elif user_input == "1":
                
                chose_back = self.airplaneUI.list_all_airplanes()


            elif user_input == "2":
                
                chose_back = self.employeeUI.get_all_employees()

            elif user_input == "3":
                
                chose_back = self.employeeUI.list_all_flight_attendants()
            elif user_input == "4":
                
                chose_back = self.employeeUI.list_all_pilots()

            elif user_input == "5":
                
                chose_back = self.employeeUI.available_employees()

            elif user_input == "6":
                
                chose_back = self.employeeUI.busy_employees()

            elif user_input == "7":
                
                chose_back = self.employeeUI.get_employee()
            else: 
                self.valid = False
                return False




# user = VoyageUI()

# user.man_voyage_SM()

user = User()
exit = False

while(not exit):
    user_selection = user.Home()
    exit = user_selection



# if user.first_pick == "1":
#     user.Staff_manager()

# elif user.first_pick== "2":
#     user.Planning_manager()

#print("home window: {} second_window: {}".format(user.first_pick,user.second_pick))


# print(user)

