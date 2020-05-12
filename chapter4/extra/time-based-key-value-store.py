# Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.
# It should contain the following methods:
# set(key, value, time): sets key to value for t = time.
# get(key, time): gets the key at t = time.
# https://leetcode.com/problems/time-based-key-value-store/

# Time Complexity: O(1) for each set operation, and O(log N) for each get operation, where NN is the number of entries in the TimeMap.
# Space Complexity: O(N)

import collections


class TimeMap(object):

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        arr = self.dic[key]
        n = len(arr)

        left = 0
        right = n

        while left < right:
            mid = (left + right) / 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid

        return "" if right == 0 else arr[right - 1][1]
