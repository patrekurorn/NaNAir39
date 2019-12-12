from Models.airplane import Airplane
from LogicLayer.airplaneLL import AirplaneLL
from UI.employeeUI import EmployeeUI
from LogicLayer.voyageLL import VoyageLL
from UI.page import Page

class AirplaneUI(Page):

    def __init__(self):
        self.__airplaneLL = AirplaneLL()
        self.__employeeUI = EmployeeUI()
        self.__voyageLL = VoyageLL()
        super().__init__()


    def list_all_airplanes(self):
        """ List of all airplanes """
        
        header = "All airplanes"
        self._print_header(header)
        airplanes = self.__airplaneLL.get_all_airplanes()

        header = "\n{:<5} {:>12} {:>28} {:>8} {:>10}\n".format("Plane insignia", "Type ID", "Manufacturer", "Model", "Capacity")

        print(header)

        for x in airplanes:
            print("{:<16}\t{:<20}\t{:<15}\t{:<5}\t{:<5}".format(x[0], x[1], x[2], x[3], x[4]))

        plane = input().strip()

        return True

    def register_airplane(self):
        """ Registers a new airplane in csv file """

        self.header("Registering a new airplane")

        isValid = True
        while isValid:
            planeInsignia = input("\nEnter plane insignia: ")
            if self.__airplaneLL.check_airplane(planeInsignia):
                print("\nAirplane already exists.\n")
                choice = input("Y: Yes\nAnything else: No\nDo you want to continue? ").upper()
                if choice == "Y":
                    continue
                else:
                    break

            else:
                try:
                    planeTypeId = input("Enter plane type ID: ")
                    manufacturer = input("Enter manufacturer: ")
                    model = input("Enter model: ")
                    capacity = int(input("Enter capacity: "))

                    new_airplane = Airplane(planeInsignia, planeTypeId, manufacturer, model, capacity)
                    print("\n{}\n".format(new_airplane))
                    inputed = input("Do you want to register this airplane?").upper()

                    if inputed == "Y".upper()  or inputed == "YES":
                        self.__airplaneLL.register_airplane(new_airplane)
                        print("\nNew airplane registered!\n")
                        choice = input("Y: Yes\nAnything else: No\nDo you want to continue? ").upper()
                        if choice == "Y":
                            continue
                        else:
                            break
                    else:
                        print("\nAirplane not registered.\n")
                        choice = input("Y: Yes\nAnything else: No\nDo you want to continue? ").upper()
                        if choice == "Y":
                            continue
                        else:
                            break
                except:
                    print("\nInvalid input.\n")
                    choice = input("Y: Yes\nAnything else: No\nDo you want to continue? ").upper()
                    if choice == "Y":
                        continue
                    else:
                        break

    def available_airplanes(self):
        """ Lists available airplanes for a given date. """

        self.header("Available airplanes")

        isValid = True
        while isValid:

            date = self.__employeeUI.get_date()

            available = self.__airplaneLL.available_airplanes(date)

            print("\nAvailable airplanes on {}".format(date))
            header = "{:<5}".format("Airplane insignia")
            print("{}\n".format(header))

            for i, row in enumerate(available):
                print("{}.\t{}".format(i+1, row))

            choice = input("\nY: Yes\nAnything else: No\nWould you like to enter another date? ").upper()
            if choice == "Y":
                continue
            else:
                break


if __name__ == "__main__":
    a = AirplaneUI()
    a.register_airplane()
