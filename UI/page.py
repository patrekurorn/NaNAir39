import os

class Page:
    def Clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def Last_input_valid_check(self):
        if self.valid == False:
            print("Please enter a valid number")
            self.valid = True

    def Print_header(self):
        print("___________________________________________________________\n" +
              "                        NaN Air                            \n" +
              "___________________________________________________________\n" +
              "-----------------------------------------------------------\n")

    def Print_footer(self):
        print("\n" +
              "-----------------------------------------------------------\n" +
              "___________________________________________________________\n" +
              "\n" +
              "                          _|_                              \n" +
              "                   *---o--(_)--o---*                       \n" +
              "___________________________________________________________")
