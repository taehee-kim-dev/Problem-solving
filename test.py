from itertools import permutations

operators = ['+', '-', '*']
operators_permutations = list(permutations(operators))

print(operators_permutations)
