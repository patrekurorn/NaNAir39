from LogicLayer.voyageLL import VoyageLL
from Models.voyage import Voyage
from Models.voyage_Sm import VoyageSm
from UI.page import Page
from UI.employeeUI import EmployeeUI
from datetime import datetime


# Need "list of unmanned voyages" for improved "man voyage"

class VoyageUI(Page):

    def __init__(self):
        self.__voyageLL = VoyageLL()
        self.__employeeUI = EmployeeUI()
        super().__init__()

        super().__init__()


    def header(self,head):
        """ prints a header on the user interface
                   :param head:
               """

        print("-" * 62)
        print("|{:^60}|".format(head))
        print("-" * 62)
        print()

    def edit_voyage_input(self):

        isValid = True
        while isValid == True:
            editNumber = input("1. edit voyage arrival\n2. edit voyage departure\nEnter number: ").strip()
            if editNumber == "q" or editNumber == "1" or editNumber == "2":
                isValid = False
            else:
                print("Error: please enter a valid number")
                continue
        return editNumber

    def edit_voyage_secondInput(self):
        isvalid = True
        while isvalid:
            voyageName = input("Enter voyage id: ").strip()
            if voyageName !="q":
                if not self.__voyageLL.check_flight_number(voyageName):
                    print("Error: Voyage does not exist")
                    continue
                else:
                    isvalid = False
            else:
                isvalid = False

        return voyageName


    def edit_voyage_date(self):

        self.voyage_screen_header("Edit voyage date")
        print("Enter q an any time to quit")

        editNumber = self.edit_voyage_input()
        if editNumber == "q":
            return True

        voyageName= self.edit_voyage_secondInput()
        if voyageName == "q":
            return True

        isValid = False
        while not isValid:
            user_in_date = input("Enter date,time (i.e. 'mm/dd/yy,hh:mm:ss'): ").strip()
            try:
                date_obj = datetime.strptime(user_in_date, '%y/%m/%d,%H:%M:%S')
                isValid = True

            except KeyError:
                print("Error: please enter a valid number")
                continue

        dateformat_str = str(date_obj)
        date,time = dateformat_str.split()

        voyage_object = self.__voyageLL.get_voyage(voyageName)
        selectedVoyageData = VoyageSm(voyage_object[0], voyage_object[1], voyage_object[2], voyage_object[3],
                                       voyage_object[4], voyage_object[5], voyage_object[6], voyage_object[7],
                                       voyage_object[8], voyage_object[9], voyage_object[10])

        self.__voyageLL.edit_voyage(voyageName,date,time,selectedVoyageData,editNumber)
        self.voyage_screen_header("Edit voyage date")

        print()
        print ("Voyage {} has been changed to:\n{}".format(voyageName,selectedVoyageData))
        print()
        again = input("Would you like to edit another voyage? (Yes) to continue \nAnything else to exit: ").upper()

        if again == "YES" or again == "Y":
            self.edit_voyage_date()

        else:
            return True

    def voyage_screen_header(self,headerString):

        pageWidth = 136
        self._header(headerString, pageWidth)
        all_voyages = self.__voyageLL.get_all_upcoming_voyages()

        employeeHeader = "|{:<8} {:>3} {:>3} {:>12} {:>19} {:>17} {:>16} {:>8} {:>12} {:>12} {:>14} |\n".format(
            "Flight", "From", "To", "Departure", "Arrival", "Cpt", "Copilot", "FSM", "FA1", "FA2",
            "Plane") + "| " + "-" * (pageWidth - 2) + " |"
        print(employeeHeader)


        for x in all_voyages:
            try:
                print("|{:<8} {:<5} {:<5} {:<4} {:>21} {:>12} {:>12} {:>12} {:>12} {:>12} {:>8}|".format(x[0], x[1], x[2],
                                                                                                     x[3], x[4], x[5],
                                                                                                     x[6], x[7], x[8], x[9],
                                                                                                     x[10]))
            except:
                print("|{:<8} {:<5} {:<5} {:<4} {:>21} {:>12} {:>12} {:>12} {:>12} {:>12} {:>8}|".format(x[0], x[1], x[2],
                                                                                                     x[3], x[4], "",
                                                                                                     "", "", "", "",
                                                                                                     ""))

        self._footer(pageWidth, None)
        return None

    def register_voyage_PM(self):
        self.voyage_screen_header("Register voyage")

        again = True
        while again:
            flightNumber_str = input("Enter flight number: ").upper()

            if self.__voyageLL.check_flight_number(flightNumber_str):
                print("\nVoyage already exists.")
                choice = input('"Yes" to continue (anything else) to exit\n Do you want to try again? ').upper()
                if choice == "YES":
                    continue
                else:
                    break

            else:
                departingFromStr = input("Enter departure city: ").strip().upper()
                arravingAtStr    = input("Enter arrival city: ").strip().upper()
                departueDateStr  = input("Enter departure date (i.e YEAR-MM-DD): ").strip()
                departureTimeStr = input("Enter departure time (i.e HH:MM:SS): ").strip()
                arrivalDateStr   = input("Enter arrival date date (i.e YEAR-MM-DD): ").strip()
                arrivalTimeStr   = input("Enter arrival time (i.e HH:MM:SS): ").strip()

                new_voyage = Voyage(flightNumber_str, departingFromStr, arravingAtStr, departueDateStr+"T"+departureTimeStr, arrivalDateStr+"T"+arrivalTimeStr)
                #print("\n{}\n".format (new_voyage))
                continue_it = input('To quit enter "q"\n "Yes" to register, (anyting else to cancel)\nDo you want to register this voyage? ').upper()
                if continue_it == "Q":
                    break
                elif continue_it == "YES":
                    self.__voyageLL.register_voyage_PM(new_voyage)
                    self.voyage_screen_header("Register voyage")
                    print("\nNew voyage registered!\n")
                    if input("(Yes) to continue, anything else to exit\nWould you like to register another voyage? ").upper() != "YES":
                        break
                    else:
                        continue

                else:
                    print("\nVoyage not registered.\n")
                    again = input("(Yes) to continue, anything else to exit\nWould you like to register another voyage? ").upper()

                    if again == "YES":
                        continue

                    else:
                        break


    def cancel_voyage(self):
        """ Removes an voyage from the csv file,
            sends voyage fligt number to a function already made in voyageLL to delete specific flight Number
        """
        self.voyage_screen_header("Cancel voyage")
        print("To quit press q at any time.")
        voyage = input("Enter a flight number of voyage to be canceled: ").strip()

        if voyage!= "q":
            if not self.__voyageLL.check_flight_number(voyage):
                print("Error: voyage: {} was not found.".format(voyage))

                continue_process = self.continue_it()
                if continue_process == "YES":
                    self.cancel_voyage()

                else:
                    return True

            else:
                self.__voyageLL.cancel_voyage(voyage)
                self.voyage_screen_header("Cancel voyage")
                print("Voyage: {} has been canceled.".format(voyage))

                continue_process = self.continue_it()
                if continue_process != "YES":
                    return True

                else:
                    self.cancel_voyage()
        else:
            return True


    def try_again(self):
        wantToTryStr = input("Would you like to try again?\n(Yes) to continue\nAnything else to exit: ").strip().upper()
        return wantToTryStr

    def continue_it(self):
        wantToContinue = input("Would you like to continue?\n(Yes) to continue\nAnything else to exit: ").strip().upper()
        return wantToContinue


    def man_voyage_SM(self):

        again = True
        while again:
            flightNumber = input("Enter a flight number: ")
            voyage = self.__voyageLL.get_voyage(flightNumber)

            if voyage == False:
                print("No voyage with this flight number.")
                break

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

        while voyage != None:
            print("\n{:<5}{:>8}{:>6}{:>10}{:>19}{:>12}{:>16}{:>16}{:>18}".format("Flight", "From", "To", "Cpt.","Copilot", "FSM", "FA1", "FA2","Plane"))
            for x in range(len(voyage)):
                if x == 3 or x == 4:
                    pass
                else:
                    print(voyage[x], end="\t  ")

            if len(voyage) == 11:
                print("\n\nVoyage is fully staffed on {}".format(date))
                choice = input("Do you want to continue? (Y/N) ").upper()
                if choice == "Y":
                    self.list_voyage_day()
                else:
                    break
            else:
                print("\n\nVoyage is not fully staffed on {}".format(date))
                choice = input("Do you want to continue? (Y/N) ").upper()
                if choice == "Y":
                    self.list_voyage_day()
                else:
                    break

        if voyage == None:
            print("Date isn't in system.")
            input()
            return True




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
    a.print_all_voyages()

