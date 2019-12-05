import csv
from NaNAir39 import Airplane


class Airplanes:
    def __init__(self):
        pass

    @staticmethod   # útaf erum ekki að nota neitt self
    def get_all_airplanes():
        airplanes = []
        path = "../Data/Aircraft.csv"
        file = open(path, newline="")
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            planeInsignia_str = row[0]
            planeTypeId_str = row[1]

            airplanes.append(Airplane(planeInsignia_str, planeTypeId_str))

        file.close()
        return airplanes


if __name__ == "__main__":
    a = Airplanes()
    for x in a.get_all_airplanes():
        print(x)
