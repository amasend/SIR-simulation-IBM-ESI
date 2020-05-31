__all__ = [
    'SGroup',
    'IGroup',
    'RGroup',
    'DGroup'
]

from simulation import groups_interface
import random


class SGroup(groups_interface.PopulationGroup):
    def __init__(self, x: float, y: float, label: str, inf_dist: float, infection_prob: float, recover_prob: float,
                 death_prob: float) -> None:

        super().__init__(x, y, label, inf_dist, infection_prob, recover_prob, death_prob)

    def __del__(self):
        pass

    def move(self, x_distance: float, y_distance: float, box_width: int,
             box_height: int) -> bool:

        can_move = True

        if not 0 < self.x + x_distance < box_width:
            can_move = False

        if not 0 < self.y + y_distance < box_height:
            can_move = False

        if can_move:
            self.x += x_distance
            self.y += y_distance

            return True
        else:
            return False

    def is_in_area(self, member_x: float, member_y: float, member_inf_dis: float) -> bool:
        if self.x > member_x:
            x_difference = self.x - member_x
        else:
            x_difference = member_x - self.x

        if self.y > member_y:
            y_difference = self.y - member_y
        else:
            y_difference = member_y - self.y

        if x_difference < member_inf_dis or \
                y_difference < member_inf_dis:
            return True
        else:
            return False

    def infect(self):
        x = random.random()

        if x < self.infection_probability:
            return True
        else:
            return False

    def recover(self):
        x = random.random()

        if x < self.recover_probability:
            return True
        else:
            return False

    def death(self):
        x = random.random()

        if x < self.death_probability:
            return True
        else:
            return False

    # Documentation inheritance handling
    __doc__ = groups_interface.PopulationGroup.__doc__
    move.__doc__ = groups_interface.PopulationGroup.move.__doc__
    is_in_area.__doc__ = groups_interface.PopulationGroup.is_in_area.__doc__
    infect.__doc__ = groups_interface.PopulationGroup.infect.__doc__
    recover.__doc__ = groups_interface.PopulationGroup.recover.__doc__
    death.__doc__ = groups_interface.PopulationGroup.death.__doc__


class IGroup(groups_interface.PopulationGroup):
    def __init__(self, x: float, y: float, label: str, inf_dist: float, infection_prob: float, recover_prob: float,
                 death_prob: float) -> None:

        super().__init__(x, y, label, inf_dist, infection_prob, recover_prob, death_prob)

    def __del__(self):
        pass

    def move(self, x_distance: float, y_distance: float, box_width: int,
             box_height: int) -> bool:

        can_move = True

        if not 0 < self.x + x_distance < box_width:
            can_move = False

        if not 0 < self.y + y_distance < box_height:
            can_move = False

        if can_move:
            self.x += x_distance
            self.y += y_distance

            return True
        else:
            return False

    def is_in_area(self, member_x: float, member_y: float, member_inf_dis: float) -> bool:
        if self.x > member_x:
            x_difference = self.x - member_x
        else:
            x_difference = member_x - self.x

        if self.y > member_y:
            y_difference = self.y - member_y
        else:
            y_difference = member_y - self.y

        if x_difference < member_inf_dis or \
                y_difference < member_inf_dis:
            return True
        else:
            return False

    def infect(self):
        x = random.random()

        if x < self.infection_probability:
            return True
        else:
            return False

    def recover(self):
        x = random.random()

        if x < self.recover_probability:
            return True
        else:
            return False

    def death(self):
        x = random.random()

        if x < self.death_probability:
            return True
        else:
            return False

    # Documentation inheritance handling
    __doc__ = groups_interface.PopulationGroup.__doc__
    move.__doc__ = groups_interface.PopulationGroup.move.__doc__
    is_in_area.__doc__ = groups_interface.PopulationGroup.is_in_area.__doc__
    infect.__doc__ = groups_interface.PopulationGroup.infect.__doc__
    recover.__doc__ = groups_interface.PopulationGroup.recover.__doc__
    death.__doc__ = groups_interface.PopulationGroup.death.__doc__


