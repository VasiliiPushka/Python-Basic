import random

class KillError(Exception):
    def __str__(self):
        return 'KillError: Убил'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError: Напился'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError: ДТП'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError: Обожрался'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError: Депрессия'


def one_day():
    if random.random() > 0.1:
        return random.randint(1, 7)
    else:
        return random.choice([
            KillError(),
            DrunkError(),
            CarCrashError(),
            GluttonyError(),
            DepressionError()
        ])

karma_total = 0
count = 0

while karma_total < 500:
    count += 1
    try:
        day_result = one_day()
        if isinstance(day_result, Exception):
            raise day_result
        karma_total += day_result
    except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
        with open('karma.log', 'a', encoding='utf-8') as karma_file:
            karma_file.write(f"{count}) - {e}\n")

print(f"Просветление достигнуто за {count} дней!")




