from fractions import Fraction

x = Fraction(2,3)
y = Fraction(5,6)
print(x/y)
print(Fraction(0.125))
print(Fraction(2,5)+Fraction(4,3)+Fraction(9,2))

print(Fraction(0.3))
print(x.denominator,x.numerator)
import math
print(Fraction(math.pi))

print(Fraction(math.pi).limit_denominator(10))