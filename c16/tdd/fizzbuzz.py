#!/usr/bin/python3
"""
This is the `fizzbuzz' module
It contains the `fizzbuzz` function
"""

def fizzbuzz(numbers):
    """implements the fizzbuzz program"""
    new_list = []

    for number in numbers:
        if type(number) is not int:
            raise TypeError("number must be an integer")

        if number % 15 == 0:
            new_list.append('fizzbuzz')
        elif number % 3 == 0:
            new_list.append('fizz')
        elif number % 5 == 0:
            new_list.append('buzz')
        else:
            new_list.append(number)
    return new_list
