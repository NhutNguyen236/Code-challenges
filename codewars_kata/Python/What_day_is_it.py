# H table query

H = {8: -3, 2: -2, 3: -2, 11: -2, 6: -1, 9: 0, 12: 0, 4: 1, 7: 1, 1: 2, 10: 2, 5: 3}
day = {0: 'Saturday', 1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}

# To return what date is it
def date_counter(n, t):
    T = n + H[t]
    d = T % 7 

    return day[d]

print(date_counter(20, 11))