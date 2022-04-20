# madlib-cli
Lab 03 - Class 03

### Author: Polo Gonzalez

### Description
Madlib game structure.
3 distinct functions, each of which has individual responsibility.

- **read_template** raises and exception if the path passed does not lead to a file, otherwise returns a string of the file's text
- **parse_template** takes a string (for this game the one returned by read_template) and returns a string with language parts removed and a separate list of those language parts
- **merge** takes a string with language parts removed and a list of user entered language parts and returns a string with the language parts inserted into the template

### Setup

Python3 with Pytest

##### Tests

- Run `pytest` to run tests
- 4 tests passed:
  - read_template -asserts proper return output
  - parse_template -asserts proper return output
  - merge -proper return output
  - read_template -asserts the right exception is raised if the path does not lead to a file

---