d1 = {
    "Math": ["Alice", "Bob"],
    "History": ["Charlie"],
    "Art": ["David", "Eve"]
}
d2 = {
    "Math": ["Frank"],
    "History": ["Grace", "Henry"],
    "Music": ["Ivan"]
}
merged = {}
for x in d1:
    if x in d2:
        merged[x] = d1[x] + d2[x]
    else:
        merged[x] = d1[x]
for x in d2:
    if x not in merged:
        merged[x] = d2[x]
        
        
print(merged)