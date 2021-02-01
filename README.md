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

This should print `{'abc': 2, 'string with spaces': 1, 'wz': 0}` in the console.

### Using Docker and CLI

Refer to previous release tagged with 
[docker-cli](https://github.com/nicolasgorrity/docker-flask-simple-app/tree/docker-cli#using-cli)
to use the Dockerized Python app with CLI.

### Using Dockerized Flask application

This application can be deployed in a Dockerized Flask API.

Build the image with
```shell script
docker build . -t test_mdm
```

Run the image with
```shell script
docker run -d -p 8000:5000 test_mdm 
```
to redirect the Docker internal port 5000 to your localhost port 8000.

After that, open a web browser and go to <http://localhost:8000>. 
This should automatically redirect to <http://localhost:8000/docs>, 
which displays the [Swagger UI](https://swagger.io/tools/swagger-ui/) of the 
API.

Use the URL <http://localhost:8000/app> to make requests to the app, such as:

<http://localhost:8000/app?query=abc&query=ab&query=de>

to query the strings `["abc", "ab", "de"]` to the application.

It should display the resulting JSON dictionary.

Error messages should be displayed in case of any wrong request.

Some parameters can be controlled using docker environment variables by adding
to the `docker run` command:
- `-e STRINGS=abcde,ab,...` to change the strings array to count from
(default is ab,abc,ab,def)
- `-e FLASK_PORT=8080` to change the port used by Flask application in the 
container (default is 5000). 
Also change the value in the port forwarding `-p 8000:8080`

## Author
[Nicolas Gorrity](https://github.com/nicolasgorrity/)

## License

Refer to [LICENSE](LICENSE) file.
