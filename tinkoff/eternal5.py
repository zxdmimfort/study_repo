def get_num(num: str, lower: bool):
    dd = sorted(list(set(num)), reverse=lower)

    if lower:
        if num[0] == dd[0]:
            return 9 - int(num[0]) + 1
        else:
            return 9 - int(num[0])
    else:
        if num[0] == dd[0]:
            return int(num[0])
        else:
            return int(num[0]) - 1


if __name__ == "__main__":
    l, r = input().split()

    res = 0
    if (diff:=(len(r) - len(l))) >= 2:
        res += 9 * (diff)
    elif diff == 1:
        res += get_num(l, lower=True)
        res += get_num(r, lower=False)
    else:
        res += get_num(l, lower=True)
        res -= 9 - get_num(r, lower=False)

    print(res)
