from LogicLayer.employeeLL import EmployeeLL
from Models.employee import Employee
from LogicLayer.voyageLL import VoyageLL
from datetime import datetime
from UI.page import Page
###
from datetime import datetime
from datetime import timedelta



class EmployeeUI(Page):


    def __init__(self):
        self.__employee_LL = EmployeeLL()
        self.__voyage_LL = VoyageLL()
        super().__init__()

    def header(self, i):
        return " "

    def get_all_employees(self):
        """ Lists information about all employees. """
        # ssn,name,position,rank,licence,address,mobile,landlineNr,email

        page_width = 90

        self.header("All employees")
        self._print_header("All employees", page_width)

        # self.show_page()

        all_employees = self.__employee_LL.get_all_employees()
        print(all_employees)

        employee_header =   "| {:<12} {:<19} {:<14} {:<24} {:<19} {:<14} {:<9} {:<9} {:<28} |\n".format("SSN", "Name", "Position", "Rank", "Licence", \
                            "Address", "Mobile", "Landline", "email") + \
                            "| " + "-" * (page_width-2) + " |"

        print(employee_header)

        for x in all_employees:
            print("| {:<13}{:<20}{:<15}{:<25}{:<20}{:<15}{:<10}{:<10}{:<29} |".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))
        input()
        return True

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

                print("\nSSN: \t\t\t{}\nName: \t\t\t{}\nPosition: \t\t{}\nRank: \t\t\t{}\nLicence: \t\t{}\nAddress: \t\t{}\nMobile: \t\t{}\nLandline nr: \t{}\nEmail: \t\t\t{}".format(\
                    employee[0], employee[1], employee[2], employee[3], employee[4], employee[5],
                    employee[6],employee[7], employee[8]))
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
                if choice == "Y" or choice == "YES":
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

                email_list = name.split()
                email = ""
                for x in email_list:
                    email += x

                email = email.lower()
                email += "@nanair.is"

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
                        name = input("\nEnter new name: ")
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
                        address = input("\nEnter new address: ")
                        employee_edit.set_address(address)
                        print("Address changed to {}".format(choice))

                    elif action == "6":
                        mobile = input("\nEnter new mobile: ")
                        employee_edit.set_mobile(mobile)
                        print("Mobile changed to {}".format(mobile))

                    elif action == "7":
                        landlineNr = input("\nEnter new landline nr.: ")
                        employee_edit.set_landlineNr(landlineNr)
                        print("Landline nr. changed to {}".format(landlineNr))

                    elif action == "8":
                        username = input("\nEnter new username: ").lower()
                        email = username + "@nanair.is"
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

            try:
                datetime_str = input("Enter date  (i.e. 'mm/dd/yy'): ").strip()
                if datetime_str == "q":
                    break

                datetime_object = datetime.strptime(datetime_str, '%m/%d/%y')
                datetime_object = str(datetime_object)
                datetime_object = datetime_object.split(" ")

                return datetime_object[0]

            except ValueError:
                print("\nPlease enter a valid date.\n")
        return None


    def available_employees(self):
        """ Lists all available employees on a given day. """

        self.header("All available employees")

        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            try:
                voyage = self.__voyage_LL.get_all_upcoming_voyages()
                all_employees = self.__employee_LL.get_all_employees()
                busy = []
                available = []


                for x in voyage:
                    busy_date = x[3]
                    busy_date = busy_date.split("T")

                    if busy_date[0] == date:
                        busy.append(x[5])
                        busy.append(x[6])
                        busy.append(x[7])
                        busy.append(x[8])
                        busy.append(x[9])

                for i in all_employees:
                    if i[0] in busy:
                        pass
                    else:
                        available.append(i)

                if len(available) > 0:
                    header = "\n   {:<5} {:>11} {:>23} {:>15}\n".format("SSN", "Name", "Position", "Rank")
                    print(header)

                for index, z in enumerate(available):
                    print("{}. {:<5}\t{:<17}\t{:<17}\t{:<15}".format(index+1, z[0], z[1], z[2], z[3]))
                print()

            except:
                print("No available employees at this time.")


    def available_pilots(self):
        """ Lists all available pilots on a given day/time. """

        self.header("All available pilots")

        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            try:
                voyage = self.__voyage_LL.get_all_upcoming_voyages()
                all_employees = self.__employee_LL.get_all_employees()
                busy = []
                available = []

                for x in voyage:
                    busy_date = x[3]
                    busy_date = busy_date.split("T")

                    if busy_date[0] == date:
                        busy.append(x[5])
                        busy.append(x[6])
                        busy.append(x[7])
                        busy.append(x[8])
                        busy.append(x[9])

                for i in all_employees:
                    if i[0] not in busy and i[2] == "Pilot":
                        available.append(i)
                    else:
                        pass

                if len(available) > 0:
                    header = "\n   {:<5} {:>11} {:>23} {:>15}\n".format("SSN", "Name", "Position", "Rank")
                    print(header)

                for index, z in enumerate(available):
                    print("{}. {:<5}\t{:<17}\t{:<17}\t{:<15}".format(index+1, z[0], z[1], z[2], z[3]))
                print()

            except:
                print("No available pilots at this time.")

    def available_flight_attendants(self):
        """ Lists all available flight attendants on a given day/time. """

        self.header("All available flight attendants")

        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            try:
                voyage = self.__voyage_LL.get_all_upcoming_voyages()
                all_employees = self.__employee_LL.get_all_employees()
                busy = []
                available = []

                for x in voyage:
                    busy_date = x[3]
                    busy_date = busy_date.split("T")

                    if busy_date[0] == date:
                        busy.append(x[5])
                        busy.append(x[6])
                        busy.append(x[7])
                        busy.append(x[8])
                        busy.append(x[9])

                for i in all_employees:
                    if i[0] not in busy and i[2] == "Cabincrew":
                        available.append(i)
                    else:
                        pass

                if len(available) > 0:
                    header = "\n   {:<5} {:>11} {:>23} {:>15}\n".format("SSN", "Name", "Position", "Rank")
                    print(header)

                for index, z in enumerate(available):
                    print("{}. {:<5}\t{:<17}\t{:<17}\t{:<15}".format(index+1, z[0], z[1], z[2], z[3]))
                print()

            except:
                print("\nNo available flight attendants at this time.\n")


    def busy_employees(self):
        """ Lists information about all employees who are busy at the given date/time and the
            destination they are going to. """

        self.header("All busy employees")
        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            try:
                voyage = self.__voyage_LL.get_all_upcoming_voyages()

                for x in voyage:
                    busy_date = x[3]
                    busy_date = busy_date.split("T")

                    if busy_date[0] == date:
                        employees = x[5:10]
                        destination = x[1]



                if len(employees) > 0:
                    header = "\n   {:<5} {:>11} {:>23} {:>15}\n".format("SSN", "Name", "Position", "Rank")
                    print(header)

                for index, i in enumerate(employees):
                    employee = self.__employee_LL.get_employee(i)
                    print("{}. {:<5}\t{:<17}\t{:<17}\t{:<15}".format(index+1, employee[0], employee[1], employee[2], employee[3]))

                print("\nDestination:\t\t{}".format(destination))
                if input("\nY: Yes\nAnything else: No\nWould you like to enter another date? ").upper() == "Y":
                    isValid = False
                else:
                    break
            except:
                print("\nNo busy employees at this time.\n")


    def busy_pilots(self):
        """ Lists information about all pilots who are busy at the given date/time and the
            destination they are going to. """

        self.header("All busy pilots")
        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            try:
                voyage = self.__voyage_LL.get_all_upcoming_voyages()

                for x in voyage:
                    busy_date = x[3]
                    busy_date = busy_date.split("T")

                    if busy_date[0] == date:
                        pilots = x[5:7]
                        destination = x[1]

                if len(pilots) > 0:
                    header = "\n   {:<5} {:>11} {:>19}\n".format("SSN", "Name", "Rank")
                    print(header)

                for index, i in enumerate(pilots):
                    employee = self.__employee_LL.get_employee(i)

                    print("{}. {:<5}\t{:<17}\t{:<15}".format(index+1, employee[0], employee[1], employee[3]))

                print("\nDestination:\t\t{}".format(destination))
                if input("\nY: Yes\nAnything else: No\nWould you like to enter another date? ").upper() == "Y":
                    isValid = False
                else:
                    break
            except:
                print("\nNo busy pilots at this time.\n")


    def busy_flight_attendants(self):
        """ Lists information about all flight attendants who are busy at the given date/time and the
            destination they are going to. """

        self.header("All busy flight attendants")
        isValid = False
        while isValid == False:
            date = self.get_date()
            if date == None:
                break

            try:
                voyage = self.__voyage_LL.get_all_upcoming_voyages()

                for x in voyage:
                    busy_date = x[3]
                    busy_date = busy_date.split("T")

                    if busy_date[0] == date:
                        flight_attendants = x[7:10]
                        destination = x[1]

                if len(flight_attendants) > 0:
                    header = "\n   {:<5} {:>11} {:>19}\n".format("SSN", "Name", "Rank")
                    print(header)

                for index, i in enumerate(flight_attendants):
                    employee = self.__employee_LL.get_employee(i)

                    print("{}. {:<5}\t{:<17}\t{:<15}".format(index+1, employee[0], employee[1], employee[3]))

                print("\nDestination:\t\t{}".format(destination))
                if input("\nY: Yes\nAnything else: No\nWould you like to enter another date? ").upper() == "Y":
                    isValid = False
                else:
                    break
            except:
                print("\nNo busy flight attendants at this time.\n")


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


    def list_pilots_by_airplane(self, licence):
        """ Lists which pilots have licence to given airplanes. """

        self.header("List pilots by airplane")

        isValid = False
        while isValid == False:
            header = "\n{:<5} {:>10} {:>19}\n".format("SSN", "Name", "Rank")
        
            airplanes = self.__employee_LL.list_pilots_by_airplane(licence)
            print(header)
            for x in airplanes:
                print("{:<5}\t{:<17}\t{:<15}".format(x[0], x[1], x[3]))
            

    def list_all_flight_attendants(self):
        """ Lists all flight attendants (Cabincrew) in employee.csv file. """

        self.header("All flight attendants")
        all_flight_attendants = self.__employee_LL.list_all_flight_attendants()
        flight_attendants = ""
        for index, row in enumerate(all_flight_attendants):
            for x in row:
                flight_attendants += (x + ", ")
            print("{}.  \t{}".format(index+1, flight_attendants))
            flight_attendants = ""

    def print_week_of_employee(self):
        self.get_all_employees()
        upcomingVoyagesList = self.__voyage_LL.get_all_upcoming_voyages()
        upcomingVoyagesList_len = len(upcomingVoyagesList)

        ssn_employee = input("\nEnter the ssn of the employee you want to get the week plan for: ")

        #Checks if the ssn_employee is the ssn of a employee
        if self.__employee_LL.ssn_valid(ssn_employee) == True:

            #checks if the format is correct
            correctFormat = False
            while correctFormat != True:
                error = 0
                getDateFromUser_str = input("Enter the starting day(YYYY/MM/DD): ")
                try:
                    splittedGetDateFromUser = getDateFromUser_str.split("/")
                    splittedGetDateFromUserLen = len(splittedGetDateFromUser)
                    selectedYear_str = splittedGetDateFromUser[0]
                    selectedMonth_str = splittedGetDateFromUser[1]
                    selectedDay_str = splittedGetDateFromUser[2]

                    if splittedGetDateFromUserLen != 3:
                        print("Error. You have to use the correct format.")
                        error = 1
                        correctFormat = False
                    else:
                        correctFormat = True
                        #Checks if the year is integer and has 4 integers
                        try:
                            selectedYear_int = int(selectedYear_str)
                            selectedYearLen = len(selectedYear_str)
                            
                            if selectedYearLen != 4:
                                print("Error. The year has to have 4 integers.")
                                error = 1
                                correctFormat = False
                            elif selectedYear_int < 2019:
                                print("Error. The year has to be 2019 or above.")
                                error = 1
                                correctFormat = False
                            else:
                                correctFormat = True

                        except ValueError:
                            print("Error. The year has to be integer.")
                            error = 1
                            correctFormat = False

                        #Checks if the month is integer and has 2 integers
                        try:
                            selectedMonth_int = int(selectedMonth_str)
                            selectedMonthLen = len(selectedMonth_str)

                            if selectedMonthLen != 2:
                                print("Error. The month has to have 2 integers.")
                                error = 1
                                correctFormat = False
                            elif selectedMonth_int > 12:
                                print("Error. The month has to be between 01-12.")
                                error = 1
                                correctFormat = False
                            else:
                                correctFormat = True         
                                
                        except ValueError:
                            print("Error. The month has to be integer.")
                            error = 1
                            correctFormat = False

                        #Checks if the day is integer and has 2 integers
                        try:
                            selectedDay_int = int(selectedDay_str)
                            selectedDayLen = len(selectedDay_str)

                            if selectedDayLen != 2:
                                print("Error. The day has to have 2 integers.")
                                error = 1
                                correctFormat = False
                            elif selectedDay_int > 31:
                                print("Error. The day has to be between 01-31.")
                                error = 1
                                correctFormat = False
                            else:
                                correctFormat = True 

                        except ValueError:
                            print("Error. The day has to be integer.")
                            error = 1
                            correctFormat = False
                        if error > 0:
                            correctFormat = False
                        
                except IndexError:
                    print("Error. You have to use the correct format.")
                    error = 1
                    correctFormat = False


                if correctFormat == True:
                    selectedDate_str = "{}-{}-{}T00:00:00".format(selectedYear_int, selectedMonth_int, selectedDay_int)

                    selectedDate_obj = datetime.strptime(selectedDate_str, "%Y-%m-%dT%H:%M:%S")            
                    week_obj = timedelta(days=6)
                    weekFromSelectedDate_obj = selectedDate_obj + week_obj
                    #selectedDate_obj: is the selected date from the user
                    #weekFromSelectedDate_obj: is the date week from the selected date 

                    #creates a list of the selected employee, all the work trips
                    currEmployeeWork_list = []
                    for i in range(upcomingVoyagesList_len):
                        if ssn_employee in upcomingVoyagesList[i]:
                            currEmployeeWork_list.append(upcomingVoyagesList[i])
                    
                    #create a list of all the work trips that the employee went on that week
                    employeeWorkWeek_list = []
                    currEmployeeWorkLen = len(currEmployeeWork_list)
                    for i in range(currEmployeeWorkLen):
                        iDate_str = currEmployeeWork_list[i][3]
                        iDate_obj = datetime.strptime(iDate_str, "%Y-%m-%dT%H:%M:%S")
       
                        if selectedDate_obj < iDate_obj and iDate_obj < weekFromSelectedDate_obj:
                            employeeWorkWeek_list.append(currEmployeeWork_list)
                            
                    print(employeeWorkWeek_list)

                    #get the employee name
                    employeeName = ""
                    allEmployees_list =  self.__employee_LL.get_all_employees()
                    for i in range(len(allEmployees_list)):
                        if allEmployees_list[i][0] == ssn_employee:
                            employeeName = allEmployees_list[i][1] 
                    
                    print(employeeName)





if __name__ == "__main__":
    a = EmployeeUI()
    a.available_employees()
