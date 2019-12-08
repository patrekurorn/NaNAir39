

class Voyage:

    def __init__(self, flightNumber, departingFrom, arrivingAt, departure, arrival):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departureTime = departure
        self.arrivalTime = arrival

    def __str__(self):
        return "Flight number: {}\nDeparting from: {}\nArraving at: {}\nDeparture time: {}\nArrival time: {}".format(self.flightNumber,
                                                                                                                     self.departingFrom,
                                                                                                                     self.arrivingAt,
                                                                                                                     self.departureTime,
                                                                                                                     self.arrivalTime)

    """Getters"""
    def get_flight_number(self):
        return self.flightNumber

    def get_departing_from(self):
        return self.departingFrom

    def get_arriving_at(self):
        return self.arrivingAt

    def get_departure_time(self):
        return self.departureTime

    def get_arrival_time(self):
        return self.arrivalTime

    """Setters"""
    def set_flight_number(self,other):
        self.flightNumber = other

    def set_departing_from(self,other):
        self.departingFrom = other

    def set_arriving_at(self,other):
        self.arrivingAt = other

    def set_departure_time(self,other):
        self.departureTime = other

    def set_arrival_time(self,other):
        self.arrivalTime = other