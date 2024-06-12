#!/usr/bin/env python3
""" Async Generator module """
import asyncio
from typing import List
import random


async def async_generator() -> List[float]:
    """ Async Generator """
    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
