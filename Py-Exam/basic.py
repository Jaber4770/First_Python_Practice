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

constructorList = list((1,2,3,4,4))
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


fruits = ['apple','mapple', 'tapple', 'capple', 'bapple', 'topple']
newList = []

for x in fruits:
    if 'a' in x:
        newList.append(x)
    
print(newList)


newlist = [ x for x in fruits if 'a' in x]
print(newlist)


rangeList = [x for x in range(10)]
print(rangeList)

helloList = ['hello' for x in fruits]
print(helloList)



fruits.sort()
print(fruits)
fruits.sort(reverse = True)
print(fruits)

letterList = ['a','b','c']
listNum = [1,3,4]
for x in listNum:
    letterList.append(x)
print(letterList)


#tuple
tuples = (1,3,4)
print(tuples)

tu= (1,2,3,4,5)
print('tuples: ',tu)
listTup = list(tu)
print(listTup)
listTup[1] = 'update'
ccc = tuple(listTup)
print(ccc)

color = ('red','green','blue')
(red,green,blue) = color
print(red,green,blue)
(red, *green) = color
print(red,green)

for c in color:
    print('color: ',c)
    
#loop on touple
for i in range(len(color)):
    print(i+1, color[i])
    
#using while loop:
i = 0
while i<len(color):
    print('color: ',color[i])
    i+=1
    

#set

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
 
 
#arrived at dictionary:
thisDict = {
    'brand':'ford',
    'model': 'mustang',
    'year': 1964
}
print(thisDict)
print(type(thisDict))
print(thisDict['year'])
print(len(thisDict))

paglaDict = {
    'colors': ['red','green','blue'],
    'year': 1010,
    'true':False
}
print(paglaDict)
print(type(paglaDict))
print(type(paglaDict['colors']))

#we can have nested dict
myfamily = {
    'child1':{
        'name':'jack',
        'age':5
    },
    'child2':{
        'name': 'mack',
        'age':6
    }
}
print(myfamily)
print(type(myfamily))
print(type(myfamily['child1']))
print(myfamily['child1']['name'])

#loop in dict:
for x,obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ":", obj[y])



#we have arrived at conditions:
val1= 44
val2 = 343
if val1>val2:
    print('jaha bolecho sotto bolecho')
else:
    print("he botsho tmi mittha bolecho.")



