def designer_door_mat():
    row, col = map(int, input().split())

    patterns = []

    #  generate upper part textile
    for r in range(row // 2):
        patterns.append(design_textile_pattern(col, 2 * r + 1, '.|.'))

    #  print upper part textile
    for pattern in patterns:
        print(pattern)
    #  print welcome textile
    print(design_textile_pattern(col, 1, 'WELCOME'))
    # print lower part textile
    patterns.reverse()
    for pattern in patterns:
        print(pattern)


def design_textile_pattern(length: int, pattern_number: int, textile_pattern: str) -> str or None:
    if 3 * pattern_number >= length:
        return None

    remaining_spaces = length - len(textile_pattern) * pattern_number

    return '-' * (remaining_spaces // 2) + textile_pattern * pattern_number + '-' * (remaining_spaces // 2)


if __name__ == '__main__':
    designer_door_mat()







