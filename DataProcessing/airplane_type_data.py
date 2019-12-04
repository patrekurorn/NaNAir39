import csv
from NaNAir39.DataLayer.airplane_type import AirplaneType


def main():
    data = []
    path = "../DataClasses/AircraftType.csv"
    file = open(path, newline="")
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        planeTypeId = row[0]
        manufacturer = row[1]
        model = row[2]
        capacity = int(row[3])

        data.append(AirplaneType(planeTypeId, manufacturer, model, capacity))

        print(row)

main()