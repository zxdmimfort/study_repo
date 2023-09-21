from string import ascii_uppercase
peoples = [input().split(',') for _ in range(int(input()))]


def encrypt(p_info: list[str]):
	f, i, o, day, month, _ = p_info
	summ = 0
	summ += len(set(f + i + o))
	summ += 64 * sum([int(digit) for digit in list(day) + list(month)])
	summ += 256 * (ascii_uppercase.index(f[0].upper()) + 1)
	return f'{summ:X}'[-3:]


res = [encrypt(people) for people in peoples]
print(' '.join(res))
