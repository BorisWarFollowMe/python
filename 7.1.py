class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in
                        range(len(self.matrix[i]))] for i in range(len(self.matrix))])

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % j for j in i]) for i in self.matrix])


matrix_1 = Matrix([[1, 2], [3, 4]])
matrix_2 = Matrix([[5, 6], [7, 8]])
print(matrix_1 + matrix_2)
