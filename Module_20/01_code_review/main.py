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

def function(dict):
    hobby = []
    string = ''
    for i_elem in dict:
        hobby += (dict[i_elem]['interests'])
        string += dict[i_elem]['surname']
    len_count = 0
    for len_sym in string:
        len_count += 1
    return hobby, len_count

pairs = []
for i_id in students:
    id = i_id
    age = students[i_id]['age']
    id_age = (id, age)
    pairs.append(id_age)
print('Список пар "ID студента — возраст:', pairs)

my_list = function(students)[0]
len_sym = function(students)[1]
print(f'Полный список интересов всех студентов: {my_list}')
print(f'Общая длина всех фамилий студентов: {len_sym}')


