class Voyage:
    def __init__(self, ID, destination_ID, flightOut, flightReturn, airplaneInsignia):
        self.ID = int(ID)
        self.destination_ID = str(destination_ID)
        self.flightOut = flightOut
        self.flightReturn = flightReturn
        self.airplaneInsignia = str(airplaneInsignia)

    def __str__(self):
        return "ID: {}\nDestination_ID: {}\nDeparture: {}\nArrival: {}\nAirplaneInsignia: {}\n".format(self.ID, self.destination_ID, self.flightOut, self.flightReturn, self.airplaneInsignia)
    
    def listAllByDate():
        return None

    def listAllByWeek():
        return None

a = Voyage(1,"Nuuk", "10:15", "12:15", "blah")
print(a)