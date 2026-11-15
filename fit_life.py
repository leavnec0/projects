"""Модуль для расчёта индекса массы тела и нормы воды."""

import sys


def fit_life():
    """Выполняет расчёт индекса массы тела и потребления воды."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    introduction = "Добро пожаловать в FitLife"
    user_name = input("Как вас зовут? ")
    user_age = int(input("Сколько вам лет? "))

    print(f"{introduction}, {user_name}! Вам {user_age} лет.")

    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(input("Введите ваш рост в метрах, применяя точку: "))

    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)

    print(f"Ваш индекс массы тела: {bmi}")

    water_ml = weight * 30
    water_l = round(water_ml / 1000, 2)

    print(f"Вам необходимо пить {water_l} литров воды в день.")

    print("Расчет окончен. Будьте здоровы!")


if __name__ == "__main__":
    fit_life()
