#!/usr/bin/python3
import datetime
import random
import sys
from time import sleep

for i in range(10000):
    sleep(random.random())
    sys.stdout.write(
        f'{random.randint(1, 255):d}.{random.randint(1, 255):d}.{random.randint(1, 255):d}.{random.randint(1, 255):d} - [{datetime.datetime.now()}] "GET /projects/260 HTTP/1.1" {random.choice([200, 301, 400, 401, 403, 404, 405, 500])} {random.randint(1, 1024)}\n'
    )
    sys.stdout.flush()
