
import os
import string
from LogicLayer.destinationsLL import DestinationsLL
from Models.destination import Destination

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

if __name__ == "__main__":
    a = DestinationUI()
    a.register_destination()

