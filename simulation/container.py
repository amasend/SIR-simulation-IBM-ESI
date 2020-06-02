__all__ = [
    'Container',
]

from simulation import groups
from simulation import container_interface as con_int
import random
import time


class Container(con_int.ContainerInterface):
    """
    Container class is wrapper for simulation and play ground from
    representation SIR model based classes.

    Parameters
    ----------
    size: int, required
        Container instance is square and the size parameter is length of the
        square side. Width and height is equal size.
    population: int, required
        This parameters store amount of max count of population based objects.
    time_to_live: int, required
        It is time in which all simulation's events and population's behaviours
        could happen. This value should be given is seconds eg. if we want
        1 minute simulation we should insert 60.
    action_interval: float, required
        Segment of time after new container's events and population's
        behaviours will repeat.
    move_dist_length: float, required
        Length in which instances inside container could move.
    """

    def __init__(self, size: int, population: int, time_to_live: int, action_interval: float,
                 move_dist_length: float) -> None:
        super().__init__(size, population, time_to_live, action_interval, move_dist_length)

    def count_susceptible(self) -> int:
        """
        Count amount of SGroup instances in object_list.

        Returns
        -------
        Amount of SGroup instances in object_list.

        Example
        -------
        >>> container.count_susceptible()
        """

        return super().count_objects_in_list(groups.SGroup)

    def count_infected(self) -> int:
        """
        Count amount of IGroup instances in object_list.

        Returns
        -------
        Amount of IGroup instances in object_list.

        Example
        -------
        >>> container.count_infected()
        """

        return super().count_objects_in_list(groups.IGroup)

    def count_recovered(self) -> int:
        """
        Count amount of RGroup instances in object_list.

        Returns
        -------
        Amount of RGroup instances in object_list.

        Example
        -------
        >>> container.count_recovered()
        """

        return super().count_objects_in_list(groups.RGroup)

    def count_dead(self) -> int:
        """
        Count amount of DGroup instances in object_list.

        Returns
        -------
        Amount of DGroup instances in object_list.

        Example
        -------
        >>> container.count_dead()
        """

        return super().count_objects_in_list(groups.DGroup)

    def initial_set_up(self, susceptible: int, infected: int, recovered: int,
                       dead: int, ) -> None:
        """
        Method which specified amount of specific population group in object_list.
        When sum of groups is greater than population parameter raise ValueError.

        Parameters
        ----------
        susceptible: int, required
            Amount of susceptible instances to place in container.
        infected: int, required
            Amount of infected instances to place in container.
        recovered: int, required
            Amount of infected instances to place in container.
        dead: int, required
            Amount of dead instances to place in container.

        Example
        -------
        >>> container.initial_set_up(90, 10, 0, 0)
        """

        if susceptible + infected + recovered + dead > self.population:
            raise ValueError("Sum of population groups is greater than population")

        self.add_instances(self.smember, susceptible)
        self.add_instances(self.imember, infected)
        self.add_instances(self.rmember, recovered)
        self.add_instances(self.dmember, dead)

    def simulation(self) -> None:
        """
        Core logic of container instance contains path of live from susceptible
        instance to recover or dead instance.
        One cycle is:
            - instances moves
            - if susceptible instance is in infected instance infection area
              check if infect
            - if is infected remove this instance from object list and add
              new infected instance
            - check if infected instance get recovered, if true removed this
              instance and add new recovered instance
            - check if infected instance died, if true removed this instance
              and add new dead instance
        """

        while self.is_alive():
            for instance in self.object_list:
                x = random.uniform(-self.move_distance_length, self.move_distance_length)
                y = random.uniform(-self.move_distance_length, self.move_distance_length)
                instance.move(x, y, self.width, self.height)

                if isinstance(instance, groups.SGroup):
                    for infected in self.object_list:
                        if isinstance(infected, groups.IGroup):
                            if instance.is_in_infection_area(infected.x, infected.y,
                                                             infected.infection_range):
                                if instance.infect():
                                    self.object_list.remove(instance)
                                    self.add_instances(self.imember, 1)

                if isinstance(instance, groups.IGroup):
                    if instance.recover():
                        self.object_list.remove(instance)
                        self.add_instances(self.rmember, 1)

                    if instance.death():
                        # TODO
                        # Dead instance can move
                        self.object_list.remove(instance)
                        self.add_instances(self.dmember, 1)

            print("Time to live: {ttl}\n"
                  "Current susceptible amount: {sus}\n"
                  "Current infected amount: {inf}\n"
                  "Current recovered amount: {rec}\n"
                  "current dead amount: {dead}\n".format(ttl=self.time_to_live,
                                                         sus=self.count_susceptible(),
                                                         inf=self.count_infected(),
                                                         rec=self.count_recovered(),
                                                         dead=self.count_dead()))

            time.sleep(self.action_interval)
            self.time_to_live -= self.action_interval
