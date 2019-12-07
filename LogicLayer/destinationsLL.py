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



    @staticmethod
    def register_destination(destination):
        """
        :return: Adds a new destination to the cvs file
        """
        destinationID = Destination.get_destinationID()
        country = Destination.get_country()
        airport = Destination.get_airport()
        flightDuration = Destination.get_flightDuration()
        distanceFromIceland = Destination.get_distance_from_iceland()
        contactName = Destination.get_contact_name()
        contactNumber = Destination.get_contact_number()

        path = "../Data/Destinations.csv"
        with open(path, "a+", encoding="utf-8") as file:
            try:
                theWriter = csv.writer(file)
                theWriter.writerow(destination)
                theWriter.writerow("{} {} {} {} {} {} {}".format(destinationID, country, airport, flightDuration, distanceFromIceland, contactName, contactNumber))
            except:
                print("Couldn't add destination")
                return
                # setja error input í UI


    def edit_destination(self):
        pass

    def edit_contact_info(self):
        pass



if __name__ == "__main__":
    a = DestinationsLL()
    print(a.get_all_destinations())

    a.register_destination("desti")




