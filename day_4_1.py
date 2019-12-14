def has_two_adjacent(string) -> bool:
    padded_string = ' ' + string + ' '
    for left, l_middle, r_middle, right in zip(padded_string[:-3],
                                               padded_string[1:-2],
                                               padded_string[2:-1],
                                               padded_string[3:]):
        if l_middle == r_middle and left != l_middle and right != r_middle:
            return True
    return False


def decreases(string: str) -> bool:
    for i, j in zip(string[:-1], string[1:]):
        if int(i) > int(j):
            return True
    return False


def is_valid(password: int,
             range_min: int = 353096,
             range_max: int = 843212) -> bool:
    string: str = str(password)
    if len(string) != 6:
        return False
    if not has_two_adjacent(string):
        return False
    if decreases(string):
        return False
    return True


min_ = 353096
max_ = 843212


assert decreases('43') == True # noqa
assert decreases('5422222') == True # noqa
assert decreases('234567') == False # noqa

assert has_two_adjacent('345678') == False # noqa
assert has_two_adjacent('987') == False # noqa
assert has_two_adjacent('4466709') == True # noqa
assert has_two_adjacent('434444') == False # noqa

assert is_valid(112233) == True # noqa
assert is_valid(123444) == False # noqa
assert is_valid(111122) == True # noqa

count = 0
for i in range(min_, max_):
    if is_valid(i):
        count += 1

print(count)
