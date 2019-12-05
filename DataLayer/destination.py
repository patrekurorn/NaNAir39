class Destination:

    def __init__(self, destinationID, country, airport, flightDuration, distanceFromIceland, contactName, contactNumber):
        
        self.destinationID = destinationID
        self.country = country
        self.airport = airport
        self.flightDuration = flightDuration
        self.distanceFromIceland = distanceFromIceland
        self.contactName = contactName
        self.contactNumber = contactNumber

    def __str__(self):
        return self.destinationID + "," + self.country + "," + self.airport + "," + self.flightDuration + "," \
            + self.distanceFromIceland + "," + self.contactName + "," + self.contactNumber

    def list_attributes(self):
        return [self.destinationID, self.country, self.airport, self.flightDuration, self.distanceFromIceland, \
            self.contactName, self.contactNumber]