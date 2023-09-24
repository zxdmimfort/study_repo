


def fun(n, m, c2, c5):
    if n >= m:
        return 0
    if c2 < c5 / 4:
        return c2 * (m - n)
    
    total_c5 = (m - n) // 4
    total_c2 = (m - n) % 4
    return min(total_c5 * c5 + total_c2 * c2, (total_c5 + 1) * c5)


print(fun(*[int(input()) for _ in range(4)]))
