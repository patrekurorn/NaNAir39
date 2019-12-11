
from UI.destinationUI import DestinationUI
import keyboard
import string
from UI.voyageUI import VoyageUI
from NaNAir39.UI.page import Page
from NaNAir39.UI.employeeUI import EmployeeUI
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

    def __str__(self):
        return "First pick:{}, second pick: {}".format(str(self.first_pick), str(self.second_pick))

    def Home(self):

        self.valid_inputs = ["1", "2"]

        self.header()
        print("1.Staff manager\n2.Planning manager")
        self.footer()

        # Read_key() reads key_down and key_up events seperately. Since there's no use for the 
        # "key_up" I don't assign it to a variable but I write it here to keep it from interfering
        # with the program and for clarifications.
        user_input = keyboard.read_key()
        keyboard.read_key()

        # Debug, remove before turn in
        print(user_input)


        if user_input in self.valid_inputs:
            escaped = False
            self.first_pick = user_input
            if user_input == "1":

                while not escaped:
                    escaped = self.Staff_manager()

                return False
            else:

                while not escaped:
                    escaped = self.Planning_manager()

                return False
        else:
            if user_input == "esc":
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
        print("1. Man flights \n2. Workforce information\n3. Manage work force")
        self.footer()
        

        user_input = keyboard.read_key()
        keyboard.read_key()
        print(user_input)

        if user_input not in self.valid_inputs:

            if user_input == "esc":
                # return "True" so the loop displaying the screen ends.
                return True

            else:
                # set valid to false to display a "... valid input..." message
                self.valid = False
                # Return "False" to display the screen again
                return False

        else:
            if user_input == "1":
                escaped = False
                """Man flights"""
                while not escaped:

                    escaped = self.voyageUI.man_voyage_SM()

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
        print("1. Manage voyages\n2. Voyage informations\n3. Manage destinations")
        self.footer()
        

        user_input = keyboard.read_key()
        keyboard.read_key()
        print(user_input)
        

        def manage_voyages():
            
            self.header()
            voyage_pick = input("1.Register a new voyager\n2.Edit a voyage\n3.Cancel a voyage ").strip()
            self.footer()
            if voyage_pick not in self.valid_inputs:
                
                
                manage_voyages()

            elif voyage_pick =="1":
                self.footer()
                #Register a new voyager
                pass

            elif voyage_pick =="2":
                self.footer()
                pass
                # edit a voyage

            elif voyage_pick == "3":
                self.footer()
                #Cancel a voyage
                pass




        def list_of_voyages():
            pass

        def manage_destinations():
            pass



        if user_input not in self.valid_inputs:

            if user_input == "esc":
                # return "True" so the loop displaying the screen ends.
                return True
            else:
                # set valid to false to display a "... valid input..." message
                self.valid = False
                # Return "False" to display the screen again
                return False

        else:
            
            if user_input == "1":
                print("MANAGE VOYAGES")
            if user_input == "2":
                print("List of voyages".upper())
            if user_input == "3":
                print("Manage destinations".upper())
                DestinationUI()


    def Workforce_information(self):
        
        
        self.header()
        print(  "1. List of all airplanes\n" + \
                "2. List of all employees\n" + \
                "3. List of all flight attendants\n" + \
                "4. List of all pilots\n" + \
                "5. List of all available employees\n" + \
                "6. List of all busy employees\n" + \
                "7. find employee")
        self.footer()







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

