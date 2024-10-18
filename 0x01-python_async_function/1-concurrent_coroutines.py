#!/usr/bin/env python3
""" Asynchronous Coroutine function """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
        A function that spawn wait_random function n times
        with the specified max_delay.

        Args:
            n(int) - number of times to return wait_random

            max_delay(int) - The specifed maximiun delay.

        Return(float):
            Return a list of all the delays
    """
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
