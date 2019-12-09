
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
            print("{}. {}".format(index+1, employees))
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

            if input("Do you want to create this employee? ").upper() == "Y":
                self.__employee_LL.register_employee(new_employee)
                print("\nEmployee created!\n")
            else:
                print("\nNo employee created.\n")

    def edit_employee(self):
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
                        employee_edit.set_name(input("Enter new name: "))
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
                                        print("Rank changed to Flight Attendan.t")
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
                        employee_edit.set_address(input("Enter new address: "))
                    elif action == "6":
                        employee_edit.set_mobile(input("Enter new mobile: "))
                    elif action == "7":
                        employee_edit.set_landlineNr(input("Enter new landline nr.: "))
                    elif action == "8":
                        employee_edit.set_email(input("Enter new email: "))

                self.__employee_LL.remove_employee(ssn_edit)
                self.__employee_LL.register_employee(employee_edit)
                print("\nEmployee succesfully edited!")
                break



            else:
                print("\nEmployee not in system.")



if __name__ == "__main__":
    a = EmployeeUI()
    a.edit_employee()