from collections import defaultdict

def solution(k, score):

    count_score_differences = defaultdict(int)
    score_differences_scores_set = defaultdict(set)

    manipulated_score_rank = set()
    not_manipulated_score_rank = set()

    for i in range(0, (len(score) - 1) - 1 + 1):
        count_score_differences[score[i] - score[i + 1]] += 1
        score_differences_scores_set[score[i] - score[i + 1]] |= {i + 1, i + 2}

    for difference, count in count_score_differences.items():
        if count >= k:
            manipulated_score_rank |= score_differences_scores_set[difference]
        else:
            not_manipulated_score_rank |= score_differences_scores_set[difference]

    return len(not_manipulated_score_rank - manipulated_score_rank)


print(solution(3, [24,22,20,10,5,3,2,1]))
# 3

print(solution(2, [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]))
# 4
