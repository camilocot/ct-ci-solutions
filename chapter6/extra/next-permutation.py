# Given a number represented by a list of digits, find the next greater permutation of a number,
# in terms of lexicographic ordering. If there is not greater permutation possible,
# return the permutation with the lowest value/ordering.
# https://leetcode.com/problems/next-permutation/

# Initial seq: 0125330
# Find longest non-ascending suffix: 012 5330
# Identify pivot: 01 2 5330
# Find rightmost successor to pivot on the suffix: 01 2 53 3 0
# Swap with pivot: 01 3 53 2 0
# Reverse the suffix: 013 0253
# Done


def nextPermutation(self, nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   # nums are in descending order
        nums.reverse()
        return
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
