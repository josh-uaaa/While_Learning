NUMBERS = {0: [" _ ", "| |", "|_|", "   "],
           1: ["   ", "  |", "  |", "   "],
           2: [" _ ", " _|", "|_ ", "   "],
           3: [" _ ", " _|", " _|", "   "],
           4: ["   ", "|_|", "  |", "   "],
           5: [" _ ", "|_ ", " _|", "   "],
           6: [" _ ", "|_ ", "|_|", "   "],
           7: [" _ ", "  |", "  |", "   "],
           8: [" _ ", "|_|", "|_|", "   "],
           9: [" _ ", "|_|", " _|", "   "]}

def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    grid_layers = len(input_grid) // 4
    separated_grids = separate_grids(input_grid, grid_layers)

    converted_grid = ""
    if grid_layers == 1:
        for grid in separated_grids:
            converted_grid += convert_helper(grid)
    else:
        for index, layer in enumerate(separated_grids):
            for grid in layer:
                converted_grid += convert_helper(grid)
            if index != len(separated_grids) - 1:
                converted_grid += ","

    return converted_grid

def convert_helper(valid_grid):
    for i in range(10):
        if NUMBERS[i] == valid_grid:
            return str(i)
    return "?"

def separate_grids(input_grid, grid_layers):
    separated_grids = []

    if grid_layers == 1:
        left, right = 0, 3
        while right <= len(input_grid[0]):
            curr_grid = []
            for row in input_grid:
                curr_grid.append(row[left:right])
            left = right
            right += 3
            separated_grids.append(curr_grid)
    else:
        top, down = 0, 4
        while down <= len(input_grid):
            curr_layer, curr_rows = [], input_grid[top:down]
            left, right = 0, 3
            while right <= len(input_grid[0]):
                curr_grid = []
                for row in curr_rows:
                    curr_grid.append(row[left:right])
                left = right
                right += 3
                curr_layer.append(curr_grid)
            top = down
            down += 4
            separated_grids.append(curr_layer)

    return separated_grids