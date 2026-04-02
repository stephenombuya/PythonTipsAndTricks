import unittest
from exercises.basics.list_operations import flatten_example
from exercises.intermediate.dictionaries import merge_dictionaries


class TestExercises(unittest.TestCase):

    def test_flatten(self):
        result = flatten_example()
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_merge_dict(self):
        result = merge_dictionaries()
        self.assertEqual(result, {'a': 1, 'b': 3, 'c': 4})


if __name__ == "__main__":
    unittest.main()
