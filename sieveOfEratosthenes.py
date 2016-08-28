"""
Generate prime numbers efficiently using Sieve of Eratosthenes algorithm.
"""
def primes_sieve2(limit):
    limit = limit + 1
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            print i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

# Test: Generate prime numbers until number 10
primes_sieve2(10)