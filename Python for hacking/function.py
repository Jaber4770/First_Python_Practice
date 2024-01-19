#!/bin/python3

#function

def who_am_i(): #here i did not pass any perameter
	name = "Jack" #here i am declareing local variable. which is only 					 availabe onside of a function.
	age = 22
	print("My name is " + name + " and I am " + str(age) + " years old.")
	
who_am_i()


def addition(number):
	print(number + 10)
	
addition(4)



def multiplication(x,y):
	print(x * y)
	
multiplication(5, 5)




def multiply(a,b):
	return a * b
	
print(multiply(2,3))



def square_root(x):
	print(x ** 0.5)
	
square_root(64)


def nl(): #new line
	print('\n')
	
nl()










