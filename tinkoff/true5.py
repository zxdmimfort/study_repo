from typing import cast


def func(counts: dict[int, int], pairs: list[tuple[int, int]], queries: list[tuple[str, str]]) -> list[int]:
    friends = dict()
    res = []
    for a, b in pairs:
        friends[a] = friends.get(a, []) + [b]
        friends[b] = friends.get(b, []) + [a]
    for query, params in queries:
        if query == '?':
            res.append(counts[int(params)])
        else:
            sender, manuls = [int(x) for x in params.split()]
            for friend in friends[sender]:
                counts[friend] += manuls
    
    return res


if __name__ == "__main__":
    n, m, q = [int(x) for x in input().split()]
    counts = {i: int(x) for i, x in enumerate(input().split(), 1)}
    pairs = [tuple([int(x) for x in input().split()]) for _ in range(m)]
    in_queries = [input().split() for _ in range(q)]
    queries = []
    for query in in_queries:
        queries.append(query if len(query) == 2 else [query[0], ' '.join(query[1:])])
    print(pairs)
    print(*func(counts, cast(list[tuple[int, int]], pairs), queries), sep='\n')
    