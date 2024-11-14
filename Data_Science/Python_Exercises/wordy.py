def answer(question):
    valid_operations = ("plus", "minus", "multiplied", "divided")
    split_question = question[8:-1].split()

    if not split_question:
        raise ValueError("syntax error")

    equation_stack = []
    last_item = "operation"
    for item in split_question:
        if item.isdigit() or item[0] == "-":
            if last_item == "operation":
                equation_stack.append(int(item))
                last_item = "digit"
            else:
                raise ValueError("syntax error")
        elif item.isalpha():
            if item in valid_operations:
                if last_item == "digit":
                    equation_stack.append(item)
                    last_item = "operation"
                else:
                    raise ValueError("syntax error")
            elif item != "by":
                raise ValueError("unknown operation")

    if last_item != "digit":
        raise ValueError("syntax error")

    a, op, b, result = 0, "", 0, 0
    while equation_stack:
        if len(equation_stack) == 1:
            return equation_stack[0]
        else:
            a, op, b = equation_stack[0], equation_stack[1], equation_stack[2]
            if op == "plus":
                result = a + b
            elif op == "minus":
                result = a - b
            elif op == "multiplied":
                result = a * b
            else:
                result = a // b
            equation_stack = [result] + equation_stack[3:]