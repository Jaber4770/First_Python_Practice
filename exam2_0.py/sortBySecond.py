#7. **Sort List of Tuples by Second Value**
#   Example:
#   ```
#   data = [(1, 5), (3, 2), (6, 8)]
#   Output: sorted ascending by 2nd value → [(3,2), (1,5), (6,8)]
#   ``
data = [(1, 5), (3, 2), (6, 8)]

sorted_data = sorted(data, key=lambda x:x[1])
print(sorted_data)

sortedData = sorted(data, key=lambda x:x[1])
print(sortedData)