# main.py

from contact import Contact, ContactBook


def print_menu() -> None:
    print("\n--- Contacts App ---")
    print("1. Add contact")
    print("2. View contact")
    print("3. Delete contact")
    print("4. List all contacts")
    print("5. Exit")


def add_contact_flow(book: ContactBook) -> None:
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name:
        print("Name cannot be empty. Contact not added.")
        return

    contact = Contact(name, phone, email)
    # If same name exists, this will overwrite (simple choice for this app)
    if book.has_contact(name):
        print("A contact with this name already exists. It will be updated.")
    book.add_contact(contact)
    print("Contact saved.")


def view_contact_flow(book: ContactBook) -> None:
    name = input("Enter name to view: ").strip()
    contact = book.get_contact(name)
    if contact:
        print("Contact details:")
        print(contact)
    else:
        print("No contact found with that name.")


def delete_contact_flow(book: ContactBook) -> None:
    name = input("Enter name to delete: ").strip()
    if book.delete_contact(name):
        print("Contact deleted.")
    else:
        print("No contact found with that name.")


def list_contacts_flow(book: ContactBook) -> None:
    contacts = book.list_contacts()
    if not contacts:
        print("No contacts saved.")
        return

    print("\nAll contacts:")
    for contact in contacts:
        print(contact)


def main() -> None:
    book = ContactBook()

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact_flow(book)
        elif choice == "2":
            view_contact_flow(book)
        elif choice == "3":
            delete_contact_flow(book)
        elif choice == "4":
            list_contacts_flow(book)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
