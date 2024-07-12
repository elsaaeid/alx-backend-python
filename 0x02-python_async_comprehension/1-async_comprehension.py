#!/usr/bin/env python3
"""
Define the async_comprehension coroutine,
which takes no arguments and returns a list of floats.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Each iteration of the comprehension asynchronously waits
    for the next value yielded by async_generator()
    and adds it to the resulting list.
    """
    return [i async for i in async_generator()]
