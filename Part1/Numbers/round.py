print(round(12.4,-1))

print(round(13.5))


from math import copysign
def round_up(num):

    return round(num + 0.5 * copysign(1,num))


print(round_up(42.2))