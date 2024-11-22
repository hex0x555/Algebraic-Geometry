#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 17:04:08 2024

@author: laurentharrington
"""

from sympy import LT, poly, ZZ, cancel
from sympy.abc import x,y,z

f = (x**2+y**2)*(x**2+z**2)*(y**2+z**2)
s1 = x + y + z
s2 = x*y + x*z + y*z
s3 = x*y*z

# Leading terms
LT_f = LT(f)
LT_s12s22 = LT(s1**2*s2**2)

#second iteration
f1 = f - s1**2*s2**2
LT_f1 = LT(f1)
LT_s13s3 = LT(s1**3*s3)

#third iteration
f2 = f1 - (-2)*(s1**3*s3)
LT_f2 = LT(f2)
LT_s23 = LT(s2**3)

#fourth iteration
f3 = f2 - (-2)*(s2**3)
LT_f3 = LT(f3)
LT_s1s2s3 = LT(s1*s2*s3)

#fifth iteration
f4 = f3 - 4*(s1*s2*s3)
LT_f4 = LT(f4)
LT_s32 = LT(s3**2)

#sixth iteration
f5 = f4 - -1*(s3**2)
LT_f5 = LT(f5)