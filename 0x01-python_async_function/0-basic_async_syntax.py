#!/usr/bin/env python3
"""
Defines an asynchronous coroutine that
takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a random delay
    between 0 and max_delay (included and float value) seconds

    Args:
        max_delay (int): maximum delay value

    Returns:
       the random delay time value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
