# String counter

Simple Python app built with Docker and Flask.

## Description

Allows to query the number of occurrences of multiple strings from a given array
of strings. 

The usage is inspired and similar to this simple
[coding challenge](https://www.hackerrank.com/challenges/sparse-arrays/problem).

## Requirements
This code was developed and tested on Ubuntu 18.04 with `python==3.7.5`.

To install required dependencies in your virtual environment:
```
pip install -r requirements.txt
```

## Module `StringCounter`

The `StringCounter` class is defined in [string_counter/](string_counter/).

The object is constructed using the string array to search:
```python
from string_counter import StringCounter
string_counter = StringCounter(['ab', 'bc', 'ab', 'def'])
```
All the counting will actually happen in the constructor with a time complexity 
of *O*(n), n being the length of the string array.

To query the number of occurrences of some strings, the class provides two 
methods:
- `count_query(...)` to get the number of occurrences of one string with a time
complexity of *O*(1):
```python
assert string_counter.count_query('ab') == 2
```
- `count_queries(...)` to get the number of occurrences of multiple strings in
a dictionary with a time complexity *O*(m), m being the number of queries:
```python
assert string_counter.count_queries(['ab', 'xz']) == {'ab': 2, 'xz': 0}
```

## Usage

### Using CLI

The script `main.py` uses the `StringCounter` class and builds an instance using
the strings in the environment variable `STRINGS`. Then it queries the
occurrences of input strings and prints the resulting dictionary.

Each string array must be delimited by commas and no space. For a string
containing spaces, use quotation marks.

```shell
STRINGS=abc,abc,"string with spaces" python -m main abc,"string with spaces",wz
```
or
```shell
export STRINGS=abc,abc,"string with spaces"
python -m main abc,"string with spaces",wz
```

### Using Docker

The program in [main.py](./main.py) can be dockerized.

Build the image with
```shell script
docker build . -t test_mdm
```

Run the image with
```shell script
docker run -t test_mdm ab,abc,bc
```
to run the program with the default strings array defined in the 
[Dockerfile](./Dockerfile). The queries can be specified as CLI arguments of
`docker run`. This should print:
```shell script
{'ab': 2, 'ab': 1, 'def': 0}
```

To run the image using a custom strings array, add the following `-e` or `--env`
parameter to the command:
```shell script
docker run -t -e STRINGS=abc,abc,abc test_mdm ab,abc,bc
```
which should print
```shell script
{'ab': 0, 'abc': 3, 'bc': 0}
```

## Author
[Nicolas Gorrity](https://github.com/nicolasgorrity/)

## License

Refer to [LICENSE](LICENSE) file.
