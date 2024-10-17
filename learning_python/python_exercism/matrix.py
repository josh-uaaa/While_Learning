class Matrix:
    def __init__(self, matrix_string):
        self.matrix_rows = [tuple(row.split(" ")) for row in matrix_string.split("\n")]
        self.matrix_cols = list(zip(*self.matrix_rows))

    def row(self, index):
        return [int(num) for num in self.matrix_rows[index - 1]]

    def column(self, index):
        return [int(num) for num in self.matrix_cols[index - 1]]