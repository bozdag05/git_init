import pytest
from application.app import Calculator


@pytest.mark.parametrize(
    "x, y, res",
    [
        (1, 2, 0.5),
        (5, -1, -5),
        (5, -1, -5.0),
        (10, 2, 5),
        (10, 2, 5.0),
    ]
)
def test_div(x, y, res):
    assert Calculator().div(x, y) == res
