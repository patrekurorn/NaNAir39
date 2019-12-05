class Flight:

    def __init__(self, flightID, seatsSold, departingFrom, destinationID, arrival):

        self.flightID = flightID
        self.seatsSold = seatsSold
        self.departingFrom = departingFrom
        self.destinationID = destinationID
        self.arrival = arrival

    def __str__(self):
        return self.flightID + "," + self.seatsSold + "," + self.departingFrom + "," + destinationID + "," + self.arrival

    def get_flightID(self):
        return self.flightID

    def get_seatsSold(self):
        return self.seatsSold

    def get_departingFrom(self):
        return self.departingFrom

    def get_destinationID(self):
        return self.destinationID

    def get_arrival(self):
        return self.arrival
        