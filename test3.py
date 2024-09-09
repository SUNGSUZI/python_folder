#!/usr/bin/env python
# coding: utf-8

# In[11]:


def plus(*args) :
    sum = 0
    for el in args :
        sum += el
    return sum
    


# In[17]:


def mul(*args) :
    result = 1
    for el in args :
        result *= el
    return result


# In[18]:


# print(mul(1,2,3,4))

if __name__ == "__main__" :
    plus(1,2,3,4)
    mul(1,2,3,4)
    # pass

