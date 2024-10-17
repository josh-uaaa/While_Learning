def transpose(text):
    transpose_list = []
    split_text = text.split("\n")
    for i, rows in enumerate(split_text):
        for j, col in enumerate(rows):
            while len(transpose_list) <= j:
                transpose_list.append([])
            while len(transpose_list[j]) < i:
                transpose_list[j].append(" ")
            transpose_list[j].append(col)

    transposed_text = "\n".join("".join(row) for row in transpose_list)
    return transposed_text