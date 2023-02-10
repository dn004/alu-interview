#!/usr/bin/python3
#least number of operations using copy all & paste

def minOperations(n):
# least number of operations resulting in n & H

    if n <= 1:
        return 0

    for i in range(2, int((n/2)+1)):
        if n % i == 0:
            return minOperations(int(n/i)) + i
    return n
