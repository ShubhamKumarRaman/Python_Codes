# pip install sympy

from sympy import *

g1 = isprime(30)
g2 = isprime(13)
g3 = isprime(2)

print(g1) 
print(g2) 
print(g3) 

import math

n = 11
if n <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)


from math import sqrt

n = 17
p_fl = 0

if(n > 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            p_fl = 1
            break
    if (p_fl == 0):
        print("True")
    else:
        print("False")
else:
    print("False")
