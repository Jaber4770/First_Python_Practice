#18. **Sort Dictionary by Value**
#    Sort a dictionary in descending order of its values.

my_dict = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "History": 88,
    "Art": 95
}
sorted_dict = {}
for key,value in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
    sorted_dict[key] = value
    
print(sorted_dict)
