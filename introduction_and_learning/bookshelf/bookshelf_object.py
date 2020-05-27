__all__ = [
    'Bookshelf'
]


class Bookshelf:
    def __init__(self, name: str, owner: str, size: int) -> None:
        """
        Bookshelf class constructor.

        Parameters
        ----------
        name: string, required
            Name of the Bookshelf instance.
        owner: string, required
            Bookshelf instance owner's name.
        size: int, required
            Amount of books that can be stored in Bookshelf instance.

        Example
        -------
        >>> my_bookshelf = Bookshelf("My books", "Jan Kowalski", 100)
        """

        self.name = name
        self.owner = owner
        self.maxSize = size
        self.books = {}
        self.currentBookNumber = 0

    def add_book(self, author: str, title: str) -> bool:
        """
        Insert in books dictionary new book as books[author] = title.

        Parameters
        ----------
        author: string, required
            Author of new added book.
        title: string, required
            Title of new added book.

        Returns
        -------
        Returns True if book was succesfull added or False on failure.

        Example
        -------
        >>> my_bookshelf.add_book("Aldous Huxley", "Brave new world")
        """

        self.books[author] = title

        if self.books[author] == title:
            self.currentBookNumber += 1
            return True
        else:
            return False

    def remove_book(self, author: str) -> bool:
        """
        Remove book from books dictionary by key which is author of the book.

        Parameters
        ----------
        author: sting, required
            Name of the book author.

        Returns
        -------
        Return True if book was successfully removed from books dictionary
        or False on failure and when key author does not exist in books.

        Example
        -------
        >>> my_bookshelf.remove_book("Aldous Huxley")
        """

        if self.books.pop(author, False):
            self.currentBookNumber -= 1
            return True
        else:
            return False

    def rename(self, name: str) -> bool:
        """
        Change current name of Bookshelf instance.

        Parameters
        ----------
        name: string, required
            New name for Bookshelf instance.

        Returns
        -------
        Return True if name was successfully change or False on failure.

        Example
        -------
        >>> my_bookshelf.rename("My new books")
        """

        self.name = name

        if self.name == name:
            return True
        else:
            return False

    def books_count(self) -> int:
        """
        Return amount of current books held in books dictionary.

        Returns
        -------
        Return Bookshelf's instance attribute which holds number of current
        stored books.

        Example
        -------
        >>> my_bookshelf.book_count()
        """

        return self.currentBookNumber

    def available_space(self) -> int:
        """
        Return amount of books that can be still held in books dictionary.

        Returns
        -------
        Result of subtraction Bookshelf instance attributes maxSize and
        currentBookNumber.

        Example
        -------
        >>> my_bookshelf.avaiable_space()
        """
        return self.maxSize - self.currentBookNumber

    def is_empty(self) -> bool:
        """
        Check if Bookshelf data structure books is empty.

        Returns
        -------
        Return True if books dictionary is has 0 elements or False if has
        more than 0 elements.
        """

        if self.books.__len__() == 0:
            return True
        else:
            return False
