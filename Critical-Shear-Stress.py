#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:25:58 2017

@author: livbeaulieu30
"""

#Finding Critical Shear Stress 

import numpy as np
import math


#inputs
rho_s = 2.65 #input('Enter sediment density (g/cm3):') #sed density
rho_f = 1.0 #input('Enter fluid density (g/cm3):') #fluid density
D = 0.05 #input('Enter mean grain size (m):') #D50
v = 1E-6 #kinematic viscosity 
g = 9.8 #gravity
s = rho_s / rho_f

#create a class to calculate critical shear stress
class shear_stress():
    def __init__(self, D):
        self.D = D

    def Reynolds(self):
        self.Re = ((math.sqrt((s - 1) * g * self.D) * self.D) / v)  #particle reynolds number
        return (0.22 * (self.Re ** -0.6) + 0.06 * (10 ** (-7.7 * (self.Re ** -0.6)))) #critical shear stress
        
#def shields():
    #Re = ((math.sqrt((s - 1) * g * D) * D) / v) #particle reynolds number
    #return (0.22 * (Re ** -0.6) + 0.06 * (10 ** (-7.7 * (Re ** -0.6)))) #critical shear stress

stress = shear_stress(0.05)
print(stress.Reynolds())
    
