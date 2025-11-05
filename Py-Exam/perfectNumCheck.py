# 25. **Perfect Number Checker**
#    A number is perfect if the sum of its divisors equals the number itself.
#    Write a program to check this.

def perfectFinder(n):
    total = 0
    for x in range(1, n):
        if n % x == 0:
            total += x
    if total == n:
        print("the number is perfect.")
    else:
        print("the number is not perfect.")

perfectFinder(28)