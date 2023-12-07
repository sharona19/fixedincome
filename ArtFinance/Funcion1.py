#!/usr/bin/env python
# coding: utf-8

# In[6]:


# your_library/your_module.py
def funcion1(num1, num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        result = None
    return result

