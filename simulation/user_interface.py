__all__ = [
    'UserInterface',
]


class UserInterface:
    """
    Class which contains methods to output friendly console interface to user.
    """
    @staticmethod
    def ask_parameter(question: str) -> str:
        """
        Wrapper to input() build in method.

        Parameters
        ----------
        question: str, required
            Text display to user when ask for input.

        Returns
        -------
        Return string which is user input.

        Example
        -------
        >>> ask_parameter("How old are you?")
        """
        return input(question)

    @staticmethod
    def draw_title(title: str) -> None:
        """
        Method draw outstand title and check if given parameter is string if
        not raise TypeError.

        Parameters
        ----------
        title: str, required
            Text which be displayed as title.

        Example
        -------
        >>> draw_title("SIR simulation")
        """

        if isinstance(title, str):
            print("======================================================================\n"
                  "                                {titl}                                \n"
                  "======================================================================\n"
                  "======================================================================\n".format(titl=title))
        else:
            raise TypeError("You do not input str type.")

    @staticmethod
    def draw_category_name(category_name: str) -> None:
        """
        Method prints something like header section if not string given
        raise TypeError.

        Parameters
        ----------
        category_name: str, required
            Text witch be displayed as category (header).
        """
        if isinstance(category_name, str):
            print("\n+++++++++         {nam}        +++++++++\n".format(nam=category_name))
        else:
            raise TypeError("You do not input str type.")
