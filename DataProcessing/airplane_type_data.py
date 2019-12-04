import csv
from NaNAir39.DataLayer.airplane_type import AirplaneType


def main():
    data = []
    path = "DataClasses/AircraftType.csv"
    file = open(path, newline="")
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        planeTypeId_str= row[0]
        manufacturer_str = row[1]
        model_str = row[2]
        capacity_int = int(row[3])
        data.append(AirplaneType(planeTypeId_str, manufacturer_str, model_str, capacity_int))

        print(row)

main()