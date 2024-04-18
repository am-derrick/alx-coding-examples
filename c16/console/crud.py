import cmd

class AddressBook(cmd.Cmd):
    intro = "Welcome to my Adress Book. Type 'help' for  more info.\n"
    prompt = "(Address Book)> "

    def __init__(self):
        super().__init__()
        self.contacts = {}

    def do_add(self, args):
        """Adds a new contact. Usage: add <name> <phone>"""
        name, phone = args.split()
        if name not in self.contacts:
            self.contacts[name] = phone
            print(f"Contact added: {name} - {phone}")
        else:
            print(f"Contact {name} exists. Use 'update' to change contact details")

    def do_read(self, args):
        """Reads all contacts."""
        if not self.contacts:
            print("No contact found.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name} - {phone}")

    def do_update(self, args):
        """Updates a contact number. Usage: update <name> <new_phone>"""
        name, new_phone = args.split()
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"Contact updated: {name} - {new_phone}")
        else:
            print(f"{name} not found. Use 'add' to create new contact.")

    def do_delete(self, args):
        """Deletes a contact. Usage: delete <name>"""
        name = args
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print(f"{name} not found.")

    def do_exit(self, args):
        """Exits the address book"""
        return True

if __name__ == "__main__":
    AddressBook().cmdloop()
