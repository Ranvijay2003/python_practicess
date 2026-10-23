from math import factorial

#5 1*2*3*4*5

def get_factorial(y):
    fact=1
    for i in range(1, y+1):
        fact=fact*i
    print("fact=",fact)
    return fact


# x = int(input())
# get_factorial(x)