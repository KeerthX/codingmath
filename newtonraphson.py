import numpy as np 
import sympy as sp
from sympy import *

def newtonraphson(f,x0,acc=1e-5):
    x = sp.symbols('x')
    dy = diff(f) #first derivative
    x_n = x - (f/dy)
    approx_root = x0
    y_n = f.subs(x,x0)
    dy_n = dy.subs(x,x0)
    n = 0 #counter
    while not -acc<y_n<acc:
     approx_root = x_n.subs([(x,approx_root),(f,y_n),(dy,dy_n)])
     y_n = f.subs(x,approx_root)
     dy_n = dy.subs(x,approx_root)
     n += 1
    return approx_root.evalf()
    

x = symbols('x')
print(newtonraphson(f= x**2-51,x0=7))