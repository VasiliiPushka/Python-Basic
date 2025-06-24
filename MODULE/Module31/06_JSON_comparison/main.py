import json


def get_difference(massiv1, massiv2, diff_list):
    def get_deep_difference(massiv1, massiv2, deepcheck):
        nonlocal changes, diff_list
        difference = False

        try:
            # Основной цикл по словарю
            for key in massiv1.keys():
                check = deepcheck or diff_list and key in diff_list
                try:
                    if get_deep_difference(massiv1[key], massiv2[key], check):
                        if diff_list and key in diff_list:
                            changes[key] = massiv2[key]
                        if deepcheck:
                            return True
                        difference = True
                except KeyError:  # В massiv2 отсутствует ключ
                    if diff_list and key in diff_list:
                        changes[key] = None
                    if deepcheck:
                        return True
                    difference = True

        except AttributeError:  # massiv1 не словарь

            if isinstance(massiv1, str):  # обработка строки
                return massiv1 != massiv2

            try:
                # Обработка других типов данных (список, кортеж, множество)
                for index, elem in enumerate(massiv1):
                    try:
                        if get_deep_difference(massiv1[index], massiv2[index], deepcheck):
                            if deepcheck:
                                return True
                            difference = True
                    except IndexError:
                        return True

            except TypeError:
                return massiv1 != massiv2

        return difference
        # конец функции get_deep_difference

    changes = dict()
    get_deep_difference(massiv1, massiv2, False)
    return changes
# конец функции get_difference


with open('json_old.json') as file_1, open('json_new.json') as file_2:
    data_old = json.load(file_1)
    data_new = json.load(file_2)

diff_list = ["services", "staff", "datetime"]

changes = []

result = get_difference(data_old, data_new, diff_list)
print(result)


