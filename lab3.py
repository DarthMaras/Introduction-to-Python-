# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:02:17 2022

@author: hsamarag
"""

#numbers in a list
list_a = [1,2,3,4]
#a list of strings
list_b = ["string", "in", "a", "list"]
#a list of lists, each sublist with numbers
list_c = [[1,2,3],[4,5,6],[7,8,9]]
#an empty list to use later
list_d = []
#a range of converted in a list 
list_e = list(range(10))

print(list_a)
print(list_b)
print(list_c)
print(list_d)
print(list_e)




#adding items to the list
list_a.append(5) #or
list_a.insert(0,0) #or
list_a += [6] #or
print(list_a)

#removing items
list_b.remove("in") #or
del(list_b[0]) 
print(list_b)

#length of the list
print(len(list_c[0]))

#length of the sublist of c
print(len(list_c[0]))

#finding where something is in a list

print(list_a.index(1))

print(list_c[2].index(8))

#moving items around

list_a.sort()
print(list_a)
list_a.sort(reverse = True)
print(list_a)
list_a.reverse()
print(list_a)

#Append vs extend
list_d.append(1)  #append a single number
print(list_d)
list_d.append([7,2]) #append using a list of 2 numbers
print(list_d)
list_d.extend([3,5]) #extend using a list of 2 numbers
print(list_d)

#slicing
print(list_e[:])
print(list_e[:5])
print(list_e[5:])
print(list_e[-1])

#modifying items in a list
list_e[:2] *= 2      #this is why we need to be careful multiplying lists/other objects
print(list_e)
list_e[2:] = list(range(2,12))    #replace items in a list
print(list_e)



#EXERCISE 1

# + operator
# sum() function
# itertools module

lista = [23, 689, 56, 89, 143, 897]
listb = [56.8, 89, 898, 45, 897, 569]
listc = [57, 1, 2, 3, 5, 2,11]

#sum operator 
sumall = lista + listb + listc
print(sumall)

#sum function

summ=(lista, listb, listc)
print(summ)

#intertools module

import itertools
concat_list = itertools.chain( lista, listb, listc)
concat_list = list(concat_list)
print(concat_list)



#EXERCISE 2

#2d list
a = [[4, 8, 6], [3,2,8], [2,3,3,8]]
#how to convert a 2d list to 1d
print(sum(a, []))

#calculate max, min, mean
print(max(a))
print(min(a))
# sum of the functions / length to find the mean
print(len(a))
meana = (sum(a,[])/len(a))
print(meana)

#sort the flattened nested list
a.sort ()
print(a)


#TUPLE 
#convertinga tuble
a = ("income", "cash flow", "currency", 8000.458)
a_list = list(a)
print(a)      
      
#assign a new value to a desired index in the list
a_list[2] = "tax" #new value at index [2]      
print(a_list)

#add a single item by append()
a_list.append("interest rate")
print(a_list)

#add multiple items by extend ([])
a_list.extend(["interest rate2", 23.78, "code"])
print(a_list)

#convert list back to tuple
a = tuple(a_list)
print(a)





#EXCERISE 3










