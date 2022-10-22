# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:00:33 2022

@author: hsamarag

"""

#LAB WORK 4 

#Exercise 1

x = "python interpreter and the extensive standard library are freely available in source or binary from for all major platforms from the Python Web site"


#capitalize first character only first word of the string

print(x.capitalize())
#strings concatenation: add THE and . full stop at the end of string x
list_x=[]
list_x.extend(["the", "."])
print(list_x)


#Exercise 2
#print hello multiple time
string1 = "*Hello*"

print(string1*2)
print(string1*3)
print(string1*4)
print(string1*5)


#Exercise 3

y = "Your line spacing options are not limited to the ones in the Line and Paragraph Spacing meno. To adjust spacing with more precisio, select Line Spacing Options from the menu to access the Paragraph dialog box. You willl then have a few additional options you can use to customize spacing."
#step 1.1: to change ARE NOT to AREN'T
print(y)
y = "are not \\ aren't "
print(y)

#step 1.2: chnage YOU WILL to YOU'LL
 
y = "you will \\ you'll"
print(y)

#Exercise 4

# use str.format() and modulo operator % to perform string formatting

string = "Hey! {name}, your account has been credited £{amount:9.3f}".format(name = "John", amount = 5786.72478)
print(string)


#EXERCISE 5
#step1 use datetime module to dins current date
import datetime

current_date = datetime.datetime.now()

#step2: convert string data type
current_date= str(current_date) 
print(current_date)

#step3: strip date and time from the stirng current_date
date_time_obj = datetime.datetime.strptime(current_date, "%Y-%m-%d %H:%M:%S.%f")
print("the data type of the striped date:", type(date_time_obj))
print("the date is", date_time_obj)



#EXERCISE 6
#prompt the user to imput their name, city, and country of residence and store these values by using input()
#eg
name = input("what is your name?: ")
print(name)

date = input("what is the date?: ")






