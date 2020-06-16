import unittest
import requests
from prediction import api_handling


class GettingDataFromApiTestCase(unittest.TestCase):
    def test_01__check_if_get_countries_names_returns_list(self):
        countries_names = api_handling.get_countries_names()

        self.assertIsInstance(countries_names, list, msg="Function get_countries_names()"
                                                         " does not return, a list.")
        print("> (test 1) Function get_countries_names() correctly returns list "
              "with countries.")

    def test_02__check_if_prepare_data_to_save_returns_list(self):
        url = f"https://api.covid19api.com/dayone/country/poland/status/confirmed"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        country_data = api_handling.prepare_data_to_save(response.json())

        self.assertIsInstance(country_data, list, msg="Function prepare_data_to_save() "
                                                      "does not return a list.")
        print("> (test 2) Function prepare_data_to_save() returns list.")

    def test_03__check_if_prepare_data_to_save_correctly_returns_values(self):
        url = f"https://api.covid19api.com/dayone/country/poland/status/confirmed"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        country_data = api_handling.prepare_data_to_save(response.json())

        self.assertGreater(len(country_data), 0, msg="Function prepare_data_to_save() "
                                                     "does not return values from correct country.")
        print("> (test 3) Function prepare_data_to_save() correctly get data form "
              "existing country.")

    def test_04__check_if_save_to_csv_correctly_create_csv_file(self):
        data = [[1, 2, 3], [1, 2, 3]]
        self.assertTrue(api_handling.save_to_csv(data, 'simple'),
                        msg="Function save_to_csv() does not correctly save data.")

        print("> (test 4) Function save_to_csv() correctly create .csv file.")

    def test_05__check_if_prepare_data_to_save_correctly_change_input(self):
        url = f"https://api.covid19api.com/dayone/country/poland/status/confirmed"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.json()

        prepared_data = api_handling.prepare_data_to_save(data)

        self.assertEqual(len(data), len(prepared_data), msg="Function prepare_data_to_save() "
                                                            "incorrectly returns data.")

        print("> (test 5) Function prepare_data_to_save() correctly change and output "
              "given data.")


if __name__ == '__main__':
    unittest.main()
