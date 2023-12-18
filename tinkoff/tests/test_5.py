import pytest
from true5 import func


@pytest.mark.parametrize(
    "counts, pairs, queries, res",
    [
        ({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)], [('?', '1'), ('?', '5'), ('+', '1 2'), ('?', '1'), ('?', '5')], [1, 5, 1, 7])
    ]
)
def test_func(counts: dict[int, int], pairs: list[tuple[int, int]], queries: list[tuple[str, str]], res: list[int]):
    assert func(counts, pairs, queries) == res
