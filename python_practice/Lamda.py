from functools import *
def is_ev(nums):
    return nums%2 == 0
def is_dob(nums):
    return nums*2
def is_sum(n):
    return 1
nums = [2, 3, 4, 5, 6, 7, 8, 9]
ev = list(filter(lambda nums : nums%2 == 0, nums))
print(ev)
double = list(map(lambda a : a*2 ,ev))
print(double)
sum = reduce(lambda a,b : a+b,double)
print(sum)
