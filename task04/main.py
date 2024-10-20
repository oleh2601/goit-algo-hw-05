import sys
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide valid data"
        except IndexError:
            return "Please provide valid data."
        except TypeError:
            return "Please provide valid data."
        except KeyError:
            return "Please provide valid data."

    return inner

@input_error
def add_contact(args, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

        
@input_error
def get_all_contacts(contacts: dict) -> str:
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."
    

@input_error
def get_phone(args, contacts: dict) -> str:
    name = args[0]
    return contacts.get(name, "Contact not found")

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def change_contact(args, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

@input_error
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
                print(add_contact(args, contacts=contacts))     
            case "change":
                print(change_contact(args, contacts=contacts))  
            case "phone":
                print(get_phone(args, contacts=contacts))
            case "all":
                print(get_all_contacts(contacts=contacts))
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