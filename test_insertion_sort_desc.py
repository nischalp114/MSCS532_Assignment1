import unittest
from insertion_sort_desc import insertion_sort_desc

class TestInsertionSortDesc(unittest.TestCase):
    def test_basic(self):
        a = [5, 2, 9, 1]
        insertion_sort_desc(a)
        self.assertEqual(a, [9, 5, 2, 1])

    def test_already_desc(self):
        a = [10, 10, 5, 0, -3]
        insertion_sort_desc(a)
        self.assertEqual(a, [10, 10, 5, 0, -3])

    def test_with_duplicates(self):
        a = [3, 3, 2, 2, 1, 1]
        insertion_sort_desc(a)
        self.assertEqual(a, [3, 3, 2, 2, 1, 1])

    def test_negatives(self):
        a = [-1, -5, -3, 0]
        insertion_sort_desc(a)
        self.assertEqual(a, [0, -1, -3, -5])

    def test_empty(self):
    a = []
    insertion_sort_desc(a)
    self.assertEqual(a, [])

    def test_single(self):
    a = [42]
    insertion_sort_desc(a)
    self.assertEqual(a, [42])

if __name__ == "__main__":
    unittest.main()
