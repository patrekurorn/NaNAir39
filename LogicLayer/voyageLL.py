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

    def get_only_voyages(self):
        return self.__voyageDL.get_only_voyages()



    def check_flight_number(self, flightNumber):
        return self.__voyageDL.check_flight_number(flightNumber)



    def register_voyage_PM(self, new_voyage):  # Planning manager gerir þetta
        return self.__voyageDL.register_voyage_PM(new_voyage)


    def register_voyage_PM2(self, new_voyage):  # Þarf að vera 2 svona svo cancel_voyage fokkist ekki upp
        return self.__voyageDL.register_voyage_PM2(new_voyage)


    def check_if_busy(self, date, ssn):
        return self.__voyageDL.check_if_busy(date, ssn)


    def list_unmanned_voyages(self):
        all_voyages = self.__voyageDL.get_all_voyages_after_current_date()

        all_unmanned_voyages = []
        
        for voyage in all_voyages:
            if  voyage[5] == "-" or voyage[6] == "-" or voyage[7] == "-" or \
                voyage[8] == "-" or voyage[9] == "-" or voyage[10] == "-":
                all_unmanned_voyages.append(voyage)

        return all_unmanned_voyages

    def list_available_dates(self):
         pass


    def list_available_times(self):
         pass


    def voyage_repetition(self):
         pass


    def edit_voyage(self,voyageName,date,time,selectedVoyageData,editNumber):
        return self.__voyageDL.edit_voyage_date(voyageName,date,time,selectedVoyageData,editNumber)




    def edit_time(self):
         pass


    def edit_date(self):
         pass




    def cancel_voyage(self, flightNumber):
        return self.__voyageDL.cancel_voyage(flightNumber)



    def csv_dictionary(self):
        return self.__voyageDL.csv_dictionary()


    def list_voyages_day(self, date):     # checkar hvort voyage sé fullmönnuð á ákveðnum degi
        return self.__voyageDL.list_voyages_day(date)


    def list_voyages_week(self, date):    # checkar hvort voyage sé fullmönnuð í ákveðinni viku
        return self.__voyageDL.list_voyages_week(date)


if __name__ == "__main__":
    a = VoyageLL()
    a.edit_date()