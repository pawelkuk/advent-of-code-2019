from functools import namedtuple
from collections import defaultdict
# import math
# from pprint import pprint
from typing import Tuple, Dict, NamedTuple, List


class Grid:
    def __init__(self,
                 points: Dict[Tuple[int], int] = None,
                 basis=(0, 0)) -> None:
        if points is None:
            self.points = defaultdict(int)
        else:
            self.points = points
        self.basis = basis
        self.head = basis

    def add_intruction(self, instruction: NamedTuple) -> None:
        points: List[Tuple] = self._generate_points(instruction)
        self.head = points[-1]
        for point in points:
            self.points[point] += 1

    def _generate_points(self, instruction: NamedTuple) -> List[Tuple]:
        points = []
        direction = instruction.direction
        if direction == 'R':
            points = [(self.head[0] + i, self.head[1])
                      for i in range(1, instruction.number_of_fields + 1)]
        if direction == 'L':
            points = [(self.head[0] - i, self.head[1])
                      for i in range(1, instruction.number_of_fields + 1)]
        if direction == 'U':
            points = [(self.head[0], self.head[1] + i)
                      for i in range(1, instruction.number_of_fields + 1)]
        if direction == 'D':
            points = [(self.head[0], self.head[1]-i)
                      for i in range(1, instruction.number_of_fields + 1)]
        return points

    def _get_intersections(self) -> List[Tuple[int]]:
        intersections = []
        for k, v in self.points.items():
            if v == 2:
                intersections.append(k)
        return intersections

    def _calculate_distance(self, point: Tuple[int]) -> int:
        return abs(point[0] - self.basis[0]) + abs(point[1] - self.basis[1])

    def get_min_distance(self) -> int:
        intersections = self._get_intersections()
        return min(self._calculate_distance(point) for point in intersections)

    def prepare_state_for_next_wire(self):
        for k, v in self.points.items():
            if v > 1:
                self.points[k] = 1
        self.head = self.basis

    def __add__(self, other):
        points = self.points.copy()
        for k, v in other.points.items():
            if k in self.points:
                points[k] += 1
        return Grid(points=points)


if __name__ == "__main__":

    with open('input3.txt', mode='r') as f:
        first_wire = f.readline()
        second_wire = f.readline()
    # first_wire = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    # second_wire = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    first_wire = first_wire.strip().split(',')
    second_wire = second_wire.strip().split(',')

    Instruction = namedtuple('Instruction', 'direction number_of_fields')
    first_wire = list(map(lambda x: Instruction(x[0], int(x[1:])), first_wire))
    second_wire = list(map(lambda x: Instruction(x[0], int(x[1:])),
                           second_wire))
    grid_1 = Grid()
    for instr in first_wire:
        grid_1.add_intruction(instr)
    grid_1.prepare_state_for_next_wire()

    grid_2 = Grid()
    for instr in second_wire:
        grid_2.add_intruction(instr)
    grid_2.prepare_state_for_next_wire()
    grid = grid_1 + grid_2
    min_ = grid.get_min_distance()
    print(min_)
    # import ipdb; ipdb.set_trace()
