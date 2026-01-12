i = 0 
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
    
#---------------------------------------------------------------------------

my_list = [1,2,3,4,5,6,7,8]
for num in my_list:
    if num % 2 == 0:
        print("num: ", num)
        
#---------------------------------------------------------------------------
#finding only odd num
def onlyodd(xlist):
    oddNum = []
    for x in xlist:
        if x % 2 != 0:
            oddNum.append(x)
    return oddNum

numbers = [1,12,3,14,5,16,17,8,19,4]
result = onlyodd(numbers)
print(result)

# ---------------------------------------------------------------------------

x = 5
if x < 10:
    print("x is less than 10")
else:
    print('x is greater than 10')
    
# ---------------------------------------------------------------------------

def digit_sum(n):
    sum = 0
    
    if n == 0:
        return 0
    else:
        return (n % 10) + digit_sum(n // 10)

numb = 123
sumResult = digit_sum(numb)
print('recursively sum: ', sumResult)

# ---------------------------------------------------------------------------

# apply discount
def apply_discount(price, discount_percent):
    discount_price = price - (price * discount_percent/100)
    rounded_discount_price = round(discount_price, 2)
    return rounded_discount_price

price = 100
discount_parcent = 10
discount = apply_discount(price, discount_parcent)
print('discount: ', discount)

# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
