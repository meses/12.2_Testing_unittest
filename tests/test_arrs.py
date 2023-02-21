import unittest
from utils.arrs import get, my_slice

class TestGet(unittest.TestCase):

    def test_positive_index(self):
        self.assertEqual(get([1, 2, 3],1), 2)

    def test_negative_index(self):
        self.assertEqual(get([1, 2, 3],-1), None)

class TestMy_slice(unittest.TestCase):

    def test_positive_start(self):
        self.assertEqual(my_slice([1, 2, 3],1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1, 3), [2, 3])

    def test_negative_start(self):
        self.assertEqual(my_slice([1, 2, 3], -1), [3])
        self.assertEqual(my_slice([1, 2, 3], -4), [1, 2, 3])

    def test_empty_array(self):
        self.assertEqual(my_slice([], 0), [])

'''
if __name__ == '__main__':
    unittest.main()
'''
