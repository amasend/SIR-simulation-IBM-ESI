import unittest
from simulation import groups


class SGroupTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s_member = groups.SGroup(5, 5, "member1", 0.25, 0.3, 0.2, 0.2)
        self.s_member2 = groups.SGroup(4, 2, "member2", 0.25, 0.3, 0.2, 0.2)

    def test_01__check_if_constructor_work_correctly__return_SGroup_instance(self):
        self.assertIsInstance(self.s_member, groups.SGroup,
                              msg="Constructor was not return a SGroup instance.")

    def test_02__check_if_change_instance_position_in_grid_system__return_bool(self):
        self.assertIsInstance(self.s_member.move(1, 2, 10, 10), bool,
                              msg="Method move() was not return a bool object.")

    def test_03__check_if_method_correctly_is_in_area__return_bool(self):
        self.assertIsInstance(self.s_member.is_in_area(self.s_member2.x,
                                                       self.s_member2.y,
                                                       self.s_member2.infection_distance), bool,
                              msg="Method is_in_area() was not return "
                                  "a bool object.")

    def test_04__check_if_method_returns_new_instance__return_bool(self):
        self.assertIsInstance(self.s_member.infect(), bool,
                              msg="Method infect() was not return bool.")

    def test_05__check_if_instance_was_recovered__return_bool(self):
        self.assertIsInstance(self.s_member.recover(), bool,
                              msg="Method recover() was not return bool.")

    def test_06__check_if_instance_died__return_bool(self):
        self.assertIsInstance(self.s_member.death(), bool,
                              msg="Method recover() was not return bool.")


class IGroupTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.i_member = groups.IGroup(5, 5, "member1", 0.25, 0.3, 0.2, 0.2)
        self.i_member2 = groups.IGroup(4, 2, "member2", 0.25, 0.3, 0.2, 0.2)

    def test_01__check_if_constructor_work_correctly__return_SGroup_instance(self):
        self.assertIsInstance(self.i_member, groups.IGroup,
                              msg="Constructor was not return a IGroup instance.")

    def test_02__check_if_change_instance_position_in_grid_system__return_bool(self):
        self.assertIsInstance(self.i_member.move(1, 2, 10, 10), bool,
                              msg="Method move() was not return a bool object.")

    def test_03__check_if_method_correctly_is_in_area__return_bool(self):
        self.assertIsInstance(self.i_member.is_in_area(self.i_member2.x,
                                                       self.i_member2.y,
                                                       self.i_member2.infection_distance), bool,
                              msg="Method is_in_area() was not return "
                                  "a bool object.")

    def test_04__check_if_method_returns_new_instance__return_bool(self):
        self.assertIsInstance(self.i_member.infect(), bool,
                              msg="Method infect() was not return bool.")

    def test_05__check_if_instance_was_recovered__return_bool(self):
        self.assertIsInstance(self.i_member.recover(), bool,
                              msg="Method recover() was not return bool.")

    def test_06__check_if_instance_died__return_bool(self):
        self.assertIsInstance(self.i_member.death(), bool,
                              msg="Method recover() was not return bool.")


class RGroupTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.r_member = groups.RGroup(5, 5, "member1", 0.25, 0.3, 0.2, 0.2)
        self.r_member2 = groups.RGroup(4, 2, "member2", 0.25, 0.3, 0.2, 0.2)

    def test_01__check_if_constructor_work_correctly__return_SGroup_instance(self):
        self.assertIsInstance(self.r_member, groups.RGroup,
                              msg="Constructor was not return a RGroup instance.")

    def test_02__check_if_change_instance_position_in_grid_system__return_bool(self):
        self.assertIsInstance(self.r_member.move(1, 2, 10, 10), bool,
                              msg="Method move() was not return a bool object.")

    def test_03__check_if_method_correctly_is_in_area__return_bool(self):
        self.assertIsInstance(self.r_member.is_in_area(self.r_member2.x,
                                                       self.r_member2.y,
                                                       self.r_member2.infection_distance), bool,
                              msg="Method is_in_area() was not return "
                                  "a bool object.")

    def test_04__check_if_method_returns_new_instance__return_bool(self):
        self.assertIsInstance(self.r_member.infect(), bool,
                              msg="Method infect() was not return bool.")

    def test_05__check_if_instance_was_recovered__return_bool(self):
        self.assertIsInstance(self.r_member.recover(), bool,
                              msg="Method recover() was not return bool.")

    def test_06__check_if_instance_died__return_bool(self):
        self.assertIsInstance(self.r_member.death(), bool,
                              msg="Method recover() was not return bool.")


class DGroupTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.d_member = groups.DGroup(5, 5, "member1", 0.25, 0.3, 0.2, 0.2)
        self.d_member2 = groups.DGroup(4, 2, "member2", 0.25, 0.3, 0.2, 0.2)

    def test_01__check_if_constructor_work_correctly__return_SGroup_instance(self):
        self.assertIsInstance(self.d_member, groups.DGroup,
                              msg="Constructor was not return a SGroup instance.")

    def test_02__check_if_change_instance_position_in_grid_system__return_bool(self):
        self.assertIsInstance(self.d_member.move(1, 2, 10, 10), bool,
                              msg="Method move() was not return a bool object.")

    def test_03__check_if_method_correctly_is_in_area__return_bool(self):
        self.assertIsInstance(self.d_member.is_in_area(self.d_member2.x,
                                                       self.d_member2.y,
                                                       self.d_member2.infection_distance), bool,
                              msg="Method is_in_area() was not return "
                                  "a bool object.")

    def test_04__check_if_method_returns_new_instance__return_bool(self):
        self.assertIsInstance(self.d_member.infect(), bool,
                              msg="Method infect() was not return bool.")

    def test_05__check_if_instance_was_recovered__return_bool(self):
        self.assertIsInstance(self.d_member.recover(), bool,
                              msg="Method recover() was not return bool.")

    def test_06__check_if_instance_died__return_bool(self):
        self.assertIsInstance(self.d_member.death(), bool,
                              msg="Method recover() was not return bool.")


if __name__ == '__main__':
    unittest.main()
