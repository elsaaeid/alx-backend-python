#!/usr/bin/env python3
"""This function creates a task that runs the
wait_random function with the specified max_delay"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer and returns an asyncio task
    Args:
        max_delay (int)
    Returns:
        task: An asynchronous task
    """
    return asyncio.create_task(wait_random(max_delay))
