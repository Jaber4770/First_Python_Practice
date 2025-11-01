# 9. **Sum of Digits**
#   Input a number like `1234`, output should be `1+2+3+4 = 10`.
def sum():
    digit = input('enter the number: ')
    total = 0
    for char in digit:
        x = int(char)
        total += x
    print(f"sum of the {digit} is {total}")


sum()
