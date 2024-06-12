#!/usr/bin/env python3
""" Tasks module """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times with the specified max_delay """
    coroutine = []
    for i in range(n):
        coroutine.append(task_wait_random(max_delay))
    res = await asyncio.gather(*coroutine)
    return sorted(res)
