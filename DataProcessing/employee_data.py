import csv
from NaNAir39 import Employee


def main():
    data = []
    path = "DataClasses/Crew.csv"
    file = open(path, newline= "")
    reader = csv.reader(file)

    header = next(reader) #The first line is a header

    for row in reader:
        ssn = int(row[0])
        name = str(row[1])
        position = str(row[2])
        rank = str(row[3])
        licence = str(row[4])
        address = str(row[5])
        mobile = int(row[6])
        data.append(Employee("vantar_id", ssn, name, position, rank, licence, address, mobile, "vantar_landlineNR",
                             "vantar_email"))
        print(row)




main()