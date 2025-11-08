#14. **Students Marks Analysis**
#    Given a dict of students and their marks:
#
#    * Find highest mark
#    * Print names of students who passed (≥ 40)
#
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Eve": 88
}

highestMarks = student_marks["Alice"]

for x in student_marks:
    if student_marks[x] > highestMarks:
        highestMarks = student_marks[x]
    if student_marks[x] >= 40:
        print('students got more than 40: ',x)
        
print('highest marks: ',highestMarks)
