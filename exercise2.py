def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def run_test():
    x = [[12, 7], [4, 5], [3, 8]]
    print(transpose_matrix(x) == [[12, 4, 3], [7, 5, 8]])

run_test()
