"""
    ### Finding the numbers

    You are given an array A containing 2*N+2 positive numbers, out of which
N numbers are repeated exactly once and the other two numbers occur exactly 
once and are distinct. You need to find the other two numbers and print them
in ascending order.

Input :

    The first line contains a value T, which denotes the number of test cases.
Then T test cases follow .The first line of each test case contains a value N.
The next line contains 2*N+2 space separated integers.

Output :

    Print in a new line the two numbers in ascending order.

    Constraints :
    * 1<=T<=100
    * 1<=N<=10^6
    * 1<=A[i]<=5*10^8

    Example:
    ```
        Input :
        2
        2
        1 2 3 2 1 4
        1
        2 1 3 2

        Output :
        3 4
        1 3
    ```

    See [The Google example problem](http://practice.geeksforgeeks.org/problems/finding-the-numbers/0)
"""
import sys
import argparse

debugging = False
logging = True

def dbg(f, *args):
    if debugging:
        print(('  DBG:' + f).format(*args))

def log(f, *args):
    if logging:
        print((f).format(*args))
        
def log_error(f, *args):
    if logging:
        print(('*** ERROR:' + f).format(*args))       

#-----------------------------------------------------------------------------

def undups(A):
    nope = set()
    for v in A:
        if v in nope:
            nope.remove(v)
        else:
            nope.add(v)
    return sorted(nope)

#-----------------------------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("-d", 
                    "--debug", help="log debugging information",
                    action="store_true")
args = parser.parse_args()

debugging = args.debug

with sys.stdin as f:
    testcases = int(f.readline().strip())
    for t in range(testcases):
        dbg('--- Test case: {0}', t)
        n = int(f.readline().strip())       
        A = [int(x) for x in f.readline().strip().split()]
        dbg('N is {0}', n)
        dbg('{0}', A)
        assert len(A) == n*2+2
        r = undups(A)
        print(' '.join([str(x) for x in r]))

        
