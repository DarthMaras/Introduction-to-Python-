# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 18:01:44 2022

@author: Andreas Maragkos
"""

#redoing Q1 as i want to correct the last part

Line1= "Python was created by Guido van Rossum a Dutch Programmer."
Line2= "First version of Python 0.9.0 was developed in Centrum Wiskunde & Informetica (CWI) in Netherlands in 1991."
Line3= "Python 3.0 was released on 3 December 2008."

X1= "Line1"
X2= "Line2"
X3= "Line3"


print (type(X1))
print (type(X2))
print (type(X3))

# we found that they are not real
# now we want the true value.. to find the real value we use (== or and)

X1_type = (type(X1) == str)
X2_type = (type(X2) == str)
X3_type = (type(X3) == str)

print (type(X1) == str)
print (type(X2) == str)
print (type(X3) == str)

#all 3 lines together 

check1 = X1_type and X2_type and X3_type
print (check1)

check2 = X1_type == X2_type == X3_type
print (check2)

# the new line character in Python is /n. It is used to indicate the end of the line of text.
#method 1
print("method1:/n", Line1,Line2,Line3)
#method 2
print("method2: /n", Line1+Line2+Line3)

#However it should be X1,X2,X3 & X1+X2+X3 in the methods above, but i have done a mistake


#EXCERSISE 2 A

# we have to a mathematical equation therefore import math
import math 
C= 2000 #cash flow
i= 0.05 #5% interest rate
n= 7 #years of payments

#FV is the FUTURE VALUE of an ordinary annuity
FV = C*((math.pow(1+i, n)-1)/i)  #math.pow used before 1+i to indicate there is a power and then use ,n which is the power.

print("Worth of future value at the end of 7 years is £", FV)

#round (number, digits) is used to round off a float ti ndigits

print("worth of future value at the end of 7 year is £", round(FV, 3)) 

#EXERCISE 2 B
import math
C= 1000 #cash flow per period
i= 0.05 #interest rate
n= 5 #number of payments

#Present value of annuity due
PV= C*((1-math.pow(1+i, -n))/i)*(1+i)     
print("Present Value of Annuity Due:", PV)

#then again we have to round it to three digits

print("present value of annuity date:", round(PV, 3)) #DONT FORGET TO CLOSE BRACKETS

#IN PLACE OPERATORS
#mathematical operators (+,-etc) first , then assignment operators (=)
#the statements below are equivalent
 a+ = 3
 a =a+3 
#if you write x=+4 is going to be an error

#divide in-place Trial 1
x = 4
x/= 2

file"<python-input-10-c5ee9eb37bd6>", Line 3
x=/2 syntaxerror invalid 

#Divide in-place Trial 2
x=4
x/=2
print(x)

#ERRORS TO DEBUG CODE

value1 = 250            
value2 = "5"
result = value1/value2
print("The result is:", result)

#value2 is a string number 
#type error unsupported operand type(s) for/: int and str

value1 = 250

#value2 is changed from string to integer

value2 = 5
resule = value1/value2
print("the result is:", result)
print("the result is:", int(result)) #use int to fix a float value to integer

a=25/0
division error

import math
print(math.sqrt(-3))
math domain error

value1 = 100
value2 = int("hello mars")
print (value1+value2)
value error











