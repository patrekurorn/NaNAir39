from LogicLayer.voyageLL import VoyageLL
from Models.voyage import Voyage

class VoyageUI:

    def __init__(self):
        self.__voyageLL = VoyageLL()

    def header(self):
        pass


    def register_voyage(self):

        # setja header

        print("Registering a new voyage\n")
        flightNumber = input("Enter flight number: ")
        if self.__voyageLL.check_flight_number(flightNumber):
            print("\nVoyage already exists.")
        else:
            departingFrom = input("Enter departure city: ")
            arravingAt = input("Enter arrival city: ")
            departure = input("Enter departure time: ")
            arrival = input("Enter arrival time: ")

            new_voyage = Voyage(flightNumber, departingFrom, arravingAt, departure, arrival)
            print("\n{}\n".format(new_voyage))

            if input("Do you want to register this voyage? ").upper() == "Y":
                self.__voyageLL.register_voyage(new_voyage)
                print("\nNew voyage registered!\n")
            else:
                print("\nVoyage not registered.\n")


if __name__ == "__main__":
    a = VoyageUI()
    a.register_voyage()