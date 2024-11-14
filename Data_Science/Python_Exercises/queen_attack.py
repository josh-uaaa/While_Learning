class Queen:
    def __init__(self, row, column):
        self.row = self.validate_row(row)
        self.column = self.validate_column(column)
        self.queen = (self.row, self.column)

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        elif self.row == another_queen.row or self.column == another_queen.column: # Vertical, Horizontal.
            return True
        else:
            if another_queen.row < self.row and another_queen.column < self.column:
                return self.check_diagonal(-1, -1, another_queen)
            if another_queen.row < self.row and another_queen.column > self.column:
                return self.check_diagonal(-1, 1, another_queen)
            if another_queen.row > self.row and another_queen.column < self.column:
                return self.check_diagonal(1, -1, another_queen)
            if another_queen.row > self.row and another_queen.column > self.column:
                return self.check_diagonal(1, 1, another_queen)

    def check_diagonal(self, row_change, col_change, another_queen):
        temp_row, temp_col = self.row, self.column
        if another_queen.row < temp_row:
            while temp_row >= another_queen.row:
                if temp_row == another_queen.row and temp_col == another_queen.column:
                    return True
                temp_row += row_change
                temp_col += col_change
            return False
        elif another_queen.row > temp_row:
            while temp_row <= another_queen.row:
                if temp_row == another_queen.row and temp_col == another_queen.column:
                    return True
                temp_row += row_change
                temp_col += col_change
            return False

    def validate_row(self, row):
        if row < 0:
            raise ValueError("row not positive")
        elif row > 7:
            raise ValueError("row not on board")
        return row

    def validate_column(self, column):
        if column < 0:
            raise ValueError("column not positive")
        elif column > 7:
            raise ValueError("column not on board")
        return column