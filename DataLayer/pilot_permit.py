class PilotPermit:
    def __init__(self, pilotID, pilot, allowedPlaneType):
        self.__pilotID = int(pilotID)
        self.__pilot = pilot
        self.__allowedPlaneType = allowedPlaneType

    def ChangeLicence(self, allowedPlaneType):
        self.__allowedPlaneType = allowedPlaneType

    def __str__(self):
        return "Pilot rank: {}\nPilot ID: {}\nPilot licence: {}".format(self.__pilot, self.__pilotID, self.__allowedPlaneType)

    def get_pilotID(self):
        return self.__pilotID

    def get_pilot(self):
        return self.__pilot

    def get_allowedPlaneType(self):
        return self.__allowedPlaneType

pilot = PilotPermit(123, "Captain", "F100")
print(pilot)
print()
pilot.ChangeLicence("F230")
print(pilot)

print()

print(pilot.get_allowedPlaneType())