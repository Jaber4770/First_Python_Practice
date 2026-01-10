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

def count_case(s):
    upper = 0
    lower = 0
    for x in s:
        if x.isupper():
            upper +=1
        elif x.islower():
            lower +=1
    return (upper, lower)

text = "Hello"
result = count_case(text)
print(result)

# ------------------------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


result = factorial(5)
print('factorial :', result)
        
# ------------------------------------------------
for i in range(3):
    if i == 2:
        break
else:
    print('Done')
# ------------------------------------------------

def common_elements(a,b):
    result = a
    for x in b:
        if x not in result:
            result.append(x)
    return result

list1 = [1,2,3,4]
list2 = [1,3,4,5,6,7,8,9,0]
removeDuplicate = common_elements(list1, list2)
print("removed duplicate: ", removeDuplicate)
        