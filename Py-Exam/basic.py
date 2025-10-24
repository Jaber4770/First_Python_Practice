print('jack'); print('hi')
#somethimes ; are important when i am writing multi statement on a same line.

print('this is a line.', end=' ')
print('i will print it on the sameline.')

print(4)
print(3+4)


a = 5
b = 'jack'
#casting
x = str(3)
y = int(3)
z = float(3)
print(x,y,z)

print(type(x))
print(type(y))
print(type(z))

#multi value 
xx,yy,zz = 1,2,3
print(xx,yy,zz)

#unpack
fruits = ['apple','ball','cat']
aa,bb,cc = fruits
print(aa,bb,cc)

print('Hello', 'World')


#global variable
aw = 'awesome'
def myfunc():
    print('python is ' +aw)
    
myfunc()
    
    
def myfunction():
    aw = 'fantastic'
    print('python is '+aw)

myfunction()


#global keyword
def globalFunc():
    global fan
    fan = 'fantastiC'

globalFunc()

print('python is '+ fan)

a1 = 'hello python'
def helloFunc():
    global a1
    a1 = 'hello world'
helloFunc()

print(a1)

complexNum = 1j
print(complexNum)
print(type(complexNum))

#random
import random

print(random.randrange(1, 20))

#loop in a string
for x in 'banana':
    print(x)

#length
text = 'hello world'
print('length:', len(text))

txt = 'the quick brown fox jumps over the lazy dog.'
print( 'brown' in txt)

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
print(txxt.replace("r","R"))
print(txt.split(' '))

#f-string
age = 24
textt = f'my name is jack and i am {age}'
print(textt)
#using f string  i can put the number inside the text.

price = 59
des = f'the price of the product is {price:.2f} dollar'
print(des)

multiplication = f'multiplication is: {5*5}'
print(multiplication)


#escape chachacter
character = "we are the so-called \"Vikings\" from the north"
print(character)


#boolean
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
    
#instance
k = 200
print(isinstance(k,int))


#Arithmatic math by python
u = 5
v = 6

print('py arithmatic math: ',u+v)
print('py arithmatic math: ',u-v)
print('py arithmatic math: ',u*v)
print('py arithmatic math: ',u/v)
print('py arithmatic math: ',u%v)
print('py arithmatic math: ',u**v)
print('py arithmatic math: ',u//y)


#Assignment Operators
