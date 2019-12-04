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

    def get_destinatiodID(self):
        return self.destinationID

    def get_country(self):
        return self.country

    def get_airport(self):
        return self.airport

    def get_flightDuration(self):
        return self.flightDuration

    def get_distanceFromIceland(self):
        return self.distanceFromIceland

    def get_contactName(self):
        return self.contactName

    def get_contactNumber(self):
        return self.contactNumber