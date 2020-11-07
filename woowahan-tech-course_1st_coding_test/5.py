

def solution(penter, pexit, pescape, data):
    answer = penter
    in_words = [penter, pexit, pescape]
    data_length = len(penter)
    for data_split_last_index_plus_one in range(data_length, len(data) + 1, data_length):
        data_part = data[data_split_last_index_plus_one - data_length: data_split_last_index_plus_one]
        if data_part in in_words:
            answer += pescape
        answer += data_part
    answer += pexit
    return answer
