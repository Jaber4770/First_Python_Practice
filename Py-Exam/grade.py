#   Take marks for 5 subjects and print total, average, and letter grade.

def grade():
    print("heighest marks is 100")
    math = int(input("Enter your math marks: "))
    ict = int(input("Enter your ICT marks: "))
    chemistry = int(input("Enter your chemistry marks: "))
    biology = int(input("Enter your biology marks: "))
    physics = int(input("Enter your physics marks: "))
    
    total = math + ict + chemistry + biology + physics
    print(f"your total marks is: {total} out of 500")
    average = total/ 5
    print(f"your average marks is: {average}")
    
    if average >= 80 and average <= 100:
        print("your grade is A+")
    elif average >= 70 and average <= 79:
        print("your grade is A")
    elif average >= 60 and average <= 69:
        print("your grade is A-")
    elif average >= 50 and average <= 59:
        print("toi abar exam de.")
    else:
        print("vag ente")
grade()
