def proverb(*inputs, qualifier=None):
    proverb_string = []

    if not inputs:
        return proverb_string

    for i in range(len(inputs) - 1):
        proverb_string.append(f"For want of a {inputs[i]} the {inputs[i + 1]} was lost.")
    if qualifier:
        proverb_string.append(f"And all for the want of a {qualifier} {inputs[0]}.")
    else:
        proverb_string.append(f"And all for the want of a {inputs[0]}.")

    return proverb_string