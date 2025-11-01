#10. **Find Largest Among Three Numbers**
#    Input 3 numbers and print the largest.

def findLargest():
    num1 = int(input("enter 1 of the 3 number: "))
    num2 = int(input("enter 2 of the 3 number: "))
    num3 = int(input("enter 3 of the 3 number: "))
    if num1 > num2 and num1>num3:
        print(f"{num1} is the larges.")
    elif num2>num1 and num2>num3:
        print(f"{num2} is the largest.")
    else:
        print(f"{num3} is the largest.")
findLargest()
