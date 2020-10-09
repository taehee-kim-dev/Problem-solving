


def solution(N):
    max_k = 0
    max_digits_product = 0
    for k in range(2, 9 + 1):
        tmp_digits_product = 1
        q = N
        while q >= k:
            q, r = q // k, q % k
            if r != 0:
                tmp_digits_product *= r
        tmp_digits_product *= q
        if max_digits_product <= tmp_digits_product:
            max_k = k
            max_digits_product = tmp_digits_product

    return [max_k, max_digits_product]



print(solution(10))
# [6, 4]

print(solution(14))
# [5, 8]