# Power Set: Write a method to return all subsets of a set.

# Time complexity: 2^n When we generate a subset, each element has the "choice" of either being in there or not. ç
# That is, for the first element, there are two choices: it is either in the set or it is not. For
# the second, there are two, etc. So, doing {2 * 2 * . . .} n times gives us 2" subsets.

# Space complexity: There are 2" subsets and each of the n elements will be contained in half of the
# subsets(which 2^n-1 subsets). Therefore, the total number of elements across all of
# those subsets is n * 2^n-1.

# Generating P(n) for the general case is just a simple generalization of the above steps. We compute
# P(n-1), clone the results, and then add an to each of these cloned sets.


def power_set(arr):

    res = [[]]

    for item in arr:
        res += [i + [item] for i in res]

    return res


def power_set_recursive(arr):

    def helper(index):
        all_subsets = []
        # Base case - add empty set
        if index == len(arr):
            all_subsets.append([])
        else:
            subsets = helper(index + 1)

            for subset in subsets:
                all_subsets.append(subset)
                all_subsets.append(subset + [arr[index]])

        return all_subsets

    return helper(0)


# Combinatorial

# We have 2 choices for each element, 1.- the element is in the set (the yes state)
# or 2.- the element is not in the set (the "no" state). We can represent this as a binary
# string, iterating through all the binary numbers from 0 to 2^n and convert them to the set

def power_set_bitwise(arr):
    def convert_int_to_set(k):
        fmt = '0{}b'.format(len(arr))
        digits = [int(d) for d in format(k, fmt)]

        subset = []
        for i, v in enumerate(digits):
            if v:
                subset.append(arr[i])
        return subset

    # Compute 2^n
    high = 1 << len(arr)
    subset = []
    for k in range(high):
        subset.append(convert_int_to_set(k))

    return subset


def convertIntToSet(x, aset):
    subset = []
    index = 0
    k = x
    while k > 0:
        if k & 1 == 1 and aset[index] not in subset:
            subset.append(aset[index])
        index += 1
        k >>= 1
    return subset


print(power_set_bitwise([1, 2, 3]))
