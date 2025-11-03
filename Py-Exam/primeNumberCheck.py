#
#21. **Prime Number Checker (Function)**
#    Write a function `is_prime(n)` that returns True/False.
def is_prime(n):
    if n<=1:
        return False
    if n == 2:
        return True
    if n % 2 == 0 :
        return False
    return all(n % i != 0 for i in range(3, int(n ** 0.5) + 1,2))        
        

print(is_prime(5))