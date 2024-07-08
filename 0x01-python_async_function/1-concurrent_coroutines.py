#!/usr/bin/env python3
"""
Execute multiple coroutines at the same time
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times with the specified max_delay
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): delay value to be passed to wait_random
    Returns:
        List[float]: list of delay values
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
