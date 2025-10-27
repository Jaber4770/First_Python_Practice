import random
print('jack')
print('hi')
# somethimes ; are important when i am writing multi statement on a same line.

print('this is a line.', end=' ')
print('i will print it on the sameline.')

print(4)
print(3+4)


a = 5
b = 'jack'
# casting
x = str(3)
y = int(3)
z = float(3)
print(x, y, z)

print(type(x))
print(type(y))
print(type(z))

# multi value
xx, yy, zz = 1, 2, 3
print(xx, yy, zz)

# unpack
fruits = ['apple', 'ball', 'cat']
aa, bb, cc = fruits
print(aa, bb, cc)

print('Hello', 'World')


# global variable
aw = 'awesome'


def myfunc():
    print('python is ' + aw)


myfunc()


def myfunction():
    aw = 'fantastic'
    print('python is '+aw)


myfunction()


# global keyword
def globalFunc():
    global fan
    fan = 'fantastiC'


globalFunc()

print('python is ' + fan)

a1 = 'hello python'


def helloFunc():
    global a1
    a1 = 'hello world'


helloFunc()

print(a1)

complexNum = 1j
print(complexNum)
print(type(complexNum))

# random

print(random.randrange(1, 20))

# loop in a string
for x in 'banana':
    print(x)

# length
text = 'hello world'
print('length:', len(text))

txt = 'the quick brown fox jumps over the lazy dog.'
print('brown' in txt)

if 'fox' in txt:
    print('yes fox in the line')

if 'rabit' not in txt:
    print('rabit is not here.')

print(txt[0:5])
print(txt[:6])
print(txt[2:])
print(txt[-5:-3])

print(txt.upper())
print(txt.lower())
print(txt.strip())

txxt = 'replacing'
print(txxt.replace("r", "R"))
print(txt.split(' '))

# f-string
age = 24
textt = f'my name is jack and i am {age}'
print(textt)
# using f string  i can put the number inside the text.

price = 59
des = f'the price of the product is {price:.2f} dollar'
print(des)

multiplication = f'multiplication is: {5*5}'
print(multiplication)


# escape chachacter
character = "we are the so-called \"Vikings\" from the north"
print(character)


# boolean
print(bool('hello'))
print(bool(12))
print(bool(''))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool({}))
print(bool([]))


def myFunction():
    return True


if myFunction():
    print('it return True')
else:
    print('it return false')

# instance
k = 200
print(isinstance(k, int))


# Arithmatic math by python
u = 5
v = 6

print('py arithmatic math: ', u+v)
print('py arithmatic math: ', u-v)
print('py arithmatic math: ', u*v)
print('py arithmatic math: ', u/v)
print('py arithmatic math: ', u % v)
print('py arithmatic math: ', u**v)
print('py arithmatic math: ', u//y)


# Assignment Operators
"""+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:="""

# walrus operator
numbers = [1, 2, 3, 4, 5, 6]
count = len(numbers)
if count > 3:
    print(f'List has {count} element')

if (count := len(numbers)) > 3:
    print(f'list has {count} elemnt')


# Comparison Operators
"""
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
"""

# Logical Operators

"""
and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
"""

# identity oparator
"""is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y
"""

# membership oparator of python
"""
in - jodi thake taile true
not in - jodi na thake taile false
"""

# operator precedence
print((6+4) - (6+3))

print(100 + 5 * 3)


# List in python, which is array of js

myList = ['apple', 'mango', 'banana']
print(myList)


list1 = [1, 2, 3, 4]
list2 = ['am', 'is', 'are']
list3 = [True, False, True]

constructorList = list((1, 2, 3, 4, 4))
print(constructorList, type(constructorList))


"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""


fruits = ['apple', 'mapple', 'tapple', 'capple', 'bapple', 'topple']
newList = []

for x in fruits:
    if 'a' in x:
        newList.append(x)

print(newList)


newlist = [x for x in fruits if 'a' in x]
print(newlist)


rangeList = [x for x in range(10)]
print(rangeList)

helloList = ['hello' for x in fruits]
print(helloList)


fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)

letterList = ['a', 'b', 'c']
listNum = [1, 3, 4]
for x in listNum:
    letterList.append(x)
print(letterList)


# tuple
tuples = (1, 3, 4)
print(tuples)

tu = (1, 2, 3, 4, 5)
print('tuples: ', tu)
listTup = list(tu)
print(listTup)
listTup[1] = 'update'
ccc = tuple(listTup)
print(ccc)

