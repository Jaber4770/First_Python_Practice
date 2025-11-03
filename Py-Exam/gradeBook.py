#20. **Student Gradebook**
#    Create a dictionary of students → marks.
#    Print student names who scored above average.

marksDict = {
    'jack': 28,
    'bock': 29,
    'heck': 30,
    'joe': 27,
    'mack': 26
}
def  gradeBook():
    totalMarks = 0
    length = len(marksDict)
    for x in marksDict:
        marks = marksDict[x]
        totalMarks += marks
    averageMarks = totalMarks / length
    avobeAverage = []
    for x in marksDict:
        if marksDict[x] > averageMarks:
            avobeAverage.append(x)
    print("Student got above average marks: ",avobeAverage)
        
        
gradeBook()