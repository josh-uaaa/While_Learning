def cipher_text(plain_text):
    normalized_text = ""
    for char in list(plain_text):
        if char.isalnum():
            normalized_text += char.lower()

    if len(normalized_text) <= 1:
        return normalized_text

    rows, cols = 1, 1
    while True:
        if rows * cols >= len(normalized_text):
            if (rows - 1) * cols >= len(normalized_text):
                rows -= 1
            break
        else:
            rows += 1
            cols += 1

    if rows * cols > len(normalized_text):
        normalized_text += " " * ((rows * cols) - len(normalized_text))

    rectangle_text = []
    prev_i = 0
    for i in range(cols, len(normalized_text) + 1, cols):
        curr_row = normalized_text[prev_i:i]
        rectangle_text.append(list(curr_row))
        prev_i = i

    cipher_rectangle = ["".join(item) for item in zip(*rectangle_text)]
    return " ".join(cipher_rectangle)