#!/usr/bin/env python
# coding: utf-8

# 1. What is a Python library? Why do we use Python libraries?
Python Libraries are the collection of codes that helps us to perform specific operation by using the methods available 
in the library. we use python libraries in order to simplify our code and reuse the code again and again
# 2. What is the difference between Numpy array and List?
1.A numpy array contains homogeous data where as list can contain heterogenous data.
2. A Numpy array is faster than list
# 3. Find the shape, size and dimension of the following array?
# [[1, 2, 3, 4]
# [5, 6, 7, 8],
# [9, 10, 11, 12]]

# In[5]:


import numpy as np
arr=np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])


# In[6]:


arr.shape


# In[7]:


arr.size


# In[8]:


arr.ndim


# 4. Write python code to access the first row of the following array?
# [[1, 2, 3, 4]
# [5, 6, 7, 8],
# [9, 10, 11, 12]]

# In[9]:


arr=np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])


# In[11]:


arr[0]


# 5. How do you access the element at the third row and fourth column from the given numpy array?
# [[1, 2, 3, 4]
# [5, 6, 7, 8],
# [9, 10, 11, 12]]

# In[12]:


arr=np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])


# In[15]:


arr[2][3]


# 6. Write code to extract all odd-indexed elements from the given numpy array?
# [[1, 2, 3, 4]
# [5, 6, 7, 8],
# [9, 10, 11, 12]]

# In[16]:


arr=np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])


# In[20]:


arr[::,1::2]


# How can you generate a random 3x3 matrix with values between 0 and 1?

# In[21]:


arr=np.random.rand(3,3)
arr


# 8. Describe the difference between np.random.rand and np.random.randn?
np.random.rand generates random numbers drawn from a uniform distribution over the interval [0,1),
which means the numbers are evenly distributed between 0 and 1.
                                                                                             
np.random.randn generates random numbers drawn from a normal (or Gaussian) distribution with a variance of 1 and a mean of 0. 
This means the numbers are normally distributed around 0 with a standard deviation of 1. 
# In[24]:


arr=np.random.rand(2,3)
arr


# In[26]:


arr1=np.random.randn(2,3)
arr1


# 9. Write code to increase the dimension of the following array?
# [[1, 2, 3, 4]
# [5, 6, 7, 8],
# [9, 10, 11, 12]]

# In[27]:


arr=np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])


# In[28]:


arr


# In[29]:


arr.ndim


# In[31]:


arr1=np.expand_dims(arr, axis=1)


# In[32]:


arr1


# 10. How to transpose the following array in NumPy?
# [[1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12]]

# In[33]:


arr=np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12]])


# In[34]:


arr1=np.transpose(arr)


# In[35]:


arr1


# In[36]:


arr.T


# 11. Consider the following matrix:
# Matrix A2 [[1, 2, 3, 4] [5, 6, 7, 8],[9, 10, 11, 12]]
# Matrix B2 [[1, 2, 3, 4] [5, 6, 7, 8],[9, 10, 11, 12]]

# In[37]:


#Index wise Multiplication
arr=np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
arr1=np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])


# In[38]:


arr*arr1


# In[39]:


np.multiply(arr,arr1)


# In[41]:


#Matix multiplication
arr1.reshape(4,3)


# In[44]:


np.matmul(arr,arr1.reshape(4,3))


# In[45]:


#Add both the matrix
np.add(arr,arr1)


# In[46]:


#Subtact matix B from a
np.subtract(arr,arr1)


# In[47]:


#Divide Matix B by A
np.mod(arr1,arr)


# 12. Which function in Numpy can be used to swap the byte order of an array?
np.byteswap() is used to swap the byte order of an array
# 13. What is the significance of the np.linalg.inv function?
np.linalg.inv() function is used to find the inverse of the array14. What does the np.reshape function do, and how is it used?np.reshape function reshape the array into the desired shape 
but the reshape dimension should be the factor of the size of the array
np.reshape takes the new shape, the original array and order as parameters and reaarange the aray in the specified shape
# 15. What is broadcasting in Numpy?
Broadcasting is an operation of matching the dimensions of differently shaped arrays 
in order to be able to perform further operations on those arrays (eg per-element arithmetic).