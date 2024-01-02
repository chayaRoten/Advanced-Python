def find_primes(end):
    primes = set(range(0, end))
    k = 2
    while k < end:
        for number in set(primes) - set([k]):
            if (number % k) == 0:
                primes.remove(number)
        k += 1
    return primes


def sort_list(myList):
    Mylist = list(myList)
    return sorted(Mylist)


