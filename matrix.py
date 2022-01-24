class Matrix:
    @staticmethod
    def matrix(arrs):
        m = Matrix(0, 0)
        m.value = [[x for x in y] for y in arrs]
        return m

    @staticmethod
    def is_square(m):
        return len(m.value) == len(m.value[0])

    def __init__(self, nr_col, nr_row):
        self.value = [[0 for _ in range(nr_col)] for _ in range(nr_row)]

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Matrix.matrix([[x * other for x in y] for y in self.value])
        elif type(other) == Matrix and len(self.value[0]) == len(other.value):
            m = [[] for _ in self.value]
            for i in range(len(self.value)):
                r = [0 for _ in other.value[0]]
                for j in range(len(other.value[0])):
                    s = 0
                    for k in range(len(self.value[0])):
                        s += self.value[i][k] * other.value[k][j]
                    r[j] = s
                m[i] = r
            return Matrix.matrix(m)

    def transpose(self):
        v = [[] for _ in range(len(self.value[0]))]
        for i in range(len(self.value[0])):
            row = [0 for _ in range(len(self.value))]
            for j in range(len(self.value)):
                row[j] = self.value[j][i]
            v[i] = row

        self.value = v
        return self

    def det(self):
        if Matrix.is_square(self):
            if len(self.value) <= 0:
                return "NAN"
            elif len(self.value) == 1:
                return self.value[0][0]
            elif len(self.value) == 2:
                return self.value[0][0] * self.value[1][1] - self.value[1][0] * self.value[0][1]
            else:
                res = 0
                sign = 1
                for i in range(len(self.value)):
                    new_mat = [[0 for _ in range(len(self.value) - 1)] for _ in range(len(self.value) - 1)]
                    diff = 0
                    for j in range(len(self.value)):
                        if j == i:
                            diff = 1
                        elif j != i:
                            for k in range(1, len(self.value)):
                                new_mat[k-1][j-diff] = self.value[k][j]
                    new = Matrix.matrix(new_mat)
                    res += sign * self.value[0][i] * new.det()
                return res

    def rref(self, augmented=True):
        m = [[float(x) for x in y] for y in self.value]
        pivot_row = 0
        pivot_col = 0
        for i in range(len(m)):
            for j in range(pivot_col, len(m[0]) - (1 if augmented else 0)):
                all_zero = True
                first_non_zero = pivot_row
                for k in range(pivot_row, len(m)):
                    if all_zero and m[k][j] != 0:
                        all_zero = False
                        first_non_zero = k
                    if not all_zero:
                        if m[k][j] == 1 or m[k][j] == -1:
                            first_non_zero = k
                            break
                if not all_zero:
                    temp = [x / m[first_non_zero][pivot_col] for x in m[first_non_zero]]
                    m[first_non_zero] = [x for x in m[pivot_row]]
                    m[pivot_row] = temp

                    for k in range(pivot_row):
                        p_rate = m[k][pivot_col]
                        for idx in range(pivot_col, len(m[0])):
                            m[k][idx] -= p_rate * m[pivot_row][idx]
                    for k in range(pivot_row + 1, len(m)):
                        p_rate = m[k][pivot_col]
                        for idx in range(pivot_col, len(m[0])):
                            m[k][idx] -= p_rate * m[pivot_row][idx]
                    pivot_row += 1
                pivot_col += 1
        return Matrix.matrix(m)

    def solve_augmented(self):
        m = self.rref(True)
        if m.value[len(self.value)-1][len(self.value[0])-1] != 0.0:
            return f"the matrix is inconsistent"
        else:
            st = ""
            for i in range(len(self.value[0])-1):
                st += f"x_{i+1} = {m.value[i][-1]:g}" + ('\n' if i != len(self.value[0])-2 else '')
            return st

    def __str__(self):
        st = ""
        for i in range(len(self.value) - 1):
            st += f"{self.value[i]}\n"
        st += f"{self.value[len(self.value) - 1]}"
        return st
