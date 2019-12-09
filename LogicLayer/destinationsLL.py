import csv
import os
from Models import destination
from Models.destination import Destination

class DestinationsLL(object):

    def __init__(self):
        pass

    def get_all_destinations(self):
        """
        :return: List of all destinations
        """
        destination = []
        path = "../Data/Destinations.csv"
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                destination.append(row)
        return destination


    def check_destination(self, id):
        data = self.get_all_destinations()

        for row in data:
            if row[0] == id:
                return True

        return False



    @staticmethod
    def register_destination(new_destination):
        """
        :return: Adds a new destination to the cvs file
        """
        destinationID = new_destination.get_destinationID()
        country = new_destination.get_country()
        airport = new_destination.get_airport()
        flightDuration = new_destination.get_flightDuration()
        distanceFromIceland = new_destination.get_distance_from_iceland()
        contactName = new_destination.get_contact_name()
        contactNumber = new_destination.get_contact_number()

        path = "../Data/Destinations.csv"
        with open(path, "a+", encoding="utf-8") as file:
            try:
                file.write("{} {} {} {} {} {} {}".format(destinationID, country, airport, flightDuration, distanceFromIceland, contactName, contactNumber))
                file.write("\n{},{},{},{},{},{},{}".format(destinationID, country, airport, flightDuration, distanceFromIceland, contactName, contactNumber))

            except:
                return False

    def edit_destination(self):
        """ örruglega gert í UI"""

        pass

    def edit_contact_info(self):
        """ Örruglega gert í UI"""
        pass



if __name__ == "__main__":
    a = DestinationsLL()
<<<<<<< HEAD
    print(a.get_all_destinations())
    b = ("a","a","a","a","a","a","a",)
    a.register_destination(b)
=======

>>>>>>> b527158fd7e593b1292c9b921968bf7b0e9522cb




