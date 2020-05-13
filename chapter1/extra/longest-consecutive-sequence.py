# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Your algorithm should run in O(n) complexity.
# https://leetcode.com/problems/longest-consecutive-sequence/

# it considers numbers in nums that are the begining of a sequence,
# attempting to count as high as possible from that number using only numbers in nums.
# After it counts too high (i.e. currentNum refers to a number that nums does not contain),
# it records the length of the sequence if it is larger than the current best.

# It runs on O(n) since the while loop will only run n times, it will only executed for numbers that
# are the begining of a sequence.


class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0

        nums = set(nums)

        for num in nums:
            if num - 1 in nums:
                current_num = num
                current_streak = 1

                while current_num + 1 in nums:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
