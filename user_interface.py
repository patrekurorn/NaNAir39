
class User:

    def __init__(self):

        #self.header = get_header()
        #self.footer = get_footer()
        pass

    def home(self):
        choice = ""
<<<<<<< HEAD
        get_header()

        print("1. Staff manager")
        print("2. Planning manager")
        print(get_feed())
=======
        print(get_header())
        print("1. Staff manager")
        print("2. Planning manager")
        print(get_footer())

        choice = input().lower()
>>>>>>> ae12a843fcd26a40c4db111f5c8019fb81d5fe4a

        if choice == "1":
            print("1. Man flights")
            print("2. List of work force")
            print("3. Manage work force")
        if choice == "2":
            print("1. Manage voyages")
            print("2. List of voyages")
            print("3. Manage destinations")

    
    def get_header(self):
        return ("___________________________________________________________\n" + \
                "                        NaN Air                            \n" + \
                "___________________________________________________________\n" + \
                "-----------------------------------------------------------\n" + \
                "\n")


    def get_footer(self):
        return ("-----------------------------------------------------------\n" + \
                "___________________________________________________________\n" + \
                "\n" + \
                "                          _|_                              \n" + \
                "                   *---o--(_)--o---*                       \n" + \
                "___________________________________________________________")


user = User()

print(user.get_header())