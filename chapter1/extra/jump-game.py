# Given an integer list where each number represents the number of hops you can make,
# determine whether you can reach to the last index starting at index 0.
# I just iterate and update the maximal index that I can reach
# https://leetcode.com/problems/jump-game


def can_jump(arr):
    reach = 0
    n = len(arr)
    for i in range(n):
        if i > reach:
            return False

        reach = max(i + arr[i], reach)
    return True


print(can_jump([2, 2, 0, 0]))
