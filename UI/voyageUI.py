from LogicLayer.voyageLL import VoyageLL
from Models.voyage import Voyage
from Models.voyage_Sm import VoyageSm
from UI.page import Page
from UI.employeeUI import EmployeeUI


class VoyageUI(Page):

    def __init__(self):
        self.__voyageLL = VoyageLL()
        self.__employeeUI = EmployeeUI()


    def header(self,head):
        """ prints a header on the user interface
                   :param head:
               """

        print("-" * 50)
        print("|{:^48}|".format(head))
        print("-" * 50)
        print()

    def edit_voyage_date(self):
        self.header("Edit voyage data")
        print("Enter q an any time to quit")

        isValid = True
        while isValid == True:
            try:
                voyage_int = int(input("1. edit voyage arrival\n2. edit voyage departure\nEdit number: "))
            except:
                print("-> Invalid input, please enter 1 or 2")
                continue

            else:
                isValid = False


        user_voyage_input = input("Enter voyage id: ").strip()
        if not self.__voyageLL.check_flight_number(user_voyage_input):
            print("--> Voyage does not exist")
            wantToContinue_str = input("Do you want to try again?\n(Yes) to continue, anything else to exit: ").strip().upper()
            if wantToContinue_str == "YES" or wantToContinue_str == "Y":
                self.edit_voyage_date()
            else:
                return None

        isValid = False
        while not isValid:
            print("Date time")
            user_in_date = input("Enter date  (i.e. 'mm/dd/yy hh:mm:ss'): ").strip()
            try:
                date_obj = datetime.strptime(user_in_date, '%y/%m/%d %H:%M:%S')
                isValid = True

            except KeyError:
                print("Error: please enter a valid number")
                continue

        voyage_object = self.__voyageLL.get_voyage(user_voyage_input)
        voyage_object_edit = VoyageSm(voyage_object[0], voyage_object[1], voyage_object[2], voyage_object[3],
                                       voyage_object[4], voyage_object[5], voyage_object[6], voyage_object[7],
                                       voyage_object[8], voyage_object[9], voyage_object[10])
        if voyage_int == 1:
            voyage_object_edit.set_arrival_time(date_obj)

        if voyage_int == 2:
            voyage_object_edit.set_departure_time(date_obj)


    def register_voyage_PM(self):
        """ Header """

        self.header("Register new voyage")

        again = True

        while again:

            flightNumber_str = input("Enter flight number: ")

            if self.__voyageLL.check_flight_number(flightNumber_str):
                print("\nVoyage already exists.")
                choice = input("Do you want to try again? (Y/N) ").upper()
                if choice == "Y":
                    continue
                else:
                    break

            else:
                departingFrom_str = input("Enter departure city: ").strip()
                arravingAt_str = input("Enter arrival city: ").strip()
                departure_str = input("Enter departure time: ").strip()
                arrival_str = input("Enter arrival time: ").strip()

                new_voyage = Voyage(flightNumber_str, departingFrom_str, arravingAt_str,departure_str, arrival_str)
                print("\n{}\n".format (new_voyage))
                continue_it = input("To quit enter q\nDo you want to register this voyage? (Y/N) ").upper()

                if continue_it == "Y":
                    self.__voyageLL.register_voyage_PM(new_voyage)
                    print("\nNew voyage registered!\n")
                elif continue_it == "Q":
                    break
                else:
                    print("\nVoyage not registered.\n")

                again = input("Would you like to register another voyage? (Y/N) ").upper()

                if again == "Y":
                    continue
                else:
                    break



    def cancel_voyage(self):
        """ Removes an voyage from the csv file,
            sends voyage fligt number to a function already made in voyageLL to delete specific flight Number
        """
        # væri best að setja self.header("Cancel voyage") í kall fallið svo það repeati sig ekki endalaust
        self.header("Cancel voyage")

        print("To quit press q at any time.")

        voyage = input("Enter a flight number of voyage to be canceled: ").strip()

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
        want_to_continue = input("Would you like to try again? (Y/N) ").strip().upper()
        return want_to_continue


    def man_voyage_SM(self):

        again = True
        while again:
            flightNumber = input("Enter a flight number: ")
            voyage = self.__voyageLL.get_voyage(flightNumber)

            if voyage == False:
                print("No voyage with this flight number.")
                continue

            busy_date = voyage[3]
            busy_date = busy_date.split("T")
            date = busy_date[0]
            print(date)

            while True:
                captain = input("Enter Captain SSN: ")
                if self.__voyageLL.check_if_busy(date, captain):
                    print("Employee is busy at this date.")
                    continue
                else:
                    break
            while True:
                copilot = input("Enter copilot SSN: ")
                if self.__voyageLL.check_if_busy(date, copilot):
                    print("Employee is busy at this date.")
                    continue
                else:
                    break
            while True:
                fsm = input("Enter flight service manager SSN: ")
                if self.__voyageLL.check_if_busy(date, fsm):
                    print("Employee is busy at this date.")
                    continue
                else:
                    break
            while True:
                fa1 = input("Enter first flight attendant SSN: ")
                if self.__voyageLL.check_if_busy(date, fa1):
                    print("Employee is busy at this date.")
                    continue
                else:
                    break
            while True:
                fa2 = input("Enter second flight attendant SSN: ")
                if self.__voyageLL.check_if_busy(date, fa2):
                    print("Employee is busy at this date.")
                    continue
                else:
                    break
            planeInsignia = input("Enter plane insignia: ")


            voyage_added_staff = VoyageSm(voyage[0], voyage[1],voyage[2], voyage[3], voyage[4], captain, copilot, fsm,fa1,fa2,planeInsignia)

            self.__voyageLL.cancel_voyage(flightNumber)
            self.__voyageLL.register_voyage_PM2(voyage_added_staff)
            print("Voyage successfully manned!")
            choice = input("Do you want to man another voyage? (Y/N) ").upper()
            if choice == "Y":
                continue
            else:
                break


    def list_voyage_day(self):

        date = self.__employeeUI.get_date()

        voyage = self.__voyageLL.list_voyages_day(date)

        if voyage != False:
            print("\n{:<5}{:>8}{:>6}{:>10}{:>19}{:>12}{:>16}{:>16}{:>18}".format("Flight", "From", "To", "Cpt.","Copilot", "FSM", "FA1", "FA2","Plane"))
            for x in range(len(voyage)):
                if x == 3 or x == 4:
                    pass
                else:
                    print(voyage[x], end="\t  ")

            if len(voyage) == 11:
                print("\n\nVoyage is fully staffed on {}".format(date))
            else:
                print("\n\nVoyage is not fully staffed on {}".format(date))
        else:
            print("Date isn't in system.")


    def print_all_voyages(self):
        self.header("All voyages")
        voyages = self.__voyageLL.get_all_upcoming_voyages()

        print("\t{:>5}{:>7}{:>4}{:>13}{:>20}{:>19}{:>16}{:>9}{:>13}{:>13}{:>15}\n".format("Flight", "From", "To","Departure","Arrival", "Cpt.", "Copilot", "FSM", "FA1", "FA2", "Plane"))
        for index, x in enumerate(voyages):
            print("{}.\t{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}".format(index+1, x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10]))



    def print_list_voyage_by_week(self):
        self.header("Voyage by week")
        week_dict = self.__voyageLL.list_voyages_week()
        print(week_dict)




if __name__ == "__main__":
    a = VoyageUI()
    a.man_voyage_SM()

