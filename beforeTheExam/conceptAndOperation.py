# **Basic Concepts & Operators**
#

# 1. Write a Python program to swap two variables without using a third variable.
x = 1
y = 2
print(x,y)
[x,y]=[y,x]
print(x,y)

# 2. Write a program that takes a user's name and age and prints:
#   *“Hello <name>, you will be <age+1> next year!”*
def NameAge():
    name = input("name: ")
    age = input("Age(number): ")
    # print(type(age))
    nextAge = int(age) + 1
    print(f"Hello {name}, you will be {nextAge} next year!")
NameAge()


# 3. Check if a given number is even, odd, or zero.
def numCheck(num):
    if num == 0:
        print("the number is zero")
    elif num % 2 == 0:
        print("the number is even.")
    elif num % 2 != 0:
        print("the number is odd")

numCheck(10)

# 4. Write a program to calculate the area of a circle using user input radius.


# 5. Convert temperature from Celsius to Fahrenheit.
