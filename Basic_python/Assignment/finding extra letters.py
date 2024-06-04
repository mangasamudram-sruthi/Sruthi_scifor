#!/usr/bin/env python
# coding: utf-8

# In[5]:


def find_added_letter(s, t):
    
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in t:
        if char in char_count:
            char_count[char] -= 1
        else:
            return char
        if char_count[char] == -1:
            return char

s = "apple"
t = "apples"
print(find_added_letter(s, t))


# In[ ]:





# In[ ]:




