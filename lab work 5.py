#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Lab work 5
#If-Ele, If-Elif-Else

# Get the user input
number = input("Please provide a number: ")

# First check if they gave an integer
if int(number) != float(number):
    print("You gave a decimal!?")
    print("Now it's an integer")


# In[7]:


#regardless, convert it to an int (remember it is a string)
number = int(number)


# In[14]:


#Check what range the value is in
if number == 0:
    print("Zero")
elif number < 0:
    print("Dont be so negative!")
elif number > 0:
    print("Stay positive ;)")
elif number==3: #Can you spot a problem here? Try entering 3
    print("You guessed my favourite number!")


# In[15]:


#check what kind of number it is
if number %2 == 0:
    print("That's an even number!")
else:
    print("What an odd number!")


# In[29]:


#exercise 1

#Simple for loops
for i in range(5):
    print(i)

#Range can have more users
#It can take the form range(start, stop, step)
for i in range(1, 11, 2):
    print(i)

#Loop over a list of strings
for text_var in ["text", "to", "print"]:
    print(text_var)

#enumerate is a very useful function! It allows us to get a counter (i), 
#and the value (text_var)
for i, text_var in enumerate(["number"]*4):
    print(text_var, i)
    
#Assignment in and outside a for loop
a = 0
for i in range(5):
    b = 0
    a += i
    b += i
    print("Final:", a,b)
    
#loops and mutable objects
a_list = [1,2,3,4,5]
for val in a_list:
    a_list.remove(val)
    print(val)
    print(a_list)
    
#If you're ensure why the above happens, try this
a_list = [1,2,3,4,5]
for i, val in enumerate(a_list):
    del(a_list[i])
    print(i)
    print(a_list)
    


# In[ ]:


#Exercise 2
#import the random module. To generate random numbers.
import random

#select a random number
number_to_guess = random.randint(1, 10)

#Initialise our variables outside the range of what we are guessing
guess_val = 0 

#While we have guessed incorrectly, keep trying
while number_to_guess != int(guess_val):
    guess_val = input("Guess a number between 1 and 10: ")
    print("Correct!:)


# In[ ]:


# Sometimes we use while True so that we can use an if statement to break later
n = 0
while True:
    # Add 2 to n
    n += 2
    # This might print a lot
    print(n)
    # Break when equals to 5...which it never does!
    if n == 5:
        break


# In[ ]:


#using continue and break in a for loop
for letter in "aPaYaTaHaOaN_TEXT":
    if letter == "a":
        continue
        if letter == "_"
        break
        print(letter)

#skip certain numbers in the while loop
n = 0
while n < 10:
    n +=1
    if n % 2 == :
        continue
    print(n)


# In[ ]:


#Exercise 3 
for num in range(1, 31):
#firsst check if both conditions are met
if num % 3 == 0 and num % 5 == 0:
    print("Edinburgh")
if num % 3 == 0
    print("Liverpool")
if num % 5 == 0:
    print("Manchester")


# In[ ]:





# In[ ]:




