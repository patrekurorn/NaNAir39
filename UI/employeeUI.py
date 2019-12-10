
from LogicLayer.employeeLL import EmployeeLL
from Models.employee import Employee
from LogicLayer.voyageLL import VoyageLL
import datetime
import dateutil.parser

class EmployeeUI:

    def __init__(self):
        self.__employee_LL = EmployeeLL()
        self.__voyage_LL = VoyageLL()


    def header(self, i):

        print("-" * 50)
        print("|{:^48}|".format(i))
        print("-" * 50)
        print()


    def get_all_employees(self):
        """ Lists information about all employees. """

        self.header("All employees")

        all_employees = self.__employee_LL.get_all_employees()

        employees = ""
        for index, row in enumerate(all_employees):
            for x in row:
                employees += (x + ", ")
            print("{}. {}".format(index+1, employees))
            employees = ""


    def get_employee(self):
        """ Lists information about a specific employee. """

        self.header("Employee information")

        isValid = False
        while isValid == False:
            ssn = input("\nEnter q to quit.\nEnter a social security number: ")
            if ssn == "q":
                break
            try:
                employee = self.__employee_LL.get_employee(ssn)

                print("\nSSN: \t\t\t{}\nName: \t\t\t{}\nPosition: \t\t{}\nRank: \t\t\t{}\nLicence: \t\t{}\nAddress: \t\t{}\nMobile: \t\t{}\nLandline nr: \t{}\nEmail: \t\t\t{}".format(employee[0],employee[1],
                                                                                                                                             employee[2],employee[3],
                                                                                                                                             employee[4],employee[5],
                                                                                                                                             employee[6],employee[7],
                                                                                                                                             employee[8]))

            except:
                print("\nSocial security number not in system.")



    def register_employee(self):
        """ Registers a new employee and adds him to the employee.csv file. """

        self.header("Register new employee")

        isValid = False
        while isValid == False:
            ssn = input("Enter a social security number: ")
            if self.__employee_LL.ssn_valid(ssn):
                print("\nEmployee already exists.\n")
                choice = input("Y: Yes\nAnything else: No\nDo you want to continue? ").upper()
                if choice == "Y":
                    continue
                else:
                    break
            else:
                new_ssn = ssn
                name = input("Enter name: ")
                position = input("Enter position: ")
                rank = input("Enter rank: ")
                licence = input("Enter licence: ")
                address = input("Enter address: ")
                mobile = input("Enter mobile: ")
                landlineNr = input("Enter landline number: ")
                email = input("Enter email: ")

                new_employee = Employee(new_ssn, name, position, rank, licence, address, mobile, landlineNr, email)
                print("\n{}\n".format(new_employee))

                choice = input("Y: Yes\nAnything else: No\nDo you want to create this employee? ").upper()
                if choice == "Y":
                    self.__employee_LL.register_employee(new_employee)
                    print("\nEmployee created!\n")

                    choice = input("Y: Yes\nAnything else: No\nDo you want to register another employee? ").upper()
                    if choice == "Y":
                        continue
                    else:
                        break
                else:
                    print("\nNo employee created.\n")
                    choice = input("Y: Yes\nAnything else: No\nDo you want to continue? ").upper()
                    if choice == "Y":
                        continue
                    else:
                        break


    def edit_employee(self):
        """ Edits information for a specific employee. SSN can not be edited. """

        self.header("Edit employee")

        self.get_all_employees()

        editing_employee = True
        while editing_employee:
            action = ""

            ssn_edit = input("\nEnter q to quit.\nEnter the ssn of the employee you want to edit: ")
            if ssn_edit == "q":
                break

            if self.__employee_LL.ssn_valid(ssn_edit):
                employee = self.__employee_LL.get_employee(ssn_edit)
                employee_edit = Employee(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5],employee[6],employee[7],employee[8])

                print(self.__employee_LL.print_employee(ssn_edit))

                while action != "q":
                    action = input(("\nEnter q to quit.\nChoose what you want to edit (1-8): "))

                    if action == "1":
                        name = input("Enter new name: ")
                        employee_edit.set_name(name)
                        print("Name changed to {}".format(name))

                    elif action == "2":
                        print("\n1. Pilot\n2. Cabincrew\n")

                        isValid = False
                        while isValid == False:
                            choice = input("Enter 1 or 2: ")
                            try:
                                choice = int(choice)
                                if choice == 1:
                                    employee_edit.set_position("Pilot")
                                    print("Position changed to pilot.")
                                    isValid = True
                                elif choice == 2:
                                    employee_edit.set_position("Cabincrew")
                                    print("Position changed to cabincrew.")
                                    isValid = True
                                else:
                                    isValid = False
                            except ValueError:
                                continue

                    elif action == "3":
                        if employee[2] == "Pilot":
                            print("\n1. Captain\n2. Copilot\n")
                            isValid = False

                            while isValid == False:
                                choice = input("Enter 1 or 2: ")
                                try:
                                    choice = int(choice)
                                    if choice == 1:
                                        employee_edit.set_rank("Captain")
                                        print("Rank changed to captain.")
                                        isValid = True
                                    elif choice == 2:
                                        employee_edit.set_rank("Copilot")
                                        print("Rank changed to copilot")
                                        isValid = True
                                    else:
                                        isValid = False
                                except ValueError:
                                    continue

                        elif employee[2] == "Cabincrew":
                            print("\n1. Flight Service Manager\n2. Flight Attendant\n")
                            isValid = False

                            while isValid == False:
                                choice = input("Enter 1 or 2: ")
                                try:
                                    choice = int(choice)
                                    if choice == 1:
                                        employee_edit.set_rank("Flight Service Manager")
                                        print("Rank changed to Flight Service Manager.")
                                        isValid = True
                                    elif choice == 2:
                                        employee_edit.set_rank("Flight Attendant")
                                        print("Rank changed to Flight Attendant")
                                        isValid = True
                                    else:
                                        isValid = False
                                except ValueError:
                                    continue

                    elif action == "4":
                        if employee[2] == "Pilot":
                            print("\n1. NABAE146\n2. NAFokkerF28\n3. NAFokker100\n")
                            isValid = False

                            while isValid == False:
                                choice = input("Enter 1, 2 or 3: ")
                                try:
                                    choice = int(choice)
                                    if choice == 1:
                                        employee_edit.set_licence("NABAE146")
                                        print("Licence changed to NABAE146.")
                                        isValid = True
                                    elif choice == 2:
                                        employee_edit.set_licence("NAFokkerF28")
                                        print("Licence changed to NAFokkerF28.")
                                        isValid = True
                                    elif choice == 3:
                                        employee_edit.set_licence("NAFokker100")
                                        print("Licence changed to NAFokker100.")
                                        isValid = True
                                    else:
                                        isValid = False
                                except ValueError:
                                    continue
                        else:
                            print("Licence can only be changed if employee is a pilot.")
                            continue

                    elif action == "5":
                        address = input("Enter new address: ")
                        employee_edit.set_address(address)
                        print("Address changed to {}".format(choice))

                    elif action == "6":
                        mobile = input("Enter new mobile: ")
                        employee_edit.set_mobile(mobile)
                        print("Mobile changed to {}".format(mobile))

                    elif action == "7":
                        landlineNr = input("Enter new landline nr.: ")
                        employee_edit.set_landlineNr(landlineNr)
                        print("Landline nr. changed to {}".format(landlineNr))

                    elif action == "8":
                        email = input("Enter new email: ")
                        employee_edit.set_email(email)
                        print("Email changed to {}".format(email))

                self.__employee_LL.remove_employee(ssn_edit)
                self.__employee_LL.register_employee(employee_edit)
                print("\nEmployee successfully edited!")
                break

            else:
                print("\nEmployee not in system.")


    def get_date(self):
        """ Returns a date in ISO format. """

        isValid = False
        while isValid == False:
            print("Enter q anytime to quit.")
            year = input("Enter a year: ").lower()
            if year == "q":
                break
            month = input("Enter a month: ").lower()
            if month == "q":
                break
            day = input("Enter a day: ").lower()
            if day == "q":
                break
            hour = input("Enter an hour: ").lower()
            if hour == "q":
                break
            minute = input("Enter a minute: ").lower()
            if minute == "q":
                break
            second = 0

            try:
                year = int(year)
                month = int(month)
                day = int(day)
                hour = int(hour)
                minute = int(minute)

                date = datetime.datetime(year,month,day,hour,minute,second).isoformat()
                return date

            except ValueError:
                print("\nPlease enter a valid number for each attribute.\n")
        return None


    def available_employees(self):
        pass

    def available_pilots(self):
        pass

    def available_flight_attendants(self):
        pass


    def busy_employees(self):
        """ Lists information about all employees who are busy at the given date/time and the
            destination they are going to. """

        self.header("All busy employees")
        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            voyage = self.__voyage_LL.get_all_upcoming_voyages()

            for x in voyage:
                if x[3] == date or x[4] == date:
                    employees = x[5:]
                    destination = x[2]

            print()
            header = "\n{:<5} {:>10} {:>23} {:>15}\n".format("SSN", "Name", "Position", "Rank")
            print(header)

            for i in employees:
                employee = self.__employee_LL.get_employee(i)

                print("{:<5}\t{:<17}\t{:<17}\t{:<15}".format(employee[0], employee[1], employee[2], employee[3]))

            print("\nDestination:\t\t{}".format(destination))
            if input("\nY: Yes\nAnything else: No\nWould you like to enter another date? ").upper() == "Y":
                isValid = False
            else:
                break


    def busy_pilots(self):
        """ Lists information about all pilots who are busy at the given date/time and the
            destination they are going to. """

        self.header("All busy pilots")
        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            voyage = self.__voyage_LL.get_all_upcoming_voyages()

            for x in voyage:
                if x[3] == date or x[4] == date:
                    pilots = x[5:7]
                    destination = x[2]

            print()
            header = "\n{:<5} {:>10} {:>19}\n".format("SSN", "Name", "Rank")
            print(header)

            for i in pilots:
                employee = self.__employee_LL.get_employee(i)

                print("{:<5}\t{:<17}\t{:<15}".format(employee[0], employee[1], employee[3]))

            print("\nDestination:\t\t{}".format(destination))
            if input("\nY: Yes\nAnything else: No\nWould you like to enter another date? ").upper() == "Y":
                isValid = False
            else:
                break

    def busy_flight_attendants(self):
        """ Lists information about all flight attendants who are busy at the given date/time and the
            destination they are going to. """

        self.header("All busy flight attendants")
        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            voyage = self.__voyage_LL.get_all_upcoming_voyages()

            for x in voyage:
                if x[3] == date or x[4] == date:
                    flight_attendants = x[7:]
                    destination = x[2]

            print()
            header = "\n{:<5} {:>10} {:>19}\n".format("SSN", "Name", "Rank")
            print(header)

            for i in flight_attendants:
                employee = self.__employee_LL.get_employee(i)

                print("{:<5}\t{:<17}\t{:<15}".format(employee[0], employee[1], employee[3]))

            print("\nDestination:\t\t{}".format(destination))
            if input("\nY: Yes\nAnything else: No\nWould you like to enter another date? ").upper() == "Y":
                isValid = False
            else:
                break

    def list_all_pilots(self):
        """ Lists all pilots in employee.csv file. """

        self.header("All pilots.")
        all_pilots = self.__employee_LL.list_all_pilots()

        pilots = ""
        for index, row in enumerate(all_pilots):
            for x in row:
                pilots += (x + ", ")
            print("{}. {}".format(index+1, pilots))
            pilots = ""

    def list_airplane_by_pilot(self):
        """ Lists which airplane the given pilot has a licence to. """

        self.header("List airplane by pilot")
        pilots = self.__employee_LL.list_all_pilots()

        isValid = False
        while isValid == False:
            ssn = input("Enter q to quit.\nEnter a social security number: ")
            if ssn == "q":
                break
            try:
                licence = self.__employee_LL.list_airplane_by_pilot(ssn)
                if licence == "N/A":
                    print("\nEmployee must be a pilot.\nPlease try agan.\n")
                else:
                    for x in pilots:
                        if x[0] == ssn:
                            print("\nEmployee:\t{}, {}\nLicence:\t{}".format(ssn, x[1], licence))

                    choice = input("\nY: Yes\nAnything else: No\nWould you like to list another pilot? ").upper()
                    if choice == "Y":
                        continue
                    else:
                        break
            except TypeError:
                print("\nPlease enter a valid social security number.\n")


    def list_pilots_by_airplane(self):
        """ Lists which pilots have licence to given licence. """

        NABAE146 = 1
        NAFokkerF28 = 2
        NAFokkerF100 = 3

        self.header("List pilots by airplane")

        isValid = False
        while isValid == False:
            print("\n1. NABAE146\n2. NAFokkerF28\n3. NAFokkerF100\n")
            licence = input("Enter q to quit.\nEnter a licence: ")
            header = "\n{:<5} {:>10} {:>19}\n".format("SSN", "Name", "Rank")
            if licence == "q":
                break
            try:
                licence = int(licence)
                if licence == NABAE146:
                    airplanes = self.__employee_LL.list_pilots_by_airplane("NABAE146")
                    print(header)
                    for x in airplanes:
                        print("{:<5}\t{:<17}\t{:<15}".format(x[0], x[1], x[3]))
                    if input("\nY: Yes\nAnything else: No\nDo you want to enter another licence: ").upper() == "Y":
                        continue
                    else:
                        break

                elif licence == NAFokkerF28:
                    airplanes = self.__employee_LL.list_pilots_by_airplane("NAFokkerF28")
                    print(header)
                    for x in airplanes:
                        print("{:<5}\t{:<17}\t{:<15}".format(x[0], x[1], x[3]))
                    if input("\nY: Yes\nAnything else: No\nDo you want to enter another licence: ").upper() == "Y":
                        continue
                    else:
                        break

                elif licence == NAFokkerF100:
                    airplanes = self.__employee_LL.list_pilots_by_airplane("NAFokkerF100")
                    print(header)
                    for x in airplanes:
                        print("{:<5}\t{:<17}\t{:<15}".format(x[0], x[1], x[3]))
                    if input("\nY: Yes\nAnything else: No\nDo you want to enter another licence: ").upper() == "Y":
                        continue
                    else:
                        break

                else:
                    print("\nPlease enter 1, 2 or 3.")
                    continue
            except ValueError:
                print("\nPlease enter 1, 2 or 3.")
                continue



    def list_all_flight_attendants(self):

        self.header("All flight attendants")
        all_flight_attendants = self.__employee_LL.list_all_flight_attendants()

        flight_attendants = ""
        for index, row in enumerate(all_flight_attendants):
            for x in row:
                flight_attendants += (x + ", ")
            print("{}. {}".format(index+1, flight_attendants))
            flight_attendants = ""




if __name__ == "__main__":
    a = EmployeeUI()
    a.busy_flight_attendants()