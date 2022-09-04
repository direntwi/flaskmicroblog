import sys
import time

sys.setrecursionlimit(1500)

def tailcall(n, a):
    if n == 0 or n == a:
        return a
    else:
        return tailcall(n-1, n*a)

def main():
    startTime = time.time()
    ans = tailcall(1000, 1)
    endTime = time.time()
    print('Answer is ' + str(ans))
    print('Runtime for tail call optimization is {}'.format(endTime - startTime))

main()