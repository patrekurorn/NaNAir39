

class  Voyage:

    def __init__(self, flightNumber, departingFrom, arrivingAt, departure, arrival):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departure = departure
        self.arrival = arrival

    def __str__(self):
        return "{} {} {} {} {}".format(self.flightNumber, self.departingFrom, self.arrivingAt, self.departure, self.arrival)
    
    def get_flightNumber(self):
        return self.flightNumber

    def get_departingFrom(self):
        return self.departingFrom

    def get_arrivingAt(self):
        return self.arrivingAt

    def get_departure(self):
        return self.departure

    def get_arrival(self):
        return self.arrival