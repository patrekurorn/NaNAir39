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
        with open(path, "a+") as file:
            try:
                writer = csv.writer(file)
                writer.writerow([destinationID,country,airport,flightDuration,distanceFromIceland,contactName,contactNumber])
            except:
                return False

    def get_destination(self, id):    # list information about a specific destination.
            """
            :param id: string, id of the destination
            :return: a list of information about a specific destination
            """
            data = self.get_all_destinations()

            if self.check_destination(id):
                for row in data:
                    if row[0] == id:
                        return row

            return False

    def remove_destination(self, id):
        """ 
        :Takes in the id of the destination that you want to be removed
        """
        destination = self.get_destination(id)
        destinations = self.get_all_destinations()

        selected_destination = destination[0]

        os.remove("../Data/Destinations.csv")
        header = "id,destination,country,FlightDuration,distanceFromIceland,ContactName,ContactNumber\n"
        with open("../Data/Destinations.csv", "a+", encoding="utf-8") as file:
            file.write(header)

        for x in destinations:
            if x[0] == selected_destination:
                pass
            else:
                new_destination = Destination(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
                self.register_destination(new_destination)

    """def list_all_destinations(self):
        destinations = []
        path = "../Data/Destinations.csv"
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                destinations.append(row[1])

        return destinations"""




if __name__ == "__main__":
    a = DestinationsLL()
    print(a.get_all_destinations())

