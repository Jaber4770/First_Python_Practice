# 18. **Group Words by First Letter**
#    Input: `["cat","car","dog","apple","door"]`
#    Output:
#
#    ```
#    {
#       'c': ['cat','car'],
#       'd': ['dog','door'],
#       'a': ['apple']
#    }
#    ```
lisst = ["cat", "car","dog","apple","door"]
group = {}
for x in lisst:
    firstLetter = x[0]
    if firstLetter not in group:
        group[firstLetter] = [x]
    else:
        group[firstLetter].append(x)

print(group)