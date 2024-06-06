#!/usr/bin/env python3
""" Duck type module """
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ the function to Annotate """
    return [(i, len(i)) for i in lst]
