#2. **Simple Interest Calculator**
#   Input `principal`, `rate`, and `time`, then calculate the simple interest.
def interestCalculator():
    p = int(input("input your principle money: "))
    r = float(input("input your interest rate: "))
    t = float(input("input period of time: (year)"))
    
    interest = p * r * t
    total_amount = p + interest
    print(f'interest of your {p} bdt is {interest} and the interest rate is {r}%, time{t}. your final blance is: {total_amount}')
    
interestCalculator()