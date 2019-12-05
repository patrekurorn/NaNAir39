import csv
from NaNAir39.DataLayer.airplane import Airplane

def main():
    data = []
    path = "../DataClasses/Aircraft.csv"
    file = open(path, newline="")
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        planeInsignia_str = row[0]
        planeTypeId_str = row[1]

        data.append(Airplane(planeInsignia_str, planeInsignia_str))

        print(row)

main()