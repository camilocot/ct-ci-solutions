# Find two prime numbers with given sum
# Given an even number(greater than 2), print two prime numbers whose sum will be equal to given number.
# There may be several combinations possible. Print only first such pair.

# An interesting point is, a solution always exist according to Goldbach’s conjecture.
# The idea is to find all the primes less than or equal to the given number N using Sieve of Eratosthenes.
# Python 3 program to find a prime number
# pair whose sum is equal to given number
# Python 3 program to print super primes
# less than or equal to n.

# Generate all prime numbers less than n.


def SieveOfEratosthenes(n, isPrime):

    # Initialize all entries of boolean
    # array as True. A value in isPrime[i]
    # will finally be False if i is Not a
    # prime, else True bool isPrime[n+1]
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1):
        isPrime[i] = True

    p = 2
    while(p*p <= n):

        # If isPrime[p] is not changed,
        # then it is a prime
        if (isPrime[p] == True):

            # Update all multiples of p
            i = p*p
            while(i <= n):
                isPrime[i] = False
                i += p
        p += 1

# Prints a prime pair with given sum


def findPrimePair(n):

    # Generating primes using Sieve
    isPrime = [0] * (n+1)
    SieveOfEratosthenes(n, isPrime)

    # Traversing all numbers to find
    # first pair
    for i in range(0, n):

        if (isPrime[i] and isPrime[n - i]):

            print(i, (n - i))
            return


# Driven program
n = 74
findPrimePair(n)
