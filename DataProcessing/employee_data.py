import csv
from NaNAir39 import Employee

class Employees:

    employees = get_all_employees()

    def get_all_employees(self):
        employees = []
        path = "DataClasses/employee.csv"
        file = open(path, newline= "")
        reader = csv.reader(file)

        header = next(reader) # The first line is a header

        for row in reader:
            ssn_int = int(row[1])
            name_str = row[2]
            position_str = row[3]
            rank_str = row[4]
            licence_str = row[5]
            address_str = row[6]
            mobile_int = int(row[7])
            landlineNr_int = row[8]
            email_str = row[9]
            employees.append(Employee(ssn_int, name_str, position_str, rank_str, licence_str, \
                address_str, mobile_int, landlineNr_int, email_str))

        return employees

