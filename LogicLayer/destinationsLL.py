import csv
from Models import destination

class DestinationsLL:

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
    def register_destination():
        """
        :return: Adds a new destination to the cvs file
        """
      #  destinationID = Destination.get_destinatiodID()
      #  country = Destination.get_country()
     #   airport = Destination.get_airport()
      #  flightDuration = Destination.get_flightDuration()
      #  distanceFromIceland = Destination.get_distanceFromIceland()
      #  contactName = Destination.get_contactName()
      #  contactNumber = Destination.get_contactNumber()

        path = "../Data/Destinations.csv"
        with open(path, "a+", encoding="utf-8") as file:
            try:
                file.write(super(destination).__init__())
                #file.write("{} {} {} {} {} {} {}".format(destinationID, country, airport, flightDuration, distanceFromIceland, contactName, contactNumber))
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
    print(a.register_destination())

