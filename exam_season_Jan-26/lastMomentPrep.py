#last moments exam preparation:
def count_case(s):
    upper = 0
    lower = 0
    
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return (upper, lower)

txt = 'Hello'
result = count_case(txt)
print(result)

#---------------------------------------
for i in range(3):
    if i == 2:
        break
else:
    print("done")
    
#ans: no output

