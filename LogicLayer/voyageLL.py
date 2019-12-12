import csv
from Models.voyage import Voyage
from DataLayer.voyageDL import VoyageDL
from Models.voyage_Sm import VoyageSm
import os
import pathlib


class VoyageLL:

    def __init__(self):
        self.__voyageDL = VoyageDL()


    def get_voyage(self, flightNumber):
        return self.__voyageDL.get_voyage(flightNumber)



    def get_all_upcoming_voyages(self):  # display voyages
        return self.__voyageDL.get_all_upcoming_voyages()



    def check_flight_number(self, flightNumber):
        return self.__voyageDL.check_flight_number(flightNumber)



    def register_voyage_PM(self, new_voyage):  # Planning manager gerir þetta
        return self.__voyageDL.register_voyage_PM(new_voyage)


    def list_unmanned_voyages(self):
         pass


    def list_available_dates(self):
         pass


    def list_available_times(self):
         pass


    def voyage_repetition(self):
         pass


    def edit_voyage(self):
         pass


    def edit_time(self):
         pass


    def edit_date(self):
         pass




    def cancel_voyage(self, flightNumber):
        return self.__voyageDL.cancel_voyage(flightNumber)



    def csv_dictionary(self):
        return self.__voyageDL.csv_dictionary()


    def list_voyages_day(self):
        return self.__voyageDL.list_voyages_day()


    def list_voyages_week(self):
        return self.__voyageDL.list_voyages_week()

if __name__ == "__main__":
    a = VoyageLL()

