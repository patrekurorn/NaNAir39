import csv
from NaNAir39.DataLayer.airplane_type import AirplaneType


def main():
    data = []
    path = "DataClasses/AircraftType.csv"
    file = open(path, newline="")
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        planeTypeId = int(row[0])

        print(row)

main()