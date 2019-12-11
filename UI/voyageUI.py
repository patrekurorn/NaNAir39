from LogicLayer.voyageLL import VoyageLL
from Models.voyage import Voyage
from Models.voyage_Sm import VoyageSm
from NaNAir39.UI.page import Page

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

    def register_voyage(self):  # Planning manager
        pass




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

    # def cancel_voyage(self, flightNumber):
    #     """ Removes an voyage from the csv file, by deleting all employees and all the employees baack withou the 
    #         specific employee that is given by us in paramter
    #     """
    #     self.header(#Cancel voyage)

    #     voyage = input("Please enter a flight number of voyage to be canceled ")


    #     with open("./..UpcomingFlightsPM.csv")



    # def continue_it(self):
    #     want_to_continue = input("Would you like to try again? ").strip().upper()
    #     return want_to_continue


    def register_voyage_SM(self):
        """ checkar líka á villumeldingum """
        """ Header """
        self.header("Shift manager: register voyage")

        fligtNumber_int = input("Enter flight number: ").strip()

        if not self.__voyageLL.check_flight_number(fligtNumber_int):
            print("Voyage does not exist ")
            want_2_continue = self.continue_it()
            if want_2_continue == "YES" or want_2_continue == "Y":
                self.register_voyage_SM()
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
                self.register_voyage_SM()
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


if __name__ == "__main__":
    a = VoyageUI()
    a.header("Voyage")
    a.register_voyage_SM()

