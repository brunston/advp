#1a)

from sympy import *
init_printing(use_unicode=True)
from sympy.abc import a,r
i1,i2,i3,i4,i5=symbols('i1,i2,i3,i4,i5')

A = Matrix([[0,0,0,4*r,5*r,a],
            [r,2*r,0,0,0,a],
            [-r,0,3*r,4*r,0,0],
            [0,-2*r,3*r,0,5*r,0],
            [0,2*r,3*r,4*r,0,a],
            [r,0,-3*r,0,5,a]])

B = Matrix([[0,0,0,4*r,5*r,a],
            [r,2*r,0,0,0,a],
            [1,-1,1,0,0,0],
            [0,0,-1,1,-1,0],
            [0,2*r,3*r,4*r,0,a],
            [r,0,-3*r,0,5,a]])

print("A: \n",A)
print("rref of A (augmented):\n", solve_linear_system(A,i1,i2,i3,i4,i5))

print("B: \n",B)
print("rref of B (augmented):\n", solve_linear_system(B,i1,i2,i3,i4,i5))
