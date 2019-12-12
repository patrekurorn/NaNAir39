
from DataLayer.destinationDL import DestinationDL

class DestinationsLL(object):

    def __init__(self):
        self.__destinationDL = DestinationDL()


    def get_all_destinations(self):
        return self.__destinationDL.get_all_destinations()


    def check_destination(self, id):
        return self.__destinationDL.check_destination(id)


    def register_destination(self, new_destination):
        return self.__destinationDL.register_destination(new_destination)


    def get_destination(self, id):    # list information about a specific destination.
        return self.__destinationDL.get_destination(id)

    def remove_destination(self, id):
        return self.__destinationDL.remove_destination(id)




if __name__ == "__main__":
    a = DestinationsLL()
    print(a.get_all_destinations())

