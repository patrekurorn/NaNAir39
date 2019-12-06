from Models.employee import Employee

class FlightAttendant(Employee):

    def __init__(self, rank):
        self.__rank = rank

    def get_rank(self):
        return self.__rank