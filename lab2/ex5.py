
def transform_diagonal(m):
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            if i == j:
                m[i][j] = 0
    return m


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
r = transform_diagonal(matrix)
print(r)
