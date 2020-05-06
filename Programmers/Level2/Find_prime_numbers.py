from itertools import permutations


def solution(numbers):

    answer = 0

    # 입력받은 숫자 문자열을 내림차순으로 정렬된 숫자로 만든다.
    # 종이조각들로 만들 수 있는 가장 큰 수에 해당한다.
    max_num = int("".join(sorted(numbers, reverse=True)))

    # 0이상 max_num이하의 인덱스를 갖는, 모든 원소들이 True로 초기화된 리스트를 생성한다.
    # 인덱스값은 특정 수를 의미하고, 각 원소값은 소수여부를 의미한다.
    all_numbers_is_prime_number = [True for _ in range(max_num + 1)]

    # 0과 1은 소수가 아니므로 False로 초기화한다.
    all_numbers_is_prime_number[0] = False
    all_numbers_is_prime_number[1] = False

    # 알고리즘 : 에라토스테네스의 체 : 소수의 배수들을 모두 지우면, 소수들만 남는다.

    # 2(소수 중 제일작은 수) 부터 최대값의 제곱근의 정수값까지만 검사를 한다.
    # 아래에서 False처리를 할 때, num_to_check의 제곱값부터 False처리를 하므로,
    # num_to_check의 제곱값이 max_num값 이하여야 한다.
    for num_to_check in range(2, int(max_num ** 0.5) + 1):

        # 숫자가 소수라면,
        if all_numbers_is_prime_number[num_to_check]:
            # 해당 숫자의 배수는 모두 소수가 아니므로 False로 바꿔준다.

            # num_to_check의 제곱 미만의 값들 중 소수가 아닌 수들은,
            # 소인수분해를 했을 때 num_to_check보다 작은 소수를 인수로 갖는다.
            # 따라서 num_to_check보다 작은 소수의 배수들을 False처리할 때 이미 처리되었다.

            # 그러므로 num_to_check의 제곱이상인 수 들 중에서, num_to_check의 배수들을 False처리한다.
            for multiple_of_prime in range(num_to_check ** 2, max_num + 1, num_to_check):
                all_numbers_is_prime_number[multiple_of_prime] = False

        # 숫자가 소수가 아니라면, 그보다 작은 소수들의 배수 False처리에서 이미 처리되었다.



    # 문자열 numbers의 각 문자를 원소로 갖는 리스트를 만든다.
    number_char_list = list(numbers)

    # 숫자가 적힌 종이 조각들을 붙여 만들 수 있는 모든 경우의 수들을 list에 저장한다.
    all_possible_number_list = []

    # 만들 수 있는 수의 길이는 1부터 numbers의 길이까지이다.
    for number_length in range(1, len(numbers) + 1):
        # 각 길이로 만들 수 있는 모든 경우의 문자의 조합(tuple)들의 list를 만들어서 
        # all_possible_number_char_tuple_list에 추가한다.
        all_possible_number_list.extend(list(permutations(number_char_list, number_length)))

    for i in range(len(all_possible_number_list)):
        # all_possible_number_char_tuple_list안에 있는 모든 튜플들을 숫자로 바꾼다.
        all_possible_number_list[i] = int(''.join(all_possible_number_list[i]))

    # 수들의 중복을 제거한다.
    all_possible_number_list = list(set(all_possible_number_list))

    # 각 수들이 소수인지 검사하여 소수라면 answer을 1 증가시킨다.
    for possible_number in all_possible_number_list:
        if all_numbers_is_prime_number[possible_number]:
            answer += 1

    return answer
