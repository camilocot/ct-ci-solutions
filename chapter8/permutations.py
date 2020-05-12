# Given a collection of distinct integers, return all possible permutations.

# Basically, for each item from left to right, all the permutations of the remaining
# items are generated (and each one is added with the current elements).
# This can be done recursively until the last item is reached at which point there is only one possible order.
# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

# Time Complexity: O(n*n!) Note that there are n! permutations and it requires O(n) time to print a a permutation.


def permute(nums):
    def helper(l):
        if l == n:
            output.append(nums[:])
        else:
            for r in range(l, n):
                nums[l], nums[r] = nums[r], nums[l]
                print(nums)
                helper(l+1)
                nums[l], nums[r] = nums[r], nums[l]
    n = len(nums)
    output = []
    helper(0)
    return output


print(permute([1, 2, 3]))
