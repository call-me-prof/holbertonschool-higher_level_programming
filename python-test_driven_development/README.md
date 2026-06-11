# Python - Test-Driven Development (TDD)

This repository contains tasks for learning and practicing **Test-Driven Development (TDD)** in Python using `doctest` and `unittest` modules. The goal is to write reliable, clean, and well-tested code according to PEP 8 standards.

## Technologies & Tools
* **Language:** Python 3.10
* **Style Guide:** [PEP 8 / pycodestyle](https://pep8.org/)
* **Testing Frameworks:** `doctest` and `unittest`
* **OS/Environment:** Ubuntu 20.04 LTS

## Files & Tasks Description

| Task | File Name | Test File | Description |
| --- | --- | --- | --- |
| **0. Integers addition** | `0-add_integer.py` | `tests/0-add_integer.txt` | A function that adds 2 integers/floats after casting them to integers. |
| **1. Divide a matrix** | `1-matrix_divided.py` | `tests/1-matrix_divided.txt` | A function that divides all elements of a matrix by a given number. |
| **2. Say my name** | `3-say_my_name.py` | `tests/3-say_my_name.txt` | A function that prints `My name is <first name> <last name>`. |
| **3. Print square** | `4-print_square.py` | `tests/4-print_square.txt` | A function that prints a square with the `#` character based on size. |
| **4. Text indentation** | `5-text_indentation.py` | `tests/5-text_indentation.txt` | A function that prints a text with 2 new lines after `.`, `?`, and `:`. |
| **5. Max integer - Unittest** | `6-max_integer.py` | `tests/6-max_integer_test.py` | Writing comprehensive unittests for an existing `max_integer` function. |

## How to Run Tests Locally

To run the interactive doctests:
```bash
python3 -m doctest -v ./tests/0-add_integer.txt
