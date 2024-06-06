#!/usr/bin/env python3
""" sum_mixed_list function module """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes a list of integers and floats and returns their sum """
    sum: float = 0.0
    for element in mxd_lst:
        sum += element
    return sum
