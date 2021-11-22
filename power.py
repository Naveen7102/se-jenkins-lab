#!/usr/bin/python3
# Source code for power

def power(a):
    ans = 1.0
    for i in range(a[1]):
        ans = ans*a[0]
     
    return ans
