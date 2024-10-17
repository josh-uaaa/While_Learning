def prime(number):
    prime_number = 0

    if number < 1:
        raise ValueError('there is no zeroth prime')
    primes_list = []
    prime_count, curr_number = 0, 2
    while prime_count < number:
        if curr_number == 2 or curr_number == 3 or (curr_number % 2 != 0 and curr_number % 3 != 0):
            is_prime = True
            if primes_list:
                for prime in primes_list:
                    if curr_number % prime == 0:
                        is_prime = False
                        break
            if is_prime:
                prime_count += 1
                prime_number = curr_number
                primes_list.append(prime_number)
        curr_number += 1

    return prime_number