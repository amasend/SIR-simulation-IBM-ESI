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

    def initial_set_up(self, number_of_susceptible: int, number_of_infected: int,
                       number_of_recovered: int, number_of_dead: int, ) -> None:
        """
        Method which specified amount of specific population group in object_list.
        When sum of groups is greater than population parameter raise ValueError.

        Parameters
        ----------
        number_of_susceptible: int, required
            Amount of susceptible instances to place in container.
        number_of_infected: int, required
            Amount of infected instances to place in container.
        number_of_recovered: int, required
            Amount of infected instances to place in container.
        number_of_dead: int, required
            Amount of dead instances to place in container.

        Example
        -------
        >>> container.initial_set_up(90, 10, 0, 0)
        """

        if number_of_susceptible + number_of_infected + number_of_recovered + number_of_dead \
                > self.population:
            raise ValueError("Sum of population groups is greater than population")

        self.add_instances(self.smember, number_of_susceptible)
        self.add_instances(self.imember, number_of_infected)
        self.add_instances(self.rmember, number_of_recovered)
        self.add_instances(self.dmember, number_of_dead)

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

        self.susceptible_list.sort(key=lambda parameter: parameter.x)
        self.infected_list.sort(key=lambda parameter: parameter.x)

        while self.is_alive():
            infected_amount = 0
            recovered_amount = 0
            dead_amount = 0
            for instance in self.object_list:
                x = random.uniform(-self.move_distance_length, self.move_distance_length)
                y = random.uniform(-self.move_distance_length, self.move_distance_length)
                instance.move(x, y, self.width, self.height)

            for susceptible in self.susceptible_list:
                for infected in self.infected_list:
                    if susceptible.is_in_infection_area(infected.x, infected.y,
                                                        infected.infection_range):
                        if susceptible.infect():
                            infected_amount += 1
                            break

            for infected in self.infected_list:
                if infected.recover():
                    recovered_amount += 1

                if infected.death():
                    # TODO
                    # Dead instance can move
                    dead_amount += 1

            for number in range(infected_amount):
                if self.susceptible_list:
                    item = self.susceptible_list.pop()
                    self.object_list.remove(item)

            for number in range(recovered_amount + dead_amount):
                if self.infected_list:
                    item = self.infected_list.pop()
                    self.object_list.remove(item)

            self.add_instances(self.imember, infected_amount)
            self.add_instances(self.rmember, recovered_amount)
            self.add_instances(self.dmember, dead_amount)
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
