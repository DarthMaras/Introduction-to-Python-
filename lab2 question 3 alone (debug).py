# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 20:01:28 2022

@author: Andreas Maragkos
"""

#exercise 3 debug the following pice of code
import math

divide_by = 2
subtract_by = 3
multiply_by = 4

var = 1
var1 = int(var) - subtract_by
print("subtracting your value of", var, "by", subtract_by, "will give", var1)

var2 = var1 / divide_by
print("dividing your value", var1, "by", divide_by, "will give", var1)

var3 = 0.5
print("the ceiling of", var3,"is", math.ceil(float(var3)))

var4 = 2
var5 = 3

print("multiplying", var, "by", var5, "will give", var4, int(var5))
print("multiplying", var4, "by", var5, "will give", int(var4)*int(var5))
print("multiplying", var4, "by", var5, "will give", (float(var4)*int(var5)))

# need to be carefull at the , and " also, import math at the begginig is important 