#!/usr/bin/python3
"""
def rain(walls)
"""


def rain(walls):
    """
    calculate how many square units of water will be retained after it rains
    """
    if not walls:
        return 0
    walls_length = len(walls)
    water = 0
    for x in range(walls_length):
        left = walls[x]
        for i in range(x):
            left = max(left, walls[i])
        right = walls[x]
        for i in range(x + 1, len(walls)):
            right = max(right, walls[i])
        water += min(left, right) - walls[x]
    return water
