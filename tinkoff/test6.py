_, q = [int(x) for x in input().split()]
a = [0] + [int(x) for x in input().split()]
queries = [input().split() for _ in range(q)]

for q, *params in queries:
    if q == '+':
        l, r, x = [int(num) for num in params]
        for i in range(l, r + 1):
            a[i] += x
    else:
        l, r, k, b = [int(num) for num in params]
        mins = []
        for i in range(l, r + 1):
            mins.append(min(a[i], k*i+b))
        print(max(mins))
