# Given a sorted list of integers, square the elements and give the output in sorted order.
# https://www.geeksforgeeks.org/sort-array-converting-elements-squares/

# Efficient solution is based on the fact that given array is already sorted. We do following two steps.

# Divide the array into two part “Negative and positive “.
# Use merge function to merge two sorted arrays into a single sorted array.

# Python3 program to Sort square of the numbers of the array

# function to sort array after doing squares of elements


def sortSquares(arr, n):

    # first dived array into part negative and positive
    K = 0
    for K in range(n):
        if (arr[K] >= 0):
            break

    # Now do the same process that we learn
    # in merge sort to merge to two sorted array
    # here both two half are sorted and we traverse
    # first half in reverse meaner because
    # first half contain negative element
    i = K - 1  # Initial index of first half
    j = K  # Initial index of second half
    ind = 0  # Initial index of temp array

    # store sorted array
    temp = [0]*n
    while (i >= 0 and j < n):

        if (arr[i] * arr[i] < arr[j] * arr[j]):
            temp[ind] = arr[i] * arr[i]
            i -= 1

        else:

            temp[ind] = arr[j] * arr[j]
            j += 1

        ind += 1

    ''' Copy the remaining elements of first half '''
    while (i >= 0):

        temp[ind] = arr[i] * arr[i]
        i -= 1
        ind += 1

    ''' Copy the remaining elements of second half '''
    while (j < n):
        temp[ind] = arr[j] * arr[j]
        j += 1
        ind += 1

    # copy 'temp' array into original array
    for i in range(n):
        arr[i] = temp[i]


# Driver code
arr = [-6, -3, -1, 2, 4, 5]
n = len(arr)

print("Before sort ")
for i in range(n):
    print(arr[i], end=" ")

sortSquares(arr, n)
print("\nAfter Sort ")
for i in range(n):
    print(arr[i], end=" ")

# This code is contributed by shubhamsingh10
