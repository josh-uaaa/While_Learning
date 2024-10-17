BRACKETS = {'[': ']', '{': '}', '(': ')'}

def is_paired(input_string):
    bracket_stack = []
    for char in input_string:
        if char in BRACKETS.keys():
            bracket_stack.append(char)
        elif char in BRACKETS.values():
            if len(bracket_stack) > 0:
                last_appended_bracket = bracket_stack.pop()
                if char != BRACKETS.get(last_appended_bracket):
                    return False
            else:
                return False

    return len(bracket_stack) == 0