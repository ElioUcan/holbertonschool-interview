#!/usr/bin/python3

"""
Min operations problem of reasoning

"""


def minOperations(n):
    """min operations function"""
    if n <= 1:
        return 0

    numOp = 0
    f = 2

    while f * f <= n:
        while n % f == 0:
            numOp += f
            n //= f
        f += 1

    if n > 1:
        numOp += n
    return numOp
