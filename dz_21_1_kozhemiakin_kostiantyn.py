import random


class Matrix:
    def __init__(self, my_matrix=[[]]):
        self.__matrix = my_matrix.copy()
        self.__len_row = len(self.__matrix)
        self.__len_col = self.__matrix_max_len_col()

    def __str__(self):
        my_str = ""
        for row in self.__matrix:
            my_str += f"{str(row)}\n"
        return my_str

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self.__sum_to_matrix_num(other)
        elif type(other) == list:
            return self.__sum_to_matrix_list(other)
        elif type(other) == Matrix:
            return self.__sum_to_matrix_matrix(other)
        else:
            raise "TypeError"

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            return self.__sub_to_matrix_num(other)
        elif type(other) == list:
            return self.__sub_to_matrix_list(other)
        elif type(other) == Matrix:
            return self.__sub_to_matrix_matrix(other)
        else:
            raise "TypeError"

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return self.__mul_to_matrix_num(other)
        elif type(other) == list:
            return self.__mul_to_matrix_list(other)
        elif type(other) == Matrix:
            return self.__mul_to_matrix_matrix(other)
        else:
            raise "TypeError"

    def __matrix_max_len_col(self):
        max_len = 0
        for i in range(0, self.__len_row):
            if len(self.__matrix[i]) > max_len:
                max_len = len(self.__matrix[i])
        return max_len

    def print_matrix(self):
        for row in self.__matrix:
            print(row)

    def add_zero(self):
        self.__len_col = self.__matrix_max_len_col()
        self.__len_row = len(self.__matrix)
        for i in range(0, self.__len_row):
            if len(self.__matrix[i]) < self.__len_col:
                count = self.__len_col - len(self.__matrix[i])
                for j in range(0, count):
                    self.__matrix[i].append(0)
        return self.__matrix

    def add_col(self, count_of_col):
        for i in range(count_of_col):
            self.__matrix[0].append(0)
            self.add_zero()
        return self

    def add_row(self, count_of_row):
        for i in range(count_of_row):
            self.__matrix.append([0])
        self.add_zero()
        return self

    def __change_size_of_matrix(self, matrix_for_verification):
        if self.__len_row < matrix_for_verification.__len_row:
            self.add_row(matrix_for_verification.__len_row - self.__len_row)
        elif self.__len_row > matrix_for_verification.__len_row:
            matrix_for_verification.add_row(self.__len_row - matrix_for_verification.__len_row)
        if self.__len_col < matrix_for_verification.__len_col:
            self.add_col(matrix_for_verification.__len_col - self.__len_col)
        elif self.__len_col > matrix_for_verification.__len_col:
            matrix_for_verification.add_col(self.__len_col - matrix_for_verification.__len_col)

    def create_random_matrix(self, len_row=0, len_col=0, rand_start=0, rand_finish=0):
        for i in range(0, len_row):
            if i >= self.__len_row:
                self.__matrix.append([])
            for j in range(0, len_col):
                if j >= len(self.__matrix[i]):
                    self.__matrix[i].append([])
                self.__matrix[i][j] = random.randint(rand_start, rand_finish)
        self.add_zero()
        return self

    def create_copy(self):
        my_list = []
        for i in range(self.__len_row):
            my_list.append([])
            for j in range(self.__len_col):
                my_list[i].append(self.__matrix[i][j])
        copy_matrix = Matrix(my_list)
        return copy_matrix

    def __sum_to_matrix_num(self, to_add):
        new_matrix = Matrix()
        new_matrix.create_random_matrix(self.__len_row, self.__len_col)
        for i in range(self.__len_row):
            for j in range(self.__len_col):
                new_matrix.__matrix[i][j] = self.__matrix[i][j] + to_add
        return new_matrix

    def __sum_to_matrix_list(self, to_add: list):
        return self.__sum_to_matrix_matrix(Matrix(to_add))

    def __sum_to_matrix_matrix(self, to_add):
        self_copy = self.create_copy()
        to_add_copy = to_add.create_copy()
        self_copy.__change_size_of_matrix(to_add_copy)
        for i in range(self_copy.__len_row):
            for j in range(self_copy.__len_col):
                self_copy.__matrix[i][j] = self_copy.__matrix[i][j] + to_add_copy.__matrix[i][j]
        return self_copy

    def __sub_to_matrix_num(self, to_sub):
        new_matrix = Matrix()
        new_matrix.create_random_matrix(self.__len_row, self.__len_col)
        for i in range(self.__len_row):
            for j in range(self.__len_col):
                new_matrix.__matrix[i][j] = self.__matrix[i][j] - to_sub
        return new_matrix

    def __sub_to_matrix_list(self, to_sub: list):
        return self.__sub_to_matrix_matrix(Matrix(to_sub))

    def __sub_to_matrix_matrix(self, to_sub):
        self_copy = self.create_copy()
        to_add_copy = to_sub.create_copy()
        self_copy.__change_size_of_matrix(to_add_copy)
        for i in range(self_copy.__len_row):
            for j in range(self_copy.__len_col):
                self_copy.__matrix[i][j] = self_copy.__matrix[i][j] - to_add_copy.__matrix[i][j]
        return self_copy

    def __mul_to_matrix_num(self, to_mul: int):
        new_matrix = Matrix()
        new_matrix.create_random_matrix(self.__len_row, self.__len_col)
        for i in range(self.__len_row):
            for j in range(self.__len_col):
                new_matrix.__matrix[i][j] = self.__matrix[i][j] * to_mul
        return new_matrix

    def __mul_to_matrix_list(self, to_mul: list):
        return self.__mul_to_matrix_matrix(Matrix(to_mul))

    def __mul_to_matrix_matrix(self, to_mul):
        if self.__len_col == to_mul.__len_row:
            new_matrix = Matrix()
            new_matrix = new_matrix.create_random_matrix(self.__len_row, to_mul.__len_col)
            for i in range(self.__len_row):
                for j in range(to_mul.__len_col):
                    for k in range(to_mul.__len_row):
                        new_matrix.__matrix[i][j] += self.__matrix[i][k] * to_mul.__matrix[k][j]
            return new_matrix
        else:
            raise "The number of columns of the first matrix is not equal to the number of rows of the second matrix"

    def trans_matrix_matrix(self):
        self_copy = self.create_copy()
        trans_matrix = Matrix([])
        trans_matrix.create_random_matrix(self.__len_col, self.__len_row)
        for i in range(self_copy.__len_row):
            for j in range(self_copy.__len_col):
                trans_matrix.__matrix[j][i] = self_copy.__matrix[i][j]
        return trans_matrix


X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9],
     [3, 4, 1]]

Y = [[5, 8, 1, 2, 2],
     [6, 7, 3, 2, 2],
     [4, 5, 9, 2, 2]]

Z = [[2, 2],
     [4, 3]]

matrix = Matrix(X)
matrix_2 = Matrix(Y)

matrix_sum_1 = matrix + Y
matrix_sum_2 = matrix + matrix_2
matrix_sum_1.print_matrix()
print()
matrix_sum_2.print_matrix()
print()
matrix_subtract_1 = matrix - Z
matrix_subtract_2 = matrix - matrix_2
matrix_subtract_1.print_matrix()
print()
matrix_subtract_2.print_matrix()
print()
matrix_multiply_1 = matrix * Y
matrix_multiply_2 = matrix * matrix_2
matrix_multiply_1.print_matrix()
print()
matrix_multiply_2.print_matrix()
print()
matrix_transpose = matrix.trans_matrix_matrix()
matrix_transpose.print_matrix()
