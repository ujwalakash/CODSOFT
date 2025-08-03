class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        print("\n--- Add New Contact ---")
        store_name = input("Enter store name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")

        contact = {
            "store_name": store_name,
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contact_list(self):
        if not self.contacts:
            print("\nNo contacts to display.")
            return

        print("\n--- Contact List ---")
        for i, contact in enumerate(self.contacts):
            print(f"{i+1}. Name: {contact['store_name']}, Phone: {contact['phone_number']}")

    def search_contact(self):
        if not self.contacts:
            print("\nNo contacts to search.")
            return

        print("\n--- Search Contact ---")
        search_term = input("Enter name or phone number to search: ").lower()
        found_contacts = []

        for contact in self.contacts:
            if search_name_or_number(contact, search_term):
                found_contacts.append(contact)

        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("\n--- Search Results ---")
            for contact in found_contacts:
                display_contact_details(contact)

    def update_contact(self):
        if not self.contacts:
            print("\nNo contacts to update.")
            return

        self.view_contact_list()
        try:
            choice = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= choice < len(self.contacts):
                contact = self.contacts[choice]
                print(f"\n--- Update Contact: {contact['store_name']} ---")
                contact['store_name'] = input(f"Enter new store name (current: {contact['store_name']}): ") or contact['store_name']
                contact['phone_number'] = input(f"Enter new phone number (current: {contact['phone_number']}): ") or contact['phone_number']
                contact['email'] = input(f"Enter new email address (current: {contact['email']}): ") or contact['email']
                contact['address'] = input(f"Enter new address (current: {contact['address']}): ") or contact['address']
                print("Contact updated successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_contact(self):
        if not self.contacts:
            print("\nNo contacts to delete.")
            return

        self.view_contact_list()
        try:
            choice = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= choice < len(self.contacts):
                deleted_contact = self.contacts.pop(choice)
                print(f"Contact '{deleted_contact['store_name']}' deleted successfully!")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_contact_details(contact):
    print(f"\nStore Name: {contact['store_name']}")
    print(f"Phone Number: {contact['phone_number']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")

def search_name_or_number(contact, search_term):
    return search_term in contact['store_name'].lower() or search_term in contact['phone_number'].lower()

def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contact_list()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.update_contact()
        elif choice == '5':
            manager.delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()