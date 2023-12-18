import random
import time

def money():
    n, m = random.randint(1, 10**4), random.randint(1, 10**5)
    a = [random.randint(1, 10**4) for _ in range(n)]
    # n, m = [int(x) for x in input().split()]
    # a = [int(x) for x in input().split()]

    max_ms = []
    for cur_m in range(m+1):
        for a_i in a:
            if cur_m - a_i >= 0:
                cur_m -= a_i
        max_ms.append(cur_m)

    print(max(max_ms))

start_time = time.time()
money()
print(time.time() - start_time)
