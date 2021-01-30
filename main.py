import argparse
import os
from typing import List

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


def main(args: argparse.Namespace) -> None:
    """ Prints in stdout the number of occurences of each input query in the
    list of strings contained in environment variable STRINGS

    :param args: argparse namespace containing strings attribute
    """
    queries = args.queries.split(',')
    strings = read_strings_from_env()

    string_counter = StringCounter(strings)
    counts = string_counter.count_queries(queries)

    print(counts)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple string counter')
    parser.add_argument('queries', type=str)

    main(parser.parse_args())
