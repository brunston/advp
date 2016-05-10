#1a)

from sympy import *
init_printing(use_unicode=True)
from sympy.abc import a,r

A = Matrix([[1,2,0,0,0,a],[0,0,0,4,5,a],[0,2,3,4,0,a],[1,0,3,0,5,a],[0,2,3,0,5,0]])
print("A: ",A)
print("A.rref()",A.rref())