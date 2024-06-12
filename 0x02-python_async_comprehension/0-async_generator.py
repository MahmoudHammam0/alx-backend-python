#!/usr/bin/env python3
""" Async Generator module """
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
