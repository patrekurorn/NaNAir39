VALID = ["1","2","3"]

class User:
    def __init__(self,first_pick = None, second_pick = None):
        self.first_pick = first_pick
        self.second_pick = second_pick

    def __repr__(self):
        return User()

    def __str__(self):
        return "{} {}".format(self.first_pick,self.second_pick)

    def home(self):
        userInput_str = input("1. Staff manager \n2. Planning manager \nYour pick: ")
        if userInput_str == "1" or userInput_str == "2":
            self.first_pick = userInput_str
            return self.first_pick

        else:
            print("Wrong input")
            return user.home()

    def second_window(self):

        def first_pick():
            pick_input = input("1. Man flights \n2. List of work force\n3. Manage work force\nYour pick: ")
            if pick_input not in VALID:
                print("wrong input")
                return first_pick()
            else:
                self.second_pick = pick_input
                return pick_input


        def second_pick():
            pick_input = input("1. Manage voyages\n2. List of voyages\n3. Manage destinations\Your pick: ")
            if pick_input not in VALID:
                print("wrong input")
                return second_pick()
            else:
                self.second_pick = pick_input
                return pick_input


        if self.first_pick == "1":
            first_pick()

        elif self.first_pick  == "2":
            second_pick()



    
    def get_header(self):
        print ("___________________________________________________________\n" + \
                "                        NaN Air                            \n" + \
                "___________________________________________________________\n" + \
                "-----------------------------------------------------------\n" + \
                "\n",end="")


    def get_footer(self):
        print("-----------------------------------------------------------\n" + \
                "___________________________________________________________\n" + \
                "\n" + \
                "                          _|_                              \n" + \
                "                   *---o--(_)--o---*                       \n" + \
                "___________________________________________________________")


user = User()
user.get_header()
user_selection = user.home()
user.get_footer()

user.second_window()
print(user)




