# test_functions.py
import pytest
from functions import add, get_user_full_name
@pytest.mark.math
def test_add():
    """Проверяем, что функция add() правильно складывает два числа."""
    assert add(2, 3) == 5
    assert add(2, 2) == 4 
    assert add(10, -5) == 5
# ШАГ 1: Создаем фикстуру
@pytest.fixture
def sample_user_data():
    """Фикстура, которая возвращает словарь с данными пользователя."""
    return {
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@example.com" 
    }

# ШАГ 2: Используем фикстуру в тестах
@pytest.mark.user_profile
def test_get_user_full_name_with_fixture(sample_user_data):
    # Pytest автоматически вызовет фикстуру и передаст ее результат
    # в аргумент sample_user_data
    assert get_user_full_name(sample_user_data) == "Jane Doe"
@pytest.mark.user_profile
def test_user_has_email_with_fixture(sample_user_data):
    assert "email" in sample_user_data
    
test_cases = [
    (1, 2, 3), # Обычное сложение
    (-1, -1, -2), # Сложение отрицательных чисел
    (5, 0, 5), # Сложение с нулем
    (-1, 1, 0), # Противоположные числа
    (3.5, 2.5, 6.0) # Сложение чисел с плавающей точкой
]

@pytest.mark.parametrize("a, b, expected", test_cases)
@pytest.mark.math
def test_add_parametrized(a, b, expected):
    """Проверяем функцию add() с разными наборами данных."""
    assert add(a, b) == expected

from functions import divide
def test_divide_by_zero_raises_error():
    """Проверяем, что деление на ноль вызывает ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.skip(reason="Эта функция еще в разработке")
def test_new_feature():
    # Код теста для новой, еще не готовой функции
    assert false
@pytest.mark.xfail(reason="Известный баг с точностью float, тикет #123")
def test_float_precision_bug():
    assert (0.1 + 0.2) == 0.3 # Этот тест упадет из-за особенностей float

#Задача №1
from functions import is_valid_password
def test_valid_password_10_chars():
    assert is_valid_password("password12") == True

def test_short_password_5_chars():
    assert is_valid_password("short") == False

def test_boundary_password_8_chars():
    assert is_valid_password("12345678") == True

@pytest.mark.parametrize("password,expected", [
    ("password12", True),    
    ("short", False),         
    ("12345678", True),      
])
def test_all_cases(password, expected):
    assert is_valid_password(password) == expected

#Задача №2    
from functions import get_age_group
@pytest.mark.parametrize("age,expected_group", [
    #Граничные значения
    (0, "ребенок"),
    (12, "ребенок"),
    (13, "подросток"),
    (14, "подросток"),
    (17, "подросток"),
    (18, "взрослый"),
    (19, "взрослый"),
])
def test_get_age_group(age, expected_group):
    result = get_age_group(age)
    assert result == expected_group, f"Возраст {age}: ожидалось '{expected_group}', получено '{result}'"