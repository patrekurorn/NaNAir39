from Models.voyage import Voyage

class VoyageSm(Voyage):
    def __init__(self, flightNumber, departingFrom, arrivingAt, departure, arrival,captain,copilot,fsm,fa1,fa2):
        super.__init__(flightNumber, departingFrom, arrivingAt, departure, arrival)
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2


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





