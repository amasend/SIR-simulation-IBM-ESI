__all__ = [
    'PopulationGroup'
]


from abc import abstractmethod, ABCMeta


class PopulationGroup(metaclass=ABCMeta):
    """
    Abstract class for specific population groups based on SIR model.
    """
    @abstractmethod
    def __init__(self, x: float, y: float, label: str, inf_dist: float,
                 infection_prob: float, recover_prob: float, death_prob: float) -> None:
        self.x = x
        self.y = y
        self.label = label
        self.infection_distance = inf_dist
        self.infection_probability = infection_prob
        self.recover_probability = recover_prob
        self.death_probability = death_prob

    @abstractmethod
    def __del__(self):
        pass

    @abstractmethod
    def move(self, x_distance: float, y_distance: float, box_width: int,
             box_height: int) -> bool:
        """
        Method that handling instance movement in specified area. First checks
        is instance can move. Then change instance position.

        Parameters
        ----------
        x_distance: float, required
            Value of reallocation on X axis.
        y_distance: float, required
            Value of reallocation on Y axis.
        box_width: integer, required
            Width of container that contains instance. Width starts in point
            (0, 0) in coordinate system.
        box_height: integer, required
            Height of container that contains instance. Height starts in point
            (0, 0) in coordinate system.

        Returns
        -------
        Returns True if instance can move and do not move outside the
        container else return False.
        """

        raise NotImplementedError

    @abstractmethod
    def is_in_area(self, member_x: float, member_y: float, member_inf_dis: float) -> bool:
        """
        Method check if current instance is in infection area of different
        object.

        Parameters
        ----------
        member_x: float, required
            Object to compare position with.
        member_y: float, required

        member_inf_dis


        Returns
        -------
        Return True if instance is in infection area of different object or
        False if is not.
        """

        raise NotImplementedError

    @abstractmethod
    def infect(self):
        """
        Method checks if current instance infect. Generate random float
        number between 0.0 and 1.0 then compare to value of
        infection_probability.

        Returns
        -------
        True if generated number was less then infection_probability else
        returns False.
        """

        raise NotImplementedError

    @abstractmethod
    def recover(self):
        """
        Method check if current instance get recover. Generate random float
        number between 0.0 and 1.0 then compare to value of recover_probability.

        Returns
        -------
        True if generated number was less then recover_probability else
        returns False.
        """

        raise NotImplementedError

    @abstractmethod
    def death(self):
        """
        Method check if current instane died. Generate random float
        number between 0.0 and 1.0 the compare to value of death_probability.

        Returns
        -------
        True if generated number was less then death_probability else
        returns False.
        """

        raise NotImplementedError
