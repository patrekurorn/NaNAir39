from LogicLayer.voyageLL import VoyageLL
from Models.voyage import Voyage
from Models.voyage_Sm import VoyageSm

from UI.page import Page
from LogicLayer import voyageLL
import os

class VoyageUI(Page):

    def __init__(self):
        self.__voyageLL = VoyageLL()

    def header(self,head):
        """ prints a header on the user interface
                   :param head:
               """

        print("-" * 50)
        print("|{:^48}|".format(head))
        print("-" * 50)
        print()


    def register_voyage_PM(self):
        """ Header """
        again = True

        self.header("Register new voyage")
        flightNumber_str = input("Enter flight number: ")

        while again == True:

            if self.__voyageLL.check_flight_number(flightNumber_str):
                print("\nVoyage already exists.")

            else:
                departingFrom_str = input("Enter departure city: ").strip()
                arravingAt_str = input("Enter arrival city: ").strip()
                departure_str = input("Enter departure time: ").strip()
                arrival_str = input("Enter arrival time: ").strip()

                new_voyage = Voyage(flightNumber_str, departingFrom_str, arravingAt_str,departure_str, arrival_str)
                print("\n{}\n".format (new_voyage))
                continue_it = input("Do quit enter q\nDo you want to register this voyage? ")

                if continue_it.upper() == "Y" or continue_it.upper() == "YES":
                    self.__voyageLL.register_voyage_PM(new_voyage)
                    print("\nNew voyage registered!\n")
                elif continue_it =="q":
                    return True
                else:
                    print("\nVoyage not registered.\n")
                again = input("Would you like to register another voyage? Yes/No").lower()

                if again != "yes" or again != "y":
                    return True





    def cancel_voyage(self):
        """ Removes an voyage from the csv file,
            sends voyage fligt number to a function already made in voyageLL to delete specific flight Number
        """
        # væri best að setja self.header("Cancel voyage") í kall fallið svo það repeati sig ekki endalaust
        self.header("Cancel voyage")

        print("To quit press q at any time.")

        voyage = input("Enter a flight number of voyage to be canceled:").strip()

        if voyage!= "q":
            if not self.__voyageLL.check_flight_number(voyage):
                print("--> Voyage: {} was not found.".format(voyage))

                continue_process = self.continue_it()

                if continue_process.upper() == "Y" or continue_process.upper() == "YES":
                    self.cancel_voyage()
                else:
                    return True

            else:
                self.__voyageLL.cancel_voyage(voyage)
                print("Voyage: {} has been canceled.".format(voyage))

                continue_process = self.continue_it()
                if continue_process != "YES" or continue_process != "Y":
                    return True
                else:
                    self.cancel_voyage()

        else:
            return True


    def continue_it(self):
        want_to_continue = input("Would you like to try again? ").strip().upper()
        return want_to_continue

    def man_voyage_SM(self):
        """ checkar líka á villumeldingum """
        """ Header """
        self.header("Staff manager: register voyage")

        fligtNumber_int = input("Enter flight number: ").strip()

        if not self.__voyageLL.check_flight_number(fligtNumber_int):
            print("Voyage does not exist ")
            want_2_continue = self.continue_it()
            if want_2_continue == "YES" or want_2_continue == "Y":
                self.man_voyage_SM()
            return None

        """ my_list """
        copilot = input("Enter copilot ID: ")
        captain = input("Enter Captain ID: ")
        fsm = input("Enter flight service manager ID: ")
        fa1 = input("Enter first flight attendant ID: ")
        fa2 = input("Enter second flight attendant ID: ")
        """ end of my_list"""

        try:
            int(copilot),int(captain),int(fsm),int(fa1),int(fa2)

        except:
            print("Invalid: please enter valid numbers")
            want_2_continue = self.continue_it()

            if want_2_continue == "Yes" or "Y":
                self.man_voyage_SM()
            else:
                return None

        add_to_voyage = copilot,captain,fsm,fa1,fa2
        print("\n{}\n".format(add_to_voyage))

        register = input("Do you want to register this voyage? ").upper()
        if register == "Y" or  register == "YES":

            self.__voyageLL.register_voyage_SM(add_to_voyage)
            print("\nNew voyage registered!\n")
        else:
            print("\nVoyage not registered.\n")

<<<<<<< HEAD
    def print_all_voyages(self):
        self.header("All voyages")
        allDict = self.__voyageLL.get_all_upcoming_voyages()
        
        for index,v in enumerate(allDict):
            print("{},{}".format(index,v))
        
=======

>>>>>>> 35d2a9ef03da4339d61d038040247f145acc3bce

    def print_list_voyage_by_day(self):
        self.header("Voyage by day")
        dayDict = self.__voyageLL.list_voyages_day()

        for key,value in dayDict.items():
            print("{}: {}".format(key,value))

    def print_list_voyage_by_week(self):
        self.header("Voyage by week")
        week_dict = self.__voyageLL.list_voyages_week()
        print(week_dict)


if __name__ == "__main__":
    a = VoyageUI()

