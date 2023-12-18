def check_devs(devs: list[int]) -> bool:
    devs.sort(reverse=True)
    connections = 0
    connections += devs[0]
    for dev in devs[1:]:
        if connections <= 0:
            return False
        connections += dev - 2
    return True


if __name__ == "__main__":
    t = int(input())
    res = []
    for _ in range(t):
        input()
        nums = [int(x) for x in input().split()]
        res.append("Yes" if check_devs(nums) else "No")
    print(*res, sep="\n")
        