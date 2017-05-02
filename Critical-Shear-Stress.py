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
rho_s = input('Enter sediment density (g/cm3):') #sed density
rho_f = input('Enter fluid density (g/cm3):') #fluid density
D = input('Enter mean grain size (m):') #D50
v = 1E-6 #kinematic viscosity
g = 9.8 #gravity

s = rho_s / rho_f 

#create a class to calculate critical shear stress
class shear_stress():
    def shields():
        Re = ((math.sqrt((s - 1) * g * D) * D) / v) #particle reynolds number
        return (0.22 * (Re ** -0.6) + 0.06 * (10 ** (-7.7 * (Re ** -0.6)))) #critical shear stress
Tc = shields()
print Tc

    
