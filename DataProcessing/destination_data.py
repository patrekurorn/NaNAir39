import csv
from NaNAir39 import Destination

class All_Destinations:

    destinations = get_all_destinations()

    def get_all_destinations(self):
        destinations = []
        path = "../DataClasses/Destinations.csv"
        file = open(path, newline= "")
        reader = csv.reader(file)

        header = next(reader)
        # destinationID, country, airport, flightDuration, distanceFromIceland, contactName, contactNumber

        for row in reader:
            destinationId = row[0]
            country = row[1]
            airport = row[2]
            flightDuration = row[3]
            distanceFromIceland = row[4]
            contactName = row[5]
            contactNumber = row[6]
            destinations.append(Destination(destinationId, country, airport, flightDuration, distanceFromIceland, \
                contactName, contactNumber))

        return destinations
