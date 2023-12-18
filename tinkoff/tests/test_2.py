import pytest
from true2 import check_devs


@pytest.mark.parametrize(
    "devs, res",
    [
        ([100000], True),
        ([1, 1], True),
        ([1, 1, 1], False),
        ([1, 1, 2, 2], True),
    ]
)
def test_check_devs(devs: list[int], res: bool):
    assert check_devs(devs) == res
