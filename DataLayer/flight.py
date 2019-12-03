class Flight:

    def __init__(self, flightID, seatsSold, departingFrom, destinationID, arrival):

        self.flightID = flightID
        self.seatsSold = seatsSold
        self.departingFrom = departingFrom
        self.destinationID = destinationID
        self.arrival = arrival

    def __str__(self):
        return self.flightID + " " + self.departingFrom + " " + self.arrival