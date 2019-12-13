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

    def header(self, i):
        """ prints a header on the user interface
            :param head:
        """

        print("-" * 50)
        print("|{:^48}|".format(i))
        print("-" * 50)
        print()


    def list_all_airplanes(self):
        """ List of all airplanes """
        
        page_width = 84
        self._clear_screen()
        header = "All airplanes"
        self._print_header(header, page_width)
        airplanes = self.__airplaneLL.get_all_airplanes()

        airplane_header =   "| {:<20} {:<20} {:<20} {:<10} {:<8} |\n".format("Plane insignia", "Type ID", "Manufacturer", "Model", "Capacity") + \
                            "| " + "-" * (page_width-2) + " |"
        print(airplane_header)
        

        plane_insignias = dict()
        for x in airplanes:
            plane_insignias[x[0]] = x[1]
            print("| {:<21}{:<21}{:<21}{:<11}{:<8} |".format(x[0], x[1], x[2], x[3], x[4]))

        

        print("| " + "-" * (page_width-2) + " |")
        self._footer(page_width, 'Type a plane insignia for a list of pilots permitted to fly the plane or "q" to quit')

        user_input = input().strip().upper()

        chose_quit = False
        while not chose_quit:
            if user_input == "Q":
                return True 
            if user_input in plane_insignias:
                chose_quit = self.__employeeUI.list_pilots_by_airplane(plane_insignias[user_input])
                print(plane_insignias[user_input])
            else:
                self.valid = False
                return False

        return False

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
                    inputed = input("Do you want to register this airplane? (Y/N) ").upper()

                    if inputed == "Y"  or inputed == "YES":
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
    a.available_airplanes()
