__all__ = [
    'SGroup',
    'IGroup',
    'RGroup',
    'DGroup'
]

from simulation import groups_interface
from itertools import count
import math


class SGroup(groups_interface.PopulationGroup):
    """
    Class that represents susceptible people that can be infected. Has own
    behaviour method infect() which define if person get infected or not.

    Parameters
    ----------
    x: float, required
        Instance starting position on X axis on cartesian grid defined by
        container wrapper.
    y: float, required
        Instance starting position on Y axis on cartesian grid defined by
        container wrapper.
    infection_prob: float, required
        Probability to infect it should be value between 0.0 and 1.0.
    prefix: str, optional
        Prefix for auto labeling logic which is {prefix}_{id}.
        Should not be changed. Default value: susceptible
    """

    id = count(1)

    def __init__(self, x: float, y: float, infection_prob: float,
                 prefix: str = 'susceptible') -> None:
        self.x = x
        self.y = y
        self.infection_probability = infection_prob
        super().__init__(x, y, prefix)

    def is_in_infection_area(self, member_x: float, member_y: float,
                             member_inf_range: float) -> bool:
        """
        Method check if current instance is in infection area of infected
        instance.

        Parameters
        ----------
        member_x: float, required
            Object to compare with position on X axis.
        member_y: float, required
            Object to compare with position on Y axis.
        member_inf_range: float, required
            Object infection area in with current instance could be infected.

        Returns
        -------
        Return True if instance is in infection area of different infected
        object or False if is not.

        Example
        -------
        >>> s_member.is_in_infection_area(i_member.x, i_member.y,
                                          i_member.infection_range)
        """

        distance = math.sqrt(math.pow(member_x - self.x, 2)
                             + math.pow(member_y - self.y, 2))

        if distance < member_inf_range:
            return True
        else:
            return False

    def infect(self) -> bool:
        """
        Method checks if current instance get infected based on attribute
        infection_probability.

        Returns
        -------
        True if instance get infected or False if not. Logic base on
        random.choices() method.

        Example
        -------
        >>> s_member.infect()
        """

        return super().behaviour_probability(self.infection_probability)


class IGroup(groups_interface.PopulationGroup):
    """
    Class that represents already infected people. Class define two behaviours
    for infected people recover() or death().

    Parameters
    ----------
    x: float, required
        Instance starting position on X axis on cartesian grid defined by
        container wrapper.
    y: float, required
        Instance starting position on Y axis on cartesian grid defined by
        container wrapper.
    infection_range: float, required
        Area around IGroup instance in which SGroup instance could be infected.
        It is a radius value.
    recover_prob: float, required
        Probability to trigger the recover behaviour it should be value
        between 0.0 and 1.0.
    death_prob: float, required
        Probability trigger the death behaviour it should be value
        between 0.0 and 1.0.
    prefix: str, optional
        Prefix for auto labeling logic which is {prefix}_{id}.
        Should not be changed. Default value: infected.
    """

    id = count(1)

    def __init__(self, x: float, y: float, infection_range: float,
                 recover_prob: float, death_prob: float, prefix: str = 'infected') -> None:
        self.recover_probability = recover_prob
        self.death_probability = death_prob
        self.infection_range = infection_range
        super().__init__(x, y, prefix)

    def recover(self) -> bool:
        """
        Method checks if current instance get recovered based on attribute
        recover_probability.

        Returns
        -------
        True if instance get recovered or False if not. Logic base on
        random.choices() method.

        Example
        -------
        >>> i_member.recover()
        """

        return super().behaviour_probability(self.recover_probability)

    def death(self) -> bool:
        """
        Method checks if current instance died based on attribute
        death_probability.

        Returns
        -------
        True if instance died or False if not. Logic base on
        random.choices() method.

        Example
        -------
        >>> i_member.death()
        """

        return super().behaviour_probability(self.death_probability)


class RGroup(groups_interface.PopulationGroup):
    """
    Class represent people that can not be infected second time. Instances of
    this class do not define specific behaviours.

    Parameters
    ----------
    x: float, required
        Instance starting position on X axis on cartesian grid defined by
        container wrapper.
    y: float, required
        Instance starting position on Y axis on cartesian grid defined by
        container wrapper.
    prefix: str, optional
        Prefix for auto labeling logic which is {prefix}_{id}.
        Should not be changed. Default value: recovered.
    """

    id = count(1)

    def __init__(self, x: float, y: float, prefix: str = 'recovered') -> None:
        super().__init__(x, y, prefix)


class DGroup(groups_interface.PopulationGroup):
    """
    Class represent people that died and can not be infected second time.
    Instances of this class do not define specific behaviours.

    Parameters
    ----------
    x: float, required
        Instance starting position on X axis on cartesian grid defined by
        container wrapper.
    y: float, required
        Instance starting position on Y axis on cartesian grid defined by
        container wrapper.
    prefix: str, optional
        Prefix for auto labeling logic which is {prefix}_{id}.
        Should not be changed. Default value: dead.
    """

    id = count(1)

    def __init__(self, x: float, y: float, prefix: str = 'dead') -> None:
        super().__init__(x, y, prefix)
