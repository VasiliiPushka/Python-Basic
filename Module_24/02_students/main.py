class Student:
    def __init__(self, name, group_num, estimates):
        self.name = name
        self.group_num = group_num
        self.estimates = estimates

    def gpa(self):
        point = 0
        count = 0
        for i in self.estimates:
            point += i
            count += 1
        gpa = point / count
        return gpa

std_1 = Student('Егор', 4008, [4, 3, 5, 4, 5])
std_2 = Student('Виталий', 4008, [4, 3, 3, 4, 5])
std_3 = Student('Олег', 4009, [5, 5, 4, 4, 5])

sorted_student = sorted([std_1, std_2, std_3], reverse=True, key=Student.gpa)
for student in sorted_student:
    print(student.name, student.gpa())



























































