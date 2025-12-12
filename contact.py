# contacts.py

from typing import Dict, List, Optional


class Contact:
    """
    Represents a single contact with name, phone, and email.
    """

    def __init__(self, name: str, phone: str, email: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return f"{self.name} | {self.phone} | {self.email}"

    def to_dict(self) -> Dict[str, str]:
        """
        Helper method to convert a contact to a dictionary.
        Useful if you later want to save/export.
        """
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }


class ContactBook:
    """
    Stores contacts in a dictionary keyed by name.

    This gives average-case O(1) time for add, search, and delete
    which is ideal for a contacts app.
    """

    def __init__(self) -> None:
        # key: name (string), value: Contact object
        self.contacts: Dict[str, Contact] = {}

    def add_contact(self, contact: Contact) -> None:
        """
        Add or update a contact.

        If a contact with the same name already exists, it will be replaced.
        """
        self.contacts[contact.name] = contact

    def get_contact(self, name: str) -> Optional[Contact]:
        """
        Return the contact with the given name, or None if not found.
        """
        return self.contacts.get(name)

    def delete_contact(self, name: str) -> bool:
        """
        Delete a contact by name.
        Returns True if deleted, False if it did not exist.
        """
        if name in self.contacts:
            del self.contacts[name]
            return True
        return False

    def list_contacts(self) -> List[Contact]:
        """
        Return a list of all contacts sorted by name (A-Z).
        """
        return [self.contacts[name] for name in sorted(self.contacts.keys())]

    def has_contact(self, name: str) -> bool:
        """
        Check if a contact exists by name.
        """
        return name in self.contacts
