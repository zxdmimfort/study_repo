def solve_fence(n: int, k: int):
    planks = [int(num) for num in input().split()]
    planks.sort()
    if k == 0:
        return planks[-1] - planks[0]
    return min([planks[n - k - 1 + i] - planks[i] for i in range(k)])

print(solve_fence(*[int(num) for num in input().split()]))