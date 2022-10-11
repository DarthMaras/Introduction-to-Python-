# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:27:56 2022

@author: Andreas Maragkos
"""

#recap from lecture 2 

#multiple variable assaigned
income, tax_code = 9000, "1250L"
print(income)
print(tax_code)

#swap variables
A1 = 50
A2 = 10
print(A1)
print(A2)
A1, A2 = A2, A1
print(A1)
print(A2)





#numerical types

#integer
y1 = 3
print(type(y1))

#float
y2 = 5.2
print(type(y2))

#complex number
y3 = 15j
print(type(y3))




#strings using ""
example1 = "total sales price is:", "principle rate 1", "i don't know"
print(type(example1))

string1 = "z"
print(type(string1))

string2 = "the principle amount is 3000"
print(string2)

#print strings with an assaigned variable
amount = 5000 #numerical variable
print("the principle amount is", amount)




#BOOLEAN True or False

a = True
print(type(a))

b = False
print(type(b))

#false float with 0
c = 0.0
print(bool(c))

d = 0-0j
print(bool(d))

e = 5+18j
print(bool(e))

#boolean arithmetic and operators
#operators are: or and not ==(equal) != (not equal)

X = True
Y = False
Z = False

#or
test1 = X or Y
print(test1)
#and
test2 = Y and Z
print(test2)
#not
test3 = not X
print(test3)
#equal==
test4 = Z == Y
print(test4)
#not equal !=
test5 = X != Y
print(test5)
#compound boolean expression
test6 = (X and Y) or Z
print(test6)

#ARITHMETIC OPERATORS, + - * / % ** // 
a = 20
b = 4
#addition
print(a+b)
#subtraction
print(a-b)
#multiplication
print(a*b)
#division
print(a/b)
#modulus
print(a%b)
#exponent
print(a**b)
#floor division
print(a//b)

#python comparison operators == != < > <= >=
#equal 
print(a==b)
#not equal
print(a!=b)
#greater than
print(a>b)
#less than
print(a<b)
#greater than or equal to
print(a>=b)
#less than or equal to
print(a<=b)

#in place operators 
y = 8
print(y)
# add 4 to the assigned value 
y += 4
print(y)
#multiply by 2
y *= 2
print(y)
#division by 3 
y /= 3
print(y)

#PEDMAS excecution like normal math equation first brackets, then indices, then multi div, then add sub
#calculating expressions in python
#calculating compound interest annually


