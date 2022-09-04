import sys
import time

sys.setrecursionlimit(1500)

def recursive(n):
    if n == 0:
        return 1
    return n * recursive(n-1)

def main():
    startTime = time.time()
    ans = recursive(5)
    endTime = time.time()
    print ('Answer is ' + str(ans))
    print('Runime for recursive algorithm is {}'.format(endTime - startTime))

main()

#for some reason the runtime for 1000! is less for this recursion algorithm as compared to the TCO