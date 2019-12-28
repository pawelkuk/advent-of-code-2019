from typing import List
from collections import namedtuple
import numpy as np
import math
from collections import deque

Asteroid = namedtuple("Asteroid", "x y can_detect angle")


def calculate_angle(to: "Asteroid", center: "Asteroid") -> float:
    y = center.x - to.x
    x = to.y - center.y

    return math.atan2(y, x)


def get_asteroids(lines: List[str]) -> List["Asteroid"]:
    asteroids: List["Asteroid"] = []
    for enum_y, line in enumerate(lines):
        for enum_x, char in enumerate(line):
            if char == "#":
                asteroids.append(
                    Asteroid(x=enum_x, y=enum_y, can_detect=[0], angle=[0])
                )  # noqa
    return asteroids


def get_space(asteroids: List["Asteroid"]) -> "np.ndarray":
    space_dim_x = max(asteroids, key=lambda x: x.x)
    space_dim_y = max(asteroids, key=lambda x: x.y)

    space = np.ndarray((space_dim_x.x + 1, space_dim_y.y + 1), dtype=np.bool)
    space[:, :] = False

    for ast in asteroids:
        space[ast.x, ast.y] = True
    return space


def get_greatest_common_divider(x_: int, y_: int) -> int:
    x = max(x_, y_)
    y = min(x_, y_)
    while True:
        if x % y == 0:
            return y
        x, y = y, x - x // y * y


def check_if_visible(from_: "Asteroid", to: "Asteroid", space: "np.ndarray") -> bool:

    dx = to.x - from_.x
    dy = to.y - from_.y

    # if dx == 2 and dy == 0:
    #     breakpoint()
    if dx == 0:
        gcd = abs(dy)
    if dy == 0:
        gcd = abs(dx)
    if dx != 0 and dy != 0:
        gcd = get_greatest_common_divider(abs(dx), abs(dy))
    for i in range(1, gcd):
        if space[from_.x + (i * dx) // gcd, from_.y + (i * dy) // gcd]:
            return False

    return True


with open("input10.txt", mode="r") as f:
    lines = f.readlines()

lines = list(map(lambda x: x.strip(), lines))

test_0 = """.#..#
.....
#####
....#
...##"""

test_1 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

test_2 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""

test_3 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""

test_4 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

lines_0 = test_0.split("\n")
lines_1 = test_1.split("\n")
lines_2 = test_2.split("\n")
lines_3 = test_3.split("\n")
lines_4 = test_4.split("\n")


def calculate_max_visible(lines: List[str]) -> "Asteroid":
    asteroids = get_asteroids(lines)
    space = get_space(asteroids)

    for ast_inspected in asteroids:
        for ast in asteroids:
            if ast_inspected.x == ast.x and ast_inspected.y == ast.y:
                continue
            ast_inspected.can_detect[0] += check_if_visible(
                ast_inspected, ast, space
            )  # noqa
    # breakpoint()
    return max(asteroids, key=lambda x: x.can_detect[0]), asteroids


def destroy_nth_asteroid(lines: List[str], n: int) -> "Asteroid":
    station_ast, asteroids = calculate_max_visible(lines)
    for asteroid in asteroids:
        angle = calculate_angle(asteroid, station_ast)
        asteroid.angle[0] = angle if angle >= 0 else angle + 2 * math.pi
    ast_queue = deque(sorted(asteroids, key=lambda x: x.angle))

    breakpoint()
    # for _ in range(n)
    #     val = ast_queue.popleft()


assert get_greatest_common_divider(30, 9) == 3
assert get_greatest_common_divider(11, 121) == 11
assert calculate_max_visible(lines_0)[0].can_detect[0] == 8
assert calculate_max_visible(lines_1)[0].can_detect[0] == 33
assert calculate_max_visible(lines_2)[0].can_detect[0] == 35
assert calculate_max_visible(lines_3)[0].can_detect[0] == 41
assert calculate_max_visible(lines_4)[0].can_detect[0] == 210
# assert calculate_angle(Asteroid(20, 20, [0], [0]), Asteroid(10, 20, [0], [0])) == math.pi / 2  # noqa
destroy_nth_asteroid(lines_0, 1)
# breakpoint()
