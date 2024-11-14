import unittest
import convert


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_str_to_float_1(self):
        string = "3463.45"
        expected = 3463.45
        result = convert.str_to_float(string)
        self.assertEqual(expected, result)

    def test_str_to_float_2(self):
        string = "$3463.45"
        expected = None
        result = convert.str_to_float(string)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()