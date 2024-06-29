def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0 or value <= 0:
        return matrix
    for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
print(result1)
result2 = get_matrix(3, 5, 42)
print(result2)
result3 = get_matrix(4, 2, 13)
print(result3)