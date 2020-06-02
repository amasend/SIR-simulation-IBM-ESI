import unittest
from simulation import user_interface as ui


class UserInterfaceTestCase(unittest.TestCase):
    def test_01__check_if_draw_title_accept_no_str_type(self):
        if self.assertRaises(TypeError, ui.UserInterface.draw_title, 1):
            print("draw_title method allows to insert not string type.")

    def test_01__check_if_draw_category_name_accept_no_str_type(self):
        if self.assertRaises(TypeError, ui.UserInterface.draw_category_name, 1):
            print("draw_category_name method allows to insert not string type.")


if __name__ == '__main__':
    unittest.main()
