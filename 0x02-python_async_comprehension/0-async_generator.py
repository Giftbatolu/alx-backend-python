#!/usr/bin/env python3

""" A coroutine that take no argumet """

import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    """
        A coroutine function that takes no argument and
        return a list of float.
    """
    for _ in range(10):
        rand_num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield rand_num
