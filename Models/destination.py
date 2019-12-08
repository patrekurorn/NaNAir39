

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
        return "Destination ID: {}\nCountry: {}\nAirport: {}\nFlight duration: {}\nDistance from Iceland: {}\nContact name: {}\nContact number: {}".format(self.destinationID, self.country,
                                                                         self.airport, self.flightDuration,
                                                                         self.distanceFromIceland, self.contactName,
                                                                         self.contactNumber)

    """ Getters """
    def get_destinationID(self):
        return self.destinationID

    def get_country(self):
        return self.country

    def get_airport(self):
        return self.airport

    def get_flightDuration(self):
        return self.flightDuration

    def get_distance_from_iceland(self):
        return self.distanceFromIceland

    def get_contact_name(self):
        return self.contactName

    def get_contact_number(self):
        return self.contactNumber

    """ Setters """
    def set_destinationID(self,other):
        self.destinationID = oth

    def set_country(self,other):
        self.country = other

    def set_airport(self,other):
        self.airport = other

    def set_flight_duration(self,other):
        self.flightDuration = other

    def set_distance_from_iceland(self,other):
        self.distanceFromIceland = other

    def set_contact_name(self,other):
        self.contactName = other

    def set_contact_number(self,other):
        self.contactNumber = other
