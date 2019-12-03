class AirplaneType:
    def __init__(self, planeTypeId, manufacturer, model, capacity):
        self.__planeTypeId = planeTypeId
        self.__manufacturer = manufacturer
        self.__model = model
        self.__capacity = int(capacity)  # passenger seats

    def get_planeTypeId(self):
        return self.__planeTypeId

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_capacity(self):
        return self.__capacity

    def __str__(self):
        return "Plane Type ID: {}\nManufacturer: {}\nModel: {}\nCapacity: {}".format(self.__planeTypeId, self.__manufacturer, self.__model, self.__capacity)
    
airplane_type = AirplaneType("NABAE146","BAE","146",82)
print(airplane_type)
print()
print(airplane_type.get_capacity())
print(airplane_type.get_manufacturer())