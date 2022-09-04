import sys
import time

sys.setrecursionlimit(1500)

def tailcall(n, a):
    if n == 0 or n == a:
        return a
    else:
        return tailcall(n-1, n*a)

def recursive(n):
    if n == 0:
        return 1
    return n * recursive(n-1)

def main():
    startTime1 = time.time()
    ans=recursive(1000)
    endTime1 = time.time()
    print('Answer is ' + str(ans))
    print('Runtime for recursive algorithm is {} seconds'.format(endTime1 - startTime1))

    startTime2 = time.time()
    tailcall(1000, 1)
    endTime2 = time.time()
    print('Runtime for tail call optimization is {} seconds'.format(endTime2 - startTime2))

main()
