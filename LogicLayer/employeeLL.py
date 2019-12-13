import csv
import os
from Models.employee import Employee
from DataLayer.employeeDL import EmployeeDL
from DataLayer.voyageDL import VoyageDL
from datetime import timedelta, datetime, date


class EmployeeLL:

    def __init__(self):
        self.__employeeDL = EmployeeDL()
        self.__voyageDL = VoyageDL()


    def get_all_employees(self):
        return self.__employeeDL.get_all_employees()


    def ssn_valid(self, ssn):
        return self.__employeeDL.ssn_valid(ssn)


    def get_employee(self, ssn):    # list information about a specific employee.
        return self.__employeeDL.get_employee(ssn)


    def print_employee(self, ssn):
        data = self.get_all_employees()

        if self.ssn_valid(ssn):
            for row in data:
                if row[0] == ssn:
                    return "\n   SSN: \t\t\t{}\n1. Name: \t\t\t{}\n2. Position: \t\t{}\n3. Rank: \t\t\t{}\n4. Licence: \t\t{}\n5. Address: \t\t{}\n6. Mobile: \t\t\t{}\n7. Landline nr: \t{}\n8. Email: \t\t\t{}".format(row[0],row[1],
                                                                                                                                                                                            row[2], row[3],
                                                                                                                                                                                            row[4],row[5],
                                                                                                                                                                                            row[6],row[7],
                                                                                                                                                                                            row[8])
        else:
            return False



    def register_employee(self, new_employee):
        return self.__employeeDL.register_employee(new_employee)


    def list_all_pilots(self):
        return self.__employeeDL.list_all_pilots()


    def list_airplane_by_pilot(self, ssn):
        return self.__employeeDL.list_airplane_by_pilot(ssn)


    def list_pilots_by_airplane(self, licence):
        return self.__employeeDL.list_pilots_by_airplane(licence)


    def list_all_flight_attendants(self):
        return self.__employeeDL.list_all_flight_attendants()


    def remove_employee(self, ssn):
        return self.__employeeDL.remove_employee(ssn)


    def print_week_of_employee(self, date, ssn_employee):  # A printable work summary can be displayed showing all employee work trips in a given week.
        voyages = self.__voyageDL.get_all_upcoming_voyages()
        return self.__employeeDL.print_week_of_employee(date, voyages, ssn_employee)


    def get_week_list(self):
        pass







if __name__ == "__main__":
    a = EmployeeLL()
    a.get_week_list()


