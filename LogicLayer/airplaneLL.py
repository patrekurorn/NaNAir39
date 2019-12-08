import csv
from NaNAir39.Models.airplane import Airplane

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

    def check_airplane(self, planeInsignia):
        data = self.get_all_airplanes()

        for row in data:
            if row[0] == planeInsignia:
                return True

        return False


    @staticmethod
    def register_airplane(new_airplane):
        planeInsignia = new_airplane.get_plane_insignia()
        planeTypeId = new_airplane.get_plane_type_id()
        manufacturer = new_airplane.get_manufacturer()
        model = new_airplane.get_model()
        capacity = new_airplane.get_capacity()

        path = "../Data/Aircraft.csv"
        with open(path, "a+", encoding="utf-8") as file:
            try:
                file.write("{},{},{},{},{}".format(planeInsignia, planeTypeId, manufacturer, model, capacity))
            except:
                return False



    def available_airplanes(self):
        pass




if __name__ == "__main__":
    a = AirplaneLL()
    print(a.register_airplane())
    print(a.get_all_airplanes())

