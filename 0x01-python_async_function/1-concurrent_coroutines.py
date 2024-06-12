#!/usr/bin/env python3
""" multiple coroutines at the same time module """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times with the specified max_delay """
    coroutine = []
    for i in range(n):
        coroutine.append(wait_random(max_delay))
    res = await asyncio.gather(*coroutine)
    return sorted(res)
