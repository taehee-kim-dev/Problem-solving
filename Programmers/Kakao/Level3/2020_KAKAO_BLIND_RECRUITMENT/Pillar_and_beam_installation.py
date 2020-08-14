from copy import deepcopy

"""
기둥과 보 설치
"""


class Pillar:
    def __init__(self, x, y):
        self.type = 0
        self.x = x
        self.y = y
        self.y_top = y + 1
        self.y_bottom = y


class Beam:
    def __init__(self, x, y):
        self.type = 1
        self.x = x
        self.y = y
        self.left_end_x = x
        self.right_end_x = x + 1


def do_task(structures_status_for_test, task):
    result = structures_status_for_test
    task_structure_x = task[0]
    task_structure_y = task[1]
    task_structure_type = task[2]
    task_type = task[3]

    if task_type == 1:
        # 설치이면
        if task_structure_type == 0:
            # 기둥이면
            result.append(
                Pillar(task_structure_x, task_structure_y))
        else:
            # 보 이면
            result.append(
                Beam(task_structure_x, task_structure_y))
    else:
        # 삭제이면
        result = \
            list(filter(
                lambda structure: structure.x != task_structure_x
                and structure.y != task_structure_y
                and structure.type != task_structure_type,
                result
            ))
    return result


def is_pillar_on_beams_end(pillar_to_check, all_installed_beams):
    for installed_beam in all_installed_beams:
        if pillar_to_check.y == installed_beam.y \
                and (pillar_to_check.x == installed_beam.left_end_x
                     or pillar_to_check.x == installed_beam.right_end_x):
            return True
    return False


def is_pillar_on_top_of_other_pillar(pillar_to_check, all_installed_pillars):
    for installed_pillar in all_installed_pillars:
        if installed_pillar == pillar_to_check:
            continue
        if pillar_to_check.x == installed_pillar.x \
                and pillar_to_check.y_bottom == installed_pillar.y_top:
            return True
    return False


def is_beam_on_top_of_pillar(beam_to_check, all_installed_pillars):
    for installed_pillar in all_installed_pillars:
        if beam_to_check.y == installed_pillar.y_top \
                and (beam_to_check.left_end_x == installed_pillar.x
                     or beam_to_check.right_end_x == installed_pillar.x):
            return True
    return False


def is_beam_connected_with_other_beams(beam_to_check, all_installed_beams):
    is_left_end_of_beam_to_check_connected = False
    is_right_end_of_beam_to_check_connected = False
    for installed_beam in all_installed_beams:
        if is_left_end_of_beam_to_check_connected and is_right_end_of_beam_to_check_connected:
            return True
        if installed_beam == beam_to_check:
            continue
        if installed_beam.y == beam_to_check.y:
            if beam_to_check.right_end_x == installed_beam.left_end_x:
                is_right_end_of_beam_to_check_connected = True
            if beam_to_check.left_end_x == installed_beam.right_end_x:
                is_left_end_of_beam_to_check_connected = True
    return False


def is_valid_structures_status(structures_status_for_test):
    all_installed_beams = list(filter(lambda x: x.type == 1, structures_status_for_test))
    all_installed_pillars = list(filter(lambda x: x.type == 0, structures_status_for_test))
    for structure in structures_status_for_test:
        if structure.type == 0:
            # 기둥이면
            pillar_to_check = structure
            if not (pillar_to_check.y_bottom == 0
                    or is_pillar_on_beams_end(pillar_to_check, all_installed_beams)
                    or is_pillar_on_top_of_other_pillar(pillar_to_check, all_installed_pillars)):
                return False
        else:
            # 보 이면
            beam_to_check = structure
            if not (is_beam_on_top_of_pillar(beam_to_check, all_installed_pillars)
                    or is_beam_connected_with_other_beams(beam_to_check, all_installed_beams)):
                return False
    return True


def convert_objects_to_arrays(current_structures_status, answer):
    for structure_object in current_structures_status:
        answer.append([structure_object.x, structure_object.y, structure_object.type])


def solution(n, build_frame):
    answer = []
    # [x, y, 구조물의 종류(0:기둥, 1:보), 작업 종류(0:삭제, 1:설치)]
    current_structures_status = []
    for task in build_frame:
        if task == [2, 0, 0, 0]:
            print('debug')
        structures_status_for_test = deepcopy(current_structures_status)
        structures_status_for_test = do_task(structures_status_for_test, task)
        if is_valid_structures_status(structures_status_for_test):
            current_structures_status = do_task(current_structures_status, task)

        print(answer)

    convert_objects_to_arrays(current_structures_status, answer)
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return

print(solution(
    5,
    [
        [0, 0, 0, 1],
        [2, 0, 0, 1],
        [4, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [2, 1, 1, 1],
        [3, 1, 1, 1],
        [2, 0, 0, 0],
        [1, 1, 1, 0],
        [2, 2, 0, 1]]
))
