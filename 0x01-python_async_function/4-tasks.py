#!/usr/bin/env python3

""" Create a function task_wait_n """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        A function that create and return a list of
        max_delay from task_wait_random.

        Args:
            n (int) - Number of task to create.
            max_delay(int) - Maximiun delay for task_wait_n

        Return:
            List[float] - list of delays in ascending order

    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
