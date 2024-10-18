import sys
from functools import wraps


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner



#getting the command and the arguments from the user
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
#converting our dictionary to a string
def get_all_contacts(contacts: dict) -> str:
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."
#checking if the key exists in our dic, returning the value
def get_phone(name, contacts: dict) -> str:
    if name in contacts:
        return contacts[name]
    else:
        return ("There is no contact with such name")
    
#changing the value of the existing item in the dictionary
def change_contact(args, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

#adding new contact to existic dictionary
#checking for correct arguments amount
def add_contact(args, contacts: dict) -> str:
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid input. Usage: add username phone"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        #our only condition to exit
        if command in ["close", "exit"]:
            print("Good bye!")
            sys.exit(0)
        elif command == "hello":
            print("How can I help you?")
        #for each command below checking if the user 
        #is passing the right amount of arguments
        elif command == "add":
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print('Wrong syntax: add *username* *phone*')        
        elif command == "change":
            if len(args) == 2:
                if args[0] in contacts:
                    print(change_contact(args, contacts))
                else:
                    print("There is no contact with such name.")
            else:
                print("Wrong syntax: change *username* *phone*")     
        elif command == "phone":
            if len(args) == 1:
                print(get_phone(args[0], contacts))
            else:
                print('Wrong syntax: phone *username*')
        elif command == "all":
            if len(args) > 0:
                print('Wrong syntax: all')
            elif not contacts:
                print('No contacts found')
            else:
                print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()