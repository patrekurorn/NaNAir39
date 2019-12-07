import csv
from Models.voyage import Voyage

class VoyageLL:

    def __init__(self):
        pass

    def get_all_voyages(self):  # display voyages
        voyages = []
        path = "../Data/UpcomingFlights.csv"
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                voyages.append(row)
        return voyages


    @staticmethod
    def voyage_registration():  # Planning manager gerir þetta
        flightNumber = Voyage.get_flight_number()
        departingFrom = Voyage.get_departing_from()
        arrivingAt = Voyage.get_arriving_at()
        departure_time = Voyage.get_departure_time()
        arrival_time = Voyage.get_arrival_time()

        path = "../Data/UpcomingFlights.csv"
        with open(path, "a+", encoding="utf-8") as file:
            try:
                #file.write(super(voyage).__init__())
                file.write("{} {} {} {} {}".format(flightNumber, departingFrom, arrivingAt, departure_time, arrival_time))
            except Exception:
                print("Couldn't register voyage.")
                # setja error input í UI


    def list_unmanned_voyages(self):
        pass

    def list_available_dates(self):
        pass

    def list_available_times(self):
        pass

    def list_all_destinations(self):
        pass

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
    a.voyage_registration()
