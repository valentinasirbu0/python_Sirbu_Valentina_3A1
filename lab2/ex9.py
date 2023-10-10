def see_the_game(matrix):
    result = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            for k in range(i + 1, len(matrix)):
                if matrix[i][j] >= matrix[k][j]:
                    result.append([k, j])
    return result


#FIELD
m = [[1, 2, 3, 2, 1, 1],
     [2, 4, 4, 3, 7, 2],
     [5, 5, 2, 5, 6, 4],
     [6, 6, 7, 6, 7, 5]]
r = see_the_game(m)
print(r)
