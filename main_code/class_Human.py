
class Human:
    def __init__(self, fullname=None, address=None, phone_number=None):
        self.fullname = fullname
        self.address = address
        self.phone_number = phone_number

    def input_characters(self):
        #print('\n\033[48;5;240m If you want to go back to the menu, enter - [0]: \033[0;0m\n')
        self.fullname = input("Enter full name: ").title()

        # if self.fullname == 0:
        #     from main import choice
        #     return choice()

        self.address = input("Enter address: ").capitalize()
        while True:
            try:
                self.phone_number = input("Enter phone number: ")
                if not self.phone_number.isdigit():
                    raise Exception
                break
            except Exception as e:
                print('\n\033[48;5;88m Invalid input!!! Only digit\'s! \033[0;0m')

    def __str__(self):
        return f'{self.fullname}, {self.phone_number}'