import csv
from Models.voyage import Voyage

class VoyageLL:

    def __init__(self):
        pass

    def get_all_upcoming_voyages(self):  # display voyages
        voyages = []
        path = "../Data/UpcomingFlightsSM.csv"
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                voyages.append(row)
        return voyages


    def check_flight_number(self, flightNumber):
        data = self.get_all_upcoming_voyages()

        for row in data:
            if row[0] == flightNumber:
                return True

        return False


    @staticmethod
    def register_voyage_PM(new_voyage):  # Planning manager gerir þetta
        flightNumber = new_voyage.get_flight_number()
        departingFrom = new_voyage.get_departing_from()
        arrivingAt = new_voyage.get_arriving_at()
        departure_time = new_voyage.get_departure_time()
        arrival_time = new_voyage.get_arrival_time()

        path = "../Data/UpcomingFlightsPM.csv"
        with open(path, "a+") as file:
            try:
                file.write("{},{},{},{},{}".format(flightNumber, departingFrom, arrivingAt, departure_time, arrival_time))
            except:
                return False

    @staticmethod
    def register_voyage_SM(new_voyage):
        pass

    def list_unmanned_voyages(self):
        pass

    def list_available_dates(self):
        pass

    def list_available_times(self):
        pass

    def list_all_destinations(self):

        destinations = []
        path = "../Data/Destinations.csv"
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                destinations.append(row[1])

        return destinations

    def voyage_repetition(self):
        pass

    def edit_voyage(self):
        pass

    def edit_time(self):
        pass

    def edit_date(self):
        pass

    def cancel_voyage(self):
        pass

    def list_voyages_day(self):
        pass

    def list_voyages_week(self):
        pass





if __name__ == "__main__":
    a = VoyageLL()
    print(a.list_all_destinations())