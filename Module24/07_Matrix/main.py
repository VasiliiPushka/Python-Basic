class Matrix:
    def __init__(self, rows, colomns):
        self.rows = rows
        self.colomns = colomns
        self.data = [[0] * colomns for _ in range(rows)]

    def print_info(self):
        print(self.data)

    def __add__(self, other):
        self_rows = [i+1 for i in range(self.rows)]
        self_colomns = [j+1 for j in range(self.colomns)]
        other_rows = [i+1 for i in range(other.rows)]
        other_colomns = [j+1 for j in range(other.colomns)]
        if self_rows == other_rows and self_colomns == other_colomns:
            result = Matrix(self.rows, self.colomns)
            for i in range(self.rows):
                for j in range(self.colomns):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            print(result.data)
        else:
            print('Размеры матриц не совпадают')

    def __sub__(self, other):
        self_rows = [i + 1 for i in range(self.rows)]
        self_colomns = [j + 1 for j in range(self.colomns)]
        other_rows = [i + 1 for i in range(other.rows)]
        other_colomns = [j + 1 for j in range(other.colomns)]
        if self_rows == other_rows and self_colomns == other_colomns:
            result = Matrix(self.rows, self.colomns)
            for i in range(self.rows):
                for j in range(self.colomns):
                    result.data[i][j] = self.data[i][j] - other.data[i][j]
            print(result.data)
        else:
            print('Размеры матриц не совпадают')

    def trunsposition(self):
        result = Matrix(self.colomns, self.rows)
        for i in range(self.rows):
            for j in range(self.colomns):
                result.data[j][i] = self.data[i][j]
        print(result.data)

    def __mul__(self, other):
        result = Matrix(self.rows, other.colomns)
        #проверка равенства строк и столбцов в матрицах
        colomns_count = 0
        rows_count = 0
        for i in range(self.rows):
            rows_count += 1
        for j in range(other.colomns):
            colomns_count += 1
        if rows_count == colomns_count:
            print(f'кол-во строк = {rows_count}, кол-во столбцов = {colomns_count}')

            for i in range(self.rows):
                for j in range(other.colomns):
                    summ = 0
                    for k in range(self.colomns):
                        summ += self.data[i][k] * other.data[k][j]
                    result.data[i][j] = summ
            print(result.data)
        else:
            print('кол-во строк и столбцов в матрицах разное. Произведение матриц невозможно')








# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

m1.__add__(m2)
m1.__sub__(m2)
m1.trunsposition()

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

m1.__mul__(m3)


# # Тестирование операций
# print("Матрица 1:")
# print(m1)
#
# print("Матрица 2:")
# print(m2)
#
# print("Сложение матриц:")
# print(m1.add(m2))
#
# print("Вычитание матриц:")
# print(m1.subtract(m2))
#
# m3 = Matrix(3, 2)
# m3.data = [[1, 2], [3, 4], [5, 6]]
#
# print("Умножение матриц:")
# print(m1.multiply(m3))
#
# print("Транспонирование матрицы 1:")
# print(m1.transpose())