import itertools


def solution(numbers):

    sums = set()
    for a, b in itertools.combinations(numbers, 2):
        sums.add(a + b)

    return sorted(list(sums))
