#Group Words by First Letter
#Input: ["cat", "car", "dog", "apple", "door"]
#Output: {'c': ['cat', 'car'], 'd': ['dog', 'door'], 'a': ['apple']}
theList = ["cat", "car", "dog", "apple", "door"]
output={}
for x in theList:
    first_letter = x[0]
    if first_letter not in output:
        output[first_letter] = [x]
    else:
        output[first_letter].append(x)

print(f"resut is: {output}")