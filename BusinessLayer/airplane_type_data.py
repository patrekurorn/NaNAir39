import csv
from NaNAir39 import AirplaneType

class Airplane_Types:

    airplane_types = get_all_airplane_types()

    def get_all_airplane_types(self):

        airplane_types = []
        path = "../DataClasses/AircraftType.csv"
        file = open(path, newline="")
        reader = csv.reader(file)

        header = next(reader)

        for row in reader:
            planeTypeId_str= row[0]
            manufacturer_str = row[1]
            model_str = row[2]
            capacity_int = int(row[3])
            airplane_types.append(AirplaneType(planeTypeId_str, manufacturer_str, model_str, capacity_int))

        return airplane_types

