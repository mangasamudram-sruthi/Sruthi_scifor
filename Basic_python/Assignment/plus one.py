#!/usr/bin/env python
# coding: utf-8

# In[3]:


def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        digits[i] += 1
        if digits[i] < 10:
            return digits
        digits[i] = 0
    return [1] + digits

digits1 = [1, 2, 3]
print(plus_one(digits1)) 

digits2 = [4, 3, 2, 1]
print(plus_one(digits2))  

digits3 = [9]
print(plus_one(digits3)) 


# In[ ]:




