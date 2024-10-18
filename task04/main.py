import sys
from functools import wraps

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide name and phone."
        except IndexError:
            return "Please provide name and phone."

    return inner

@input_error
def add_contact(args, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def get_all_contacts_error(func):
    def wrapper(contacts):
        try:
            if not contacts:
                return "No contacts found."
            return func(contacts)
        except TypeError:
            return "No contacts found."
    return wrapper
        
@get_all_contacts_error
def get_all_contacts(contacts: dict) -> str:
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    
def get_phone_error(func):
    def wrapper(*args):
        try:
            if not args or not args[0]:
                return "Please provide the name of the contact."
            name_args = args[0]
            if not name_args:
                return "Please provide the name of the contact."
            name = name_args[0]
            contacts = args[1]
            return func(name, contacts)  
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Please provide the name of the contact."
        except TypeError:
            return "Please provide the name of the contact."
    return wrapper

@get_phone_error
def get_phone(name, contacts: dict) -> str:
    return contacts[name]

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def change_contact_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide name and phone."
        except IndexError:
            return "Please provide name and phone."
        except TypeError:
            return "Please provide name and phone."

    return inner

@change_contact_error
def change_contact(args, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact changed."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:

        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        match command:
            case "close" | "exit":
                print("Good bye!")
                sys.exit(0)
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))     
            case "change":
                print(change_contact(args, contacts))  
            case "phone":
                print(get_phone(args, contacts))
            case "all":
                print(get_all_contacts(contacts))
            case "help":
                print('Available commands: \n'
                      '  "add" username number \n'
                      '  "all" \n'
                      '  "change" username number \n'
                      '  "close" \n'
                      '  "exit" \n'
                      '  "help" \n'
                      '  "hello" \n'
                      '  "phone" username \n'
                       )
            case _:
                print("I don't know this command.\n"
                      "Use 'help' to get the list of all commands."
                      )

if __name__ == "__main__":
    main()