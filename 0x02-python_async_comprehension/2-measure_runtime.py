#!/usr/bin/env python3
"""
A coroutine that mesures time
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel
    and measure_runtime should measure the total runtime and return it
    """
    start_time = time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time()
    return end_time - start_time
