class Matrix:
    def __init__(self, m, n):
        self.rows = n
        self.cols = m
        self.data = [[0] * m for _ in range(n)]

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def set(self, elem, row, column):
        if 0 <= row < self.rows and 0 <= column < self.cols:
            self.data[row][column] = elem
        else:
            return None

    def get(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.cols:
            return self.data[row][column]
        else:
            return None

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(self.get(i, j), j, i)
        return transposed

    def multiplication(self, other):
        if self.cols != other.rows:
            return None

        result = Matrix(other.cols, self.rows)

        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self.get(i, k) * other.get(k, j)
                result.set(dot_product, i, j)

        return result

    def iterate_and_apply(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                transformed_value = func(self.get(i, j))
                self.set(transformed_value, i, j)


m = Matrix(3, 3)
m.set(5, 0, 0)
m.set(3, 1, 1)
m.set(1, 2, 2)
print(m.get(0, 0))
print(m)

m = m.transpose()
print("Transposed matrix:")
print(m)

result = m.multiplication(m.transpose())
print("Matrix multiplication result:")
print(result)


double_element = lambda elem: elem * 2
m.iterate_and_apply(double_element)
print("Matrix after applying the transformation:")
print(m)