COMMANDS = ('reverse', 'jump', 'close your eyes', 'double blink', 'wink')

def commands(binary_str):
    action_list = []

    binary_str = list(binary_str)
    i = len(binary_str) - 1
    while i >= 0:
        curr_num = binary_str[i]
        if curr_num == '1':
            action_list.append(COMMANDS[i])
        i -= 1

    if 'reverse' in action_list:
        action_list = list(reversed(action_list[:-1]))

    return action_list