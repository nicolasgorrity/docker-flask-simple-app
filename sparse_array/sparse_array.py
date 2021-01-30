from collections import Counter
from typing import Iterable, Dict


class StringCounter:

    """
    Offers methods to count the occurrences of some strings in an array
    """

    def __init__(self, strings: Iterable[str]):
        """
        :param strings: array of strings to count from
        """
        self.counts = Counter(strings)

    def count_query(self, query: str) -> int:
        """
        :param query: evaluated string
        :return: number of occurrences of query in the strings array given in
            constructor
        """
        return self.counts[query]

    def count_queries(self, queries: Iterable[str]) -> Dict[str, int]:
        """
        :param queries: array of strings to count
        :return: dictionary associating key queries to number of occurrences
            in the strings array given in constructor
        """
        return dict((query, self.counts[query]) for query in queries)
