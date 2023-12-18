import pytest
from eternal5 import get_num


@pytest.mark.parametrize(
    "num, lower, res",
    [
        ('1', True, 9),
        ('3', True, 7),
        ('9', True, 1),
        ('2', False, 2),
        ('9', False, 9),
        ('10', True, 9),
        ('12', True, 8),
        ('20', True, 8),
        ('22', True, 8),
        ('210', True, 8)
    ]
)
def test_get_num(num: str, lower: bool, res: int):
    assert get_num(num, lower) == res