import csv
from NaNAir39 import Airplane

class Airplanes:

    airplanes = get_all_airplanes()

def get_all_airplanes(self):
    airplanes = []
    path = "../DataClasses/Aircraft.csv"
    file = open(path, newline="")
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
        planeInsignia_str = row[0]
        planeTypeId_str = row[1]

        airplanes.append(Airplane(planeInsignia_str, planeInsignia_str))

    return airplanes

