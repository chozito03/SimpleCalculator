import pytest

from main import add, subtract, multiply, divide




class TestClass:

    @pytest.fixture()
    def numbers(self):
        x = 10
        y = 20
        z = 25
        return [x, y, z]

    def test_add_2(self, numbers):
        x = numbers[0]
        y = numbers[1]
        assert add(x, y) == 30

    @pytest.mark.custom_mark
    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (1.5, 0.5, 2), (10, 100, 110)])
    def test_add(self, x, y, z):
        assert add(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(3, 2, 1), (3.5, 0.5, 3), (130, 100, 30)])
    def test_subtract(self, x, y, z):
        assert subtract(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(2, 2, 4), (3.5, 2, 7), (-3, 3, -9)])
    def test_multiply(self, x, y, z):
        assert multiply(x, y) == z

    @pytest.mark.parametrize("x, y, z", [(785, 5, 157), (7, 3.5, 2), (-9, 8, -1.125)])
    def test_divide(self, x, y, z):
        assert divide(x, y) == z
