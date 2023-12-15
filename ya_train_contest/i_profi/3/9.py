
def sol(n: int, k: int, a: int):
    time_1 = n
    n_d, n_u = n - (n % k), k * ((n // k) + 1)
    time_a = n_d // k * a + n - n_d
    time_b = n_u // k * a + n_u - n
    min_time = min(time_a, time_b, time_1)
    if n % k == 0:
        time_k = n // k * a
        return min(time_k, min_time)
    return min_time


n, k, a = [int(num) for num in input().split()]

print(sol(n, k, a))