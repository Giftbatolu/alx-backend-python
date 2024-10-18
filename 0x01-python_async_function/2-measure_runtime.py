#!/usr/bin/env python3

""" Asynchronous Coroutine """

import asyncio
import time
from typing import List
import random

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
        Function with integers n and max_delay as argumets
        that measures the total execution time for wait_n

        Args:
            n - Number of time to loop through wait_ramdom
            max_delay: The maximun number

        Return:
            A float number of total_time divided by n
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time

    return (elapsed_time / n)
