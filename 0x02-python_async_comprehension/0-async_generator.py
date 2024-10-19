#!/usr/bin/env python3

""" A coroutine that take no argumet """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:

    """
        A coroutine function that takes no argument and
        return a list of float.

        Yield:
            A list of random number betwwen 0 to 10
    """
    for _ in range(10):
        rand_num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand_num
