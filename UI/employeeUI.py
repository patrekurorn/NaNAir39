
from LogicLayer.employeeLL import EmployeeLL
from Models.employee import Employee

class EmployeeUI:

    def __init__(self):
        self.__employee_LL = EmployeeLL()


    def header(self, i):

        print("-" * 50)
        print("|{:^48}|".format(i))
        print("-" * 50)
        print()


    def get_all_employees(self):

        self.header("All employees")

        all_employees = self.__employee_LL.get_all_employees()

        employees = ""
        for index, row in enumerate(all_employees):
            for x in row:
                employees += (x + ", ")
            print("Employee nr. {}: {}".format(index+1, employees))
            employees = ""


    def get_employee(self):    # list information about a specific employee.

        self.header("Employee information")
        ssn = input("Enter a social security number: ")
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

        self.header("Register new employee")

        ssn = input("Enter a social security number: ")
        if self.__employee_LL.ssn_valid(ssn):
            print("Employee already exists")
        else:
            name = input("Enter name: ")
            position = input("Enter position: ")
            rank = input("Enter rank: ")
            licence = input("Enter licence: ")
            address = input("Enter address: ")
            mobile = input("Enter mobile: ")
            landlineNr = input("Enter landline number: ")
            email = input("Enter email: ")

            new_employee = Employee(ssn, name, position, rank, licence, address, mobile, landlineNr, email)
            print("\n{}\n".format(new_employee))

            if input("Do you want to create this employee? ").upper() == "Y":
                self.__employee_LL.register_employee(new_employee)
                print("\nEmployee created!\n")
            else:
                print("\nNo employee created.\n")

    def edit_employee(self):
        self.header("Edit employee")

        ssn = input("Enter a social security number: ")
        if self.__employee_LL.ssn_valid(ssn):
            editing_employee = True
            while editing_employee:




if __name__ == "__main__":
    a = EmployeeUI()
    a.edit_employee()