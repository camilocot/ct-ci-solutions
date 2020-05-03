# Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[ i] =i.
# Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
# array A.


# Brute force
def magic_index(arr):
    for idx, value in enumerate(arr):
        if idx == value:
            return True

    return False


# Intuition : We may recognize that this problem sounds a lot like the classic binary search problem.
# So, if the middle element is already too small to be a magic index, then when we move to the left,
# subtracting k indexes and (at least) k values, all subsequent elements will also be too small.

def magic_index_bs(arr):

    def binary_search(left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        if arr[mid] == mid:
            return mid

        if arr[mid] > mid:
            return binary_search(left, mid - 1)
        else:
            return binary_search(mid + 1, right)

    return binary_search(0, len(arr)-1)


print(magic_index_bs([-40, -20, -1, 1, 2, 3, 4, 7, 9, 12, 13]))

# Follow Up: What if the elements are not distinct?

# The general pattern is that we compare mid Index and mid Value for equality first.
# Then, if they are not equal, we recursively search the left and right sides as follows:
# - Left side: search indices start through Math. min(midlndex - 1, midValue).
# - Right side: search indices Math. max(midlndex + 1, midValue) through end.


def magic_index_bs_non_distinct(arr):

    def binary_search(left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        if arr[mid] == mid:
            return mid

        return binary_search(left, min(mid - 1, arr[mid])) or binary_search(max(mid + 1, arr[mid]), right)

    return binary_search(0, len(arr)-1)


print(magic_index_bs_non_distinct([-10, -5, 2, 2, 3, 4, 7, 9, 12, 13]))
