# Count Character Frequency#
# Input: "banana"#
# Output: {'b': 1, 'a':3, 'n':2}
input = 'banana'
output = {}
for char in input:
    if char not in output:
        output[char] = 1
    else:
        output[char] += 1
print(output)
