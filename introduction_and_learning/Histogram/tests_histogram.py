import unittest
import histograms as hg


class HistogramTxtTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.hg_txt = hg.HistogramTxt()

    def test_01__check_opening_and_read_result__return_read_data_as_str(self):
        source_path = "data_source/sample.txt"
        self.assertIsInstance(self.hg_txt.read_data(source_path), str,
                              msg="File specified to method was not a .txt file.")

    def test_02__check_if_histogram_was_correctly_created__return_dict(self):
        self.assertIsInstance(self.hg_txt.create("input data"), dict,
                              msg="Create method was not return dictionary.")

    def test_03__check_if_histogram_report_was_generated_correctly__return_bool(self):
        self.assertIsInstance(self.hg_txt.generate_report({"hist": "val"}, path="./reports/report"), bool,
                              msg="Generate report was not return bool.")


if __name__ == '__main__':
    unittest.main()
