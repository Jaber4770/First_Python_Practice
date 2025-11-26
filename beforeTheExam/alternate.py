#Write a function alternate_case(s) that #returns the input string with characters in #alternating upper and lower case, starting #with uppercase.

def alternate(s):
    result = []
    for i, char in enumerate(s):
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)

s = 'The Quick Brown Fox Jumps Over The Lazy Dog'
result = alternate(s)
print(result)
