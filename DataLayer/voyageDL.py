import csv
import os
from Models.voyage import Voyage
from Models.voyage_Sm import VoyageSm


class VoyageDL:

    def __init__(self):
        pass

    def get_voyage(self, flightNumber):
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
        path = os.path.join("Data", "UpcomingFlightsSM.csv")

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


    """@staticmethod
    def register_voyage_PM(new_voyage):  # Planning manager gerir þetta

        flightNumber = new_voyage.get_flight_number()
        departingFrom = new_voyage.get_departing_from()
        arrivingAt = new_voyage.get_arriving_at()
        departureTime = new_voyage.get_departure_time()
        arrivalTime = new_voyage.get_arrival_time()

        path1 = os.path.join("../Data","UpcomingFlightsPM.csv")

        with open(path1, "a+",encoding="utf-8") as file:
            try:
                if os.stat(path1).st_size == 0:
                    file.write("{},{},{},{},{},".format("flightNumber","departingFrom","arrivingAt", "departure_time", "arrival_time"))
                file.write("\n{},{},{},{},{}".format(flightNumber,departingFrom,arrivingAt,departureTime,arrivalTime))
            except:
                return False"""


    @staticmethod
    def register_voyage_PM(new_voyage):     # Planning manager gerir þetta

        flightNumber = new_voyage.get_flight_number()
        departingFrom = new_voyage.get_departing_from()
        arrivingAt = new_voyage.get_arriving_at()
        departureTime = new_voyage.get_departure_time()
        arrivalTime = new_voyage.get_arrival_time()

        path2 = os.path.join("../Data", "UpcomingFlightsSM.csv")

        with open(path2, "a+",encoding="utf-8") as file:
            try:
                if os.stat(path2).st_size == 0:
                    file.write("{},{},{},{},{},{},{},{},{},{},{}".format("flightNumber","departingFrom","arrivingAt", "departure_time", "arrival_time","captain","copilot","fsm","fa1","fa2","planeInsignia"))
                file.write("\n{},{},{},{},{}".format(flightNumber,departingFrom,arrivingAt,departureTime,arrivalTime))
            except:
                return False


    @staticmethod
    def register_voyage_PM2(new_voyage):

        flightNumber = new_voyage.get_flight_number()
        departingFrom = new_voyage.get_departing_from()
        arrivingAt = new_voyage.get_arriving_at()
        departureTime = new_voyage.get_departure_time()
        arrivalTime = new_voyage.get_arrival_time()
        captain = new_voyage.get_captain()
        copilot = new_voyage.get_copilot()
        fsm = new_voyage.get_fsm()
        fa1 = new_voyage.get_fa1()
        fa2 = new_voyage.get_fa2()
        planeInsignia = new_voyage.get_planeInsignia()

        path2 = os.path.join("../Data", "UpcomingFlightsSM.csv")

        with open(path2, "a+",encoding="utf-8") as file:
            try:
                if os.stat(path2).st_size == 0:
                    file.write("{},{},{},{},{},{},{},{},{},{},{}".format("flightNumber","departingFrom","arrivingAt", "departure_time", "arrival_time","captain","copilot","fsm","fa1","fa2","planeInsignia"))
                file.write("\n{},{},{},{},{},{},{},{},{},{},{}".format(flightNumber,departingFrom,arrivingAt,departureTime,arrivalTime,captain, copilot, fsm, fa1, fa2, planeInsignia))
            except:
                return False



    def man_voyage_SM(self, new_voyage):

        voyages = self.get_all_upcoming_voyages()


        for x in voyages:
            if x[0] ==

        captain = new_voyage.get_captain()
        copilot = new_voyage.get_copilot()
        fsm = new_voyage.get_fsm()
        fa1 = new_voyage.get_fa1()
        fa2 = new_voyage.get_fa2()
        planeInsignia = new_voyage.get_planeInsignia()

        path = os.path.join("../Data", "UpcomingFlightsSM.csv")

        with open(path, "a+",encoding="utf-8") as file:
            try:
                if os.stat(path).st_size == 0:
                    file.write("{},{},{},{},{},{}".format("captain","copilot","fsm","fa1","fa2","planeInsignia"))
                file.write("{},{},{},{},{},{}".format(captain, copilot, fsm, fa1, fa2, planeInsignia))
            except:
                return False



    def cancel_voyage(self, flightNumber):
        voyage = self.get_voyage(flightNumber)
        voyages = self.get_all_upcoming_voyages()

        selectedVoyage = voyage[0]
        path = os.path.join("../Data", "UpcomingFlightsSM.csv")
        os.remove(path)
        header = "flightNumber,departingFrom,arrivingAt,departure,arrival,captain,copilot,fsm,fa1,fa2,planeInsignia"

        with open(path, "a+", encoding="utf-8") as file:
            file.write(header)

        for x in voyages:
            if x[0] == selectedVoyage:
                pass
            else:
                if len(x) == 11:
                    newVoyage = VoyageSm(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10])
                    self.register_voyage_PM2(newVoyage)
                elif len(x) == 5:
                    newVoyage = Voyage(x[0], x[1], x[2], x[3], x[4])
                    self.register_voyage_PM(newVoyage)


    def csv_dictionary(self):
        dateDictionary = {}
        without_first= []
        path = os.path.join("Data", "UpcomingFlightsPM.csv")
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
        """ collects date from csv  and prints out a dictionary with each day and information  UI has to print out the dictionary
            return:dict
           """
        day_dict = {}
        without_first = []
        path = os.path.join("Data", "UpcomingFlightsPM.csv")

        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                without_first.append(row)

        for row in without_first:
            day = int(row[3].split("T")[0].split("-")[2])

            if day in day_dict:
                day_dict[day] += [[row[0], row[1], row[2]]]
            else:
                day_dict[day] = [[row[0], row[1], row[2]]]

        return day_dict

    def list_voyages_week(self):
        week_dict = {}
        without_first = []
        week1 = 7
        week2 = 14
        week3 = 21
        week4 = 28
        week5 = 32

        week1dict = {}
        week2dict = {}
        week3dict = {}
        week4dict = {}
        week5dict = {}

        day_dict = self.list_voyages_day()

        for key,value in day_dict.items():

            if key in range(0,week1):
                week1dict[key] = value
            if key in range(week1,week2):
                week2dict[key] = value
            if key in range(week2,week3):
                week3dict[key] = value
            if key in range(week3,week4):
                week4dict[key] = value
            if key in range(week4,week5):
                week5dict[key] = value

        """ þetta fall á ekki að prenta heldur á UI að prenta dictinarinu"""
        return "First Week: {}\nSecond week: {}\nThird week: {}\nFourth week: {}\nFifth week: {}".format(week1dict,week2dict,week3dict,week4dict,week5dict)