#16. **Merge Two Dictionaries (Without Built-in .update())**
#    If both have same key, sum their values.
#    Example:
#
#    ```
#    A={"a":3,"b":2}, B={"b":4,"c":5}
#    Output: {"a":3,"b":6,"c":5}
#    ```
A={"a":3,"b":2} 
B={"b":4,"c":5}

def mergeDict(dict1, dict2):
    result = dict1.copy()
    
    for key,value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
print(mergeDict(A,B))
    