#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random


async def wait_random(max_delay=10):
    """ waits for a random delay between 0 and max_delay """
    duration = random.uniform(0, max_delay)
    await asyncio.sleep(duration)
    return duration
