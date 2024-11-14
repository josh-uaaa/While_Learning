def factors(value):
    prime_factors = []
    if value == 1:
        return []
    else:
        remainder, i = value, 2
        while remainder != 1:
            while remainder % i == 0:
                remainder //= i
                prime_factors.append(i)
            i += 1

    return prime_factors