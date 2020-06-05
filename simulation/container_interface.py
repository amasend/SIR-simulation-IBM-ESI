__all__ = [
    'ContainerInterface'
]

from abc import ABCMeta
from simulation import person
import random


class ContainerInterface(metaclass=ABCMeta):
    """
    Abstract class that represents area in which instances from population
    groups can move and interact.
    """

    def __init__(self, size: int, population: int, time_to_live: int, action_interval: float,
                 move_dist_length: float) -> None:
        self.width = size
        self.height = size
        self.population = population
        self.time_to_live = time_to_live
        self.action_interval = action_interval
        self.move_distance_length = move_dist_length
        self.object_list = []
        self.person = None

    def count_objects_in_list(self, condition_label: str) -> int:
        """
        Method counts amount on given class type in object_list attribute.
        """

        amount = 0
        for instance in self.object_list:
            if instance.current_condition == condition_label:
                amount += 1
        return amount

    def is_alive(self) -> bool:
        """
        Method checks if container instance time_to_live attribute is
        greater than 0.
        """

        if self.time_to_live > 0:
            return True
        else:
            return False

    def add_instances(self, instance_amount: int, condition_to_set: str,
                      infection_probability: float, recover_probability: float,
                      dead_probability: float, infection_range: float) -> None:
        for i in range(instance_amount):
            x = random.uniform(0, self.width - 1)
            y = random.uniform(0, self.height - 1)
            self.person = person.Person(x=x, y=y, infection_probability=infection_probability,
                                        recover_probability=recover_probability,
                                        dead_probability=dead_probability, infection_range=infection_range)

            self.person.current_condition = condition_to_set

            self.object_list.append(self.person)
