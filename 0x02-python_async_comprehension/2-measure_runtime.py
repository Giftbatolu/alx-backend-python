#!/usr/bin/env python3

""" A fuction that runs async_comprehension 4 times in parallel """

import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
        A functon that runs async_comprehension 4 times in
        and return the total time or runtime.

        Return:
            Return the run time of the function
    """
    start_time = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    elapsed_time = time.perf_counter() - start_time

    return elapsed_time
