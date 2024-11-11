from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):

    def setUp(self) -> None:
        self.l = Library("Name")
        self.l1 = Library("Name1")

    def test_empty_entry_data_name_only(self):
        self.assertEqual('Name1', self.l1.name)
        self.assertEqual({}, self.l1.readers)
        self.assertEqual({}, self.l1.books_by_authors)

    def test_name_to_be_empty(self):
        with self.assertRaises(ValueError) as error:
            Library('')
        self.assertEqual('Name cannot be empty string!', str(error.exception))

    def test_adding_book_proper(self):
        self.l.add_book("Gosho", "Story1")
        self.assertEqual({'Gosho': ['Story1']}, self.l.books_by_authors)

    def test_adding_book_proper_with_author_already_exist(self):
        self.l.add_book("Gosho", "Story1")
        self.l.add_book("Gosho", "Story2")
        self.assertEqual({'Gosho': ['Story1', 'Story2']}, self.l.books_by_authors)

    def test_adding_book_all_empty(self):
        self.l.add_book("", "")
        self.assertEqual({'': ['']}, self.l.books_by_authors)

    def test_add_reader_proper(self):
        self.l.add_reader("Gosho")
        self.assertEqual({'Gosho': []}, self.l.readers)

    def test_add_same_reader_twice(self):
        self.l.add_reader("Gosho")
        result = self.l.add_reader("Gosho")
        self.assertEqual('Gosho is already registered in the Name library.', result)

    def test_rent_book_proper(self):
        self.l.add_reader("Gosho")
        self.l.add_book("Ivan", "Test")
        self.l.rent_book('Gosho', 'Ivan', 'Test')
        self.assertEqual({'Gosho': [{'Ivan': 'Test'}]}, self.l.readers)
        self.assertEqual({'Ivan': []}, self.l.books_by_authors)

    def test_rent_book_no_reader(self):
        self.l.add_reader("Plamen")
        self.l.add_book("Ivan", "1")
        result = self.l.rent_book('Plamena', 'Ivan', '1')
        self.assertEqual('Plamena is not registered in the Name Library.', result)

    def test_rent_book_no_author(self):
        self.l.add_reader("Plamen")
        self.l.add_book("Ivan", "1")
        result = self.l.rent_book('Plamen', 'Ivo', '1')
        self.assertEqual("Name Library does not have any Ivo's books.", result)

    def test_rent_book_no_title(self):
        self.l.add_reader("Plamen")
        self.l.add_book("Ivan", "1")
        result = self.l.rent_book('Plamen', 'Ivan', '2')
        self.assertEqual('''Name Library does not have Ivan's "2".''', result)


if __name__ == '__main__':
    main()