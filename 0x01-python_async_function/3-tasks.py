#!/usr/bin/env python3

""" Regular function that return asyncio.Task """

import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        A regular functiin that take argument max_delay
        and return asyncio.Task

        Args:
            max_delay - The maximun number passed to the
                function

        Return:
            asyncio.Task
    """
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))

    return task
