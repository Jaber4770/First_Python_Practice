# 13. **Delete a Key from Dictionary if Exists**
#    Ask user for a key → if found, delete it, else show "Key not found".

student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 95,
    'Eve': 88,
    'Frank': 76,
    'Grace': 91,
    'Henry': 82,
    'Ivy': 89,
    'Jack': 74,
    'Katie': 96,
    'Leo': 79,
    'Mia': 87,
    'Nathan': 93,
    'Olivia': 84,
    'Peter': 90,
    'Quinn': 81,
    'Rachel': 86,
    'Sam': 77,
    'Tina': 94
}


def delete(name):
    print("the old dict: ", student_scores)
    if name in student_scores:
        student_scores.pop(name)
        print(f"key {name} deleted successfully")
    else:
        print("key not found")

    print('new list: ', student_scores)


delete("Jack")
