import os
import csv
from Models.employee import Employee


class EmployeeDL:

    def __init__(self):
        pass

    def get_all_employees(self):
        """
        :return: A list of all the employees
        """
        employees = []        
        path = os.path.join("Data", "employee.csv")
        #path = os.path.join("../Data", "employee.csv")
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

        if self.ssn_valid(ssn):
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

        path = "../Data/employee.csv"
        with open(path, "a") as file:
            try:
                writer = csv.writer(file)
                writer.writerow([ssn, name, position, rank, licence, address, mobile, landlineNr, email])
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

        selected_employee = employee[0]

        os.remove("../Data/employee.csv")
        header = "ssn,name,position,rank,licence,address,mobile,landlineNr,email\n"
        with open("../Data/employee.csv", "a+", encoding="utf-8") as file:
            file.write(header)

        for x in employees:
            if x[0] == selected_employee:
                pass
            else:
                new_employee = Employee(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
                self.register_employee(new_employee)


    def print_week_of_employee(self, date):  # A printable work summary can be displayed showing all employee work trips in a given week.
        pass


    def get_week_list(self):
        pass