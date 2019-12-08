
from LogicLayer.employeeLL import EmployeeLL
from Models.employee import Employee

class EmployeeUI:

    def __init__(self):
        self.__employee_LL = EmployeeLL()


    def header(self):
        pass

    def register_employee(self):

        # Setja header

        print("Creating new employee")
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

if __name__ == "__main__":
    a = EmployeeUI()
    a.register_employee()