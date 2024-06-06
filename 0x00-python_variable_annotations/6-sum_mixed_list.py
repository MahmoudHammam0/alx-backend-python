#!/usr/bin/env python3
""" sum_mixed_list function module """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    sum: float = 0.0
    for element in mxd_lst:
        sum += element
    return sum
