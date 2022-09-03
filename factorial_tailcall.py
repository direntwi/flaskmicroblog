import sys

sys.setrecursionlimit(1500)

def factorial(n, a):
    if n == 0 or n == a:
        return a
    else:
        return factorial(n-1, n*a)

print(factorial(1000,1))

