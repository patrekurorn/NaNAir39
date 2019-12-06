#from Models.employee import Employee


class Pilot(Employee):

    def __init__(self, licence, rank):
        self.__licence = licence
        self.__rank = rank

    def get_licence(self):
        return self.__licence

    def get_rank(self):
        return self.__rank

    def change_licence(self, other):
        self.__licence = other