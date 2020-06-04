import unittest
from simulation import person


class PersonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s_member = person.Person(x=0, y=0, infection_probability=0.25,
                                      recover_probability=0.2, dead_probability=0.05,
                                      infection_range=0.8)

    def test_01__check_if_constructor_work_correctly__return_SGroup_instance(self):
        self.assertIsInstance(self.s_member, person.Person,
                              msg="Constructor was not return a SGroup instance.")
        print("> (test_01) Person class constructor works correctly.")

    def test_02__check_if_method_returns_new_instance__return_bool(self):
        self.assertIsInstance(self.s_member.infect(), bool,
                              msg="Method infect() was not return bool.")
        print("> (test_02) Method infect() returns bool type.")

    def test_03__check_if_change_instance_position_in_grid_system__return_bool(self):
        self.assertIsInstance(self.s_member.move(1, 2, 10, 10), bool,
                              msg="Method move() was not return a bool object.")
        print("> (test_03) Method move() returns bool type.")

    def test_04__check_if_instance_move_to_correct_place_in_X_axis(self):
        self.s_member.move(5, 3, 10, 10)
        self.assertEqual(self.s_member.x, 5,
                         msg="Instance move incorrect in X axis.")
        print("> (test_04) Instance correctly move in X axis.")

    def test_05__check_if_instance_move_to_correct_place_in_Y_axis(self):
        self.s_member.move(5, 3, 10, 10)
        self.assertEqual(self.s_member.y, 3,
                         msg="Instance move incorrect in Y axis.")
        print("> (test_05) Instance correctly move in Y axis.")

    def test_06__check_if_instance_can_move_outside_container_in_X_axis(self):
        result = self.s_member.move(11, 0, 10, 10)

        self.assertFalse(result, msg="Instance can move outside the "
                                     "container in X axis.")
        print("> (test_06) Instance can not move outside container in X axis.")

    def test_07__check_if_instance_can_move_outside_container_in_Y_axis(self):
        result = self.s_member.move(0, 11, 10, 10)

        self.assertFalse(result, msg="Instance can move outside the "
                                     "container in Y axis.")
        print("> (test_07) Instance can not move outside container in Y axis.")


if __name__ == '__main__':
    unittest.main()
