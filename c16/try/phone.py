import cmd

class AddressBook(cmd.Cmd):
    intro = "Welcome to the Address Book. Type 'help' to see available commands."
    prompt = "AddressBook> "

    def __init__(self):
        super().__init__()
        self.contacts = {}

    def do_add(self, args):
        """Add a new contact. Usage: add <name> <phone>"""
        name, phone = args.split()
        if name not in self.contacts:
            self.contacts[name] = phone
            print(f"Added contact: {name} - {phone}")
        else:
            print(f"Contact {name} already exists. Use 'update' to change the phone number.")

    def do_list(self, args):
        """List all contacts."""
        if not self.contacts:
            print("No contacts found.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name} - {phone}")

    def do_update(self, args):
        """Update a contact's phone number. Usage: update <name> <new_phone>"""
        name, new_phone = args.split()
        if name in self.contacts:
            self.contacts[name] = new_phone
            print(f"Updated contact: {name} - {new_phone}")
        else:
            print(f"Contact {name} not found. Use 'add' to create a new contact.")

    def do_delete(self, args):
        """Delete a contact. Usage: delete <name>"""
        name = args
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted contact: {name}")
        else:
            print(f"Contact {name} not found.")

if __name__ == "__main__":
    AddressBook().cmdloop()

