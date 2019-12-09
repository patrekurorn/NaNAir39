import os
from time import sleep
from UI.destinationUI import DestinationUi

import string


VALID_THREE= ["1","2","3"]

class User:
    def __init__(self,first_pick = None, second_pick = None):
        self.first_pick = first_pick
        self.second_pick = second_pick

    def __str__(self):
        return "First pick:{}, second pick: {}".format(str(self.first_pick),str(self.second_pick))


    def home_window(self):
        user.get_header()
        userInput = input("1.Staff manager\n2.Planning manager\nYour pick: ").strip() #strip spaces

        def invalid():
            print("Please enter a valid number ")
            self.home_window()

        if userInput == "1" or userInput == "2".strip():
            self.first_pick = userInput
            user.get_footer()
        else:
            invalid()

    def second_window_staff_manager(self):
        user.get_header()

        def invalid():
            print("Please enter a valid number ")
            user.second_window_staff_manager()

        pick_input = input("1. Man flights \n2. List of work force\n3. Manage work force\nYour pick: ").strip()

        if pick_input not in VALID_THREE:
            invalid()

        else:
            if pick_input == "1":
                """Man flights"""
                print("MAN FLIGHTS")
                pass
            elif pick_input == "2":
                """List of work force"""
                print("List of work force".upper())
            elif pick_input == "3":
                """Manage work force"""
                print("Manage work force".upper())
        user.get_footer()



    def second_window_planning_manager(self):

        def invalid():
            print("Please enter a valid number ")
            user.second_window_planning_manager()


        pick_input = input("1. Manage voyages\n2. List of voyages\n3. Manage destinations\nYour pick: ")
        if pick_input not in VALID_THREE:
            invalid()

        else:
            if pick_input == "1":
                print("MANAGE VOYAGES")
            if pick_input == "2":
                print("List of voyages".upper())
            if pick_input == "3":
                print("Manage destinations".upper())
                DestinationUi()








    def get_header(self):
        print ("-----------------------------------------------------------\n" + \
               "                        NaN Air                            \n" + \
               "___________________________________________________________\n" + \
               "___________________________________________________________\n" + \
               "\n",end="")

    def get_footer(self):
        print("-----------------------------------------------------------\n" + \
              "___________________________________________________________\n" + \
              "\n" + \
              "                          _|_                              \n" + \
              "                   *---o--(_)--o---*                       \n" + \
              "___________________________________________________________")

user = User()
user_selection = user.home_window()
sleep(1.5) # Freeze screen for n seconds
#os.system('cls')  # For Windows
#os.system('clear')  # For Linux/OS X


if user.first_pick == "1":
    user.second_window_staff_manager()

elif user.first_pick== "2":
    user.second_window_planning_manager()

#print("home window: {} second_window: {}".format(user.first_pick,user.second_pick))








