class Voyage:
    def __init__(self, ID, destinationID, flightOut, flightReturn, airplaneInsignia):
        self.ID = int(ID)
        self.destinationID = str(destinationID)
        self.flightOut = flightOut
        self.flightReturn = flightReturn
        self.airplaneInsignia = str(airplaneInsignia)

    def __str__(self):
        return "ID: {}\nDestination ID: {}\nDeparture: {}\nArrival: {}\nAirplaneInsignia: {}\n".format(self.ID, self.destinationID, self.flightOut, self.flightReturn, self.airplaneInsignia)
    
    def listAllByDate(self):
        return None

    def listAllByWeek(self):
        return None