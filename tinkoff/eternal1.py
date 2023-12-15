nums = [int(x) for x in input().split()]
a, b, c, d = nums
if b >= d:
    print(a)
else:
    print(a + (d - b) * c)
