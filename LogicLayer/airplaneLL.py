import csv
from Models.airplane import Airplane
from LogicLayer.voyageLL import VoyageLL
import os


class AirplaneLL:

    def __init__(self):
        self.__voyageLL = VoyageLL()



    def get_all_airplanes(self):
        """
        :return: A list of all the airplanes
        """
        airplanes = []
        path = os.path.join("Data", "Aircraft.csv")
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
        with open(path, "a+") as file:
            try:
                writer = csv.writer(file)
                writer.writerow([planeInsignia,planeTypeId,manufacturer,model,capacity])
            except:
                return False



    def available_airplanes(self, date):
        """ List of all busy airplanes """

        busy_airplanes = []
        all_airplanes_info = self.get_all_airplanes()
        all_airplanes_insignia = []
        all_airplanes_manufacturer = []

        for row in all_airplanes_info:
            all_airplanes_insignia.append(row[0])

        for row in all_airplanes_info:
            all_airplanes_manufacturer.append(row[1])

        voyage = self.__voyageLL.get_all_upcoming_voyages_SM()

        for x in voyage:
            busy_date = x[3]
            busy_date = busy_date.split("T")

            if busy_date[0] == date:
                busy_airplanes.append(x[10])

        available_airplanes = []

        for row in all_airplanes_insignia:
            if row not in busy_airplanes:
                available_airplanes.append(row)


        return available_airplanes




if __name__ == "__main__":
    a = AirplaneLL()
    print(a.available_airplanes("12"))

