'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
'''
class Matrix:
    def __init__(self, values):
        if isinstance(values, list):
            self.values = [[int(cell) for cell in row] for row in values]
        else:
            print(f'Incorrect parameters. Should be list')
        lines = [len(el) for el in values]
        self.qty_col = lines[0]
        self.qty_row = len(lines)
    
    def __str__(self):
        s = ''
        for row in self.values:
            for el in row:
                s += f'{el:<10}'
            s += f'\n'
        return s

    def __add__(self, other):
        if self.qty_col == other.qty_col and self.qty_row == other.qty_row:
            matrix_sum = [
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.values, other.values)]
            return Matrix(matrix_sum)
        else:
            print("Matrices have different dimensions")

m1 = Matrix([[10, 20, 30, 40], [10, 20, 30, 40], [10, 20, 30, 40]])
m2 = Matrix([[10, 20, 30, 40], [10, 20, 30, 40], [10, 20, 30, 40]])
print(m1+m2)
