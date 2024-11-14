def saddle_points(matrix):
    for row in matrix[1:]:
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")

    valid_points = []
    for r_index, row in enumerate(matrix):
        for c_index, col in enumerate(row):
            if check_point(matrix, r_index, c_index):
                row_col = {"row": r_index + 1, "column": c_index + 1}
                valid_points.append(row_col)

    return valid_points

def check_point(matrix, r_index, c_index):
    if max(matrix[r_index]) == matrix[r_index][c_index]:
        transposed_matrix = list(zip(*matrix))
        if min(transposed_matrix[c_index]) == transposed_matrix[c_index][r_index]:
            return True
    return False