





def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    new_id_removed = ''
    for char in new_id:
        if char.isalpha() or char.isdigit() or char == '-' or char == '_' or char == '.':
            new_id_removed += char

    new_id_dot_removed = ''
    dot_before = False
    for char in new_id_removed:
        if dot_before and char == '.':
            continue
        if not dot_before and char == '.':
            dot_before = True
        if dot_before and char != '.':
            dot_before = False

        new_id_dot_removed += char

    if len(new_id_dot_removed) > 0 and new_id_dot_removed[0] == '.':
        new_id_dot_removed = new_id_dot_removed[1:]

    if len(new_id_dot_removed) > 0 and new_id_dot_removed[-1] == '.':
        new_id_dot_removed = new_id_dot_removed[:-1]

    if new_id_dot_removed == '':
        new_id_dot_removed = 'a'

    if len(new_id_dot_removed) >= 16:
        new_id_dot_removed = new_id_dot_removed[:15]
        if new_id_dot_removed[-1] == '.':
            new_id_dot_removed = new_id_dot_removed[:-1]

    last_char = new_id_dot_removed[-1]
    while len(new_id_dot_removed) < 3:
        new_id_dot_removed += last_char

    answer = new_id_dot_removed

    return answer










print(solution("...!@BaT#*..y.abcdefghijklm"))
#
