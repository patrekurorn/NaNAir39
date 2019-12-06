import csv
from Models.airplane import Airplane

class AirplaneRepo:

    def __init__(self):
        pass

    def get_all_airplanes(self):
        """
        :return: A list of all the airplanes
        """
        airplanes = []
        path = "../Data/aircraft.csv"
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                airplanes.append(row)

        return airplanes




if __name__ == "__main__":
    a = AirplaneRepo()
    print(a.get_all_airplanes())

