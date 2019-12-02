class Aircraft:
    def __init__(self, plane_insignia, planeTypeId):
        self.__plane_insignia = plane_insignia
        self.__planeTypeId = planeTypeId

    def __str__(self):
        return "Plane insignia: {}\nPlane Type ID: {}".format(self.__plane_insignia, self.__planeTypeId)
