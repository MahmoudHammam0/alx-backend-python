#!/usr/bin/env python3
""" function sum_list module """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ return sum of a list of floats """
    sum: float = 0.0
    for element in input_list:
        sum += element
    return sum
