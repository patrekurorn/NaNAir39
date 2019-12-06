
class User:

    def __init__(self):
        pass

    def home(self):
        choice = ""
        get_header()

        print("1. Staff manager")
        print("2. Planning manager")
        print(get_feed())

        if choice == "1":
            print("1. Man flights")
            print("2. List of work force")
            print("3. Manage work force")
        if choice == "2":
            print("1. Manage voyages")
            print("2. List of voyages")
            print("3. Manage destinations")

