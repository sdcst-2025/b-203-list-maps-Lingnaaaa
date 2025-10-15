"""
### Assignment 2
Prime numbers
Given a list of numbers that are integers, create a map() that shows whether each of the numbers is a perfect square.
"""

data = [76, 56, 20, 77, 42, 97, 83, 47] 
def isEven(i):
    if (i**(1/2))%1==0:
        return True
    else:
        return False
answer=list(map(isEven,data))
print(answer)


# expected output:  [False, False, False, False, False, True, False, False]

