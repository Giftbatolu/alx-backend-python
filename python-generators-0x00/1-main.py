#!/usr/bin/python3
from itertools import islice
stream_mod = __import__('0-stream_users')

# iterate over the generator function and print only the first 6 rows

for user in islice(stream_mod.stream_users(), 6):
    print(user)