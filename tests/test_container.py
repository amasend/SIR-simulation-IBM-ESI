import unittest
from simulation import container
from simulation import groups


class ContainerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.box = container.Container(100, 1000, 300, 1, 0.5)
        self.s_instance = groups.SGroup(x=1, y=1, infection_prob=0.25)

    def test_01__check_if_dimensions_was_set_correctly(self):
        width = 100
        height = 100

        self.assertEqual(self.box.width, width,
                         msg="Container width was set incorrect.")

        self.assertEqual(self.box.height, height,
                         msg="Container height was set incorrect.")

    def test_02__check_if_new_object_added_correctly_to_objects_list(self):
        self.box.add_instances(self.s_instance, 1)
        self.assertEqual(len(self.box.object_list), 1,
                         msg="New instance was not correctly added to"
                             "objects list.")

    def test_03__check_if_container_time_to_live_not_elapsed__return_bool(self):
        self.assertIsInstance(self.box.is_alive(), bool,
                              msg="Box method is_alive was not return bool.")

    def test_04__check_if_container_lives_in_elapsed_time(self):
        self.box.time_to_live = 0
        self.assertFalse(self.box.is_alive(), msg="Container instance lives longer"
                                                  "than time_to_live attribute.")

    def test_05__check_if_action_time_interval_is_positive(self):
        self.assertGreater(self.box.action_interval, 0,
                           msg="action_interval parameters allows to insert"
                               "negative values.")

    def test_06__check_if_container_can_lives(self):
        self.box.time_to_live = 100
        self.assertTrue(self.box.is_alive(), msg="Container does not live in "
                                                 "correctly specified time_to_live.")

    def test_07__check_if_possible_move_distance_is_positive(self):
        self.assertGreater(self.box.move_distance_length, 0,
                           msg="move_distance parameter value can be negative.")

    def test_08__check_if_possible_move_distance_is_less_than_container_size(self):
        self.assertLess(self.box.move_distance_length, self.box.width,
                        msg="Parameter move_distance can not be longer than"
                            "container size.")

    def test_09__check_if_action_time_interval_is_less_than_minute(self):
        self.assertLessEqual(self.box.action_interval, 60,
                             msg="action_time_interval could be greater than"
                                 "minute.")

    def test_10__check_if_group_could_be_grater_than_population(self):
        self.box.smember = self.s_instance
        self.box.imember = self.s_instance
        self.box.rmember = self.s_instance
        self.box.dmember = self.s_instance
        self.assertRaises(ValueError, self.box.initial_set_up, 900, 100, 10, 0)


if __name__ == '__main__':
    unittest.main()
