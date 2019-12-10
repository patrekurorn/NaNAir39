import csv
from Models.voyage import Voyage
from Models import voyage

class VoyageRepo:

    def __init__(self):
        pass

    def work_summary(self): # A printable work summary can be displayed showing all employee work trips in a given week.
        pass


    def get_all_voyages(self):
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
        flightNumber = Voyage.get_flightNumber()
        departingFrom = Voyage.get_departingFrom()
        arrivingAt = Voyage.get_arrivingAt()
        departure = Voyage.get_departure()
        arrival = Voyage.get_arrival()

        path = "../Data/UpcomingFlights.csv"
        with open(path, "a+", encoding="utf-8") as file:
            try:
                super(voyage).__init__()
                #.write("{} {} {} {} {}".format(flightNumber, departingFrom, arrivingAt, departure, arrival))
            except:
                print("Couldn't register voyage")
                # setja error input í UI

    def employee_






if __name__ == "__main__":
    a = VoyageRepo()
