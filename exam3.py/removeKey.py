#Input: keys = ["name", "age", "city"], values = ["Alice", 25, "Paris"]
#Output: {"name": "Alice", "age": 25, "city": "Paris"}
#Remove Key from Dictionary
keys = ["name", "age", "city"]
values = ["Alice", 25, "Paris"]
output = {}

for i in range(len(keys)):
    key = keys[i]
    value = values[i]
    output[key] = value
print(output)
