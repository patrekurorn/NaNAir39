import csv
from NaNAir39 import Employee

def main():
    data = []
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
        data.append(Employee(ssn_int, name_str, position_str, rank_str, licence_str, address_str, mobile_int, landlineNr_int, email_str))


        #print(row)
        employee_a = Employee(ssn, name, position, rank, licence, address, mobile, landlineNr, email)
        employee_a.list_all_pilots()
        
        
main()
