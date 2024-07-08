#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines at the same time with async
    Args:
        n (int): number of times
        max_delay (int): delay value to be passed to wait_random
    Returns:
        List[float]: list of delay values
    """
    tasks = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(tasks)