color = ('red', 'green', 'blue')
(red, green, blue) = color
print(red, green, blue)
(red, *green) = color
print(red, green)

for c in color:
    print('color: ', c)

# loop on touple
for i in range(len(color)):
    print(i+1, color[i])

# using while loop:
i = 0
while i < len(color):
    print('color: ', color[i])
    i += 1


# set

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# arrived at dictionary:
thisDict = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 1964
}
print(thisDict)
print(type(thisDict))
print(thisDict['year'])
print(len(thisDict))

paglaDict = {
    'colors': ['red', 'green', 'blue'],
    'year': 1010,
    'true': False
}
print(paglaDict)
print(type(paglaDict))
print(type(paglaDict['colors']))

# we can have nested dict
myfamily = {
    'child1': {
        'name': 'jack',
        'age': 5
    },
    'child2': {
        'name': 'mack',
        'age': 6
    }
}
print(myfamily)
print(type(myfamily))
print(type(myfamily['child1']))
print(myfamily['child1']['name'])

# loop in dict:
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])


# we have arrived at conditions:
val1 = 44
val2 = 343
if val1 > val2:
    print('jaha bolecho sotto bolecho')
else:
    print("he botsho tmi mittha bolecho.")

# elif:
day = 3
if day == 1:
    print('monday')
elif day == 2:
    print('tuesday')
elif day == 3:
    print('wednesday')
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday'")
elif day == 6:
    print('saturday')
elif day == 7:
    print('sunday')

# if-elif-else
v1 = 1
v2 = 2
if v1 > v2:
    print('value 1 i greater than value 2')
elif v1 == v2:
    print('both value are same')
else:
    print('vvalue 1 is greater than value 1')


# short if-else
if v1 < v2:
    print('v1 is less than v2.')

print('A') if v1 < v2 else print('B')

# assign value with if else
a1 = 10
a2 = 20
bigger = a1 if a1 > a2 else a2
print(bigger)

# logical operator:
c1 = 1
c2 = 2
c3 = 3
if c1 < c2 and c2 < c3:
    print('all conditions are ture')
if c1 == c3 or c1 < c3:
    print("one of them is ture")
if not c1 == c2:
    print('the condition is false, its true')

# nested if else
x1 = 41
if x1 > 10:
    print('above ten,')
    if x1 > 20:
        print('also above tweenty,')
    else:
        print("less then 20")

# pass oparator:
agee = 17
if agee < 18:
    pass  # todo: add use logic here.
else:
    print('access granted')

# match, which is also known as switch
d = 50
match d:
    case 1:
        print('the number is 1')
    case 2:
        print('number is 2')
    case 3:
        print("the number is 3")
    case 4:
        print('the number 4')
    case 5:
        print("5")
    case 6:
        print('6')
    case _:
        print('7')

# loop:
mangos = ['mango1', 'mango2', 'mango3']
for x in mangos:
    if x == 'mango2':
        continue
    print(x)

for x in mangos:
    if x == 'mango2':
        break
    print(x)

# loop with range:
for x in range(3, 33, 2):
    print(x)

# reached at funtion


def gretings(a):
    print('ki obosta?', a)


gretings('bro')

# sum func


def sum(a, b):
    return a+b


print(sum(1, 2))
print(sum(2, 3))


def my_function(fname):
    print(fname + ' Refsnes')


my_function('Emil')
my_function('tobias')
my_function('linus')

# default value:


def my_friend(name='friend'):
    print('hello ', name)


my_friend('emil')
my_friend('')
my_friend('jemil')


# positional arguments and  keyword arguments:
def positionalKeyArgu(a, b, /, *, c, d):
    print(a, b, c, d)


result = positionalKeyArgu(1, 2, c=3, d=4)
print(result)


# multiple arguments
def multiArgu(*kids):
    print('they have a kid name: ', kids[0])
    print('they have a kid name: ', kids[1])
    print('they have a kid name: ', kids[2])


multiArgu('emil', 'jemil', 'temil', 'memil')


# basic problems:
def sumso(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sumso(1, 2, 3))
print(sumso(10, 20, 30))
print(sumso(10, 20, 30, 40))
print(sumso(5))

# Finding the maximum value:


def findMax(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if max_num<num:
            max_num = num
    return max_num
max = findMax(1,2,3,40,5,6)
print(max)

