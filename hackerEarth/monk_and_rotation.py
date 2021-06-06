# Link: https://www.hackerearth.com/practice/codemonk/
# Input: T  - Number of testcases(also the number of input array), N - number of input integers, K - number of times to rotate
# Output: an rotated array
# The problem here is that 10 test cases will be repeated by the exact input of N, K and the array 

from time import time

def rotator(array, K):
    for i in range(0, int(K)):
        array.insert(0, array.pop())
    return array

# Input T
T = input()

# For loop work for testcase_fairplay and of course 01 but it will recieve time limit exceeded error
for i in range(0, int(T)):
    # Input N and K
    N, K = input().split()

    # Input array
    array= [int(x) for x in input().split()]
    
    t1 = time()
    new_arr = rotator(array, K)
    t2 = time()

    print(t2-t1)

    # for i in range(0, int(N)):
    #     if(i == int(N) - 1):
    #         print(new_arr[i], end = " ")
    #         print("\n")
    #     else:
    #         print(new_arr[i], end = " ")

# To overcome time limit exceeded error you need to know that algorithm complexity
