#!/usr/bin/env python3

""" Async comprehension coroutine """

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        A corountine that collect 10 randon numbers from
        async_generator.

        Return:
            A list of 10 random numbers
    """
    rand_numbers = [b async for b in async_generator()]

    return rand_numbers
