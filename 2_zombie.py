# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:24:16 2023

@author: Lenovo
"""
def Zombie(bobEnergy, n_OfZombie, arr_energyOfZombie):
    for i in range(0, len(arr_energyOfZombie)-1):
        bobEnergy-=(arr_energyOfZombie[i]%2)+(arr_energyOfZombie[i]/2)
        if bobEnergy<=arr_energyOfZombie[i]:
            res="No"
        elif bobEnergy>arr_energyOfZombie[i]:
            res="Yes"
        ''' elif bobEnergy==-1:
            return'''
        
    return res

bobEnergy, n_OfZombie=list(map(int,input("Enter Bob Energy  and Zombies Count : ").split()))
arr_energyOfZombie=list(map(int,input("Enter Energy of each zombie : ").split()))
res=Zombie(bobEnergy, n_OfZombie, arr_energyOfZombie)
print(res)
                           
            
