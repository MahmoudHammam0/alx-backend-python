#!/usr/bin/env python3
""" More involved type annotations module """
from typing import Any, Union, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ the function to annotate its paramaters """
    if key in dct:
        return dct[key]
    else:
        return default
