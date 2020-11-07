
def solution(grades, weights, threshold):

    grades_map = {
        'A+': 10,
        'A0': 9,
        'B+': 8,
        'B0': 7,
        'C+': 6,
        'C0': 5,
        'D+': 4,
        'D0': 3,
        'F': 0
    }

    total_score = 0
    for alpha_grade, weight in zip(grades, weights):
        total_score += (grades_map[alpha_grade] * weight)

    return total_score - threshold
