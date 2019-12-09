class Airplane:

    def __init__(self, planeInsignia, planeTypeId, manufacturer, model, capacity):
        self.planeInsignia = planeInsignia
        self.planeTypeId = planeTypeId
        self.manufacturer = manufacturer
        self.model = model
        self.capacity = int(capacity)  # passenger seats


    def __str__(self):
        return "Plane insignia: {}\nPlane Type ID: {}\nManufacturer: {}\nModel: {}\nCapacity: {}".format(self.planeInsignia,
                                                                                                         self.planeTypeId,
                                                                                                         self.manufacturer,
                                                                                                         self.model,self.capacity)

    """Getters"""
    def get_plane_insignia(self):
        return self.planeInsignia

    def get_plane_type_id(self):
        return self.planeTypeId

    def get_manufacturer(self):
        return self.manufacturer

    def get_model(self):
        return self.model

    def get_capacity(self):
        return self.capacity

    """Setters"""
    def set_plane_insignia(self,other):
        self.planeInsignia = other

    def set_plane_type_id(self,other):
        self.planeTypeId = other

    def set_manufacturer(self,other):
        self.manufacturer = other

    def set_model(self,other):
        self.model = other

    def set_capacity(self,other):
        self.capacity = other
