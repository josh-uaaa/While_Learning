def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        lowest = 1
        highest = number
        factors = []
        while lowest < highest:
            if number % lowest == 0:
                factors.append(lowest)
                highest = number // lowest
                if highest != number and highest not in factors:
                    factors.append(highest)
            lowest += 1

        sum_factors = sum(factors)
        if sum_factors == number:
            return "perfect"
        elif sum_factors > number:
            return "abundant"
        else:
            return "deficient"