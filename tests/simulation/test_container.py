import unittest
from simulation import container
from simulation import person


class ContainerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.box = container.Container(100, 1000, 300, 1, 0.5)
        self.s_instance = person.Person(x=0, y=0, infection_probability=0.25,
                                        recover_probability=0.2, dead_probability=0.05,
                                        infection_range=0.8)

    def test_01__check_if_dimensions_was_set_correctly(self):
        width = 100
        height = 100

        self.assertEqual(self.box.width, width,
                         msg="Container width was set incorrect.")

        self.assertEqual(self.box.height, height,
                         msg="Container height was set incorrect.")
        print("> (test_01) Container dimensions are set correctly.")

    def test_02__check_if_new_object_added_correctly_to_objects_list(self):
        self.box.add_instances(1, "susceptible", infection_probability=0.4,
                               recover_probability=0.2,
                               dead_probability=0.05, infection_range=1.25)
        self.assertEqual(len(self.box.object_list), 1,
                         msg="New instance was not correctly added to"
                             "objects list.")
        print("> (test_02) New instance correctly added to object_list.")

    def test_03__check_if_container_time_to_live_not_elapsed__return_bool(self):
        self.assertIsInstance(self.box.is_alive(), bool,
                              msg="Box method is_alive was not return bool.")
        print("> (test_03) Method is_alive() returns bool type.")

    def test_04__check_if_container_lives_in_elapsed_time(self):
        self.box.time_to_live = 0
        self.assertFalse(self.box.is_alive(), msg="Container instance lives longer"
                                                  "than time_to_live attribute.")
        print("> (test_04) Container can not have more cycles than time_to_live "
              "attribute specified.")

    def test_05__check_if_action_time_interval_is_positive(self):
        self.assertGreater(self.box.action_interval, 0,
                           msg="action_interval parameters allows to insert"
                               "negative values.")
        print("> (test_05) Parameter action_interval can not allows to insert "
              "negative values.")

    def test_06__check_if_container_can_lives(self):
        self.box.time_to_live = 100
        self.assertTrue(self.box.is_alive(), msg="Container does not live in "
                                                 "correctly specified time_to_live.")
        print("> (test_06) Container live correctly base on time_to_live"
              " parameter.")

    def test_07__check_if_possible_move_distance_is_positive(self):
        self.assertGreater(self.box.move_distance_length, 0,
                           msg="move_distance parameter value can be negative.")
        print("> (test_07) Parameter move_distance can not be negative.")

    def test_08__check_if_possible_move_distance_is_less_than_container_size(self):
        self.assertLess(self.box.move_distance_length, self.box.width,
                        msg="Parameter move_distance can be longer than"
                            "container size.")
        print("> (test_08) Parameter move_distance is smaller than container size.")

    def test_09__check_if_action_time_interval_is_less_than_minute(self):
        self.assertLessEqual(self.box.action_interval, 60,
                             msg="action_time_interval could be greater than"
                                 "minute.")
        print("> (test_09) Parameter time_interval could not be greater than minute.")

    def test_10__check_if_group_could_be_grater_than_population(self):
        self.assertRaises(ValueError, self.box.initial_set_up, 900, 100, 10, 0,
                          infection_probability=0.4, recover_probability=0.2,
                          dead_probability=0.05, infection_range=1.25)
        print("> (test_10) All specified groups can not be greater than population.")


if __name__ == '__main__':
    unittest.main()
