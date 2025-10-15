'''
### Assignment 3
Remove leading or trailing whitespace
Given a list of words, remove any spaces at the beginning or end of the word
'''
data = ['  apple', 'banana ', '  mango ', 'grape']
def isEven():
    data = ['  apple', 'banana ', '  mango ', 'grape']
    result=list(map(str.strip,data))
    return result
print(isEven())

# expected output: ['apple', 'banana', 'mango', 'grape']
# HINT: use the str.strip() method to remove whitespace from the beginning and end of a string

