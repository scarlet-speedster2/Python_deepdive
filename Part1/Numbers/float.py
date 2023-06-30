

print(float(10))
from fractions import Fraction
print(float(Fraction(22,7)))
print(float('44.234'))
print(format(0.1,'0.25f'))
print(format(0.125,'0.25f'))
a = 0.1 + 0.1 + 0.1
b = 0.3
print(a==b)

import math

print(math.isclose(a,b))

x = 0.000000000000000001
y = 0.000000000000000002
print(math.isclose(x,y))
print(math.isclose(x,y,abs_tol=1e-5))
