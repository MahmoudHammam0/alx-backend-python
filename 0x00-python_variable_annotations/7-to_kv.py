#!/usr/bin/env python3
""" to_kv function module """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple with str and float """
    return (k, v**2)
