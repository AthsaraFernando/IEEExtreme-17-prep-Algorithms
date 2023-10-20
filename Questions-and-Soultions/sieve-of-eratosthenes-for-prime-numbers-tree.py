# Question

'''
Implement the Sieve of Eratosthenes algorithm to find all the prime numbers up to a given integer n. 
Write a function sieve_of_eratosthenes(n) that takes in an integer n and returns a list of all the prime numbers up to n.
'''

def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

# Test the function with a sample integer
n = 30
print(sieve_of_eratosthenes(n))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]



