n, t = [int(x) for x in input().split()]
stages = [int(x) for x in input().split()]
limit = int(input()) - 1


if stages[limit] - stages[0] <= t or stages[-1] - stages[limit] <= t:
    print(stages[-1] - stages[0])
elif stages[limit] - stages[0] < stages[-1] - stages[limit]:
    print(stages[-1] - stages[0] + stages[limit] - stages[0])
else:
    print(stages[-1] - stages[0] + stages[-1] - stages[limit])
