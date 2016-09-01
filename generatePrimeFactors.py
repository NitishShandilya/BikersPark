"""
Given a number n, write an efficient function to print all prime factors of n.

Solution:
Following are the steps to find all prime factors.
1) While n is divisible by 2, print 2 and divide n by 2.
2) After step 1, n must be odd. Now start a loop from i = 3 to square root of n.
    While i divides n, print i and divide n by i, increment i by 2 and continue.
3) If n is a prime number and is greater than 2, then n will not become 1 by above two steps.
    So print n if it is greater than 2.
    Based on concept: the smallest prime factor of a composite number N is less than or equal to N.
    That is the reason, each time we divide the number by the prime factor and run only until the square
    root of that number.
"""
import math
def generatePrimeFactors(n):
    primeFactors = []
    while n%2 == 0:
        primeFactors.append(str(2))
        n /= 2

    # n must be odd since 2 is the only prime factor. Therefore, increment in steps of 2.
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n%i == 0:
            primeFactors.append(str(i))
            n /= i

    # This is to handle the case, when n is a prime number. If after all the reductions,
    # it is still a prime number, then it has to be greater than 2. We print this as well.
    if n > 2:
        primeFactors.append(str(n))

    return " ".join(primeFactors)

# Test
n = 276
print generatePrimeFactors(n)