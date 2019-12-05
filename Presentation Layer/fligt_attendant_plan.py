from employee import Employee

class Flight_Attendant_Plan:
    def __init__(self,id,voyage,flightAttendant):
        self.id = id
        self.voyage = voyage
        self.flightAttendant = flightAttendant

    def __str__(self):
        return "{}{}{}".format(self.id,self.voyage, self.flightAttendant)

    def get_id(self):
        return self.id

    def get_voyage(self):
        return self.voyage

    def get_flightAttendant(self):
        return self.flightAttendant
        