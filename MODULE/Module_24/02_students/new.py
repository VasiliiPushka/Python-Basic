import random

class Student:

    def __init__(self, name_surname:str, group:str, progress:list):
        self.name_surname = name_surname
        self.group = group
        self.progress = progress

    def average_score(self):
        sum_point = 0
        for i in self.progress:
            sum_point += i
        return sum_point

    def print_info(self):
        print(f'Имя и фамилия - {self.name_surname} | номер группы - {self.group} | успеваемость - {self.progress}')


student_list = []

for _ in range(3):
    stud = Student(name_surname=input("Введите имя и фамилию: ").title(),
                   group=input('Введите номер группы: '),
                   progress=[random.randint(3, 5) for _ in range(5)]
                   )
    print()
    student_list.append(stud)

sorted_student = sorted(student_list, key=lambda student:student.average_score(), reverse=True)

for student in sorted_student:
    student.print_info()



















