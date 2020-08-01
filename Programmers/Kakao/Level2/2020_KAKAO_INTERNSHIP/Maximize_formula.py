from itertools import permutations
import copy

"""
2020 카카오 인턴십
수식 최대화
"""


def solution(expression):
    answer = 0
    expression_list = []
    tmp = ''
    operator_list_in_expression = []
    for operator in ['+', '-', '*']:
        if operator in expression:
            operator_list_in_expression.append(operator)
    operator_priority = list(permutations(operator_list_in_expression))
    results = []

    for expression_index in range(len(expression)):
        if expression[expression_index].isdigit():
            tmp += expression[expression_index]
            if expression_index == len(expression) - 1:
                expression_list.append(int(tmp))
        else:
            expression_list.append(int(tmp))
            expression_list.append(expression[expression_index])
            tmp = ''

    for property_case in operator_priority:
        tmp_expression_list = copy.deepcopy(expression_list)
        for operator in property_case:
            while operator in tmp_expression_list:
                print(tmp_expression_list)
                operator_index = tmp_expression_list.index(operator)
                first_number = tmp_expression_list[operator_index - 1]
                second_number = tmp_expression_list[operator_index + 1]
                new_number = -1
                if operator == '+':
                    new_number = first_number + second_number
                elif operator == '-':
                    new_number = first_number - second_number
                elif operator == '*':
                    new_number = first_number * second_number
                tmp_expression_list.insert(operator_index + 2, new_number)
                value_to_delete = 'to_delete'
                tmp_expression_list[operator_index - 1] = value_to_delete
                tmp_expression_list[operator_index] = value_to_delete
                tmp_expression_list[operator_index + 1] = value_to_delete
                while value_to_delete in tmp_expression_list:
                    tmp_expression_list.remove(value_to_delete)
        results.append(abs(tmp_expression_list[0]))
        print(results)
    answer = max(results)
    return answer


result1 = solution("100-200*300-500+20")
result2 = solution("50*6-3*2")

print('result1 : ', result1)
print('is result1 correct? : ', result1 == 60420)
print()
print('result2 : ', result1)
print('is result2 correct? : ', result2 == 300)
