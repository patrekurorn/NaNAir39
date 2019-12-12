import csv
import os


class AirplaneDL:

    def __init__(self):
        pass

    @staticmethod
    def register_airplane(new_airplane):
        planeInsignia = new_airplane.get_plane_insignia()
        planeTypeId = new_airplane.get_plane_type_id()
        manufacturer = new_airplane.get_manufacturer()
        model = new_airplane.get_model()
        capacity = new_airplane.get_capacity()

        path = "../Data/Aircraft.csv"
        with open(path, "a+") as file:
            try:
                writer = csv.writer(file)
                writer.writerow([planeInsignia, planeTypeId, manufacturer, model, capacity])
            except:
                return False


    def get_all_airplanes(self):
        """
        :return: A list of all the airplanes
        """
        airplanes = []
        path = os.path.join("../Data", "Aircraft.csv")
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                airplanes.append(row)

        return airplanes