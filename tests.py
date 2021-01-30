import random
import string
import unittest
from typing import List

from sparse_array import StringCounter


def generate_random_string() -> str:
    letters = string.ascii_lowercase
    length = random.randint(1, 20)
    return ''.join(random.choice(letters) for _ in range(length))


def generate_n_random_strings(n: int) -> List[str]:
    return [generate_random_string() for _ in range(n)]


def generate_random_strings(min_length: int = 1,
                            max_length: int = 1000) -> List[str]:
    size = random.randint(min_length, max_length + 1)
    return generate_n_random_strings(size)


class TestStringCounter(unittest.TestCase):

    def test_output_format(self):
        strings = generate_random_strings()
        queries = generate_random_strings()

        counts = StringCounter(strings).count_queries(queries)
        self.assertEqual(type(counts), dict)
        self.assertEqual(len(counts), len(set(queries)))
        self.assertTrue(all(type(query) == str and type(cnt) == int
                            for query, cnt in counts.items()))

    def test_empty_queries(self):
        strings = generate_random_strings()
        queries = []
        self.assertEqual(StringCounter(strings).count_queries(queries),
                         dict())

    def test_empty_strings(self):
        strings = []
        nb_queries = random.randint(1, 10)
        queries = generate_n_random_strings(nb_queries)

        self.assertEqual(StringCounter(strings).count_queries(queries),
                         {query: 0 for query in queries})

    def test_case_1(self):
        strings = ['aba', 'baba', 'aba', 'xzxb']
        queries = ['aba', 'xzxb', 'ab']
        expected_counts = [2, 1, 0]
        expected_output = {query: cnt
                           for query, cnt in zip(queries, expected_counts)}
        self.assertEqual(StringCounter(strings).count_queries(queries),
                         expected_output)

    def test_case_2(self):
        strings = ['def', 'de', 'fgh']
        queries = ['de', 'lmn', 'fgh']
        expected_counts = [1, 0, 1]
        expected_output = {query: cnt
                           for query, cnt in zip(queries, expected_counts)}
        self.assertEqual(StringCounter(strings).count_queries(queries),
                         expected_output)

    def test_case_3(self):
        strings = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj',
                   'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
        queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
        expected_counts = [1, 3, 4, 3, 2]
        expected_output = {query: cnt
                           for query, cnt in zip(queries, expected_counts)}
        self.assertEqual(StringCounter(strings).count_queries(queries),
                         expected_output)


if __name__ == '__main__':
    unittest.main()
