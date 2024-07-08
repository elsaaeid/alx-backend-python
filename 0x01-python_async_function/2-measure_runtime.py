#!/usr/bin/env python3
"""
Measures the runtime of coroutine
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    It takes two integers n and max_delay to
    measures the total execution time
    Args:
        int (int)
        max_delay (int)
    Returns:
        float: total execution time / n
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    return (end_time - start_time)
