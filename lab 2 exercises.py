# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#these are some examples given in lab2 to work on print() function


print (4*5)
print (4%15)
print (3*6*6)
print (279/3)

x1 = 4*5
x2 = 4%15
x3 = 3*6*6
x4 = 279/3

# print seperately 

print (x1)
print (x2)
print (x3)
print (x4)

# print using text/string statement

print ( "the value of x1, x2, x3 amd x4 is", x1,",", x2,",", x3,", and", x4,", respectvely" )

x1, x2, x3, x4 = 4*5, 4%15, 3*6*6, 279/3

# print seperately 

print(x1)
print(x2)
print(x3)
print(x4)

# calculating following expression using PEDMAS operator precedence
# quadratic equations 

a= (2-4*11-(2/4))
print(a)
b= (2-9)*13
print(b)

# if x = 0  c = 3x**2+6x- 34 => c=-34
#               a=3   b=6  c=-34
c= -34

import math
a, b, c = 3, 6, -34

x= (-b+math.sqrt(b**2-4*a*c))/(2*a)
print(x)
print(round(x,2))

#solve math expressions within string 
#number of stocks
energy =  24
metals = 12
telecom = 11
print ("i have total", energy+metals+telecom, "number of stocks.")

#using string to display percentage in eacg domain
print("method1:")
print("percentage of stock in energy, metals, and telecome inustry is", round (energy/(energy+metals+telecom)*100),"%"",", round (metals/(energy+metals+telecom)*100),"%"", and", round (telecom/(energy+metals+telecom)*100),"%"", respectively.")

# there are two methods to do this, the previous line was 1 of the two

# EXERCIZE 1 LAB 2

Line1= "Pyhton was created by Guiso van Rossum a Dutch."
Line2= "First version of python 0.9.0 was developed in Centrum Winskunde & Informatica (CWI) in Netherlands in 1991."
Line3= "Python 3.0, was released on 3 December 2008."

print(type(Line1))
print(type(Line2))
print(type(Line3))

Line4= 100
Line5= 200 and 5
Line6= 300==3

print(type(Line4))
print(type(Line5))
print(type(Line6))


#EXERCISE 2 A) LAB 2

print(((1+0.05)**7-1))/0.05


