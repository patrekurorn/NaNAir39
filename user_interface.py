VALID = ["1","2","3"]

class User:

    def __init__(self):

        #self.header = get_header()
        #self.footer = get_footer()
        pass

    def home(self):
      #  choice = ""
        userInput_str = input("1. Staff manager \n2. Planning manager \nYour pick: ")
        if userInput_str == "1":
            return "1"
        elif userInput_str == "2":
            return "2"
        else:
            print("Wrong input")
            return user.home()

       # print(get_feed())
      #  print(get_header())
      #  print("1. Staff manager")
      #  print("2. Planning manager")
      #  print(get_footer())

   #     choice = input().lower()
   #     def choice1(self):

    def pick(self,pick):
        def first_pick(pick):
            pick_input = input("1. Man flights \n2. List of work force\n3. Manage work force")
            if pick_input not in VALID:
                print("wrong input")
                return first_pick(pick)
            else:
                return pick_input

        def second_pick(pick):
            pick_input = input("1. Manage voyages\n2. List of voyages\n3. Manage destinations")
            if pick_input not in VALID:
                print("wrong input")
                second_pick(pick)
            else:
                return pick_input

        if pick == "1":
            first_pick(pick)  
        elif pick == "2":
            second_pick(pick)

   #     if choice == "1":
   #         print("1. Man flights")
   #         print("2. List of work force")
   #         print("3. Manage work force")

   #     def choice2)
   #     if choice == "2":
   #         print("1. Manage voyages")
   #         print("2. List of voyages")
   #         print("3. Manage destinations")

    
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
user_pick = user.home()
user.get_footer()
next_selection = user.pick(user_pick)




