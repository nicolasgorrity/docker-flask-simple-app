import argparse
import os
from typing import List, Iterable, Dict

from string_counter import StringCounter


def read_strings_from_env(variable: str = 'STRINGS') -> List[str]:
    """
    :param variable: name of environment variable to read strings from
    :return: list of strings read from environment variable
    """
    if variable not in os.environ:
        raise EnvironmentError(f'Environment variable {variable} must be '
                               f'defined and contain strings to query')
    raw_variable = os.environ[variable]
    return raw_variable.split(',')


def main_app(queries: Iterable[str]) -> Dict[str, int]:
    """ Prints in stdout the number of occurences of each input query in the
    list of strings contained in environment variable STRINGS

    :param queries: array of strings to query
    :return: dictionary matching each query to its result
    """
    strings = read_strings_from_env()

    string_counter = StringCounter(strings)
    return string_counter.count_queries(queries)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple string counter')
    parser.add_argument('queries', type=str)

    args = parser.parse_args()

    result = main_app(args.queries.split(','))
    print(result)
