#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

a = int(input())

for i in range(a) :
    x, y = sys.stdin.readline().split()
    print(int(x)+int(y))

