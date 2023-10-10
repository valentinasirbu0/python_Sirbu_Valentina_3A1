#Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix[0]
        matrix.pop(0)
        matrix = list(map(list, zip(*matrix)))[::-1]

    return ''.join(result)


matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

result = spiral_order(matrix)
print(result)
