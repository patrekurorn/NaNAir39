import os
import string

class Page:

    def __init__(self):
        self.valid = True
        self.length = 60

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
        

        nan_air_header = self.get_formatable_line_center(length).format("NaN Air")

        print(  " " + "_" * length + "\n" +
                nan_air_header + "\n" +
                "|" + "_" * length + "|\n" +
                "|" + "-" * length + "|")

        if header != None:
            page_header = self.get_formatable_line_center(length).format(header)
            print(page_header)
            print("|" + "-" * length + "|")
        
        print(self.get_formatable_line_center(length).format(" "))

    def _print_footer(self, length, instructions):

        plane_tail = self.get_formatable_line_center(length).format("_|_")
        plane_main = self.get_formatable_line_center(length).format("*---o--(_)--o---*")

        if instructions == None:
            print("|" + " " * length + "|")
        else: 
            print(self.get_formatable_line_center(length).format(instructions))

        print("|" + "-" * length + "|\n" +
              "|" + "_" * length + "|")
        print("|" + " " * length + "|")
        print(plane_tail + "\n" +
              plane_main + "\n" +
              "|" + "_" * length + "|")

    def _header(self, header, length):
        self._clear_screen()
        self._print_header(header, length)
    
    def _footer(self, length, instructions):
        self._print_footer(length, instructions)
        self._last_input_valid_check()
    
    def _lines(self, lines, length):
        for line in lines:
            print(self.get_formatable_line_left(length).format(line))

    def show_page(self, lines, header = None, length = 60, instructions = None):
        
        self._header(header, length)
        self._lines(lines, length)
        self._footer(length, instructions)

    def get_formatable_line_center(self, length):
        return "|{:^" + str(length) + "}|"

    def get_formatable_line_left(self, length):
        return "|{:<" + str(length) + "}|"