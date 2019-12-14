from typing import List
from itertools import product

OPERATIONS = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y,
}


def compute(x: List[int]) -> int:
    idx = 0
    while x[idx] != 99 and idx < len(x):
        operation = x[idx]
        x[x[idx+3]] = OPERATIONS[operation](x[x[idx+1]], x[x[idx+2]])
        idx += 4
    return x[0]

assert compute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == 3500  # noqa
assert compute([1, 0, 0, 0, 99]) == 2

with open('input2.txt', mode='r') as f:
    data_str = f.readline()
data = list(map(int, data_str.split(',')))

for noun, verb in product(range(0, 100), range(0, 100)):
    input_ = data[:]
    input_[1] = noun
    input_[2] = verb
    if compute(input_) == 19690720:
        print(100*noun + verb)
        break
