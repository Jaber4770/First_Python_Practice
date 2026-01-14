i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1

# ---------------------------------------------------------------------------

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for num in my_list:
    if num % 2 == 0:
        print("num: ", num)

# ---------------------------------------------------------------------------
# finding only odd num


def onlyodd(xlist):
    oddNum = []
    for x in xlist:
        if x % 2 != 0:
            oddNum.append(x)
    return oddNum


numbers = [1, 12, 3, 14, 5, 16, 17, 8, 19, 4]
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
# reverse text


def reverse():
    text = input("write a sentece: ")
    reverseOrdered = text[-1::-1]
    print(reverseOrdered)


reverse()

# ---------------------------------------------------------------------------

a = 0
if a == 0:
    a = 1
if a == 1:
    a = 2
else:
    a = 3
print(a)

# ---------------------
"""question: a data structure consists of a list of lists. The inner lists, whose number is not  known in advance, contain a variable number of numeric elements. For example: xs = [[1,7,12], [4,2,10,14], [15,3,2,11,20]] . implement the python function ds_oddmax(xlist) that returns a list containg the maximum elements contained in the inner lists havings an odd number of element. this questions requires that exactly only the function must be implemented. therefore no data structure nor function all are requested from the candidate."""


def ds_oddmax(xlist):
    resultList = []
    for x in xlist:
        if len(x) % 2 == 1:
            resultList.append(max(x))
    return resultList


xs = [[1, 7, 12], [4, 2, 10, 14], [15, 3, 2, 11, 20]]
result = ds_oddmax(xs)
print(result)

#-------------------------
def changeToUpper():
    textt = input("enter a text: ")
    return textt.upper()

upperText = changeToUpper()
print(upperText)

#---------------------------
for i in range(3):
    if i % 2 == 0:
        print(i)
        
#----------------------
#finding all uniquie in a list:
def all_unique(lst):
    givenlst = lst.copy()
    uniquelst = []
    for x in lst:
        if x not in uniquelst:
            uniquelst.append(x)
    if givenlst == uniquelst:
        return True
    else:
        return False

# we can solve it using set with more efficient.
# return len(lst) == len(set(lst))

thelst = [1,2,3,4,5,6,7,8]
resultOfUnique = all_unique(thelst)
print(resultOfUnique)

#-----------------
s = "Hello"
s = "h" + s[1:]
print(s)