import re


def solution(new_id):

    id_pattern = re.compile('^[a-z0-9-_.]{3,15}$')
    if (id_pattern.match(new_id) is not None) \
            and (not (new_id.startswith('.')) and (not new_id.endswith('.'))) \
            and '..' not in new_id:
        return new_id

    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r'\.{2,}', '.', new_id)
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id


# "bat.y.abcdefghi"
print(solution("...!@BaT#*..y.abcdefghijklm"))

# # "z--"
# print(solution("z-+.^."))

# # "aaa"
# print(solution("=.="))

# # "123_.def"
# print(solution("123_.def"))
#
# # "abcdefghijklmn"
# print(solution("abcdefghijklmn.p"))
