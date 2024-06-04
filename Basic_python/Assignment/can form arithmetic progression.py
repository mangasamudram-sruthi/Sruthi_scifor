#!/usr/bin/env python
# coding: utf-8

# In[2]:


def can_form_arithmetic_progression(arr):
    arr.sort()
    # Calculate the difference between the first two elements
    diff = arr[1] - arr[0]
      # Check if the difference is the same for every pair of consecutive elements
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return False
    
    return True
arr1 = [3, 5, 1]
print(can_form_arithmetic_progression(arr1))  

arr2 = [1, 2, 4]
print(can_form_arithmetic_progression(arr2))  


# In[ ]:





# In[ ]:




