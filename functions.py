    # functions.py

def add(x, y):
    """Эта функция складывает два числа."""
    return x + y

def get_user_full_name(user_data):
    """Возвращает полное имя пользователя из словаря."""
    first_name = user_data.get("first_name", "")
    last_name = user_data.get("last_name", "")
    return f"{first_name} {last_name}".strip()

def divide(a, b):
    """Делит число a на b."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def is_valid_password(password: str) -> bool:
    """Проверяет, соответствует ли пароль минимальным требованиям по длине.Требования: длина пароля должна быть не менее 8 символов."""
    return len(password) >= 8
def get_age_group(age: int) -> str:
    """
    Возвращает возрастную группу по возрасту.
    - До 13 лет: "ребенок"
    - От 13 до 18 лет: "подросток"
    - Старше 18 лет: "взрослый"
    """
    if age < 13:
        return "ребенок"
    elif 13 <= age < 18:
        return "подросток"
    else:
        return "взрослый"