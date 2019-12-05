

class Airplane:

    def __init__(self, planeInsignia, planeTypeId, manufacturer, model, capacity):
        self.__planeInsignia = planeInsignia
        self.__planeTypeId = planeTypeId
        self.__manufacturer = manufacturer
        self.__model = model
        self.__capacity = int(capacity)  # passenger seats

    def get_planeInsignia(self):
        return self.__planeInsignia

    def get_planeTypeId(self):
        return self.__planeTypeId

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def __str__(self):
        return "Plane insignia: {}\nPlane Type ID: {}\nPlane Type ID: {}\nManufacturer: {}\nModel: {}\nCapacity: {}".format(self.__planeInsignia, self.__planeTypeId, self.__planeTypeId, self.__manufacturer, self.__model, self.__capacity)

