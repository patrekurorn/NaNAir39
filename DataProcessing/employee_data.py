import csv
from NaNAir39 import Employee


def main():
    data = []
    path = "DataClasses/employee.csv"
    file = open(path, newline= "")
    reader = csv.reader(file)

    header = next(reader) # The first line is a header

    for row in reader:
        ssn = int(row[1])
        name = row[2]
        position = row[3]
        rank = row[4]
        licence = row[5]
        address = row[6]
        mobile = int(row[7])
        landlineNr = row[8]
        email = row[9]
        data.append(Employee(ssn, name, position, rank, licence, address, mobile, landlineNr, email))

        print(row)

main()