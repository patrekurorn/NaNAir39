import os

class Page:
    def _clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def _last_input_valid_check(self):
        if self.valid == False:
            print("Please enter a valid number")
            self.valid = True

    def _print_header(self):
        print("___________________________________________________________\n" +
              "                        NaN Air                            \n" +
              "___________________________________________________________\n" +
              "-----------------------------------------------------------\n")

    def _print_footer(self):
        print("\n" +
              "-----------------------------------------------------------\n" +
              "___________________________________________________________\n" +
              "\n" +
              "                          _|_                              \n" +
              "                   *---o--(_)--o---*                       \n" +
              "___________________________________________________________")

    def header(self):
        self._clear_screen()
        self._print_header()
    
    def footer(self):
        self._print_footer()
        self._last_input_valid_check()