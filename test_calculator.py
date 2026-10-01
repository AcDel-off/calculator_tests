import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()


class TestCalculatorAdd:
    """Тесты для метода сложения с параметризацией"""
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, -1, -2),
        (-5, 10, 5),
        (0, 0, 0),
        (0.1, 0.2, 0.3),
        (1000000, 1, 1000001),
    ])
    def test_add_parametrized(self, calc, a, b, expected):
        """Параметризованный тест сложения для разных входных данных"""
        result = calc.add(a, b)
        assert result == pytest.approx(expected)


class TestCalculatorDivide:
    """Тесты для метода деления"""
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (9, 3, 3),
        (-10, 2, -5),
        (0, 5, 0),
        (1, 3, 0.3333333),
    ])
    def test_divide_success(self, calc, a, b, expected):
        """Позитивные сценарии"""
        result = calc.divide(a, b)
        assert result == pytest.approx(expected)

    def test_divide_by_zero(self, calc):
        """Негативный сценарий"""
        with pytest.raises(ValueError) as excinfo:
            calc.divide(10, 0)
        assert str(excinfo.value) == "Деление на ноль невозможно!"

    def test_divide_both_zero(self, calc):
        """Деление нуля на ноль"""
        with pytest.raises(ValueError):
            calc.divide(0, 0)


class TestCalculatorIsPrime:
    """Тесты для проверки числа на простоту"""
    @pytest.mark.parametrize("number, expected", [
        #простые числа
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (97, True),
        
        #составные числа
        (4, False),
        (6, False),
        (8, False),
        (9, False),
        (15, False),
        (100, False),
        
        #граничные случаи
        (0, False),
        (1, False),
        (-5, False),
    ])
    def test_is_prime_parametrized(self, calc, number, expected):
        """Проверка корректности алгоритма определения простоты"""
        result = calc.is_prime_number(number)
        assert result == expected, f"Число {number}: ожидалось {expected}, получено {result}"
