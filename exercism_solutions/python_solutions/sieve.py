def primes(limit):
    initial_list = [i for i in range(2, limit + 1)]
    not_primes_list = []

    for num in initial_list:
        if num not in not_primes_list:
            prime_num = num + num
            while prime_num <= limit:
                not_primes_list.append(prime_num)
                prime_num += num

    final_list = sorted(list(set(initial_list) - set(not_primes_list)))
    return final_list