class RGroup(groups_interface.PopulationGroup):
    def __init__(self, x: float, y: float, label: str, inf_dist: float, infection_prob: float = 0,
                 recover_prob: float = 0, death_prob: float = 0) -> None:

        super().__init__(x, y, label, inf_dist, infection_prob, recover_prob, death_prob)

    def __del__(self):
        pass

    def move(self, x_distance: float, y_distance: float, box_width: int,
             box_height: int) -> bool:

        can_move = True

        if not 0 < self.x + x_distance < box_width:
            can_move = False

        if not 0 < self.y + y_distance < box_height:
            can_move = False

        if can_move:
            self.x += x_distance
            self.y += y_distance

            return True
        else:
            return False

    def is_in_area(self, member_x: float, member_y: float, member_inf_dis: float) -> bool:
        if self.x > member_x:
            x_difference = self.x - member_x
        else:
            x_difference = member_x - self.x

        if self.y > member_y:
            y_difference = self.y - member_y
        else:
            y_difference = member_y - self.y

        if x_difference < member_inf_dis or \
                y_difference < member_inf_dis:
            return True
        else:
            return False

    def infect(self):
        x = random.random()

        if x < self.infection_probability:
            return True
        else:
            return False

    def recover(self):
        x = random.random()

        if x < self.recover_probability:
            return True
        else:
            return False

    def death(self):
        x = random.random()

        if x < self.death_probability:
            return True
        else:
            return False

    # Documentation inheritance handling
    __doc__ = groups_interface.PopulationGroup.__doc__
    move.__doc__ = groups_interface.PopulationGroup.move.__doc__
    is_in_area.__doc__ = groups_interface.PopulationGroup.is_in_area.__doc__
    infect.__doc__ = groups_interface.PopulationGroup.infect.__doc__
    recover.__doc__ = groups_interface.PopulationGroup.recover.__doc__
    death.__doc__ = groups_interface.PopulationGroup.death.__doc__


class DGroup(groups_interface.PopulationGroup):
    def __init__(self, x: float, y: float, label: str, inf_dist: float,
                 infection_prob: float = 0, recover_prob: float = 0,
                 death_prob: float = 0) -> None:

        super().__init__(x, y, label, inf_dist, infection_prob, recover_prob, death_prob)

    def __del__(self):
        pass

    def move(self, x_distance: float, y_distance: float, box_width: int,
             box_height: int) -> bool:

        can_move = True

        if not 0 < self.x + x_distance < box_width:
            can_move = False

        if not 0 < self.y + y_distance < box_height:
            can_move = False

        if can_move:
            self.x += x_distance
            self.y += y_distance

            return True
        else:
            return False

    def is_in_area(self, member_x: float, member_y: float, member_inf_dis: float) -> bool:
        if self.x > member_x:
            x_difference = self.x - member_x
        else:
            x_difference = member_x - self.x

        if self.y > member_y:
            y_difference = self.y - member_y
        else:
            y_difference = member_y - self.y

        if x_difference < member_inf_dis or \
                y_difference < member_inf_dis:
            return True
        else:
            return False

    def infect(self):
        x = random.random()

        if x < self.infection_probability:
            return True
        else:
            return False

    def recover(self):
        x = random.random()

        if x < self.recover_probability:
            return True
        else:
            return False

    def death(self):
        x = random.random()

        if x < self.death_probability:
            return True
        else:
            return False

    # Documentation inheritance handling
    __doc__ = groups_interface.PopulationGroup.__doc__
    move.__doc__ = groups_interface.PopulationGroup.move.__doc__
    is_in_area.__doc__ = groups_interface.PopulationGroup.is_in_area.__doc__
    infect.__doc__ = groups_interface.PopulationGroup.infect.__doc__
    recover.__doc__ = groups_interface.PopulationGroup.recover.__doc__
    death.__doc__ = groups_interface.PopulationGroup.death.__doc__


s_member = SGroup(1, 1, "s_member1", 0.25, 0.25, 0.15, 0.10)
i_member = IGroup(1, 1.25, "i_member1", 0.25, 0.25, 0.15, 0.10)

if s_member.is_in_area(i_member.x, i_member.y, i_member.infection_distance):
    print("{smem} is in infection area of {imem}".format(smem=s_member.label, imem=i_member.label))

    i = 0

    while not s_member.infect():
        i += 1

    print("{smem} is infected. New IGroup instance created.".format(smem=s_member.label))
    print("Infected in {att} attempt".format(att=i))

    i_member2 = IGroup(s_member.x, s_member.y, "i_member2", 0.25, 0.25, 0.15, 0.10)

    del s_member

