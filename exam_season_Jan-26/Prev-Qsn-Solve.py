x = 'apple'
if 'a' in x:
    if 'p' in x:
        print("the word contain a and p")
    else:
        print('the word does not contain a and p')
else:
    print('the word does not contain anything')

# ------------------------------------------------
s = {1, 2, 3}
for x in s:
    if x == 3:
        print(x, "the number contain in the list")

# ------------------------------------------------


def merge_dicts(d1, d2):
    result = {}
    for x in d1:
        for y in d2:
            if x == y:
                result[x] = d1[x] + d2[y]  
    return result
        
d1 = {
    "a": [1, 2, 3],
    "b": [0, 9, 8, 7, 6]
}
d2 = {
    "a": [4, 5, 6],
    "b": [0, 9, 8, 7, 6]
}

result = merge_dicts(d1, d2)
print(result)

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------

# ------------------------------------------------
