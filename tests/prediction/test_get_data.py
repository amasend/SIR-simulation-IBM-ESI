import unittest
from prediction import api_handling


class GettingDataFromApiTestCase(unittest.TestCase):
    def test_01__check_if_get_countries_names_returns_list(self):
        countries_names = api_handling.get_countries_names()

        self.assertIsInstance(countries_names, list, msg="Function get_countries_names()"
                                                         " does not return, a list.")
        print("> (test 1) Function get_countries_names() correctly returns list "
              "with countries.")

    def test_02__check_if_prepare_data_to_save_returns_dict(self):
        raw_data = 'poland'
        country_data = api_handling.prepare_data_to_save(raw_data)

        self.assertIsInstance(country_data, dict, msg="Function prepare_data_to_save() "
                                                      "does not return a dictionary.")
        print("> (test 2) Function prepare_data_to_save() returns dictionary.")

    def test_03__check_if_prepare_data_to_save_correctly_returns_values(self):
        country = 'poland'
        country_data = api_handling.prepare_data_to_save(country, 'confirmed')

        self.assertGreater(len(country_data), 0, msg="Function prepare_data_to_save() "
                                                     "does not return values from correct country.")
        print("> (test 3) Function prepare_data_to_save() correctly get data form "
              "existing country.")

    def test_04__check_if_prepare_data_to_save_returns_data_from_incorrect_country(self):
        country = 'asdf'
        country_data = api_handling.prepare_data_to_save(country, 'confirmed')

        self.assertGreater(len(country_data), 0, msg="Function prepare_data_to_save() "
                                                     "returns values from incorrect country.")

        print("> (test 4) Function prepare_data_to_save() can not get data from "
              "not existing country.")

    def test_05__check_if_save_to_csv_correctly_create_csv_file(self):
        data = {'name': ['poland'], 'date': ['2020.06.16'], 'confirmed': [12]}
        self.assertTrue(api_handling.save_to_csv(data, 'simple'),
                        msg="Function save_to_csv() does not correctly save data.")

        print("> (test 5) Function save_to_csv() correctly create .csv file.")


if __name__ == '__main__':
    unittest.main()
