class Voyage:
    def __init__(self, flightNumber, departingFrom, flightOut, flightReturn, airplaneInsignia):
        self.flightNumber = int(flightNumber)
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departure = departure
        self.arrival = arrival

    def __str__(self):
        return "Flight number: {}\nDeparting from: {}\nArriving at: {}\nDeparture: {}\nArrival: {}\n".format(self.flightNumber, self.departingFrom, self.arrivingAt, self.departure, self.arrival)
    
    def listAllByDate(self):
        return None

    def listAllByWeek(self):
        return None