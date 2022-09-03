import sys

sys.setrecursionlimit(1500)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(1000))

#for some reason the runtime for 1000! is less for this recursion algorithm as compared to the TCO