import csv
from employee import Employee


def main():
    data = []
    path = "DataClasses/Crew.csv"
    file = open(path, newline= "")
    reader = csv.reader(file)

    header = next(reader) #The first line is a header

    for row in reader:
        ssn = int(row[0])
        name = str(row[1])
        role = str(row[2])
        rank = str(row[3])
        licence = str(row[4])
        address = str(row[5])
        phonenumber = int(row[6])

        data.append(Employee(ssn, name, role, rank, licence, address, phonenumber,"vantar","vantar","vantar"))

    for lists in data:
        print(lists)




main()