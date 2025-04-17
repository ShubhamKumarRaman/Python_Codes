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
