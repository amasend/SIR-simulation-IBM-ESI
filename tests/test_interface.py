import unittest
from simulation import groups


class SGroupTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s_member = groups.SGroup(infection_prob=0.25, label="s_member", x=0, y=0)

    def test_01__check_if_constructor_work_correctly__return_SGroup_instance(self):
        self.assertIsInstance(self.s_member, groups.SGroup,
                              msg="Constructor was not return a SGroup instance.")

    def test_02__check_if_method_returns_new_instance__return_bool(self):
        self.assertIsInstance(self.s_member.infect(), bool,
                              msg="Method infect() was not return bool.")

    def test_03__check_if_change_instance_position_in_grid_system__return_bool(self):
        self.assertIsInstance(self.s_member.move(1, 2, 10, 10), bool,
                              msg="Method move() was not return a bool object.")

    def test_04__check_if_instance_move_to_correct_place_in_X_axis(self):
        self.s_member.move(5, 3, 10, 10)
        self.assertEqual(self.s_member.x, 5,
                         msg="Instance move incorrect in X axis.")

    def test_05__check_if_instance_move_to_correct_place_in_Y_axis(self):
        self.s_member.move(5, 3, 10, 10)
        self.assertEqual(self.s_member.y, 3,
                         msg="Instance move incorrect in Y axis.")



class IGroupTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.i_member = groups.IGroup(infection_range=1.2, recover_prob=0.15,
                                      death_prob=0.02, label="i_member", x=1, y=1)

    def test_01__check_if_constructor_work_correctly__return_IGroup_instance(self):
        self.assertIsInstance(self.i_member, groups.IGroup,
                              msg="Constructor was not return a IGroup instance.")

    def test_02__check_if_instance_was_recovered__return_bool(self):
        self.assertIsInstance(self.i_member.recover(), bool,
                              msg="Method recover() was not return bool.")

    def test_03__check_if_instance_died__return_bool(self):
        self.assertIsInstance(self.i_member.death(), bool,
                              msg="Method recover() was not return bool.")


class SGroupAndIGroupInteractionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s_member = groups.SGroup(infection_prob=0.25, label="s_member", x=0, y=0)
        cls.i_member = groups.IGroup(infection_range=1.2, recover_prob=0.15,
                                     death_prob=0.02, label="i_member", x=0, y=0)

    def setUp(self) -> None:
        self.container_width = 10
        self.container_height = 10

    def test_02__check_if_s_member_is_inside_i_member_infection_range(self):
        self.s_member.move(5, 3, self.container_width, self.container_height)
        self.i_member.move(4, 3, self.container_width, self.container_height)
        # Note: Distance between s_member(5, 3) and i_member(4, 3) is 1 and
        # infect radius is 1.2 so 1 < 1.2 and method should return True.
        result = self.s_member.is_in_infection_area(self.i_member.x, self.i_member.y,
                                                    self.i_member.infection_range)

        self.assertTrue(result, msg="Invalid logic in checking if s_member "
                                    "is inside i_member infection_range.")

    def test_03__check_if_s_member_is_outside_i_member_infection_range(self):
        self.i_member.move(-3, -2, self.container_width, self.container_height)
        # Note: Now i_member position is (1, 2) and distance is about 4.5 so
        # 1.2 < 4.6 and method should return False.
        result = self.s_member.is_in_infection_area(self.i_member.x, self.i_member.y,
                                                    self.i_member.infection_range)

        self.assertFalse(result, msg="Invalid logic in checking if s_member "
                                     "is outside i_member infection_range.")

    def test_04__check_if_s_member_could_not_be_infected_with_100_chance(self):
        self.i_member.move(4, 3, self.container_width, self.container_height)
        self.s_member.infection_probability = 1

        if self.s_member.is_in_infection_area(self.i_member.x, self.i_member.y,
                                              self.i_member.infection_range):
            self.assertTrue(self.s_member.infect(),
                            msg="SGroup instance could not be infected with"
                                "100% chance.")

    def test_05__check_if_s_member_could_be_infected_with_0_chance(self):
        self.s_member.infection_probability = 0

        if self.s_member.is_in_infection_area(self.i_member.x, self.i_member.y,
                                              self.i_member.infection_range):
            self.assertFalse(self.s_member.infect(),
                             msg="SGroup instance could be infected with 0%"
                                 "chance.")

            
if __name__ == '__main__':
    unittest.main()
