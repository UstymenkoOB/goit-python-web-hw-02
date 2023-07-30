from AddressBook import *
from abc import ABC, abstractmethod


class Interface(ABC):

    @abstractmethod
    def action(self):
        pass


class Add(Interface):
    def __init__(self, book):
        self.book = book
        
    def action(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        self.book.add(record)


class Search(Interface):
    def __init__(self, book):
        self.book = book

    def action(self):
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = (self.book.search(pattern, category))
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result)


class Edit(Interface):
    def __init__(self, book):
        self.book = book

    def action(self):
        contact_name = input('Contact name: ')
        parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        return self.book.edit(contact_name, parameter, new_value)


class Remove(Interface):
    def __init__(self, book):
        self.book = book

    def action(self):
        pattern = input("Remove (contact name or phone): ")
        return self.book.remove(pattern)
    

class Save(Interface):
    def __init__(self, book):
        self.book = book

    def action(self):
        file_name = input("File name: ")
        return self.book.save(file_name)


class Load(Interface):
    def __init__(self, book):
        self.book = book

    def action(self):
        file_name = input("File name: ")
        return self.book.load(file_name)


class Congratulate(Interface):
    def __init__(self, book):
        self.book = book

    def action(self):
        print(self.book.congratulate())


class View(Interface):
    def __init__(self, book):
        self.book = book

    def action(self):
        print(self.book)


class Exit(Interface):
    def __init__(self, book):
        self.book = book

    def action(self):
        pass


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        actions = {"add": Add(self.book), "search": Search(self.book), "edit": Edit(self.book),
                   "remove": Remove(self.book), "save": Save(self.book), "load": Load(self.book),
                   "congratulate": Congratulate(self.book), "view":  View(self.book), "exit": Exit(self.book)}
        if action in actions:
            actions[action].action()
        else:
            print("There is no such command!")
