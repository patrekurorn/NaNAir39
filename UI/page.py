import os
import string

class Page:



    def __init__(self):
        self.valid = True
        self.blank_line = "|{:^59}|".format(" ")

    def _clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def _last_input_valid_check(self):
        if self.valid == False:
            print("Please enter a valid number")
            self.valid = True

    def _print_header(self, header):
        print(" ___________________________________________________________\n" +
              "|                        NaN Air                            |\n" +
              "|___________________________________________________________|\n" +
              "|-----------------------------------------------------------|")

        if header != None:
            # print("-" * 59)
            print("|{:^59}|".format(header))
            print("|-----------------------------------------------------------|")
        
        print(self.blank_line)

    def _print_footer(self):


        print(self.blank_line)
        print("|-----------------------------------------------------------|\n" +
              "|___________________________________________________________|")
        print(self.blank_line)
        print("|                          _|_                              |\n" +
              "|                   *---o--(_)--o---*                       |\n" +
              "|___________________________________________________________|")

    def _header(self, header = None):
        self._clear_screen()
        self._print_header(header)
    
    def _footer(self):
        self._print_footer()
        self._last_input_valid_check()
    
    def _options(self, lines):
        for line in lines:
            print("|{:<59}|".format(line))

    def show_page(self, lines, header = None):
        self._header(header)
        self._options(lines)
        self._footer()