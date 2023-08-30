#!/usr/bin/env python3
import os
from math import pi
 
rad = float(input("Enter the radius of a circle: "))
A = rad * rad * pi;
filename=os.path.basename(__file__)
print(filename,"radius r=",rad,"area A =",A)  # Print results

