from typing import List
from collections import deque
from typing import Deque, Tuple

BI_OPERATIONS = {1: lambda x, y: x + y, 2: lambda x, y: x * y}

UNARY_OPERATIONS = [3, 4]


def parse_instruction(instr: int) -> Tuple[Tuple[int, ...], int]:
    padded_instr = "0" * (5 - len(str(instr))) + str(instr)
    # str of the form ABCDE
    DE = int(padded_instr[-2:])
    C = int(padded_instr[2])
    B = int(padded_instr[1])
    A = int(padded_instr[0])
    return (C, B, A), DE


def compute(x: List[int], inputs: Deque[int]) -> Tuple[int, List[int]]:
    idx = 0
    returns = []
    while x[idx] != 99 and idx < len(x):
        modes, operation = parse_instruction(x[idx])
        if operation in BI_OPERATIONS:
            arg_0 = x[idx + 1] if modes[0] else x[x[idx + 1]]
            arg_1 = x[idx + 2] if modes[1] else x[x[idx + 2]]
            if modes[2] == 0:
                x[x[idx + 3]] = BI_OPERATIONS[operation](arg_0, arg_1)
            elif modes[2] == 1:
                x[idx + 3] = BI_OPERATIONS[operation](arg_0, arg_1)
            idx += 4
            continue
        elif operation in UNARY_OPERATIONS:
            if operation == 3:
                if modes[0] == 0:
                    x[x[idx + 1]] = inputs.popleft()
                elif modes[0] == 1:
                    x[idx + 1] = inputs.popleft()
            if operation == 4:
                returns.append(x[idx + 1] if modes[0] else x[x[idx + 1]])
            idx += 2
    return x[0], returns


with open("input5.txt", mode="r") as f:
    data_str = f.readline()
data = list(map(int, data_str.split(",")))


in_deque = deque([1])
result, out_codes = compute(data, in_deque)

print(result)

print(out_codes)
