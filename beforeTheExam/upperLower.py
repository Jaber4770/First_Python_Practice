s = 'The Quick Brown Fox Jumps Over The Lazy Dog'

def count_case(s):
    upper = 0
    lower = 0
    for x in s:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
    tuple = (upper, lower)
    return tuple

result = count_case(s)
print(result)
