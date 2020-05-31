import unittest
from bookshelf_object import Bookshelf


class BookTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.myBookshelf = Bookshelf("Favourite books", "Jan Kowalski", 10)
        self.myBookshelf.add_book("author2", "book title")

    def test_01__check_if_constructor_is_correct__return_BookShelf_instance(self):
        self.assertIsInstance(self.myBookshelf, Bookshelf,
                              msg="{} is not BookShelf instance.".format(self.myBookshelf))

    def test_02__check_if_book_was_correctly_added__return_true(self):
        author = "author2"
        title = "book title"

        self.assertTrue(self.myBookshelf.add_book(author, title),
                        msg="Book was not correctly added.")

    def test_03__check_if_taking_off_book_from_bookshelf_was_correct__return_true(self):
        book_author = "author"
        self.myBookshelf.add_book("author", "book title")

        self.assertTrue(self.myBookshelf.remove_book(book_author),
                        msg="Book was not correctly removed.")

    def test_04__check_if_bookshelf_rename_was_correct__return_true(self):
        new_name = "Horror books"

        self.assertTrue(self.myBookshelf.rename(new_name),
                        msg="{} was not rename".format(self.myBookshelf.name))

    def test_05__get_number_of_books_on_the_bookshelf__return_int(self):
        print("Books count: ", self.myBookshelf.books_count())

        self.assertIsInstance(self.myBookshelf.books_count(), int,
                              msg="Returned value by booksCount method "
                                  "was not an integer.")

    def test_06__check_current_available_bookshelf_size__return_int(self):
        print("Available space: ", self.myBookshelf.available_space())

        self.assertIsInstance(self.myBookshelf.available_space(), int,
                              msg="Returned value by availableSpace method"
                                  "was not an integer.")

    def test_07__check_if_bookshelf_is_empty_return_bool(self):
        self.assertIsInstance(self.myBookshelf.is_empty(), bool,
                              msg="Returned value by isEmpty method was not"
                                  "a bool.")


if __name__ == '__main__':
    unittest.main()
