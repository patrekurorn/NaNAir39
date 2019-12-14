import csv
from DataLayer.airplaneDL import AirplaneDL
from LogicLayer.voyageLL import VoyageLL
import os


class AirplaneLL:

    def __init__(self):
        self.__voyageLL = VoyageLL()
        self.__airplaneDL = AirplaneDL()



    def get_all_airplanes(self):
        return self.__airplaneDL.get_all_airplanes()



    def check_airplane(self, planeInsignia):
        data = self.get_all_airplanes()

        for row in data:
            if row[0] == planeInsignia:
                return True

        return False


    def register_airplane(self, new_airplane):
        return self.__airplaneDL.register_airplane(new_airplane)


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

        voyage = self.__voyageLL.get_all_upcoming_voyages()

        for x in voyage:
            busy_date = x[3]
            busy_date = busy_date.split("T")

            if busy_date[0] == date:
                busy_airplanes.append(x[10])

        available_airplanes = []

        for row in all_airplanes_info:
            if row[0] not in busy_airplanes:
                available_airplanes.append(row)


        return available_airplanes




if __name__ == "__main__":
    a = AirplaneLL()
    print(a.available_airplanes("12"))

