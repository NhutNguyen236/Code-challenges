def check_palindrome(number):
    #Input: A number which is passed from find_reverse_number function 
    #Output: flag value for
    temp = number
    flag = 0
    reverse = 0
    while(temp > 0):
        last_digit = temp % 10
        reverse = (reverse * 10) + last_digit
        temp = temp // 10
    if(number == reverse):
        flag = 1
        return flag
    else:
        return flag

def find_reverse_number(n):
    #Input: A random integer to tell which place that palindrome number it should be
    #Output: A palindrome number ar
    
    start_point = 0
    nth_palin = 0
    palin_assign_time = 0
    
    while(palin_assign_time < n):

        if(check_palindrome(start_point) == 1):
            nth_palin = start_point
            print(nth_palin)
            palin_assign_time += 1

        start_point += 1

    print(palin_assign_time)    
    return(nth_palin)

print(find_reverse_number(20))
