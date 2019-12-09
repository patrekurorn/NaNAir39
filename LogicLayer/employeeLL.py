import csv
from NaNAir39.Models.employee import Employee

class EmployeeLL:

    def __init__(self):
        pass

    def get_all_employees(self):
        """
        :return: A list of all the employees
        """
        employees = []
        path = "../Data/employee.csv"
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

    def print_employee(self, ssn):
        

    def print_week_of_employee(self):   # A printable work summary can be displayed showing all employee work trips in a given week.
        pass


    def edit_employee(self, ssn):
        pass
        # LÍKLEGAST BARA Í UI

    @staticmethod
    def register_employee(new_employee):
        """
        :return: Adds a new employee to the cvs file
        """
        ssn = new_employee.get_ssn()
        name = new_employee.get_name()
        position = new_employee.get_name()
        rank = new_employee.get_rank()
        licence = new_employee.get_licence()
        address = new_employee.get_address()
        mobile = new_employee.get_mobile()
        landlineNr = new_employee.get_landlineNr()
        email = new_employee.get_email()

        path = "../Data/employee.csv"
        with open(path, "a+", encoding="utf-8") as file:
            try:
                file.write("\n{},{},{},{},{},{},{},{},{}".format(ssn, name, position, rank, licence, address, mobile, landlineNr, email))
            except:
                return False



    def available_employees(self):  # list of all available employees on a specific day
        pass

    def available_pilots(self):
        pass

    def available_flight_attendants(self):
        pass

    def busy_employees(self):   # list of all employees who are working on a specific day and which destination they are going
        pass

    def busy_pilots(self):
        pass

    def busy_flight_attendants(self):
        pass

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





if __name__ == "__main__":
    a = EmployeeLL()
    print(a.add_employee())




