# Recursive Multiply: Write a recursive function to multiply two positive integers without using the
# *operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
# of those operations.

# We can think about it as the number of squares in an rxc grid.
# we could count half the squares and then double it (by adding this count to itself).
# If the number of squares is odd we divide by 2 and sum the multiplier

# This algorithm will run in O( log s) time, wheres is the smaller of the two numbers.


def mul_bitwise_memo(a, b):
    def helper(smaller, greater):
        if smaller == 0:
            return 0
        elif smaller == 1:
            return greater
        elif memo[smaller] > 0:
            return memo[smaller]

        half_prod = smaller >> 1

        if smaller % 2 == 0:
            memo[smaller] = helper(half_prod, greater) + \
                helper(half_prod, greater)
        else:
            memo[smaller] = helper(half_prod, greater) + \
                helper(half_prod + 1, greater)
        return memo[smaller]

    smaller = b if a > b else a
    greater = a if a >= b else b

    memo = [0]*(smaller+1)

    return(helper(smaller, greater))


def mul_bitwise(a, b):

    def helper(smaller, greater):
        if smaller == 0:
            return 0
        if smaller == 1:
            return greater

        half_prod = smaller >> 1

        partial = helper(half_prod, greater)

        partial += partial

        if smaller % 2 == 1:
            partial += greater

        return partial

    if a > b:
        return(helper(b, a))
    return(helper(a, b))


print(mul_bitwise_memo(5, 2))
