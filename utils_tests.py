import unittest
from utils import utils

class utils_tests (unittest.TestCase):
    def test_reversed(self):
        self.assertEqual(utils.reversed(562), 265)
        self.assertEqual(utils.reversed(-526),-625)

        self.assertEqual(utils.reversed(1.5), 'Input is not a int number')
        self.assertEqual(utils.reversed('test'), 'Input is not a int number')

    def test_formatter(self):
        self.assertEqual(utils.formatter(562), ('0b1000110010', '0o1062'))
        self.assertEqual(utils.formatter(-562), ('-0b1000110010', '-0o1062'))

        self.assertEqual(utils.formatter(1.5), 'Input is not a int number')
        self.assertEqual(utils.formatter('test'), 'Input is not a int number')
        
#if __name__ == '__main__':
 #   unittest.main()
