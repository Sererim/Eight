# Read data from files or input from a command line
# Check input file for common separators (/n, :, _, =, and etc.)
# Put it into a standartize file and read from it if user wants to
# Table inside the phonebook file database 
# | ID  |  Surename  |  Name  | Patronym  |  Phone            |
# | 1   |  Ivanov    |  Ivan  | Ivanovich | +7(900)-000-00-00 |
#  .............................................
# ..............................................


class PhoneBook():
    
    _separators = ('\n', '_', '.', ',', '~', ':', ';',
                   '%', '@', '!', '#', '=','+','<','>')
    
    _std_file_name = ("file.txt", "input.txt", "phone.txt")
    
    _output_file_name = ("phonebook.txt")
    
    def __init__(self) -> None:
        pass
    
    def open_and_read_from_file(self) -> None:
        pass
    
    def clean_file_and_prepear_it(self) -> None:
        pass
    
    def print_from_standart_file(self) -> None:
        pass
    
    def put_into_standart_file(self) -> None:
        pass
    
    def mainloop(self) -> None:
        pass
    
    
def main() -> int:
    
    book = PhoneBook()
    book.mainloop()
    
    return 0


if __name__ == "__main__":
    main()