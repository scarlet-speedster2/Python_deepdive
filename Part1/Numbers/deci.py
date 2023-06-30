import decimal
from decimal import Decimal

x = Decimal('0.13847891223494917394793')
ctx = decimal.getcontext()
print("Precision : {0} Rounding : {1}".format(ctx.prec,ctx.rounding))
y = x * 2
print(y)

with decimal.localcontext() as c:

    c.prec = 12
    c.rounding = decimal.ROUND_UP
    z = x * 2
    print(z)