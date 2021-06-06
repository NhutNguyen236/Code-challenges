'''
Input: 10
Output: 7

2^2 = 4, 2^3 = 8, 3^2 = 9, 1 

a^b in 1 to n, a and b are not less than 2
Attempt 1: High space complexity
'''
import math 
import time

def sukuna(n):
    # Initialize count
    count = 0

    # Initialize an array of n number
    n_array = [i for i in range(1,n+1)]
    
    # Find stop point in n_array as an integer
    stop_point = int(math.sqrt(n))

    # Loop from 2 to the break point
    for i in range(2, stop_point + 1):
        biggest_root = int(math.log(n,i))
        for j in range(2,biggest_root + 1):
            if(i**j in n_array):
                count = count + 1
                
    result = n - count
    
    return result


