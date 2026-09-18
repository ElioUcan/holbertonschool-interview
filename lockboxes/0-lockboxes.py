#!/usr/bin/python3
"""
Module to solve task problem.
"""


def canUnlockAll(boxes):

    """ Determines if all boxes can be opened. """

    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    unlocked = {0}
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == n
