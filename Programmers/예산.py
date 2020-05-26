#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
    d를 정렬하고, 앞에서부터 합이 예산을 초과하면 그 때의 인덱스(부서의 개수)를 반환    
'''

def solution(d, budget):
    for i in range(len(d)) :
        if sum(sorted(d)[:i+1]) >= budget :
            if i == len(d)-1 : return i+1 
            else : return i

