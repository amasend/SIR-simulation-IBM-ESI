import unittest
from simulation import container


class SimulationCase(unittest.TestCase):
    def test_01__simulation_prepare_test(self):
        box = container.Container(10, 5000, 8, 1, 2.3)
        box.set_individuals_parameters(infection_prob=0.4, infection_range=1.25,
                                       recover_prob=0.2, dead_prob=0.1)
        box.initial_set_up(4900, 100, 0, 0)
        box.simulation()


if __name__ == '__main__':
    unittest.main()
