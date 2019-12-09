import os
from time import sleep
import keyboard

VALID = [1,2,3]

class User:
    def __init__(self,first_pick = None, second_pick = None):
        self.first_pick = first_pick
        self.second_pick = second_pick

    def __str__(self):
        return "First pick:{}, second pick: {}".format(str(self.first_pick),str(self.second_pick))


    def home_window(self):
        def invalid():
            print("Please enter a valid number ")
            user.home_window()

        print("1. Staff manager \n2. Planning manager")

        # try:
        #     userInput_int = int(input("1. Staff manager \n2. Planning manager \nYour pick: "))

        # except KeyError:
        #     invalid()

        user_pick = keyboard.read_key()
        
        if user_pick == '1':
            self.first_pick = 1

        elif user_pick == '2':
            self.first_pick = 2

        else:
            invalid()

        return self.first_pick

    def second_window(self):

        def invalid():
            print("Please enter a valid number ")

        def first_pick():
            try:
                pick_input = int(input("1. Man flights \n2. List of work force\n3. Manage work force\nYour pick: "))
                if pick_input not in VALID:
                    invalid()
                    first_pick()
                else:
                    self.second_pick = pick_input
                    return self.second_pick

            except KeyError:
                invalid()
                first_pick()

        def second_pick():
            try:
                pick_input = int(input("1. Manage voyages\n2. List of voyages\n3. Manage destinations\nYour pick: "))
                if pick_input not in VALID:
                    invalid()
                    second_pick()
                else:
                    self.second_pick = pick_input
                    return self.second_pick

            except KeyError:
                invalid()
                second_pick()

        if self.first_pick == 1:
            second_pick()

        elif self.first_pick  == 2:
            second_pick()


    def get_header(self):
        print ("___________________________________________________________\n" + \
                "                        NaN Air                            \n" + \
                "___________________________________________________________\n" + \
                "-----------------------------------------------------------\n" + \
                "\n",end="")

    def get_footer(self):
        print("-----------------------------------------------------------\n" + \
                "___________________________________________________________\n" + \
                "\n" + \
                "                          _|_                              \n" + \
                "                   *---o--(_)--o---*                       \n" + \
                "___________________________________________________________")


user = User()
user.get_header()
user_selection = user.home_window()
user.get_footer()
user.second_window()

print(user)





