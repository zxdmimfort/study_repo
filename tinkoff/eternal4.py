n, k = [int(x) for x in input().split()]
nums = [[int(d) for d in x] for x in input().split()]


digits = []
for num in nums:
    for i, digit in enumerate(num[::-1]):
            digits.append((9 - digit) * 10 ** i)
digits.sort(reverse=True)
print(sum(digits[:k]))