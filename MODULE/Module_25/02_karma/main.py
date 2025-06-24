import random
class KillError(Exception):
    def __init__(self):
        super().__init__('Убийство')
class DrunkError(Exception):
    def __init__(self):
        super().__init__('Алкогольное отравление')
class CarCrashError(Exception):
    def __init__(self):
        super().__init__('Автокатастрофа')
class GluttonyError(Exception):
    def __init__(self):
        super().__init__('Обжорство')
class DepressionError(Exception):
    def __init__(self):
        super().__init__('Депрессия')

def one_day():
    if random.randint(1, 10) == 1:
        return random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
    else:
        return random.randint(1, 7)

karma = 0
day = 0

with open('karma.lor', 'a', encoding='utf-8') as karma_file:

    while karma < 500:
        day += 1

        try:
            attempt = one_day()
            if isinstance(attempt, int):
                karma += attempt
                print(f'день - {day} - кол-во кармы - {karma}')

            elif not isinstance(attempt, int):
                raise attempt

        except KillError:
            print(f'день - {day}\t{KillError()}')
            karma_file.write(f'день: {day} - {KillError()}\n')
        except DrunkError:
            print(f'день - {day}\t{DrunkError()}')
            karma_file.write(f'день: {day} - {DrunkError()}\n')
        except CarCrashError:
            print(f'день - {day}\t{CarCrashError()}')
            karma_file.write(f'день: {day} - {CarCrashError()}\n')
        except GluttonyError:
            print(f'день - {day}\t{GluttonyError()}')
            karma_file.write(f'день: {day} - {GluttonyError()}\n')
        except DepressionError:
            print(f'день - {day}\t{DepressionError()}')
            karma_file.write(f'день: {day} - {DepressionError()}\n')







































