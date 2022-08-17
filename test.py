class Human:
    def __init__(self, last_name=None, name=None, address=None, phone_number=None, from_line=None):
        if from_line is None:
            self.last_name = last_name
            self.name = name
            self.address = address
            self.phone_number = phone_number
        else:
            self.last_name, self.name, self.address, self.phone_number = str(from_line).replace(" ", '').split("|")

        def __str__(self):
            return 'Member("{}", "{}", "{}", "{}")'.format(self.last_name, self.name, self.address, self.phone_number)

    def input_characters(self):
        self.last_name = input("Enter last name: ").capitalize()
        self.name = input("Enter name: ").capitalize()
        self.address = input("Enter address: ").capitalize()
        self.phone_number = input("Enter phone number: ")

    def __str__(self):
        return 'Human --> "{}" - "{}" - "{}" - {}'.format(self.last_name, self.name, self.address, self.phone_number)


class Contacts:

    def find_human(self, query=None):
        with open('base.txt') as file:
            for line in file:
                human = Human(from_line=line)
                print(human)
                if human.last_name == query:
                    return human

    def add_human(self):
        h = Human()
        h.input_characters()
        if c.find_human(query=(h.last_name, h.name)) is None:
            f = open('base.txt', 'a')
            f.write('{0:10} | {1:10} | {2} | {3}'.format(h.last_name, h.name, h.address, h.phone_number) + '\n')
            print('\nContact {last_name} {name} successfully added\n'.format(last_name=h.last_name, name=h.name))
            f.close()
        # else:
        #     print('This contact already exists.')

    def deleted_contacts(self, query):
        global human
        objects = []
        f = open('base.txt', 'r+')
        for line in f.readline():
            human = Human(from_line=line)
            objects.append(human)
        for object in objects:
            if (human.last_name, human.name) != query:
                f.write(object.__str__())

    def show_all_contacts(self):
        with open('base.txt') as file:
            for line in file:
                human = Human(from_line=line)
                print(human)



def choice():
    sel = None
    try:
        sel = int(input('Search - "1"\n' + \
                        'New contact - "2"\n' + \
                        'Show all phone book - "3"\n' + \
                        'Deleted contact - "4"\n' + \
                        'Edit contact - "5"\n' + \
                        '\nEnter --->: '))
    except ValueError:
        print('\n\nInvalid input!!!')
        print('You must enter an integer!!!\n\n')
    return sel


c = Contacts()

while True:
    sel = choice()
    if sel == 1:
        query = (input('To search for a contact, enter his full name: ').capitalize())
        print(c.find_human(query))

    elif sel == 2:
        c.add_human()

    elif sel == 3:
        c.show_all_contacts()

    elif sel == 4:
        query = ((input('To delete a contact, enter his last name and name: ').capitalize()))
        c.deleted_contacts(query)

    elif sel == 5:
        pass