from typing import List

OPERATIONS = {1: lambda x, y: x + y, 2: lambda x, y: x * y}


def compute(x: List[int]) -> int:
    idx = 0
    while x[idx] != 99 and idx < len(x):
        operation = x[idx]
        x[x[idx + 3]] = OPERATIONS[operation](x[x[idx + 1]], x[x[idx + 2]])
        idx += 4
    return x[0]


with open("input2.txt", mode="r") as f:
    data_str = f.readline()
data = list(map(int, data_str.split(",")))

assert compute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == 3500
assert compute([1, 0, 0, 0, 99]) == 2

data[1] = 12
data[2] = 2

out = compute(data)
print(out)
