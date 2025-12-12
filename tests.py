# tests.py

import unittest
from contact import Contact, ContactBook


class TestContact(unittest.TestCase):
    def test_contact_creation(self):
        c = Contact("Alice", "123", "alice@example.com")
        self.assertEqual(c.name, "Alice")
        self.assertEqual(c.phone, "123")
        self.assertEqual(c.email, "alice@example.com")

    def test_contact_str(self):
        c = Contact("Bob", "456", "bob@example.com")
        self.assertEqual(str(c), "Bob | 456 | bob@example.com")


class TestContactBook(unittest.TestCase):
    def test_add_and_get_contact(self):
        book = ContactBook()
        c = Contact("Alice", "123", "alice@example.com")
        book.add_contact(c)
        self.assertTrue(book.has_contact("Alice"))
        retrieved = book.get_contact("Alice")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.phone, "123")

    def test_get_missing_contact(self):
        book = ContactBook()
        self.assertIsNone(book.get_contact("Bob"))

    def test_delete_contact(self):
        book = ContactBook()
        c = Contact("Alice", "123", "alice@example.com")
        book.add_contact(c)
        deleted = book.delete_contact("Alice")
        self.assertTrue(deleted)
        self.assertFalse(book.has_contact("Alice"))

    def test_delete_missing_contact(self):
        book = ContactBook()
        deleted = book.delete_contact("Charlie")
        self.assertFalse(deleted)

    def test_list_contacts_sorted(self):
        book = ContactBook()
        book.add_contact(Contact("Charlie", "333", "c@example.com"))
        book.add_contact(Contact("Alice", "111", "a@example.com"))
        book.add_contact(Contact("Bob", "222", "b@example.com"))

        contacts = book.list_contacts()
        names = [c.name for c in contacts]
        self.assertEqual(names, ["Alice", "Bob", "Charlie"])

    def test_list_contacts_empty(self):
        book = ContactBook()
        contacts = book.list_contacts()
        self.assertEqual(len(contacts), 0)


if __name__ == "__main__":
    unittest.main()
