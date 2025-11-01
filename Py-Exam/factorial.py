#8. **Factorial Using Loop**
#   Find the factorial of a number without using recursion.
def factorial():
    number = int(input("enter the number: "))
    total = 1
    while 1 < number:
        total *= number
        number -= 1
    print(f"factorial is {total}")
factorial()

        