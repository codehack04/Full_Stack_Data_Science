#!/usr/bin/env python
# coding: utf-8

# # Declare two variables, `x` and `y`, and assign them integer values. Swap the values of these variables without using any temporary variable.

# In[5]:


x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
x=x+y
y=x-y
x=x-y
print(x,y)


# # Create a program that calculates the area of a rectangle. Take the length and width as inputs from the user and store them in variables. Calculate and display the area.

# In[6]:


length=int(input("Enter the length of the rectangle:"))
breadth=int(input("Enter the breadth of the rectangle:"))
Area=length*breadth
print("Area of the rectangle is:",Area)


# # Write a Python program that converts temperatures from Celsius to Fahrenheit. Take the temperature in Celsius as input, store it in a variable,convert it to Fahrenheit, and display the result.

# In[7]:


c=int(input("Enter the temperature in celsius:"))
#formula to convert the temperatutre
f=c*(9/5)+32
print("Temperature in Fahrenheit is:",f)


# In[ ]:




