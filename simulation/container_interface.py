__all__ = [
    'ContainerInterface'
]

from abc import ABCMeta
from simulation import groups
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
        self.susceptible_list = []
        self.infected_list = []
        self.imember = None
        self.smember = None
        self.rmember = None
        self.dmember = None

    def count_objects_in_list(self, class_definition: 'instance') -> int:
        """
        Method counts amount on given class type in object_list attribute.
        """

        amount = 0
        for instance in self.object_list:
            if isinstance(instance, class_definition):
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

    def set_individuals_parameters(self, infection_prob: float, infection_range: float,
                                   recover_prob: float, dead_prob: float):
        """
        Method for connecting user input for R, I, R, D objects configuration.
        Set up objects by given input parameters.
        """

        self.smember = groups.SGroup(x=0, y=0, infection_prob=infection_prob)
        self.imember = groups.IGroup(x=0, y=0, infection_range=infection_range,
                                     recover_prob=recover_prob, death_prob=dead_prob)
        self.rmember = groups.RGroup(x=0, y=0)
        self.dmember = groups.DGroup(x=0, y=0)

    def place_instance(self, defined_instance: object) -> None:
        """
        Method handling random instance place in container object.
        Additional add placed object to object list and susceptible and infected
        instances to separate lists.
        """

        defined_instance.x = random.uniform(0, self.width - 1)
        defined_instance.y = random.uniform(0, self.height - 1)
        self.object_list.append(defined_instance)

        if isinstance(defined_instance, groups.SGroup):
            self.susceptible_list.append(defined_instance)

        if isinstance(defined_instance, groups.IGroup):
            self.infected_list.append(defined_instance)

    def add_instances(self, defined_instance: object, instance_amount: int) -> None:
        """
        Wrapper for place_instance() method for place instance multiple time in
        container.
        """
        for x in range(instance_amount):
            self.place_instance(defined_instance)
