# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

# Intuition: The very last hop the child makes-the one that lands her on the nth step-was either a 3-step hop, a
# 2-step hop, or a 1-step hop.

# note that the number of ways will quickly overflow the bounds of an integer.

import sys


def count_ways(x):
    if x < 0:
        return 0

    size = x + 1
    memo = [0] * size

    memo[0] = 1
    memo[1] = 1
    memo[2] = 2

    for i in range(3, size):
        print(i)
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo[x]


print(count_ways(200))
print(sys.maxsize)
