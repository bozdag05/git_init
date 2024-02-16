import pytest
from contextlib import nullcontext as does_not_raise
from application.app import Calculator


class TestCalculator:

    @pytest.mark.parametrize(
        "x, y, res, exception",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, -1, -5.0, does_not_raise()),
            (10, 2, 5, does_not_raise()),
            (10, 2, 5.0, does_not_raise()),
            (1, 0, 0, pytest.raises(ZeroDivisionError)),
            (1, "0", 0, pytest.raises(TypeError)),
        ]
    )
    def test_div(self, x, y, res, exception):
        with exception:
            assert Calculator().div(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, exception",
        [
            (1, 2, 2, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, -1, -5.0, does_not_raise()),
            (10, 2, 20, does_not_raise()),
            (10, 2, 20.0, does_not_raise()),
            (1, 0, 0, does_not_raise()),
            (1, "0", 0, pytest.raises(TypeError)),
        ]
    )
    def test_add(self, x, y, res, exception):
        with exception:
            assert Calculator().add(x, y) == res
