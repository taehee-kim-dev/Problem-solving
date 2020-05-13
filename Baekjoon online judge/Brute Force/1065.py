import sys
sys.setrecursionlimit(10000)

# 1000 이하의 자연수 N 입력받음 (문자열 형태)
N = input()

total_count_of_han_number_int = 0


# 현재 문자열 형태의 숫자가 한수인지 체크
def is_han_number(number_to_check_str):

    if len(number_to_check_str) == 1:
        return True

    diff = int(number_to_check_str[1]) - int(number_to_check_str[0])

    for num_index in range(1, len(number_to_check_str) - 1):
        if int(number_to_check_str[num_index + 1]) - \
                int(number_to_check_str[num_index]) \
                != diff:

            return False

    return True


# 1보다 크거나 같고, N보다 작거나 같은 수
def solution(current_number_str):

    global total_count_of_han_number_int

    if current_number_str == '0':
        return total_count_of_han_number_int

    # 매개변수로 받은 현재 수가 한수이면 총 한수의 개수 1 증가
    if is_han_number(current_number_str):
        total_count_of_han_number_int += 1

    # 현재 수에서 1보다 작은 수 재귀호출
    return solution(str(int(current_number_str) - 1))


print(solution(N))
