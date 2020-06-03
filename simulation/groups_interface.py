__all__ = [
    'PopulationGroup'
]


from abc import abstractmethod, ABCMeta
from itertools import count
import random


class PopulationGroup(metaclass=ABCMeta):
    """
    Abstract class for specific population groups based on SIR model.
    """

    id = count(0)

    @abstractmethod
    def __init__(self, x: float, y: float, infection_probability: float,
                 recover_probability: float, dead_probability: float,
                 infection_range: float, prefix: str = 'person') -> None:
        self.x = x
        self.y = y
        self.infection_probability = infection_probability
        self.recover_probability = recover_probability
        self.dead_probability = dead_probability
        self.infection_range = infection_range
        self.current_condition = None
        self.label = '{prefix}_{x}'.format(prefix=prefix, x=next(self.id))

    def move(self, x_distance: float, y_distance: float, box_width: int,
             box_height: int) -> bool:
        """
        Method that handling instance movement in specified area. First checks
        is instance can move. Then change instance position.
        """

        can_move = False

        if 0 < self.x + x_distance < box_width and \
                0 < self.y + y_distance < box_height:
            can_move = True

        if can_move:
            self.x += x_distance
            self.y += y_distance

        return can_move

    @staticmethod
    def behaviour_probability(behaviour_prob: float) -> bool:
        """
        Specify if concrete behaviour can occur base on probability change.
        """
        chance = random.choices([True, False], [behaviour_prob, 1 - behaviour_prob])

        return chance[0]
