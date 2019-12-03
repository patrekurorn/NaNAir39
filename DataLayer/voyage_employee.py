from DataLayer.employee import Employee

class Voyage_Employee(Emp):
    def __init__(self,id, voyage_id, pilot, copilot, flightServiceManager):
        self.id = id
        self.voyage_id = voyage_id
        self.pilot = pilot
        self.copilot = copilot
        self.flightServiceManager = flightServiceManager

    def __str__(self):
        return  "{} {} {} {} {}".format(self.id, self.voyage_id, self.pilot, self.copilot,self.flightServiceManager)




