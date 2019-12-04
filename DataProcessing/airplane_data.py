import csv
from NaNAir39.DataLayer.airplane import Airplane

def main():
    data = []
    path = "DataClasses/Aircraft.csv"
    file = open(path, newline="")
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        planeInsignia = row[0]
        planeTypeId = row[1]

        data.append(Airplane(planeInsignia, planeInsignia))

        print(row)

main()