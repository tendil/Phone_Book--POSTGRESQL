import csv
import sys

class Human:
    def __init__(self, name=None, last_name=None, address=None, phone_number=None, from_line=None):
        if from_line is None:
            self.name = name
            self.last_name = last_name
            self.address = address
            self.phone_number = phone_number

    def input_characters(self):
        self.name = input("Enter name: ").capitalize()
        self.last_name = input("Enter last name: ").capitalize()
        self.address = input("Enter address: ").capitalize()
        while True:
            try:
                self.phone_number = input("Enter phone number: ")
                if not self.phone_number.isdigit():
                    raise Exception
                print(self.phone_number)
                break
            except Exception as e:
                print('\nInvalid input!!! Only digit\'s!')


class Contacts:
    def find_human(self, query=None, query1=None, number=None):
        csv_file = csv.reader(open('date.csv', 'r'), delimiter=',')
        for row in csv_file:
            if query == row[0]:
                if query1 == row[1]:
                    print(row)
            if number == row[3]:
                print(row)
    def add_human(self):
        h = Human()
        h.input_characters()
        column_exist = False
        with open('date.csv', 'r') as file:
            if 'NAME,LAST NAME,ADDRESS,PHONE NUMBER\n' == file.readline():
                column_exist = True
                lst = (h.name, h.last_name, h.address, h.phone_number)
                with open('date.csv', 'a') as file:
                    writer = csv.writer(file, delimiter=',')
                    writer.writerow(lst)

        with open('date.csv', 'a') as file:
            writer = csv.writer(file, delimiter=',', lineterminator='\n')
            if not column_exist:
                writer.writerow(('NAME', 'LAST NAME', 'ADDRESS', 'PHONE NUMBER'))
            print(f'\nContact {h.name} {h.last_name} successfully added.)\n')

    def deleted_contacts(self, query):
        pass


    def show_all_contacts(self):
        with open('date.csv', 'r') as file:
            reader = csv.reader(file)
            for line in reader:
                print(f'{line}\n', "_-_-_-_-_-_-" * len(line))

    def choice_find_human(self):
        choice_find = (int(input
                           ('Select contact search mode.\n[1] - search for full name: \n[2] - search for phone number: '))
                       )
        if choice_find == 1:
            query = (input('To search for a contact, enter his name: ').capitalize())
            query1 = (input('To search for a contact, enter his last name: ').capitalize())
            print(c.find_human(query, query1))
        elif choice_find == 2:
            number = (input('To search for a contact, enter number phone: '))
            print(c.find_human(number))

def choice():
    sel = None
    try:
        sel = int(input('Search - "1"\n'
                        'New contact - "2"\n'
                        'Show all phone book - "3"\n'
                        'Deleted contact - "4"\n'
                        'Edit contact - "5"\n'
                        'EXIT - "0"\n'
                        '\nEnter --->: '))
    except ValueError:
        print('\n\nInvalid input!!!')
        print('You must enter an integer!!!\n\n')
    return sel

c = Contacts()

while True:
    sel = choice()
    if sel == 1:
        c.choice_find_human()

    #     choice_find = (int(input
    #         ('Select contact search mode.\n[1] - search for full name: \n[2] - search for phone number: '))
    #     )
    #     if choice_find == 1:
    #         query = (input('To search for a contact, enter his name: ').capitalize())
    #         query1 = (input('To search for a contact, enter his last name: ').capitalize())
    #         print(c.find_human(query, query1))
    #     elif choice_find == 2:
    #         number = (input('To search for a contact, enter number phone: ')



    elif sel == 0:
        sys.exit()

    elif sel == 2:
        c.add_human()

    elif sel == 3:
        c.show_all_contacts()

    elif sel == 4:
        query = ((input('To delete a contact, enter his last name and name: ').capitalize()))
        c.deleted_contacts(query)

    elif sel == 5:
        pass
