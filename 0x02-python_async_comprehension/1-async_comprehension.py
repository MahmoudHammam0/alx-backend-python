#!/usr/bin/env python3
""" Async Comprehensions module """
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ will collect 10 random numbers then return the 10 random numbers """
    return [num async for num in async_generator()]
