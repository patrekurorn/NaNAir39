
import os
import string
from LogicLayer.destinationsLL import DestinationsLL
from Models.destination import Destination
from NaNAir39.UI.page import Page


class DestinationUI(Page):
    """
    ID = 0
    DESTINATION = 1
    COUNTRY = 2
    FLIGHTDURATION = 3
    DISTANCEFROMICELAND = 4
    CONTACTNAME = 5
    CONTACTNUMBER = 6
    """


    def __init__(self):
        self.__destinationLL = DestinationsLL()

    def header(self):
        """ prints a header on the user interface
            :param head:
        """

        print("-" * 50)
        print("|{:^48}|".format(head))
        print("-" * 50)
        print()


    def register_destination(self):
        self.header()
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
        ID = 0
        DESTINATION = 1
        COUNTRY = 2
        FLIGHTDURATION = 3
        DISTANCEFROMICELAND = 4
        CONTACTNAME = 5
        CONTACTNUMBER = 6

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
        destinationPosInList = editDestinationChoice_int-1

        theDestination = destinationsList[destinationPosInList]

        newId_str = theDestination[ID]
        newDestination_str = theDestination[DESTINATION]
        newCountry_str = theDestination[COUNTRY]
        newFlightDuration_str = theDestination[FLIGHTDURATION]
        newDistanceFromIceland_str = theDestination[DISTANCEFROMICELAND]
        newContactName_str = theDestination[CONTACTNAME]
        newContactNumber_str = theDestination[CONTACTNUMBER]

        updateDestinationDone = False
        while updateDestinationDone != True:

            action = False
            while action != True:
                print("\n1. {:<27}{}".format("Id:", newId_str))
                print("2. {:<27}{}".format("Destination:", newDestination_str))
                print("3. {:<27}{}".format("Country:", newCountry_str))
                print("4. {:<27}{}".format("Flight duration:", newFlightDuration_str))
                print("5. {:<27}{}".format("Distance from Iceland:", newDistanceFromIceland_str))
                print("6. {:<27}{}".format("Contact name:", newContactName_str))
                print("7. {:<27}{}".format("Contact number:", newContactNumber_str))

                action = input(("\nEnter q to quit and submit.\nChoose what you want to edit (1-7): ")).lower()

                if action == "q":
                    self.__destinationLL.remove_destination(theDestination[ID])

                    updatedDestination = Destination(newId_str,newDestination_str,newCountry_str,newFlightDuration_str,newDistanceFromIceland_str,newContactName_str,newContactNumber_str)
                    self.__destinationLL.register_destination(updatedDestination)
                    return

                elif action == "1":
                    newId_str = input("Enter a new id: ")
                    print("Id changed to {}".format(newId_str))

                elif action == "2":
                    newDestination_str = input("Enter a new destination: ")
                    print("Destination changed to {}".format(newDestination_str))

                elif action == "3":
                    newCountry_str = input("Enter a new country: ")
                    print("Country changed to {}".format(newCountry_str))

                elif action == "4":
                    newFlightDuration_str = input("Enter a new flight duration: ")
                    print("Flight duration changed to {}".format(newFlightDuration_str))

                elif action == "5":
                    newDistanceFromIceland_str = input("Enter a new distance from Iceland: ")
                    print("Distance from Iceland changed to {}".format(newDistanceFromIceland_str))

                elif action == "6":
                    newContactName_str = input("Enter a new contact name: ")
                    print("Contact name changed to {}".format(newContactName_str))

                elif action == "7":
                    newContactNumber_str = input("Enter a new contact number: ")
                    print("Contact number changed to {}".format(newContactNumber_str))

                else:
                    pass

if __name__ == "__main__":
    a = DestinationUI()
    #a.register_destination()
    a.edit_destination()
