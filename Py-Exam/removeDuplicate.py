#17. **Remove Duplicate Words**
#    Input: `"python is great and python is fun"`
#    Output: `"python is great and fun"`
def removeDuplicate():
    text = input("type 'python is great and python is fun': ")
    words = text.split()
    unique = []
    for x in words:
        if x not in unique:
            unique.append(x)
    uniqueText = ' '.join(unique)
    print(uniqueText)
removeDuplicate()
    