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