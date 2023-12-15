from math import floor, ceil
from decimal import *
num = Decimal(int(input()))
snum = num ** Decimal(0.5)


if floor(snum) < snum:
	a = floor(snum)
else:
	a = floor(snum) - 1
if ceil(snum) > snum:
	b = ceil(snum)
else:
	b = ceil(snum) + 1
print(a, b)