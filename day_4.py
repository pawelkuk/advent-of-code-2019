def has_two_adjacent(string) -> bool:
    for i, j in zip(string[:-1], string[1:]):
        if i == j:
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

assert is_valid(111111) == True # noqa
assert is_valid(223450) == False # noqa
assert is_valid(123789) == False # noqa

count = 0
for i in range(min_, max_):
    if is_valid(i):
        count += 1

print(count)
