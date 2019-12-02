class Pilot:
    def __init__(self, rank, licence):
        self.__rank = rank
        self.__licence = licence

    def change_licence(self, other):
        self.__licence = other.licence

    def __str__(self):
        return "Pilot rank: {}\nPilot licence: {}".format(self.__rank, self.__licence)

pilot = Pilot("Captain", "F100")
print(pilot)