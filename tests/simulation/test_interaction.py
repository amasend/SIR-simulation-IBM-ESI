import unittest
from simulation import person


class InfectedAndSusceptibleInteractionTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.s_member = person.Person(x=0, y=0, infection_probability=0.25,
                                     recover_probability=0.2, dead_probability=0.05,
                                     infection_range=1.2)
        cls.i_member = person.Person(x=0, y=0, infection_probability=0.25,
                                     recover_probability=0.2, dead_probability=0.05,
                                     infection_range=1.2)
        cls.i_member.current_condition = "infected"

    def setUp(self) -> None:
        self.container_width = 10
        self.container_height = 10

    def test_01__check_if_s_member_is_inside_i_member_infection_range(self):
        self.s_member.move(5, 3, self.container_width, self.container_height)
        self.i_member.move(4, 3, self.container_width, self.container_height)
        # Note: Distance between s_member(5, 3) and i_member(4, 3) is 1 and
        # infect radius is 1.2 so 1 < 1.2 and method should return True.
        result = self.s_member.is_in_infection_area(self.i_member.x, self.i_member.y,
                                                    self.i_member.infection_range)

        self.assertTrue(result, msg="Invalid logic in checking if s_member "
                                    "is inside i_member infection_range.")
        print("> (test_01) Method is_in_infection_area correctly check if instance is"
              "is infection range.")

    def test_02__check_if_s_member_is_outside_i_member_infection_range(self):
        self.i_member.move(-3, -2, self.container_width, self.container_height)
        # Note: Now i_member position is (1, 2) and distance is about 4.5 so
        # 1.2 < 4.6 and method should return False.
        result = self.s_member.is_in_infection_area(self.i_member.x, self.i_member.y,
                                                    self.i_member.infection_range)

        self.assertFalse(result, msg="Invalid logic in checking if s_member "
                                     "is outside i_member infection_range.")
        print("> (test_02) Method is_in_infection_area() correctly check if instance "
              "is outside infection area.")

    def test_03__check_if_s_member_could_not_be_infected_with_100_chance(self):
        self.i_member.move(4, 3, self.container_width, self.container_height)
        self.s_member.infection_probability = 1

        if self.s_member.is_in_infection_area(self.i_member.x, self.i_member.y,
                                              self.i_member.infection_range):
            self.assertTrue(self.s_member.infect(),
                            msg="Susceptible instance could not be infected with"
                                "100% chance.")
            print("> (test_03) Susceptible instance could be infected with 100% chance.")

    def test_04__check_if_s_member_could_be_infected_with_0_chance(self):
        self.s_member.infection_probability = 0

        if self.s_member.is_in_infection_area(self.i_member.x, self.i_member.y,
                                              self.i_member.infection_range):
            self.assertFalse(self.s_member.infect(),
                             msg="Susceptible instance could be infected with 0%"
                                 " chance.")
            print("> (test_04) Susceptible instance could not be infected with 0% chance.")


if __name__ == '__main__':
    unittest.main()
