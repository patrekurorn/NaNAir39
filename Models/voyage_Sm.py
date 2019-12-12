from Models.voyage import Voyage

class VoyageSm(Voyage):
    def __init__(self,flightNumber,departingFrom,arrivingAt,departure,arrival,captain,copilot,fsm,fa1,fa2,planeInsignia):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departureTime = departure
        self.arrivalTime = arrival
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2
        self.planeInsignia = planeInsignia

    """Getters"""
    def get_flight_number(self):
        return self.flightNumber

    def get_departing_from(self):
        return self.departingFrom

    def get_arriving_at(self):
        return self.arrivingAt

    def get_departure_time(self):
        return self.departureTime

    def get_arrival_time(self):
        return self.arrivalTime

    def get_captain(self):
        return self.captain

    def get_copilot(self):
        return self.copilot

    def get_fsm(self):
        return self.fsm

    def get_fa1(self):
        return self.fa1

    def get_fa2(self):
        return self.fa2

    def get_planeInsignia(self):
        return self.planeInsignia

    """Setters"""
    def set_captain(self,other):
        self.captain = other

    def set_copilot(self,other):
        self.copilot = other

    def set_fsm(self,other):
        self.fsm = other

    def set_fa1(self,other):
        self.fa1 = other

    def set_fa2(self,other):
        self.fa2 = other

    def set_planeInsignia(self,other):
        self.planeInsignia = other

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





