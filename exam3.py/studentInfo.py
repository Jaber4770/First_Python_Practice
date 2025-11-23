#Input: dictionary of student names → marks
#Find average mark, highest mark, and student with highest marks.
#Convert Two Lists into a Dictionary
students = {
    'jolil': 89,
    'ananta': 97,
    'aj': 92,
    'borsha': 87
}
average = 0
highestMarks = students['jolil']
totalMarks = 0
studentName = ''
for x in students:
    totalMarks += students[x]
    if highestMarks< students[x]:
        highestMarks = students[x]
        studentName = x
        
    
length = len(students)
average = totalMarks/length
print("average marks is", average)
print(f"highest marks is: {highestMarks}")
print(f"highest marks is: {highestMarks} and student name {studentName}")

