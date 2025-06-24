class Matrix:

    def __init__(self, row:int, col:int):
        self.row = row
        self.col = col
        self.data = [[0 for _ in range(self.col)] for _ in range(self.row)]


    def info(self):
        for row in self.data:
            for col in row:
                print(col, end='\t')
            print()
        return self


    def __add__(self, other):
        result = Matrix(self.row, self.col)
        if isinstance(other, Matrix):
            if self.row != other.row or self.col != other.col:
                raise ValueError ("Матрицы разных размеров, сложение невозможно!")


            for i in range(self.row):
                for j in range(self.col):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]

        return result.info()


    def transposition(self):
        transposed = Matrix(self.col, self.row)

        for i in range(self.col):
            for j in range(self.row):
                transposed.data[i][j] = self.data[j][i]
        return transposed


    def __sub__(self, other):
        result = Matrix(self.row, self.col)
        if isinstance(other, Matrix):
            if self.row != other.row or self.col != other.col:
                raise ValueError("Матрицы разных размеров, вычетание невозможно!")


            for i in range(self.row):
                for j in range(self.col):
                    result.data[i][j] = self.data[i][j] - other.data[i][j]

        return result


    def __mul__(self, other):
        result = Matrix(self.row, other.col)
        if not isinstance(other, Matrix):
            raise TypeError("Можно умножить только на другую матрицу")

            # Проверка согласованности размеров
        if self.col != other.row:
            raise ValueError("Количество столбцов в первой матрице должно совпадать с количеством строк во второй матрице.")

        for i in range(self.row):
            for j in range(other.col):
                for k in range(self.col):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result


m1 = Matrix(row=2, col=3)
m1.data = [[1, 2, 3],[4, 5, 6]]
print()
m2 = Matrix(row=2, col=3)
m2.data = [[4, 5, 6], [7, 8, 9]]
print()
m3 = Matrix(3,2)
m3.data = [[3, 5], [6, 7], [9, 4]]

m1.__add__(m2).info()
print()
m1.__sub__(m2).info()
print()
m1.transposition().info()
print()
m1.__mul__(m3).info()



