class Airplane:
    def __init__(self, planeInsignia, planeTypeId):
        self.__planeInsignia = planeInsignia
        self.__planeTypeId = planeTypeId

    def __str__(self):
        return "Plane insignia: {}\nPlane Type ID: {}".format(self.__planeInsignia, self.__planeTypeId)

    def get_planeInsignia(self):
        return self.__planeInsignia

    def get_planeTypeId(self):
        return self.__planeTypeId

airplane = Airplane("TF-EPG","NAFokkerF100")
print(airplane)