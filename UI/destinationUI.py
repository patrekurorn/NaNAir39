
import os
import string
from LogicLayer.destinationsLL import DestinationsLL
from Models.destination import Destination

ID = 0
DESTINATION = 1
COUNTRY = 2
FLIGHTDURATION = 3
DISTANCEFROMICELAND = 4
CONTACTNAME = 5
CONTACTNUMBER = 6

class DestinationUI:

    def __init__(self):
        self.__destinationLL = DestinationsLL()

    def header(self):
        """ prints a header on the user interface """

        print("-" * 50)
        print("|{:^48}|".format(head))
        print("-" * 50)
        print()


    def register_destination(self):

        # setja header

        print("Registering a new destination")
        id = input("Enter a destination ID: ")
        if self.__destinationLL.check_destination(id):
            print("Destination already exists.")
        else:
            country = input("Enter a country: ")
            airport = input("Enter an airport: ")
            flightDuration = input("Enter flight duration: ")
            distanceFromIceland = input("Enter the distance from Iceland: ")
            contactName = input("Enter contact's name: ")
            contactNumber = input("Enter contact's number: ")

            new_destination = Destination(id, country, airport, flightDuration, distanceFromIceland, contactName, contactNumber)
            print("\n{}\n".format(new_destination))

            if input("Do you want to register this destination? ").upper() == "Y":
                self.__destinationLL.register_destination(new_destination)
                print("\nDestination registered!\n")
            else:
                print("\nNo destination registered.\n")
        
    def edit_destination(self):
        destinationsList = self.__destinationLL.get_all_destinations()
        destinationsListLen = len(destinationsList)
                       
        print("   {:<5}{:<17}{:<15}{:<10}{:<12}{:<30}{:<17}".format("Id", "Destinations", "Country", "Durations", "Distance", "Contact name", "Contact number"))
        print()
        for i in range(0, destinationsListLen):
            print("{}. {:<5}{:<17}{:<15}{:<10}{:<12}{:<30}{:<17}".format(i+1, destinationsList[i][ID], destinationsList[i][DESTINATION], destinationsList[i][COUNTRY], destinationsList[i][FLIGHTDURATION], destinationsList[i][DISTANCEFROMICELAND], destinationsList[i][CONTACTNAME], destinationsList[i][CONTACTNUMBER]))

        print()

        #Get the number of what destination to edit
        editDestinationChoice_int = input("Enter the number of the destination you want to edit: ")
        isInt = False
        while isInt != True:
            try:
                editDestinationChoice_int = int(editDestinationChoice_int)
                if editDestinationChoice_int >= 1 and editDestinationChoice_int <= destinationsListLen: 
                    isInt = True
                else:
                    print("Enter a valid Number between 1-{}".format(destinationsListLen))
                    editDestinationChoice_int = input("Enter the number of the destination you want to edit: ")
            except ValueError:
                print("Enter a valid Number between 1-{}".format(destinationsListLen))
                editDestinationChoice_int = input("Enter the number of the destination you want to edit: ")

        
        
    



if __name__ == "__main__":
    a = DestinationUI()
    #a.register_destination()
    a.edit_destination()