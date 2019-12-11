from LogicLayer.voyageLL import VoyageLL
from Models.voyage import Voyage
from Models.voyage_Sm import VoyageSm
from NaNAir39.UI.page import Page
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
        self.header("Plan manager: register voyage")

        print("Registering a new voyage\n")
        flightNumber_int = input("Enter flight number: ")
        if self.__voyageLL.check_flight_number(flightNumber_int):
            print("\nVoyage already exists.")
        else:
            departingFrom_str = input("Enter departure city: ").strip()
            arravingAt_str = input("Enter arrival city: ").strip()
            departure_str = input("Enter departure time: ").strip()
            arrival_str = input("Enter arrival time: ").strip()

            new_voyage = Voyage(flightNumber_int, departingFrom_str, arravingAt_str,departure_str, arrival_str)
            print("\n{}\n".format (new_voyage))

            if input("Do you want to register this voyage? ").upper() == "Y":
                self.__voyageLL.register_voyage_PM(new_voyage)
                print("\nNew voyage registered!\n")
            else:
                print("\nVoyage not registered.\n")


    def cancel_voyage(self):
        """ Removes an voyage from the csv file,
            sends voyage fligt number to a function already made in voyageLL to delete specific flight Number
        """
        # væri best að setja self.header("Cancel voyage") í kall fallið svo það repeati sig ekki endalaust
        self.header("Cancel voyage")
        print("To quit press q at any time.")

        voyage = input("Enter a flight number of voyage to be canceled:").upper().strip()

        if voyage!= "Q":
            if not self.__voyageLL.check_flight_number(voyage.upper()):
                print("--> Voyage: {} was not found.".format(voyage))
                continue_process = self.continue_it()

                if continue_process == "Y" or continue_process == "YES":
                    self.cancel_voyage()
                else:
                    return None

            else:
                self.__voyageLL.cancel_voyage(voyage)
                print("Voyage: {} has been canceled.".format(voyage))
        else:
            return None


    def continue_it(self):
        want_to_continue = input("Would you like to try again? ").strip().upper()
        return want_to_continue


    def man_voyage_SM(self):
        """ checkar líka á villumeldingum """
        """ Header """
        self.header("Shift manager: register voyage")

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

    def print_list_voyage_by_day(self):
        self.header("Voyage by day ")
        dayDict = self.__voyageLL.list_voyages_day()

        for key,value in dayDict.items():
            print("{}: {}".format(key,value))

    def print_list_voyage_by_week(self):
        self.header("Voyage by week")
        week_dict = self.__voyageLL.list_voyages_week()
        print(week_dict)


if __name__ == "__main__":
    a = VoyageUI()
    a.header("Voyage")
    #a.man_voyage_SM()
    a.print_list_voyage_by_day()
    a.print_list_voyage_by_week()
