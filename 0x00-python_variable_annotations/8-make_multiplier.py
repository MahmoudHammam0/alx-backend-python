#!/usr/bin/env python3
""" make_multiplier module """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """
    def helper(x: float) -> float:
        """ helper function that multiplies a float by multiplier """
        return x * multiplier
    return helper
