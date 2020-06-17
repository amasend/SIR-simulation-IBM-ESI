__all__ = [
    'Container',
]


from simulation import container_interface as con_int
import random
import itertools


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
        self.condition = "susceptible"
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

        return super().count_objects_in_list("susceptible")

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

        return super().count_objects_in_list("infected")

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

        return super().count_objects_in_list("recovered")

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

        return super().count_objects_in_list("dead")

    def initial_set_up(self, number_of_susceptible: int, number_of_infected: int,
                       number_of_recovered: int, number_of_dead: int,
                       infection_probability: float, recover_probability: float,
                       dead_probability: float, infection_range: float) -> None:
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
        infection_probability: float, required
            Instance porbability to get infected.
        recover_probability: float, required
            Instance probability to get recovered.
        dead_probability: float, required
            Instance probability to die.
        infection_range: float, required
            Arean in witch infected instance can infect susceptible instances.

        Example
        -------
        >>> container.initial_set_up(90, 10, 0, 0, 0.6, 0.005, 0.002, 1)
        """

        if number_of_susceptible + number_of_infected + number_of_recovered + number_of_dead > self.population:
            raise ValueError("Sum of population groups is greater than population")

        self.add_instances(number_of_susceptible, "susceptible", infection_probability,
                           recover_probability, dead_probability, infection_range)
        self.add_instances(number_of_infected, "infected", infection_probability,
                           recover_probability, dead_probability, infection_range)
        self.add_instances(number_of_recovered, "recovered", infection_probability,
                           recover_probability, dead_probability, infection_range)
        self.add_instances(number_of_dead, "dead", infection_probability,
                           recover_probability, dead_probability, infection_range)

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

        # Note: Move and can_infect parameter reset. Then sort.
        for instance in self.object_list:
            if not instance.current_condition == 'dead':
                x = random.uniform(-self.move_distance_length, self.move_distance_length)
                y = random.uniform(-self.move_distance_length, self.move_distance_length)
                instance.move(x, y, self.width, self.height)
                instance.can_infect = True

        self.object_list.sort(key=lambda parameter: parameter.x)
        # --- end.

        for counter, instance in enumerate(self.object_list, 1):
            if instance.current_condition == "susceptible":
                for next_instance in itertools.islice(self.object_list, counter, None):
                    if next_instance.current_condition == "infected":
                        if next_instance.x - instance.x >= instance.infection_range:
                            break

                        if instance.is_in_infection_area(next_instance.x, next_instance.y,
                                                         next_instance.infection_range):
                            if instance.infect():
                                instance.current_condition = "infected"
                                break

            elif instance.current_condition == "infected" and instance.can_infect:
                for next_instance in itertools.islice(self.object_list, counter, None):
                    if next_instance.current_condition == "susceptible":
                        if next_instance.x - instance.x >= instance.infection_range:
                            break

                        if next_instance.is_in_infection_area(instance.x, instance.y,
                                                              instance.infection_range):
                            if next_instance.infect():
                                next_instance.can_infect = False
                                next_instance.current_condition = "infected"

                if instance.recover():
                    instance.current_condition = "recovered"

                if instance.death():
                    instance.current_condition = "dead"
