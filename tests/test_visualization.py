import unittest
from simulation import utils_parameters as up


class VisualizationDashBoardTestCase(unittest.TestCase):
    def test_01__check_if_parameter_r_calculate_correctly(self):
        ago_susceptible = 100
        current_susceptible = 80
        current_infected = 20
        result = up.compute_r_parameter(ago_susceptible, current_susceptible, current_infected)

        # Note: Compute result expected
        # dS/dt = current_susceptible - ago_susceptible = -20
        # r_param = -dS/dt * (1 / (current_susceptible * current_infected))
        # r_param = -(-20) * 1 / 1600
        # r_param = 20 / 1600
        # r_param = 0.0125
        # --- end note.
        self.assertEqual(result, 0.0125, msg="Function compute_r_parameter() does not"
                                             " compute correct value.")
        print("Function compute_r_parameter() correctly compute value.")

    def test_02__check_if_parameter_a_calculate_correctly(self):
        ago_removed = 0
        current_removed = 20
        current_infected = 20
        result = up.compute_a_parameter(ago_removed, current_removed, current_infected)

        # Note: Compute result expected
        # dR/dt = current_removed - ago_removed = 20
        # a_param = dR/dt * (1 / (current_removed * current_infected))
        # a_param = 20 * 1 / 400
        # a_param = 20 / 400
        # a_param = 0.05
        # --- end note.
        self.assertEqual(result, 0.05, msg="Function compute_a_parameter() does not"
                                           " compute correctly value.")
        print("Function compute_a_parameter() correctly compute value.")

    def test_03__check_if_parameter_q_calculate_correctly(self):
        r_parameter = 0.0125
        a_parameter = 0.5
        result = up.compute_q_parameter(r_parameter, a_parameter)

        self.assertEqual(result, r_parameter / a_parameter, msg="Function compute_a_parameter() "
                                                                "does not compute correctly value.")
        print("Function compute_q_parameter() correctly compute value.")

    def test_04__check_if_parameter_r0_calculate_correctly(self):
        start_susceptible = 80
        r_parameter = 0.0125
        a_parameter = 0.5
        result = up.compute_r0_parameter(r_parameter, a_parameter, start_susceptible)

        # Note: Compute result expected
        # R0 = r_parameter * start_susceptible_amount / a_parameter
        # R0 = 0.0125 * 80 / 0.5
        # R0 = 0.0125 * 160
        # R0 = 2
        # --- end note.
        self.assertEqual(result, 2, msg="Function compute_r0_parameter() does not"
                                        " compute correctly value.")
        print("Function compute_r0_parameter() correctly compute value.")


if __name__ == '__main__':
    unittest.main()
