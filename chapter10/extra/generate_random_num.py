# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
# less than 0(n) time complexity

# 710. Random Pick with Blacklist
# https://leetcode.com/problems/random-pick-with-blacklist/


import random


# O(n)
def generate_random_number(l, n):
    l = set(l)
    res = []*(n - len)

    for i in range(n):
        if i not in l:
            res.append(i)

    return random.choice(res)


# Treat the first N - |B | numbers as those we can pick from. Iterate through the blacklisted numbers and map each of them
# to one of the remaining non-blacklisted | B | numbers
# For picking, just pick a random uniform int in 0, N - |B | .
# If its not blacklisted, return the number. If it is, return the number that its mapped to
# Time Complexity: O(B) preprocessing. O(1) pick.
# Space Complexity: O(B)
class Solution:
    def __init__(self, N, blacklist):
        blacklist = sorted(blacklist)
        self.b = set(blacklist)
        self.m = {}
        self.length = N - len(blacklist)
        j = 0
        for i in range(self.length, N):
            if i not in self.b:
                self.m[blacklist[j]] = i
                j += 1

    def pick(self):
        i = random.randint(0, self.length - 1)
        return self.m[i] if i in self.m else i


# Without sourting
class Solution:

    def __init__(self, N, blacklist):
        blacklist = set(blacklist)
        self.length = N - len(blacklist)
        self.remap = {}
        need_remap = []
        for x in blacklist:
            if x < self.length:
                need_remap.append(x)
        j = 0
        for i in range(self.length, N):
            if i not in blacklist:
                self.remap[need_remap[j]] = i
                j += 1

    def pick(self):
        idx = random.randrange(self.length)
        return self.remap[idx] if idx in self.remap else idx

# This search will give you a complexity of log(K.length)


# Time Complexity: BlogB preprocessing. O(logB) pick.
# Space Complexity: O(B). Or O(1) if in-place sort is used and input array is not considered extra space.

# Lets say that we are given a non-empty blacklist k and need to figure out what the rnd-th zero-based largest whitelist number,
# hereafter called W[rnd]
# Use binary search to find the largest blacklist number which is smaller than W[rnd]

# https://stackoverflow.com/questions/24045158/generate-a-random-integer-from-0-to-n-1-which-is-not-in-the-list?rq=1

def generate_random_number_bs(k, n):
    k = sorted(k)
    rnd = random.randint(0, n - len(k))
    l = 0
    r = len(k)-1

    # use binary search to find the largest blacklist number which is smaller than rnd
    while l < r:
        mid = (l + r + 1) // 2  # ??? +1
        # If k[mid] > rnd, then k[mid] is larger than W[rnd]. k[mid] and larger blacklist numbers are no longer candidates, so r=mid−1.
        # if k[mid] <= rnd, then k[mid] is smaller than W[rnd]. blacklist numbers smaller than k[mid] are no longer candidates, so l=mid.
        if (k[mid] - mid > rnd):
            r = mid - 1
        else:
            l = mid

    # the search space will narrow down to one blacklist number.
    # If it is smaller than W[rnd], it is the largest blacklist number smaller than W[rnd].
    # In this case, the equation for W[rnd] is rnd+lo+1.
    # If it is larger than W[rnd], no blacklist number is smaller than w[rnd], so W[rnd] is simply rnd.
    return rnd+l if l == r and k[l] - l <= rnd else rnd


print(generate_random_number_bs([4, 6, 9, 14], 15))
