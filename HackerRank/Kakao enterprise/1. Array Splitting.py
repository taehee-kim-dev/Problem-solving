from collections import deque


def segment(x, space):
    # Write your code here
    
    for start_index in range(0, len(space) - 1 - x + 1):
        end_index = start_index + x - 1
        new_segment = space[start_index:end_index + 1]
        if start_index == 0:
            segment_deque = deque(new_segment)
            before_min = min(new_segment)
            answer_max = before_min
            continue

        before_item = segment_deque.popleft()
        segment_deque.append(space[end_index])

        if before_item == before_min:
            if before_item in new_segment:
                before_min = min(before_item, space[end_index])
            else:
                before_min = min(new_segment)
        else:
            before_min = min(before_item, space[end_index])

        answer_max = max(answer_max, before_min)

    return answer_max


print(segment(1, [1, 2, 3, 1, 2]))