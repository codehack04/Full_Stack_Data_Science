#!/usr/bin/env python
# coding: utf-8

# # Write a Python program that takes a string as input and prints the length of the string.

# In[2]:


string=input("Enter the string:")
print(len(string))


# # Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.

# In[3]:


string=input("Enter the string:")
vowels="aeiou"
c=0
for i in string.lower():
    if i in vowels:
        c=c+1
print("There are",c,"Vowels present in the string")
        


# # Given a string, reverse the order of characters using string slicing and print the reversed string.

# In[5]:


string=input("Enter the string:")
print("Reversed string is:",string[::-1])


# # Write a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).

# In[8]:


s=input("Enter the string to check:")
if s==s[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")


# # Create a program that takes a string as input and removes all the spaces from it. Print the modified string without spaces.

# In[10]:


s=input("Enter the string:")
print(s.replace(" ",""))


# In[13]:





# In[ ]:




