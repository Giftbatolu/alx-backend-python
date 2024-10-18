#!/usr/bin/env python3
""" Asynchronous function """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        An asynchronous coroutine that waits for random
        delay between 0 and max_delay

        max_delay:
            The maxmiun delay with default value of 10.

        Return:
            The maximuin in float.
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
