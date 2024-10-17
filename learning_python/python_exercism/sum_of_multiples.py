def sum_of_multiples(limit, multiples):
    multiples_set = set()
    for i in range(limit):
        for num in multiples:
            if num != 0 and i % num == 0:
                multiples_set.add(i)

    return sum(multiples_set)