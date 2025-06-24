students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def func(dict):
    lst = []
    string = ''
    for i in dict:
        lst += dict[i]['interests']
        string += dict[i]['surname']
    length_surname = len(string)
    return lst, length_surname


pairs = [(i, students[i]['age']) for i in students]
print(f"Список пар 'ID студента — возраст': {pairs}\n"
      f"Полный список интересов всех студентов: {func(students)[0]}\n"
      f"Общая длина всех фамилий студентов: {func(students)[1]}")

