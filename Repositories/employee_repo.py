import csv
from Models.employee import Employee
from Models import employee

class EmployeeRepo():

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
            if row[1] == ssn:   # breyta?
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
                if row[1] == ssn:
                    return row

        #else:
        #    print("Invalid SSN, please try again.")   ÞARF AÐ VERA Í USER INTERFACE
        #    self.get_employee(ssn)



    def change_employee_info(self, ssn):
        pass
        # LÍKLEGAST BARA Í UI

    @staticmethod
    def add_employee():
        """
        :return: Adds a new employee to the cvs file
        """
        #id = Employee.get_id()
   #     ssn = Employee.get_ssn()
    #    name = Employee.get_name()
    #    position = Employee.get_name()
   #     rank = Employee.get_rank()
    #    licence = Employee.get_licence()
    #    address = Employee.get_address()
   #     mobile = Employee.get_mobile()
   #     landlineNr = Employee.get_landlineNr()
   #     email = Employee.get_email()

        path = "../Data/employee.csv"
        with open(path, "a+", encoding="utf-8") as file:
            try:
                super(employee).__init__()
                #file.write("{} {} {} {} {} {} {} {} {}".format(ssn, name, position, rank, licence, address, mobile, landlineNr, email))
            except:
                print("Couldn't add employee")
                # setja error input í UI


    def available_employees(self):  # list of all available employees on a specific day
        pass

    def busy_employees(self):   # list of all employees who are working on a specific day and which destination they are going to.
        pass



if __name__ == "__main__":
    a = EmployeeRepo()
    a.add_employee()




