import csv
from Models.voyage import Voyage
from Models.voyage_Sm import VoyageSm
import os


class VoyageLL:

    def __init__(self):
        pass


    def get_voyage(self,flightNumber):
        """
        Return a list of information about specific voyage
        """
        total_data = self.get_all_upcoming_voyages()

        if self.check_flight_number(flightNumber):
            for row in total_data:
                if row[0] == flightNumber:
                    return row

    def get_all_upcoming_voyages(self):  # display voyages
        """
        : Returns a list of voyages
        """
        voyages = []
        path = "../Data/UpcomingFlightsPM.csv"
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
        departureTime = new_voyage.get_departure_time()
        arrivalTime = new_voyage.get_arrival_time()

        path = "../Data/UpcomingFlightsPM.csv"
        with open(path, "a+",encoding="utf-8") as file:
            try:
                if os.stat(path).st_size == 0:
                    file.write("{},{},{},{},{},".format("flightNumber","departingFrom","arrivingAt", "departure_time", "arrival_time"))
                file.write("\n{},{},{},{},{}".format(flightNumber,departingFrom,arrivingAt,departureTime,arrivalTime))
            except:
                return False

    @staticmethod
    def register_voyage_SM(aded_voyage):
        pass
        """ Þarf að bætta við til að leifa SM að appenda í nú þegar búinn til csv skrá frá PM
        flightNumber = aded_voyage.get_captain()
        captain = added_voyage.get_copilot()
        fsm = aded_voyage.get_fsm()
        fa1 = added_voyage.get_fa1()
        fa2 = added_voyage.get_fa2()

        path = "../Data/UpcomingFlightsSM.csv"
        with open(path,"a+") as file:
            try:
                pass
                writer = file.writer(file)
                writer.writerow([aded_voyage.get_fli])

            except:
                pass
        """


    def list_unmanned_voyages(self):
        pass

    def list_available_dates(self):
        pass

    def list_available_times(self):
        pass

    def list_all_destinations(self):
        pass
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


    def cancel_voyage(self,flightNumber):
        """ til að fjarlægja línu í csv þurfum við að lesa inn allt csv sem var gert fyrir ofan, fjarlægja línuna og skrifa svo endurgerða csvið"""
        voyage = self.get_voyage(flightNumber)
        voyages = self.get_all_upcoming_voyages()

        selectedVoyage = voyage[0]
        os.remove("../Data/UpcomingFlightsPM.csv")
        header = "flightNumber,departingFrom,arrivingAt,departure,arrival"

        with open ("../Data/UpcomingFlightsPM.csv","a+",encoding="utf-8") as file:
            file.write(header)

        for index in voyages:
            if index[0] == selectedVoyage:
                pass
            else:
                newVoyage = Voyage(index[0],index[1],index[2],index[3],index[4])
                self.register_voyage_PM(newVoyage)

    def csv_dictionary(self):
        dateDictionary = {}


        without_first= []
        path = "../Data/UpcomingFlightsPM.csv"
        with open(path,encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                without_first.append(row)

        for row in without_first:
            day = row[3].split("T")[0]

            if day in dateDictionary:
                dateDictionary[day] += [[row[0],row[1],row[2]]]
            else:
                dateDictionary[day] = [[row[0],row[1],row[2]]]

        return dateDictionary

    def list_voyages_day(self):
        """ collects day of format and prints out each voyage for specific day """
        day_dict = {}
        without_first= []

        path = "../Data/UpcomingFlightsPM.csv"
        with open(path,encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                without_first.append(row)

        for row in without_first:
            day = row[3].split("T")[0].split("-")[2]

            if day in day_dict:
                day_dict[day] += [[row[0],row[1],row[2]]]
            else:
                day_dict[day] = [[row[0],row[1],row[2]]]

        for key,value in sorted(day_dict.items()):
            print("day {}: {}".format(key,value))


    def list_voyages_week(self):
        pass





if __name__ == "__main__":
    a = VoyageLL()
    print(a.list_all_destinations())
    a.list_voyages_day()


