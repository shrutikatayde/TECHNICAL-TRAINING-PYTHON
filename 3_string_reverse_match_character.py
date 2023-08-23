# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:11:25 2023

@author: Lenovo
"""

'''string
reverse string
midpoint----->2*count+1 for odd
and count*2 for even'''

def matchCount(arr):
    count=0
    n=len(arr)
    if n%2==0:
        return 2*count
    else:
        return 2*count+1

arr= input("Enter the array:")
b=arr[::-1]
rev_str = ' '.join(map(str,b))
res = matchCount(arr)
print (res)


