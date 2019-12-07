

class Voyage:

    def __init__(self, flightNumber, departingFrom, arrivingAt, departure, arrival):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departureTime = departure
        self.arrivalTime = arrival

    def __str__(self):
        return "{} {} {} {} {}".format(self.flightNumber, self.departingFrom, self.arrivingAt, self.departure_time, self.arrival_time)

    """Getters"""
    def get_flight_number(self):
        return self.flightNumber

    def get_departing_from(self):
        return self.departingFrom

    def get_arriving_at(self):
        return self.arrivingAt

    def get_departure(self):
        return self.departure_time

    def get_arrival(self):
        return self.arrival_time

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