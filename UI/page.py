import os
import string

class Page:



    def __init__(self):
        self.valid = True
        self.length = 60
        self.formatable_line_centered = "|{:^" + str(self.length) + "}|"
        self.formatable_line_left = "|{:<" + str(self.length) + "}|"

    def _clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def _last_input_valid_check(self):
        if self.valid == False:
            print("Please enter a valid number")
            self.valid = True

    def _print_header(self, header, length):

        nan_air_header = self.formatable_line_centered.format("NaN Air")

        print(  " " + "_" * length + "\n" +
                nan_air_header + "\n" +
                "|" + "_" * length + "|\n" +
                "|" + "-" * length + "|")

        if header != None:
            page_header = self.formatable_line_centered.format(header)
            print(page_header)
            print("|" + "-" * length + "|")
        
        print(self.formatable_line_centered.format(" "))

    def _print_footer(self, length):

        plane_tail = self.formatable_line_centered.format("_|_")
        plane_main = self.formatable_line_centered.format("*---o--(_)--o---*")

        print("|" + " " * length + "|")
        print("|" + "-" * length + "|\n" +
              "|" + "_" * length + "|")
        print("|" + " " * length + "|")
        print(plane_tail + "\n" +
              plane_main + "\n" +
              "|" + "_" * length + "|")

    def _header(self, header, length):
        self._clear_screen()
        self._print_header(header, length)
    
    def _footer(self, length):
        self._print_footer(length)
        self._last_input_valid_check()
    
    def _lines(self, lines, length):
        for line in lines:
            print(self.formatable_line_left.format(line))

    def show_page(self, lines, header = None, length = 60):
        self._header(header, length)
        self._lines(lines, length)
        self._footer(length)