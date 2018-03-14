import random
from math import sqrt


def rand_pairs_of_numbers(n: int) -> []:
    """
    :param n: number of pairs of numbers.
    :return: list of n random pairs of numbers.
    """
    numbers = []
    for i in range(n):
        numbers.append([random.randint(2, 1000000), random.randint(2, 1000000)])

    return numbers


def gcd(n: int, m: int) -> int:
    """
    Euclidean algorithm
    :return: Greatest common divisor of n, m
    """
    if m == 0:
        return n
    return gcd(m, n % m)


def are_coprime(n: int, m: int) -> bool:
    """
    Check if n, m are coprime.
    :return: True if n, m are coprime, otherwise False
    """
    if gcd(n, m) == 1:
        return True
    return False


def count_coprime_pairs(pairs_of_numbers: []):
    """
    :param pairs_of_numbers: list of pairs of numbers
    :return: quantity of pairs coprime numbers
    """
    counter = 0
    for pair in pairs_of_numbers:
        if are_coprime(pair[0], pair[1]):
            counter += 1
    return counter


def compute_pi(n: int) -> float:
    """
    Monte Carlo algorithm to find approximation of pi number.
    Using formula to probability of coprimness of two natural numbers:
            p = 6 / pow(pi, 2)  <=>  pi = sqrt(6, p)

    :param n: number of pairs of random numbers using to find pi.
    :return: approximation of pi number.
    """
    pairs_of_numbers = rand_pairs_of_numbers(n)

    coprime_pairs = count_coprime_pairs(pairs_of_numbers)

    pi = sqrt(6 / (coprime_pairs / n))
    return pi


if __name__ == '__main__':
    print(compute_pi(1000000))
