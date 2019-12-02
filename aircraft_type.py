class AircraftType:
    def __init__(self,planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan):
        self.__planeTypeId = planeTypeId
        self.__planeType = planeType
        self.__model = model
        self.__capacity = int(capacity)  # passenger seats
        self.__emptyWeight = int(emptyWeight)
        self.__maxTakeoffWeight = int(maxTakeoffWeight)
        self.__unitThrust = float(unitThrust)
        self.__serviceCeiling = int(serviceCeiling)
        self.__length = float(length)
        self.__height = float(height)
        self.__wingspan = float(wingspan)

    