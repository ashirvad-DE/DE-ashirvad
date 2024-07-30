import unittest
from parse_fixed_width import parse_fixed_width_file
import os

class TestParseFixedWidthFile(unittest.TestCase):
    def setUp(self):
        self.spec_file = 'data/spec_sample.txt'
        self.input_file = 'data/input_sample.txt'
        self.output_file = 'data/output_test.csv'
        self.expected_output_file = 'data/output_expected.csv'

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_parse_fixed_width_file(self):
        parse_fixed_width_file(self.spec_file, self.input_file, self.output_file)
        
        with open(self.output_file, 'r') as f:
            output = f.read()
        
        with open(self.expected_output_file, 'r') as f:
            expected_output = f.read()
        
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
