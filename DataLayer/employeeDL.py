import csv
from Models.employee import Employee
from datetime import datetime
from datetime import timedelta
import os, sys, subprocess



class EmployeeDL:

    def __init__(self):
        pass

    def get_all_employees(self):
        """
        :return: A list of all the employees
        """
        employees = []        
        path = os.path.join("Data", "employee.csv")
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                employees.append(row)

        return employees


    def ssn_valid(self, ssn):
        """
        :param ssn: string, social security number
        :return: returns True if valid, False otherwise
        """
        data = self.get_all_employees()

        for row in data:
            if row[0] == ssn:
                return True

        return False

    def get_employee(self, ssn):    # list information about a specific employee.
        """
        :param ssn: string, social security number
        :return: a list of information about a specific employee
        """
        data = self.get_all_employees()

    
        for row in data:
            if row[0] == ssn:
                return row

        return False

    @staticmethod
    def register_employee(new_employee):
        """
        :return: Adds a new employee to the cvs file
        """
        ssn = new_employee.get_ssn()
        name = new_employee.get_name()
        position = new_employee.get_position()
        rank = new_employee.get_rank()
        licence = new_employee.get_licence()
        address = new_employee.get_address()
        mobile = new_employee.get_mobile()
        landlineNr = new_employee.get_landlineNr()
        email = new_employee.get_email()

        path = os.path.join("Data","employee.csv")
        with open(path, "a", encoding="utf-8") as file:
            try:
                writer = csv.writer(file)
                file.write("\n{},{},{},{},{},{},{},{},{}".format(ssn, name, position, rank, licence, address, mobile, landlineNr, email))
            except:
                return False


    def list_all_pilots(self):
        """
        :return: A list of all the pilots
        """
        data = self.get_all_employees()
        pilots = []

        for x in data:
            if x[2] == "Pilot":
                pilots.append(x)

        return pilots


    def list_airplane_by_pilot(self, ssn):
        data = self.get_employee(ssn)

        return data[4]


    def list_pilots_by_airplane(self, licence):
        data = self.get_all_employees()
        pilots = []
        try:
            for x in data:
                if x[4] == licence:
                    pilots.append(x)

            return pilots
        except Exception:
            return False


    def list_all_flight_attendants(self):
        """
        :return: A list of all the flight attendants
        """
        data = self.get_all_employees()
        flightAttendants = []

        for x in data:
            if x[2] == "Cabincrew":
                flightAttendants.append(x)

        return flightAttendants


    def remove_employee(self, ssn):
        employee = self.get_employee(ssn)
        employees = self.get_all_employees()

        path = os.path.join("Data", "employee.csv")

        selected_employee = employee[0]

        os.remove(path)
        header = "ssn,name,position,rank,licence,address,mobile,landlineNr,email"
        with open(path, "a+", encoding="utf-8") as file:
            file.write(header)

        for x in employees:
            if x[0] == selected_employee:
                pass
            else:
                new_employee = Employee(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
                self.register_employee(new_employee)



    def print_week_of_employee(self, getDateFromUser_str, voyages, ssn_employee):  # A printable work summary can be displayed showing all employee work trips in a given week.
        # checks if the format is correct
        upcomingVoyagesList = voyages
        upcomingVoyagesList_len = len(upcomingVoyagesList)

        correctFormat = False
        while correctFormat != True:
            error = 0
            try:
                # if the format is correct then these variables hold under the input from the user
                splittedGetDateFromUser = getDateFromUser_str.split("/")
                splittedGetDateFromUserLen = len(splittedGetDateFromUser)
                selectedYear_str = splittedGetDateFromUser[0]
                selectedMonth_str = splittedGetDateFromUser[1]
                selectedDay_str = splittedGetDateFromUser[2]

                if splittedGetDateFromUserLen != 3:
                    return "Error. You have to use the correct format."
                    error = 1
                    correctFormat = False
                else:
                    correctFormat = True
                    # Checks if the year is integer and has 4 integers
                    try:
                        selectedYear_int = int(selectedYear_str)
                        selectedYearLen = len(selectedYear_str)

                        if selectedYearLen != 4:
                            return "Error. The year has to have 4 integers."
                            error = 1
                            correctFormat = False
                        elif selectedYear_int < 2019:
                            return "Error. The year has to be 2019 or above."
                            error = 1
                            correctFormat = False
                        else:
                            correctFormat = True

                    except ValueError:
                        return "Error. The year has to be integer."
                        error = 1
                        correctFormat = False

                    # Checks if the month is integer and has 2 integers
                    try:
                        selectedMonth_int = int(selectedMonth_str)
                        selectedMonthLen = len(selectedMonth_str)

                        if selectedMonthLen != 2:
                            return "Error. The month has to have 2 integers."
                            error = 1
                            correctFormat = False
                        elif selectedMonth_int > 12:
                            return "Error. The month has to be between 01-12."
                            error = 1
                            correctFormat = False
                        else:
                            correctFormat = True

                    except ValueError:
                        return "Error. The month has to be integer."
                        error = 1
                        correctFormat = False

                    # Checks if the day is integer and has 2 integers
                    try:
                        selectedDay_int = int(selectedDay_str)
                        selectedDayLen = len(selectedDay_str)

                        if selectedDayLen != 2:
                            return "Error. The day has to have 2 integers."
                            error = 1
                            correctFormat = False
                        elif selectedDay_int > 31:
                            return "Error. The day has to be between 01-31."
                            error = 1
                            correctFormat = False
                        else:
                            correctFormat = True

                    except ValueError:
                        return "Error. The day has to be integer."
                        error = 1
                        correctFormat = False
                    if error > 0:
                        correctFormat = False

            except IndexError:
                return "Error. You have to use the correct format."
                error = 1
                correctFormat = False
        if correctFormat == True:
            selectedDate_str = "{}-{}-{}T00:00:00".format(selectedYear_int, selectedMonth_int, selectedDay_int)

            selectedDate_obj = datetime.strptime(selectedDate_str, "%Y-%m-%dT%H:%M:%S")
            week_obj = timedelta(days=6)
            weekFromSelectedDate_obj = selectedDate_obj + week_obj
            weekFromSelectedDate_str = weekFromSelectedDate_obj.strftime("%Y-%m-%dT%H:%M:%S")
            # selectedDate_obj: is the selected date from the user
            # weekFromSelectedDate_obj: is the date week from the selected date

            # creates a list of the selected employee, all the work trips
            currEmployeeWork_list = []
            for i in range(upcomingVoyagesList_len):
                if ssn_employee in upcomingVoyagesList[i]:
                    currEmployeeWork_list.append(upcomingVoyagesList[i])

            # create a list of all the work trips that the employee went on that week
            employeeWorkWeek_list = []
            currEmployeeWorkLen = len(currEmployeeWork_list)
            for i in range(currEmployeeWorkLen):
                iDate_str = currEmployeeWork_list[i][3]
                iDate_obj = datetime.strptime(iDate_str, "%Y-%m-%dT%H:%M:%S")

                if selectedDate_obj < iDate_obj and iDate_obj < weekFromSelectedDate_obj:
                    employeeWorkWeek_list.append(currEmployeeWork_list)

            # get the employee name
            #employeeName = ""
            allEmployees_list = self.get_all_employees()
            for i in range(len(allEmployees_list)):
                if allEmployees_list[i][0] == ssn_employee:
                    employeeName = allEmployees_list[i][1]

            employeeWorkWeekLen = len(employeeWorkWeek_list)
            #return ("\nWork week for {}.".format(employeeName))
            #return ("From {} to {}.".format(selectedDate_str[:10], weekFromSelectedDate_str[:10]))
            os.remove(os.path.join("Data", "workWeek.csv"))
            header = "flightNumber,departingFrom,arravingAt,departure,arrival,planeInsignia\n"
            with open(os.path.join("Data", "workWeek.csv"), "a+", encoding="utf-8") as file:
                file.write(header)
            if employeeWorkWeekLen == 0:
                return ("\nNo work trips registered that week.")
            else:
                weekOfEmployee = []
                weekOfEmployeeCsv = []
                #return ("\n{} work trips registered that week.".format(employeeWorkWeekLen * 2))
                header = ("{:<9}{:<6}{:<7}{:<23}{:<22}{}".format("Number", "From", "To", "Departure", "Arrival",
                                                               "Insignia"))
                weekOfEmployee.append(header)
                employeeWorkWeek_listLen = len(employeeWorkWeek_list)

                for i in range(employeeWorkWeek_listLen):
                    # This is when you loop through the work trips from Kef and returning to Kef
                    for j in range(2):
                        weekOfEmployee.append("{:<9}{:<6}{:<7}{:<23}{:<22}{}".format(employeeWorkWeek_list[i][j][0],
                                                                       employeeWorkWeek_list[i][j][1],
                                                                       employeeWorkWeek_list[i][j][2],
                                                                       employeeWorkWeek_list[i][j][3],
                                                                       employeeWorkWeek_list[i][j][4],
                                                                       employeeWorkWeek_list[i][j][10]))
                        currWorkWeek = ("{},{},{},{},{},{}".format(employeeWorkWeek_list[i][j][0],
                                                                  employeeWorkWeek_list[i][j][1],
                                                                  employeeWorkWeek_list[i][j][2],
                                                                  employeeWorkWeek_list[i][j][3],
                                                                  employeeWorkWeek_list[i][j][4],
                                                                  employeeWorkWeek_list[i][j][10]))

                        with open(os.path.join("Data", "workWeek.csv"), "a+", encoding="utf-8") as file:
                            file.write("{}\n".format(currWorkWeek))

            filePath = os.path.normpath(os.path.join("Data", "workWeek.csv"))
            # Checks if system is windows or not
            if sys.platform == "win32":
                os.startfile(filePath)
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, filePath])

            return weekOfEmployee
