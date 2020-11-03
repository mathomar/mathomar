#!/usr/bin/env python
# coding: utf-8

# # part 2

# In[ ]:


def primitive(a, b):
    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):

                if (num % i) == 0:

                    break
            else:
                print(num)
a = int(input("Enter lower range: "))
b = int(input("Enter upper range: "))

print(primitive(a, b))


# In[2]:


primitive(a, b)


# In[3]:


primitive(a, b)


# In[ ]:




