#Given a key from user input, delete it from dictionary if it exists.
students = {
    'jolil': 89,
    'ananta': 97,
    'aj': 92,
    'borsha': 87
}
def findAndDelete(studnets):
    print(studnets)
    find = input()
    if find in students:
        students.pop(find)
    print(studnets)

findAndDelete(students)