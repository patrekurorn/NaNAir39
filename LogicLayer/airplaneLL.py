import csv
from Models.airplane import Airplane

class AirplaneLL:

    def __init__(self):
        pass

    def get_all_airplanes(self):
        """
        :return: A list of all the airplanes
        """
        airplanes = []
        path = "../Data/Aircraft.csv"
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                airplanes.append(row)

        return airplanes

    def register_airplane(self):


    def available_airplanes(self):
        pass




if __name__ == "__main__":
    a = AirplaneLL()
    print(a.get_all_airplanes())

